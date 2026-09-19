# Client Automation

## Status 

Draft

## Broadcom Software Type

Enterprise Software

## Broadcom Product Category

IT Service Management (ITSM)

## Broadcom Product Name

Client Automation

## Broadcom Product Description (Key Features) (This is important to get right)

Client Automation (CA Client Automation, formerly CA IT Client Manager) is Broadcom's endpoint lifecycle management product. TechDocs now lists release 14.6 alongside 14.5 and 14.0; the features below were verified for 14.5 (up to CU7) and the 14.6 feature list could not be retrieved.

Key features:

1. **Hardware and software discovery and inventory** - Includes user-based software scan in 14.5, with heuristic scan reading user add/remove programs and desktop start menu entries.
2. **Software delivery with scalability servers** - Location-aware package delivery; 14.5 CU1 adds downloads from an alternate scalability server.
3. **OS deployment and patch management** - Operating system imaging, software packaging and patch management for physical and virtual endpoints.
4. **Remote control** - Remote control sessions, with a View All Displays option in 14.5 to open all monitors on the host.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

Analyst cautions and commercial pressures: Gartner Peer Insights rates Broadcom CA Client Automation at 4.0 out of 5, but from only 14 verified reviews under the 2025 Endpoint Management Tools market, a materially smaller review base than competing products tracked on the same platform, such as ManageEngine Endpoint Central at 4.6 out of 5 from 1,625 reviews and Microsoft Intune at 4.2 out of 5 from 1,136 reviews. This gap in review volume is itself evidence of reduced current market visibility and adoption relative to cloud-native unified endpoint management (UEM) competitors. Reviewer feedback describes the tool as mature and reliable for endpoint and patch operations but notes that the interface "feels technologically behind." The product remains architected around on-premises infrastructure without a Broadcom-delivered cloud-native UEM model, consistent with this row's existing claim, and is subject to the same general renewal-price and bundling pressures documented across Broadcom's wider portfolio.

Broadcom exit strategies and market alternatives: Microsoft Intune and Tanium are realistic, widely adopted UEM and endpoint security alternatives, and IBM MaaS360 is a genuine cloud UEM competitor. Red Hat Satellite addresses enterprise Linux patch and configuration management specifically and is not a full UEM replacement; it should be positioned as a partial, Linux-specific option rather than a like-for-like substitute for Client Automation's full endpoint scope.
Sources: Gartner Peer Insights, Broadcom CA Client Automation and Endpoint Management Tools market reviews (gartner.com/reviews/market/endpoint-management-tools/vendor/broadcom/product/ca-technologies-client); Redress Compliance, Broadcom Enterprise Agreements guide, 2025; The Register, 2022 Broadcom account-strategy analysis.

## IBM Replacement Strength

(not provided)

## IBM Replacement Strategy - Why IBM over Broadcom

(not provided)

## PRIMARY - Key Product - IBM Alternative

IBM MaaS360

## PRIMARY - Key Product Capability Statement - IBM Alternative

General sentiment: Positive – users like the centralised console and ease of set-up for Android, iOS and other endpoints, and few documented criticisms surfaced in this pass.

IBM MaaS360 is an enterprise Unified Endpoint Management (UEM) platform that manages and secures multi-OS endpoints (Windows, macOS, Linux, iOS, Android, and IoT) from a single cloud console. It delivers automated asset discovery, over-the-air software distribution, OS patch management, continuous device compliance, and AI-driven Mobile Threat Defense (MTD).

## PRIMARY - IBM Product Page URL

https://www.ibm.com/products/maas360

## Customer Reference
(not provided)
## SECONDARY - Product Name - Supporting Product From any vendor - ONLY Where needed to for FULL Capability match for Broadcom. Extend the IBM Key Product.

(not provided)

## SECONDARY - Product Description - From any vendor - A Secondary Support Product.

(not provided)

## SECONDARY - Product Page(s) URL

(not provided)

## Sources: Analyst reviews and exist strategy

Column D and Column E reviewed and revised against sourced evidence; see Sources line at the end of Column E for citations.

## General Sources:

- New Features and Enhancements - 14.5: https://techdocs.broadcom.com/us/en/ca-enterprise-software/business-management/clarity-client-automation/14-0/Release-Information-14-5/New-Features-and-Enhancements---14-5.html
- Release Information - 14.5 CU7: https://techdocs.broadcom.com/us/en/ca-enterprise-software/business-management/clarity-client-automation/14-5/release-information/release-information-14-5-cu7.html
- Release Information - 14.5 CU1: https://techdocs.broadcom.com/us/en/ca-enterprise-software/business-management/clarity-client-automation/14-5/release-information/Release-Information---14-5-1.html
- CA Client Automation 14.6 - Broadcom TechDocs: https://techdocs.broadcom.com/us/en/ca-enterprise-software/business-management/clarity-client-automation/14-6.html

## Change history:

### 2026-09-19 - Broadcom product information verification (WebFetch pass, files 02-39)
- Corrected the current version: the earlier text said 14.5 was the current release, but TechDocs lists 14.6 (the version list shows 14.6, 14.5, 14.0). The 14.6 feature list was not retrievable, so the key features remain those verified for 14.5. Product name in TechDocs is 'CA Client Automation'.

### 2026-09-19 - Broadcom product information review
- Product description: Added current version (14.5, CU7) and verified 14.5 feature detail.
- Summary and numbered list of four key features rewritten from current Broadcom sources.
- General Sources: 3 sources recorded (Broadcom TechDocs, product pages, press releases where available).

### 2026-09-19 - IBM alternative product verification and sentiment (WebFetch and WebSearch pass, files 02-39)
- Requirement match against the Key Features section: Partially meets – gaps in OS deployment and Linux.
- Confirmed: granular patch management, device and application management, inventory visibility, application distribution, remote control (via TeamViewer integration), and management of Windows 10 and 11, macOS, iOS, iPadOS, Android and ChromeOS.
- Gap: no OS imaging or operating system deployment capability and no native Linux management were found, although the capability statement in the file claims Linux and IoT support. Treat these as unverified until IBM confirms.
- Sentiment: added a one-sentence summary of general market sentiment at the start of the Key Product Capability Statement. Existing statement text was not changed.
- Sources: https://www.ibm.com/products/maas360; https://www.ibm.com/id-en/products/maas360/endpoint-management; https://www.ibm.com/products/maas360/distribution; https://www.gartner.com/reviews/product/ibm-security-maas360
