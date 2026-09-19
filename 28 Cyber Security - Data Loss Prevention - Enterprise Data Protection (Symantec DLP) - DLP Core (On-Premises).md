# Enterprise Data Protection (Symantec DLP) - DLP Core (On-Premises)

## Status 

Draft

## Broadcom Software Type

Cyber Security

## Broadcom Product Category

Data Loss Prevention

## Broadcom Product Name

Enterprise Data Protection (Symantec DLP) - DLP Core (On-Premises)

## Broadcom Product Description (Key Features) (This is important to get right)

Symantec Data Loss Prevention (on-premises) uses a version-by-year scheme; 26.1 was released on 1 May 2026. It provides content-aware detection and enforcement across endpoint, network, storage and cloud channels, managed from the Enforce Server.

Key features:

1. **Multi-channel data protection** - Covers endpoint, email, web, storage and cloud applications.
2. **Endpoint enforcement** - Endpoint agents block or monitor USB, printing, clipboard and browser actions.
3. **Incident dashboards and workflows (26.1)** - Dynamic filtering dashboards and new Incident Workflows to automate incident lifecycle tasks.
4. **Generative AI visibility** - 26.1 adds visibility into generative AI usage.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

Following Broadcom's acquisition, commercial strategy shifted heavily toward top Global 2000 accounts, consistent with Broadcom's broader core-account model applied across its acquired security portfolios. Commercial and mid-tier accounts report steep renewal price increases and diminished direct support as primary reasons for migrating away; one independent licensing advisory reports first renewal quotes arriving 30 to 100 per cent above prior run rates before negotiation.

Gartner discontinued its ranked Magic Quadrant for Enterprise DLP some years ago in favour of a vendor-neutral Market Guide (most recently published in 2025), so there is no current Leader/Niche Player ranking to cite for Symantec DLP. Symantec DLP was recognised as a Leader in Gartner's DLP Magic Quadrant while that report format existed, according to Broadcom's own community publication, though this predates the acquisition-era commercial changes described above and should not be read as a current analyst endorsement.

Microsoft has published a formal Symantec DLP-to-Purview migration path, which is itself evidence of an established exit corridor. Customers are migrating primarily to Microsoft Purview DLP, Forcepoint DLP (for risk-adaptive behavioural policies), and cloud/SaaS-focused tools such as Nightfall AI, Netskope and Strac for GenAI and cloud channels.

Sources: Microsoft Tech Community, 'Easily migrate your Symantec DLP policies to Microsoft Purview Data Loss Prevention'; Redress Compliance, 'Symantec Enterprise Software Licensing Under Broadcom: A CIO Playbook'; Broadcom Community blog referencing historical Gartner DLP Magic Quadrant leadership; Gartner 2025 Market Guide for Data Loss Prevention (existence confirmed via Palo Alto Networks summary page).

## IBM Replacement Strength

Partial

## IBM Replacement Strategy - Why IBM over Broadcom

1. Replace Broadcom with Microsoft Purview DLP for workstations. 2. Replace with CrowdStrike Falcon Data Protection everywhere else. 3. Deploy IBM Guardium Data Protection for the Enterprise estate.

## PRIMARY - Key Product - IBM Alternative

IBM Guardium Data Security Center / Guardium Data Protection.

## PRIMARY - Key Product Capability Statement - IBM Alternative

General sentiment: Positive on data activity monitoring and compliance reporting, with reviewers citing a steep learning curve, dated interface and complex set-up.

IBM Guardium Data Security Platform (DSPM / DAM) is a leader in automated data discovery/classification across on-prem and multi-cloud databases. Analyst reports (such as Gartner's Data Security Platform Magic Quadrant) rank IBM as a leader in Data Security Posture Management (DSPM), Database Activity Monitoring (DAM). Scan data stores for vulnerabilities and guide remediation. Monitor how data is accessed to detect risky behavior. Automate database compliance to reduce manual effort.

## PRIMARY - IBM Product Page URL

https://www.ibm.com/products/guardium-data-security-center

## Customer Reference
(not provided)
## SECONDARY - Product Name - Supporting Product From any vendor - ONLY Where needed to for FULL Capability match for Broadcom. Extend the IBM Key Product.

(not provided)

## SECONDARY - Product Description - From any vendor - A Secondary Support Product.

(not provided)

## SECONDARY - Product Page(s) URL

https://www.ibm.com/products/guardium-data-security-center

## Sources: Analyst reviews and exist strategy

Retained the core claims but added verifiable sourcing and corrected the implication of a current Gartner Magic Quadrant ranking — Gartner now publishes an unranked Market Guide for DLP, not a Magic Quadrant. Tightened Column D to remove repetition.

## General Sources:

- What's New in Data Loss Prevention 26.1: https://techdocs.broadcom.com/us/en/symantec-security-software/information-security/data-loss-prevention/26-1/new-and-changed/what-s-new-in-data-loss-prevention.html
- Enforce Server Features in DLP 26.1: https://techdocs.broadcom.com/us/en/symantec-security-software/information-security/data-loss-prevention/26-1/new-and-changed/what-s-new-in-data-loss-prevention/enforce-features-in-dlp-26-1.html
- Version 25.1 Release Notes: https://techdocs.broadcom.com/us/en/symantec-security-software/information-security/data-loss-prevention/25-1/new-and-changed/release-notes.html
- End of Service dates for Symantec Data Loss Prevention: https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/product-advisories/End-of-Service-dates-for-Symantec-Data-Loss-Prevention/16164

## Change history:

### 2026-09-19 - Broadcom product information verification (WebFetch pass, files 02-39)
- Verified: Symantec DLP versions 25.1 (updated 1 October 2025) and 26.1 (May 2026); support policy is active engineering on the latest GA and GA-1 with self-service afterwards. No changes.

### 2026-09-19 - Broadcom product information review
- Product description: Updated to 26.1 (May 2026) with dashboards and Incident Workflows.
- Summary and numbered list of four key features rewritten from current Broadcom sources.
- General Sources: 3 sources recorded (Broadcom TechDocs, product pages, press releases where available).

### 2026-09-19 - IBM alternative product verification and sentiment (WebFetch and WebSearch pass, files 02-39)
- Requirement match against the Key Features section: Does not meet the DLP requirements.
- Confirmed (IBM product page): data discovery and classification across hybrid cloud and SaaS, tracking of data access, user activity and policy changes.
- Gap: Guardium is a database and data-centric security product. Endpoint enforcement (USB, print, clipboard, browser), email and web channel coverage, incident workflows and generative AI visibility were not found, so it does not replace Symantec DLP. The Gartner leadership claim in the file was not verified in this pass.
- Sentiment: added a one-sentence summary of general market sentiment at the start of the Key Product Capability Statement. Existing statement text was not changed.
- Sources: https://www.ibm.com/products/guardium-data-protection; https://www.gartner.com/reviews/product/ibm-guardium
