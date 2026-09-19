# Broadcom Symantec Security Analytics (formerly Solera Network, Blue Coat Security Analytics)

## Broadcom Software Category

Cyber Security

## Description Broadcom Primary Function & Focus

Network Forensics & Threat Hunting

## Broadcom Broadcom Product Name

Broadcom Symantec Security Analytics (formerly Solera Network, Blue Coat Security Analytics)

## Broadcom Prdouct Summary Description (This is important to get right)

A full-packet capture (FPC) and network forensics solution designed to capture, index, classify and analyse network traffic across on-premises, hybrid and cloud environments. Delivers retrospective root-cause analysis after an incident, threat intelligence enrichment from Broadcom's Global Intelligence Network (GIN) and DeepSight adversary intelligence, and encrypted traffic inspection to decrypt and analyse encrypted gateway traffic.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

Broadcom's own End-of-Life notice confirms hardware retirement activity is underway on a rolling, generation-by-generation basis, though the specific dates require precision: Generation 8 and Generation 9 appliances carry an End-of-Life Notification Date of 1 October 2025 and a Model Drop Support Date of 1 October 2030 (support continues for some years yet), while earlier Generation 7 appliances (S500, J5300, E5660) passed their own drop-support date of 1 October 2025. This lifecycle transition has prompted security operations teams to evaluate modern replacement architectures.

Gartner Peer Insights carries 41 ratings for Symantec Security Analytics (3.9 out of 5, reviews dated October 2024 to December 2025), and support quality is a recurring complaint: one reviewer stated 'Support through Broadcom is terrible, which is the main reason we are getting rid of it,' and another cited 'the amount of time it takes to get an issue resolved' as a key drawback.

Broadcom's public lifecycle articles state that once a support contract expires, the Web and File Reputation providers are no longer available to the application, hardware replacement parts are no longer supplied, and support requests go unanswered; the application and hardware otherwise continue to run, but new full releases are no longer available [3][4]. The per-model dated tables sit behind the Broadcom support portal (Product Lifecycle tool and Advisory 22012), so the specific generation dates above should be confirmed there by a customer with portal access [2][3][4].

Software is still being maintained: Security Analytics 8.3.1 (build 56489) is the newest release documented on Broadcom TechDocs, published in autumn 2025 (the TechDocs page shows 4 September 2025; a search snippet showed 6 October 2025) [5]. Broadcom's strategic direction for network visibility is now the cloud-based Symantec CBX platform announced on 23 March 2026, which combines Symantec and Carbon Black technologies and delivers integrated endpoint, network, email and cloud visibility through a single Threat Tracer interface [6]. This is XDR-style correlation, and it is not a documented like-for-like full-packet-capture successor, so customers should not assume one exists.

No independent Forrester Wave or IDC MarketScape coverage specific to this product was identified. Organisations retiring on-premises full-packet-capture appliances in this category are generally consolidating network forensics into broader SIEM/XDR platforms with integrated network detection and response, including IBM QRadar, Darktrace, and Corelight, rather than replacing full-packet capture on a like-for-like basis.

Sources:
1. Gartner Peer Insights, Symantec Security Analytics product reviews (gartner.com/reviews).
2. Broadcom, Symantec Security Analytics End of Sale/End of Life notice (ftpdocs.broadcom.com, dated 1 October 2025). Not re-fetched in the 2026-09-19 update; dates unverified there.
3. Broadcom Knowledge Base, Symantec Security Analytics Hardware Appliances End of Life Notice: https://knowledge.broadcom.com/external/article/199843/symantec-security-analytics-hardware-app.html
4. Broadcom Knowledge Base, Security Analytics EOS/EOL End of Support/End of Life: https://knowledge.broadcom.com/external/article/240317/security-analytics-eoseol-end-of-support.html
5. Broadcom TechDocs, Security Analytics 8.3.1 Release Notes: https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/security-analytics/8-3-1/security-analytics-8-3-1-release-notes.html
6. Broadcom, Introduces Symantec CBX (GlobeNewswire, 23 March 2026): https://www.globenewswire.com/news-release/2026/03/23/3260460/19933/en/Broadcom-Introduces-Symantec-CBX-Delivering-Enterprise-Grade-Security-to-Under-Resourced-SOC-Teams.html

## Yes/No - Option for IBM 1:1 Replacement ?? Move from Broadcom from IBM/Red Hat (Same capability level)

Yes. Improved.

## Replacement Strategy Summary

Replace with IBM. Will provide both function and cost benefits

## PRIMARY - Key Product - IBM Alternative

IBM QRadar Security Intelligence Platform (S/W & H/W Appliances)

## PRIMARY - Key Product Capability Statement - IBM Alternative

The combination of IBM QRadar Network Appliance familily (Packet Capture; Incident Forensics) and IBM QRadar Application (SIEM, EDR, SOAR, Network Insights) provides a 1:1 functional replacement for Broadcom Symantec Security Analytics. Transitioning to IBM's suite eliminates reliance on Broadcom's impending EOL hardware while unifying network forensics directly into a modern SIEM/SOAR/XDR ecosystem.
 
 Defence can integrate with ASD’s Cyber Threat Intelligence Sharing (CTIS) service, using the CTIS plugin for QRadar, else connect to 3rd party services such as Palto Alto Cloud-hosted Cortex service for global Threat Inteligence (https://www.paloaltonetworks.com/cortex/threat-intelligence).

## PRIMARY - IBM Product Page URL

https://www.ibm.com/products/qradar-siem

## SECONDARY - Product Name - Supporting Product From any vendor - ONLY Where needed to for FULL Capability match for Broadcom. Extend the IBM Key Product.

(not provided)

## SECONDARY - Product Description - From any vendor - A Secondary Support Product.

(not provided)

## SECONDARY - Product Page(s) URL

https://www.ibm.com/products/qradar-siem

## Sources: Analyst reviews and exist strategy

Verified and corrected the specific EOL/drop-support dates against Broadcom's own published notice (drop support is 2030 for current generations, not near-term), and added a concrete, quoted Peer Insights finding on support quality in place of the previous unattributed reference.

## Bob Changes:

## Claude Changes:

Update of 2026-09-19. Only this file was edited; no other files were changed.

1. Section "Analyst Cautions and Industry Findings": added two paragraphs.
   - Consequences of an expired support contract, per Broadcom's KB articles.
   - Latest software release (8.3.1-56489) and Broadcom's March 2026 Symantec CBX announcement as the strategic direction. The paragraph notes that CBX is not a documented like-for-like full-packet-capture replacement.
2. Section "Sources": converted to a numbered reference list [1]-[6] with URLs, and referenced the new citations inline.
3. Not verified: the 1 October 2025 / 2030 per-generation dates. Broadcom's public KB pages only link to portal-gated lifecycle tables. The existing dates were left unchanged and flagged as needing confirmation by a customer with portal access.
4. Open discrepancy: TechDocs shows 8.3.1 as 4 September 2025, while a search snippet showed 6 October 2025. Both are recorded in the text.
5. No other new analyst coverage (Forrester, IDC, Gartner) was found in this pass, and the recommendation and IBM sections were not changed.