# Broadcom Symantec Security Analytics (formerly Solera Network, Blue Coat Security Analytics)

## Page Status 

Draft

## Broadcom Software Type

Cyber Security

## Broadcom Product Category

Network Forensics & Threat Hunting

## Broadcom Product Name

Broadcom Symantec Security Analytics (Formally Solera Network, Blue Coat Security Analytics)

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

## IBM PRIMARY - Product Name (The Replacement)

IBM QRadar Network Insights & Incident Forensics

## IBM PRIMARY - IBM Product Page URL

https://www.ibm.com/products/qradar-siem

## IBM Replacement Strength

Strong Replacement, with improved outcomes

## IBM Replacement Strategy (Short)

QRadar Network Insights and Incident Forensics provide packet analysis inside SIEM, avoiding Broadcom appliance end-of-life.

## IBM Replacement Strategy (Description - Why IBM over Broadcom)

IBM QRadar Network Insights (QNI) alongside IBM Security QRadar SIEM and QRadar Incident Forensics replaces Broadcom Symantec Security Analytics. Broadcom has placed older Security Analytics hardware generations on an end-of-life path while pivoting toward the Symantec CBX cloud platform, abandoning dedicated on-premises packet forensics. IBM delivers comprehensive deep packet inspection, real-time application and content classification, and full incident reconstruction integrated natively into an enterprise on-premises SIEM architecture, eliminating proprietary appliance hardware refresh cycles and reducing long-term TCO.

## IBM PRIMARY - Product Description

IBM QRadar Network Insights (QNI) and IBM QRadar Incident Forensics deliver real-time network traffic analysis, deep packet inspection (DPI), protocol decoding, and retrospective threat hunting integrated natively into the IBM QRadar security intelligence platform.

- **Full packet capture and indexing** — IBM QRadar Incident Forensics and Packet Capture record, index, and reconstruct raw network sessions, enabling security analysts to replay full protocol conversations and trace advanced attack vectors retrospectively.
- **Deep packet inspection** — IBM QRadar Network Insights performs deep packet inspection in real time across thousands of network protocols and applications, extracting rich content metadata, suspicious file payloads, and protocol anomalies.
- **Threat intelligence** — IBM QRadar integrates out-of-the-box with IBM X-Force Threat Intelligence, STIX/TAXII threat feeds, and national sharing frameworks (such as ASD CTIS) to perform real-time IP, domain, and file reputation checks.
- **Encrypted traffic visibility** — IBM QRadar Network Insights analyzes SSL/TLS session metadata, certificate structures, and cryptographic cipher anomalies, and integrates with network decryption brokers to inspect decrypted payload streams.

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
