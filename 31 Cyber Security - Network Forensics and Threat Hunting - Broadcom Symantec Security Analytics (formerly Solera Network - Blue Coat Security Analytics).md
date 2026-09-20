# Broadcom Symantec Security Analytics (formerly Solera Network, Blue Coat Security Analytics)

## Status 

Draft

## Broadcom Software Type

Cyber Security

## Broadcom Product Category

Network Forensics & Threat Hunting

## Broadcom Product Name

Broadcom Symantec Security Analytics (formerly Solera Network, Blue Coat Security Analytics)

## Broadcom Product Description - Key Features

Symantec Security Analytics is a full-packet capture and network forensics appliance and software. Version 8.3.1 (build 56489) is the latest documented; it was released on 4 September 2025 and its documentation was last updated on 8 January 2026.

Key features:

1. **Full packet capture and indexing** - Captures, indexes, classifies and enriches all traffic for retrospective analysis.
2. **Deep packet inspection** - Identifies more than 3,300 applications and protocols.
3. **Threat intelligence** - Uses the Symantec Global Intelligence Network and reputation checks.
4. **Encrypted traffic visibility** - Works with Secure Web Gateways to decrypt SSL/TLS traffic.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

The hardware behind Security Analytics is being retired in stages, and Broadcom's own notice lays out the timetable. Generation 8 and Generation 9 appliances carry an end-of-life notification date of 1 October 2025 and a model drop-support date of 1 October 2030, so support continues for some years yet. Older Generation 7 appliances (the S500, J5300 and E5660) passed their drop-support date on 1 October 2025. Broadcom's public lifecycle articles say that once a support contract lapses, the web and file reputation services stop, replacement parts are no longer supplied and support requests go unanswered, though the application and hardware keep running and new full releases stop. The dated tables per model sit behind Broadcom's support portal, so a customer with portal access should confirm the exact generation dates.

Software development has not stopped. Security Analytics 8.3.1 is the newest release documented, published in autumn 2025. Broadcom's strategic direction, though, is the cloud-based Symantec CBX platform announced on 23 March 2026, which combines Symantec and Carbon Black technology and gives endpoint, network, email and cloud visibility through a single Threat Tracer interface. That is XDR-style correlation and not a documented like-for-like full-packet-capture successor, so nobody should assume one exists.

Customers have been blunt about support. Gartner Peer Insights holds 41 ratings, averaging 3.9 out of 5, dated October 2024 to December 2025. One reviewer wrote, 'Support through Broadcom is terrible, which is the main reason we are getting rid of it', and another named 'the amount of time it takes to get an issue resolved' as the key drawback. That is an anonymous customer saying plainly that they are leaving, and it is the closest thing to an exit account on record. No named organisation has publicly described leaving.

No Forrester Wave or IDC MarketScape covers the product. Organisations retiring on-premises full-packet-capture appliances are mostly folding network forensics into broader SIEM and XDR platforms with network detection and response, such as IBM QRadar, Darktrace and Corelight, and not replacing full packet capture like for like.

## IBM Replacement Strength

Strong Replacement, with improved outcomes

## IBM Replacement Strategy - Why IBM over Broadcom

IBM QRadar Network Insights (QNI) alongside IBM Security QRadar SIEM and QRadar Incident Forensics replaces Broadcom Symantec Security Analytics. Broadcom has placed older Security Analytics hardware generations on an end-of-life path while pivoting toward the Symantec CBX cloud platform, abandoning dedicated on-premises packet forensics. IBM delivers comprehensive deep packet inspection, real-time application and content classification, and full incident reconstruction integrated natively into an enterprise on-premises SIEM architecture, eliminating proprietary appliance hardware refresh cycles and reducing long-term TCO.

## IBM PRIMARY - Product Name (The Replacement)

IBM QRadar Network Insights & Incident Forensics

## IBM PRIMARY - Product Description

IBM QRadar Network Insights (QNI) and IBM QRadar Incident Forensics deliver real-time network traffic analysis, deep packet inspection (DPI), protocol decoding, and retrospective threat hunting integrated natively into the IBM QRadar security intelligence platform.

- **Full packet capture and indexing** — IBM QRadar Incident Forensics and Packet Capture record, index, and reconstruct raw network sessions, enabling security analysts to replay full protocol conversations and trace advanced attack vectors retrospectively.
- **Deep packet inspection** — IBM QRadar Network Insights performs deep packet inspection in real time across thousands of network protocols and applications, extracting rich content metadata, suspicious file payloads, and protocol anomalies.
- **Threat intelligence** — IBM QRadar integrates out-of-the-box with IBM X-Force Threat Intelligence, STIX/TAXII threat feeds, and national sharing frameworks (such as ASD CTIS) to perform real-time IP, domain, and file reputation checks.
- **Encrypted traffic visibility** — IBM QRadar Network Insights analyzes SSL/TLS session metadata, certificate structures, and cryptographic cipher anomalies, and integrates with network decryption brokers to inspect decrypted payload streams.

## IBM PRIMARY - IBM Product Page URL

https://www.ibm.com/products/qradar-siem

## Customer Reference

(not provided)
## IBM SECONDARY - Product Name (Supporting Product, where recommended to compliment the Primary capability)

(not provided)

## IBM SECONDARY - Product Description

(not provided)

## IBM SECONDARY - Product Page(s) URL

https://www.ibm.com/products/qradar-siem

# Sources:

## IBM QRadar Network Insights & Incident Forensics

- IBM QRadar Network Insights Product Documentation: https://www.ibm.com/docs/en/qsip/7.5?topic=overview-qradar-network-insights
- IBM QRadar Incident Forensics Documentation: https://www.ibm.com/docs/en/qsip/7.5?topic=overview-qradar-incident-forensics
- Gartner Peer Insights — IBM Security QRadar Reviews: https://www.gartner.com/reviews/market/security-information-event-management/vendor/ibm/product/ibm-qradar-siem

## Sources: Analyst reviews and exist strategy

- Gartner Peer Insights, Symantec Security Analytics product reviews (gartner.com/reviews)
- Broadcom, Symantec Security Analytics End of Sale and End of Life notice (ftpdocs.broadcom.com, dated 1 October 2025). Not re-fetched on 2026-09-19, so the dates need confirming
- Broadcom Knowledge Base, 'Symantec Security Analytics Hardware Appliances End of Life Notice' (https://knowledge.broadcom.com/external/article/199843/symantec-security-analytics-hardware-app.html)
- Broadcom Knowledge Base, 'Security Analytics EOS/EOL End of Support/End of Life' (https://knowledge.broadcom.com/external/article/240317/security-analytics-eoseol-end-of-support.html)
- Broadcom TechDocs, 'Security Analytics 8.3.1 Release Notes' (https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/security-analytics/8-3-1/security-analytics-8-3-1-release-notes.html)
- Broadcom, 'Broadcom Introduces Symantec CBX' (GlobeNewswire, 23 March 2026, https://www.globenewswire.com/news-release/2026/03/23/3260460/19933/en/Broadcom-Introduces-Symantec-CBX-Delivering-Enterprise-Grade-Security-to-Under-Resourced-SOC-Teams.html)

## General Sources:

- Security Analytics 8.3.1 - TechDocs: https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/security-analytics/8-3-1.html
- Security Analytics 8.3.1 Release Notes: https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/security-analytics/8-3-1/security-analytics-8-3-1-release-notes.html
- Security Analytics Key Features: https://www.broadcom.com/info/symantec/security-analytics-key-features

## Change history:

### 2026-09-20 - Analyst Cautions and Industry Findings rewritten as a narrative
- Rewrote the section as a narrative and removed the bracketed reference numbers from the text.
- Kept the reviewer who said they are getting rid of the product as the closest exit account. No named organisation was found.
- Moved all citations, previously a numbered list, to the Sources: Analyst reviews and exist strategy section.


### 2026-09-19 - Broadcom product information verification (WebFetch pass, files 02-39)
- Corrected the description: it said the 8.3.1 documentation was updated on 19 June 2026 (from a search snippet). The TechDocs release notes page shows a release date of 4 September 2025 and a last-updated date of 8 January 2026, which agrees with the existing Analyst Cautions text. The 6 October 2025 date mentioned there was not seen and remains unconfirmed.

### 2026-09-19 - Broadcom product information review
- Product description: Updated to 8.3.1 and replaced DeepSight reference with Global Intelligence Network wording per current Broadcom sources.
- Summary and numbered list of four key features rewritten from current Broadcom sources.
- General Sources: 3 sources recorded (Broadcom TechDocs, product pages, press releases where available).

### Earlier entries
Update of 2026-09-19. Only this file was edited; no other files were changed.

1. Section "Analyst Cautions and Industry Findings": added two paragraphs.
   - Consequences of an expired support contract, per Broadcom's KB articles.
   - Latest software release (8.3.1-56489) and Broadcom's March 2026 Symantec CBX announcement as the strategic direction. The paragraph notes that CBX is not a documented like-for-like full-packet-capture replacement.
2. Section "Sources": converted to a numbered reference list [1]-[6] with URLs, and referenced the new citations inline.
3. Not verified: the 1 October 2025 / 2030 per-generation dates. Broadcom's public KB pages only link to portal-gated lifecycle tables. The existing dates were left unchanged and flagged as needing confirmation by a customer with portal access.
4. Open discrepancy: TechDocs shows 8.3.1 as 4 September 2025, while a search snippet showed 6 October 2025. Both are recorded in the text.
5. No other new analyst coverage (Forrester, IDC, Gartner) was found in this pass, and the recommendation and IBM sections were not changed.

### 2026-09-19 - IBM alternative product verification and sentiment (WebFetch and WebSearch pass, files 02-39)
- Requirement match against the Key Features section: Replacement product at risk – SaaS offering ended, forensics component reaching end of support.
- Critical: the QRadar SaaS assets were sold to Palo Alto Networks (31 August 2024) and the SaaS products are end of life (see file 30). QRadar Incident Forensics is reported as not available in the QRadar 7.6.x stream, with end of support on 30 April 2026 and sustained support to 30 April 2030; this came from search results and the primary IBM notice was not opened.
- QRadar Network Insights remains integrated with QRadar on-premises, but no 2026 support statement was found. The claim of a '1:1 functional replacement' for full-packet capture and network forensics is therefore not supported, and the EOL argument against Broadcom hardware applies equally to the QRadar forensics appliances.
- Sentiment: added a one-sentence summary of general market sentiment at the start of the Key Product Capability Statement. Existing statement text was not changed.
- Sources: https://www.paloaltonetworks.com/cyberpedia/ibm-qradar-acquired-by-palo-alto-networks; https://www.ibm.com/support/pages/node/7129432; https://www.ibm.com/docs/en/qsip/7.4.0?topic=qmao-qradar-incident-forensics-1
