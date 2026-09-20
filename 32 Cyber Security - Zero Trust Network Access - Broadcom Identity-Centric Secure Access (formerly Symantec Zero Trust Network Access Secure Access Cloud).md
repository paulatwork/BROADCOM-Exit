# Broadcom Identity-Centric Secure Access (formerly Symantec Zero Trust Network Access / Secure Access Cloud)

## Status 

Draft

## Broadcom Software Type

Cyber Security

## Broadcom Product Category

Zero Trust Network Access

## Broadcom Product Name

Broadcom Identity-Centric Secure Access (formerly Symantec Zero Trust Network Access / Secure Access Cloud)

## Broadcom Product Description - Key Features

Symantec Zero Trust Network Access (ZTNA, formerly Secure Access Cloud) uses software-defined perimeter technology to give agentless, least-privilege access to private applications without a VPN. Broadcom TechDocs uses the name ZTNA; the name 'Identity-Centric Secure Access' does not appear there. Recent releases (May to August 2026) add Cloud SWG and DLP integration.

Key features:

1. **Application-level, agentless access** - Users reach individual applications rather than the network, with no changes to existing security configurations.
2. **Identity provider integration** - Integrates with IdPs and IAM for identity-based access.
3. **Cloud SWG and DLP integration** - One-click Cloud Data Security integration with DLP policy enforcement (July 2026), automated Cloud SWG integration management (June 2026) and DLP Cloud Detector support in Activity Policy rules (May 2026).
4. **Expanded connection types** - RDP Farm connections for pools of RDP resources and long-lived API client keys (August 2026), with copy and paste prevention for native RDP (preview).

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

It is hard to say much that is independent about this product, because so few people have reviewed it. Gartner Peer Insights lists it under the name 'Symantec Enterprise Cloud' with 4.4 out of 5, but from only five or six reviews, a tiny sample beside the many hundreds carried by identity products from Okta and Microsoft in adjacent categories. That points to limited adoption and visibility, not to a quality problem. No Gartner Magic Quadrant for security service edge, Forrester Wave or other named ranking specific to the product was found.

The commercial picture is the familiar one. Broadcom bundles zero trust network access licensing with other Symantec Enterprise Cloud products and puts its largest accounts first, as it does across the old Symantec Enterprise Security Group lines.

No named organisation has publicly described leaving the product. Competitors do make the point publicly. One vendor, dope.security, publishes a guide on leaving Symantec's cloud proxy, though that is a different Symantec service and not this one. For zero trust access itself, organisations modernising remote access are moving to cloud-native SSE and ZTNA platforms with far larger installed bases and analyst coverage, notably Zscaler Private Access, Palo Alto Networks Prisma Access, Cloudflare One and Microsoft Entra Private Access.

## IBM Replacement Strength

Partial Match

## IBM Replacement Strategy - Why IBM over Broadcom

IBM Security Verify Access with Application Gateway delivers context-aware, identity-centric zero-trust application access that replaces Broadcom Symantec ZTNA. Broadcom's ZTNA tool suffers from low market adoption, thin analyst validation, and restrictive multi-product bundling with Symantec Enterprise Cloud. IBM Security Verify provides robust identity verification, adaptive risk-based authentication, and reverse-proxy Application Gateway enforcement that secures access to private web applications and APIs without requiring legacy network VPNs or proprietary perimeter lock-in.

## IBM PRIMARY - Product Name (The Replacement)

IBM Security Verify (with Verify Access & Application Gateway)

## IBM PRIMARY - Product Description

IBM Security Verify is IBM's cloud-native and hybrid identity, access management, and Zero Trust access control platform. Through its Verify Access Application Gateway component, it enables secure, identity-driven, least-privilege access to on-premises and private cloud web applications without network-level VPN exposure.

- **Application-level, agentless access** — IBM Security Verify Access provides an agentless Application Gateway that reverse-proxies private enterprise web applications and APIs, enforcing granular per-URL access policies without exposing the underlying network.
- **Identity provider integration** — IBM Security Verify functions as a comprehensive enterprise Identity-as-a-Service (IDaaS) and identity provider, supporting seamless federation via SAML 2.0, OpenID Connect (OIDC), and multi-directory identity bridging.
- **Cloud SWG and DLP integration** — IBM Security Verify integrates directly with IBM Guardium Data Security Center and third-party Secure Web Gateways (SWG) using standard ICAP and REST APIs to evaluate real-time data loss risks during user sessions.
- **Expanded connection types** — IBM Security Verify supports diverse access methods including web applications, REST APIs, and contextual session controls, while integrating with modern remote desktop and virtual desktop infrastructure (VDI) access brokers.

## IBM PRIMARY - IBM Product Page URL

https://www.ibm.com/products/security-verify

## Customer Reference

(not provided)
## IBM SECONDARY - Product Name (Supporting Product, where recommended to compliment the Primary capability)

(not provided)

## IBM SECONDARY - Product Description

(not provided)

## IBM SECONDARY - Product Page(s) URL

https://www.ibm.com/products/security-verify

# Sources:

## IBM Security Verify

- IBM Security Verify Product Overview: https://www.ibm.com/products/security-verify
- IBM Security Verify Access Application Gateway Documentation: https://www.ibm.com/docs/en/sva/10.0.0?topic=overview-application-gateway
- Gartner Magic Quadrant for Access Management (IBM Evaluation): https://www.gartner.com/reviews/market/access-management/vendor/ibm/product/ibm-verify

## Sources: Analyst reviews and exist strategy

- Gartner Peer Insights, 'Symantec Enterprise Cloud' product page (gartner.com/reviews)
- comparative review volumes on the same platform
- dope.security, 'Symantec WSS Alternatives in 2026: Migrating Off Broadcom's Legacy Proxy Without a Six-Month Engagement' (https://dope.security/post/symantec-wss-alternatives-2026) [vendor-authored competitive content, different Symantec product]

## General Sources:

- About Zero Trust Network Access (ZTNA): https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/ztna/1-0/about-secure-access-cloud.html
- What's New in Symantec ZTNA: https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/ztna/1-0/what-is-new.html
- Symantec ZTNA - Broadcom Service Status: https://status.broadcom.com/services/symantec-ztna

## Change history:

### 2026-09-20 - Analyst Cautions and Industry Findings rewritten as a narrative
- Rewrote the section as a narrative.
- Recorded that no named organisation has publicly left the product. Noted a competitor's guide on leaving a different Symantec cloud service.
- Moved all citations to the Sources: Analyst reviews and exist strategy section.


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
