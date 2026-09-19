# Broadcom Identity-Centric Secure Access (formerly Symantec Zero Trust Network Access / Secure Access Cloud)

## Status 

Draft

## Broadcom Software Type

Cyber Security

## Broadcom Product Category

Zero Trust Network Access

## Broadcom Product Name

Broadcom Identity-Centric Secure Access (formerly Symantec Zero Trust Network Access / Secure Access Cloud)

## Broadcom Product Description (Key Features) (This is important to get right)

Symantec Zero Trust Network Access (ZTNA, formerly Secure Access Cloud) uses software-defined perimeter technology to give agentless, least-privilege access to private applications without a VPN. Broadcom TechDocs uses the name ZTNA; the name 'Identity-Centric Secure Access' does not appear there. Recent releases (May to August 2026) add Cloud SWG and DLP integration.

Key features:

1. **Application-level, agentless access** - Users reach individual applications rather than the network, with no changes to existing security configurations.
2. **Identity provider integration** - Integrates with IdPs and IAM for identity-based access.
3. **Cloud SWG and DLP integration** - One-click Cloud Data Security integration with DLP policy enforcement (July 2026), automated Cloud SWG integration management (June 2026) and DLP Cloud Detector support in Activity Policy rules (May 2026).
4. **Expanded connection types** - RDP Farm connections for pools of RDP resources and long-lived API client keys (August 2026), with copy and paste prevention for native RDP (preview).

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

Analyst visibility into this product specifically is limited. Gartner Peer Insights lists it as 'Symantec Enterprise Cloud' with a 4.4 out of 5 rating, but this is based on only five to six reviews, a very small sample compared with major SSE/ZTNA competitors in the same Gartner category (for comparison, identity products from Okta and Microsoft in adjacent categories carry many hundreds of reviews). This small sample size is indicative of limited market adoption and visibility rather than a specific quality finding. No independent Gartner Magic Quadrant for Security Service Edge (SSE), Forrester Wave placement, or other named analyst ranking specific to this Broadcom/Symantec product was identified in this research.

Broadcom's general commercial pattern of bundling ZTNA licensing with other Symantec Enterprise Cloud products, and prioritising its largest accounts, applies here as with other legacy Symantec Enterprise Security Group products.

Organisations modernising secure remote access are transitioning to cloud-native SSE/ZTNA architectures with substantially larger installed bases and analyst coverage, including Zscaler Private Access, Palo Alto Networks Prisma Access, Cloudflare One, and Microsoft Entra Private Access.

Sources: Gartner Peer Insights, 'Symantec Enterprise Cloud' product page (gartner.com/reviews); comparative review volumes on the same platform.

## IBM Replacement Strength

Not applicable. (Defence using CITRIX-based solution for Remote Desktop Access)

## IBM Replacement Strategy - Why IBM over Broadcom

This assessmenet does not address Cloud Hosted or Cloud Access services.

## PRIMARY - Key Product - IBM Alternative

IBM Security Verify

## PRIMARY - Key Product Capability Statement - IBM Alternative

General sentiment: Positive – reviewers cite strong security features, single sign-on, passwordless access and easy deployment, with slowness and console complexity the main criticisms.

IBM Security Verify is fundamentally an Identity and Access Management (IAM / IDaaS) and Web Access Management (WAM) platform rather than a full network-level VPN or standalone packet-level Zero Trust Network Access (ZTNA) tunnel solution. Defence would use the Verify suite across its entire identity landscape.

## PRIMARY - IBM Product Page URL

https://www.ibm.com/products/security-verify

## Customer Reference
(not provided)
## SECONDARY - Product Name - Supporting Product From any vendor - ONLY Where needed to for FULL Capability match for Broadcom. Extend the IBM Key Product.

(not provided)

## SECONDARY - Product Description - From any vendor - A Secondary Support Product.

(not provided)

## SECONDARY - Product Page(s) URL

https://www.ibm.com/products/security-verify

## Sources: Analyst reviews and exist strategy

Replaced generic, unattributed analyst claims with a specific, verifiable Gartner Peer Insights data point (rating and very small review count) and stated plainly that no named Magic Quadrant/Wave coverage was found for this product.

## General Sources:

- About Zero Trust Network Access (ZTNA): https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/ztna/1-0/about-secure-access-cloud.html
- What's New in Symantec ZTNA: https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/ztna/1-0/what-is-new.html
- Symantec ZTNA - Broadcom Service Status: https://status.broadcom.com/services/symantec-ztna

## Change history:

### 2026-09-19 - Broadcom product information verification (WebFetch pass, files 02-39)
- Verified: TechDocs uses the name 'Zero Trust Network Access (ZTNA)' and states the product was formerly Secure Access Cloud. The name 'Identity-Centric Secure Access' used in this file's Product Name could not be found in Broadcom documentation, so the name is unchanged but flagged as unverified. The Gartner listing 'Symantec Enterprise Cloud' and its rating could not be re-checked.

### 2026-09-19 - WebFetch verification pass
- Verified with WebFetch: current name is ZTNA and the name 'Identity-Centric Secure Access' is not used in TechDocs. Features updated to May to August 2026 releases.

### 2026-09-19 - Broadcom product information review
- Product description: Confirmed product rename to ZTNA. The 'Identity-Centric Secure Access' naming is retained from the file title but could not be independently confirmed in Broadcom TechDocs.
- Summary and numbered list of four key features rewritten from current Broadcom sources.
- General Sources: 3 sources recorded (Broadcom TechDocs, product pages, press releases where available).

### 2026-09-19 - IBM alternative product verification and sentiment (WebFetch and WebSearch pass, files 02-39)
- Requirement match against the Key Features section: Does not meet the ZTNA requirements.
- Confirmed (IBM product page): passwordless and adaptive risk-based authentication, and an Application Gateway that extends modern authentication to legacy applications.
- Gap: no ZTNA, software-defined perimeter or network-level private application access was stated, and the Cloud SWG and DLP integrations are not offered. The file itself acknowledges that Verify is an identity platform, not a ZTNA tunnel solution, so it is not a functional replacement for Symantec ZTNA.
- Sentiment: added a one-sentence summary of general market sentiment at the start of the Key Product Capability Statement. Existing statement text was not changed.
- Sources: https://www.ibm.com/products/verify; https://www.gartner.com/reviews/market/access-management/vendor/ibm/product/ibm-verify
