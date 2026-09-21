#!/usr/bin/env python3
"""
Generate BROADCOM Exit Deck PPTX from MD files.
Uses EXIT_Page_01 layout from TEMPLATE_V05.pptx.

Mapping:
  ## Broadcom Software Type        -> idx 26  (Broadcom_Software_Type)
  ## Broadcom Product Category     -> idx 27  (Broadcom_Product_Category)
  ## Broadcom Product Name         -> title   (Broadcom_Product_Name)
  ## Broadcom Product Description  -> idx 17  (Broadcom_Product_Description)
  ## Analyst Cautions              -> idx 19  (Analyst_Cautions)
  ## IBM Replacement Strength      -> idx 24  (IBM_Replacement_Strength)
  ## IBM PRIMARY - Product Name    -> idx 23  (IBM_PRIMARY_Product_Name)
  ## IBM PRIMARY - Product Desc    -> idx 18  (IBM_PRIMARY_Product_Description)
  ## IBM Replacement Strategy      -> idx 22  (IBM_Replacement_Strategy)
  ## IBM SECONDARY - Product Name  -> idx 25  (IBM_SECONDARY_Product_Name)
  ## IBM PRIMARY - IBM Product Page URL -> idx 28 (IBM_PRIMARY_IBM_Product_Page_URL)
"""

import glob
import os
import re
import copy
from lxml import etree
from pptx import Presentation
from pptx.util import Pt
from pptx.oxml.ns import qn

NSMAP = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
}

# ---- MD section heading -> placeholder idx mapping ----
# idx None = title placeholder
SECTION_MAP = {
    'broadcom software type':              26,
    'broadcom product category':           27,
    'broadcom product name':               None,  # title
    'broadcom product description - key features': 17,
    'broadcom product description':        17,
    'analyst cautions and industry findings - related to the legacy broadcom product. include newest findings on broadcom exist strategies': 19,
    'analyst cautions and industry findings': 19,
    'analyst cautions':                    19,
    'ibm replacement strength':            24,
    'ibm primary - product name (the replacement)': 23,
    'ibm primary - product name':          23,
    'ibm primary - product description':   18,
    'ibm replacement strategy - why ibm over broadcom': 22,
    'ibm replacement strategy':            22,
    'ibm secondary - product name (supporting product, where recommended to compliment the primary capability)': 25,
    'ibm secondary - product name':        25,
    'ibm primary - ibm product page url':  28,
}

# Which idx values are wanted
WANTED_IDX = {None, 17, 18, 19, 22, 23, 24, 25, 26, 27, 28}


def parse_md_sections(filepath):
    """Return dict of lowercase-heading -> text content."""
    with open(filepath, encoding='utf-8') as f:
        content = f.read()

    sections = {}
    # Split on level-2 headings
    parts = re.split(r'^## (.+)$', content, flags=re.MULTILINE)
    # parts[0] = preamble, then alternating heading / body
    for i in range(1, len(parts), 2):
        heading = parts[i].strip()
        body = parts[i + 1].strip() if i + 1 < len(parts) else ''
        sections[heading.lower()] = (heading, body)
    return sections


def get_section(sections, key_lower):
    """Fetch body text for a section key (case-insensitive prefix match)."""
    if key_lower in sections:
        return sections[key_lower][1]
    # try prefix matching
    for k, (_, body) in sections.items():
        if k.startswith(key_lower) or key_lower.startswith(k):
            return body
    return ''


def resolve_mapping(sections):
    """Return dict of idx -> text."""
    result = {}
    for key, idx in SECTION_MAP.items():
        if idx not in WANTED_IDX:
            continue
        body = get_section(sections, key)
        if body:
            result[idx] = body
    return result


def xml_text_run(text, lang='en-AU'):
    """Build a plain <a:r> run."""
    rpr = etree.SubElement(etree.Element('dummy'), qn('a:rPr'))
    rpr.set('lang', lang)
    rpr.set('dirty', '0')
    r = etree.Element(qn('a:r'))
    r.append(rpr)
    t = etree.SubElement(r, qn('a:t'))
    t.text = text
    return r


def make_plain_paragraph(text, lang='en-AU'):
    p = etree.Element(qn('a:p'))
    pPr = etree.SubElement(p, qn('a:pPr'))
    pPr.set('lvl', '0')
    r = etree.SubElement(p, qn('a:r'))
    rPr = etree.SubElement(r, qn('a:rPr'))
    rPr.set('lang', lang)
    rPr.set('dirty', '0')
    t = etree.SubElement(r, qn('a:t'))
    t.text = text
    return p


def build_txbody_paragraphs(raw_text):
    """
    Convert raw markdown-ish text into a list of <a:p> elements.
    - Preserves numbered items (1. text) keeping the number in the text.
    - Handles bold (**text**) by stripping markers (PPTX style inherits from layout).
    - Splits on newlines.
    """
    paragraphs = []
    for line in raw_text.splitlines():
        line = line.rstrip()
        if not line:
            # blank line → empty paragraph for spacing
            p = etree.Element(qn('a:p'))
            p.append(etree.Element(qn('a:endParaRPr')))
            paragraphs.append(p)
            continue

        # Strip markdown bold markers but keep the text
        # e.g. **Bold text.** rest → "Bold text. rest"
        stripped = re.sub(r'\*\*(.+?)\*\*', r'\1', line)

        # Build paragraph
        p = make_plain_paragraph(stripped)
        paragraphs.append(p)

    return paragraphs


def build_txbody_paragraphs_with_link(url_text):
    """For URL fields: make the URL a hyperlink run if present."""
    # Find the URL in the text
    url_match = re.search(r'https?://\S+', url_text)
    if not url_match:
        return build_txbody_paragraphs(url_text)

    url = url_match.group(0).rstrip('.,)')
    display = url

    # Return paragraphs with just the URL — hyperlink rId will be set by caller
    p = etree.Element(qn('a:p'))
    pPr = etree.SubElement(p, qn('a:pPr'))
    pPr.set('lvl', '0')
    r = etree.SubElement(p, qn('a:r'))
    rPr = etree.SubElement(r, qn('a:rPr'))
    rPr.set('lang', 'en-AU')
    rPr.set('dirty', '0')
    # We'll set the hlinkClick later when we have the slide rel
    rPr.set('_url_placeholder', url)  # temp marker
    t = etree.SubElement(r, qn('a:t'))
    t.text = display
    return [p], url


def set_placeholder_text(slide, idx, text, is_url=False):
    """Find placeholder by idx and set its text content."""
    from pptx.oxml.ns import nsmap as pptx_nsmap

    for sp in slide.shapes:
        ph = sp.placeholder_format
        if ph is None:
            continue
        if idx is None and ph.type.name == 'TITLE':
            target_sp = sp
            break
        if ph.idx == idx:
            target_sp = sp
            break
    else:
        return  # not found

    txBody = target_sp.text_frame._txBody

    # Remove existing <a:p> elements
    for p in txBody.findall(qn('a:p')):
        txBody.remove(p)

    if is_url:
        result = build_txbody_paragraphs_with_link(text)
        if isinstance(result, tuple):
            paragraphs, url = result
            # Add relationship to slide for the hyperlink
            rel = target_sp.part.part_related_by  # method not needed
            # Use slide part to add the relationship
            slide_part = slide.part
            rId = slide_part.relate_to(
                url,
                'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink',
                is_external=True
            )
            # Set hlinkClick on the rPr
            for p in paragraphs:
                for r in p.findall(qn('a:r')):
                    rPr = r.find(qn('a:rPr'))
                    if rPr is not None and rPr.get('_url_placeholder'):
                        del rPr.attrib['_url_placeholder']
                        hlinkClick = etree.SubElement(rPr, qn('a:hlinkClick'))
                        hlinkClick.set(
                            '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id',
                            rId
                        )
        else:
            paragraphs = result
    else:
        paragraphs = build_txbody_paragraphs(text)

    for p in paragraphs:
        txBody.append(p)

    # Ensure ends with endParaRPr
    last_p = txBody.findall(qn('a:p'))[-1]
    if last_p.find(qn('a:endParaRPr')) is None:
        end = etree.SubElement(last_p, qn('a:endParaRPr'))
        end.set('lang', 'en-AU')
        end.set('dirty', '0')


def process_md_file(filepath, prs):
    """Parse MD file and add a new slide to prs."""
    sections = parse_md_sections(filepath)
    mapping = resolve_mapping(sections)

    # Use the EXIT_Page_01 layout (only layout in this template)
    layout = None
    for sl in prs.slide_layouts:
        if sl.name == 'EXIT_Page_01':
            layout = sl
            break
    if layout is None:
        layout = prs.slide_layouts[0]

    slide = prs.slides.add_slide(layout)

    for idx, text in mapping.items():
        if not text or text.lower() in ('(not provided)', 'n/a', ''):
            continue
        is_url = (idx == 28)
        set_placeholder_text(slide, idx, text, is_url=is_url)

    return slide


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(script_dir, 'TEMPLATE_V05.pptx')
    output_path = os.path.join(script_dir, 'BROADCOM_Exit_Deck.pptx')

    # Gather MD files 02*.md to 39*.md using os.listdir (avoids glob bracket issues in path)
    all_files = [os.path.join(script_dir, f) for f in sorted(os.listdir(script_dir))
                 if f.endswith('.md') and re.match(r'^\d{2} ', f)]
    md_files = [f for f in all_files
                if int(re.match(r'^(\d{2}) ', os.path.basename(f)).group(1)) >= 2]

    print(f"Template: {template_path}")
    print(f"Found {len(md_files)} MD files")

    prs = Presentation(template_path)

    for mf in md_files:
        fname = os.path.basename(mf)
        print(f"  Processing: {fname}")
        try:
            process_md_file(mf, prs)
        except Exception as e:
            print(f"    ERROR: {e}")
            import traceback
            traceback.print_exc()

    # Remove the original template slide (slide index 0)
    # The template has 1 slide; new slides were appended starting at index 1
    # Actually python-pptx appends so original stays at 0, we remove it
    if len(prs.slides) > len(md_files):
        rId = prs.slides._sldIdLst[0].get('r:id') or prs.slides._sldIdLst[0].get(
            '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id'
        )
        # Find and remove the first slide
        slide_to_remove = prs.slides[0]
        xml_slides = prs.slides._sldIdLst
        xml_slides.remove(xml_slides[0])

    prs.save(output_path)
    print(f"\nSaved: {output_path}")
    print(f"Total slides: {len(prs.slides)}")


if __name__ == '__main__':
    main()
