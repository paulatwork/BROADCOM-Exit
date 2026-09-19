# SiteMinder

## Status 

Draft

## Broadcom Software Type

Cyber Security

## Broadcom Product Category

Identity and Access Management

## Broadcom Product Name

SiteMinder

## Broadcom Product Description (Key Features) (This is important to get right)

Symantec SiteMinder is a web access management and federation platform. Release 12.9 is now documented (with a 12.9.1 service pack listed), following 12.8.08. Version 12.9 adds Windows Server 2025 support, native ODBC drivers, vault provider integration and expanded federation and VIP Authentication Hub integration.

Key features:

1. **Web access management and SSO** - Policy-based authentication and authorisation for web applications, including a new external authentication provider scheme.
2. **Federation and token management** - SAML 2.0, OAuth 2.0 and OIDC with expanded configuration, JWT key pair management, JWKS endpoint improvements and federation REST APIs.
3. **Vault integration (12.9)** - Passwords for SiteMinder stores can be held in a vault, with out-of-the-box Symantec PAM integration and an API for custom providers.
4. **Platform and identity integration** - Enhanced VIP Authentication Hub integration, native ODBC drivers for Oracle, MySQL, PostgreSQL, SQL Server, Azure and Db2, Windows Server 2025 support, and container deployment (from 12.8.08 CR01).

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

SiteMinder holds a 4.0 out of 5 rating on Gartner Peer Insights from 36 reviews. Reviewers describe it as stable and straightforward to administer without requiring specialised certification, but consistently note that its user interface and experience are dated, with one reviewer stating the user experience is '2-3 generations behind' comparable modern access management products and in need of a complete refresh.

There is a well-established, named market of vendors selling migration tooling and services specifically to move organisations off SiteMinder and other legacy WAM platforms, including Okta ('CA SiteMinder Migration Guide' and 'WAM Modernization and Migration Guide'), Strata.io ('How to move from SiteMinder to Okta'), and Datawiza. The existence of dedicated, named migration products from multiple independent vendors is a reasonable indicator of an active exit trend for this product category, distinct from a formal analyst ranking.

No independent Gartner Magic Quadrant or Forrester Wave placement specific to SiteMinder as a standalone product was identified. Gartner's Access Management category on Peer Insights shows it rated and reviewed at materially lower volume than newer competitors in the same category (for example Okta Workforce Identity and Microsoft Entra ID each carry several hundred more reviews at the time of this review).

Broadcom's bundled licensing and core-account commercial strategy apply to SiteMinder as part of the wider identity portfolio.

Sources: Gartner Peer Insights, 'Symantec SiteMinder Reviews & Ratings' (gartner.com/reviews); Okta, 'CA SiteMinder Migration Guide' and 'WAM Modernization and Migration Guide' (okta.com); Strata.io, 'How to move from SiteMinder to Okta' (strata.io).

## IBM Replacement Strength

(not provided)

## IBM Replacement Strategy - Why IBM over Broadcom

(not provided)

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

(not provided)

## Sources: Analyst reviews and exist strategy

Column E previously contained only a two-word placeholder ('Reverse proxy access management gateway'). Replaced with researched, sourced content covering real Peer Insights ratings and quotes and the existence of a named third-party SiteMinder migration tooling market. Expanded and tightened Column D with a sentence on typical deployment pattern.

## General Sources:

- New Features in 12.8.08: https://techdocs.broadcom.com/us/en/symantec-security-software/identity-security/siteminder/12-8/release-notes/New-Features/new-features-in-12-8-08.html
- Symantec SiteMinder 12.9: https://techdocs.broadcom.com/us/en/symantec-security-software/identity-security/siteminder/12-9.html
- SiteMinder Capabilities: https://techdocs.broadcom.com/us/en/symantec-security-software/identity-security/siteminder/12-8/getting-started/siteminder-capabilities.html
- New Features in 12.9: https://techdocs.broadcom.com/us/en/symantec-security-software/identity-security/siteminder/12-9/release-notes/New-Features/new-features-in-12-9.html

## Change history:

### 2026-09-19 - Broadcom product information verification (WebFetch pass, files 02-39)
- Corrected the current release: SiteMinder 12.9 documentation is published (12.9 features verified; a 12.9a release adds OpenShift routes), so 12.8.08 was no longer the latest. Description and key features rewritten. The 12.9.1 release date could not be confirmed (a Broadcom article gave a tentative early Q2 2026 schedule, and the page was no longer retrievable).

### 2026-09-19 - WebFetch verification pass
- Verified with WebFetch: documentation for SiteMinder 12.9 and 12.9.1 exists, so 12.8.08 is not the latest line. Release dates and 12.9 features could not be retrieved from the navigation pages and remain unreviewed. The feature list still describes 12.8.08.

### 2026-09-19 - Broadcom product information review
- Product description: Added 12.8.08 features and noted that a 12.9 documentation set exists. 12.9 features were not reviewed.
- Summary and numbered list of four key features rewritten from current Broadcom sources.
- General Sources: 3 sources recorded (Broadcom TechDocs, product pages, press releases where available).

### 2026-09-19 - IBM alternative product verification and sentiment (WebFetch and WebSearch pass, files 02-39)
- Requirement match against the Key Features section: Meets most requirements.
- Confirmed: web single sign-on and access management, with Verify Access (formerly ISAM) supporting SAML 2.0, OpenID Connect and OAuth 2.0 federation, and the IBM Application Gateway extending modern authentication to legacy applications without code changes.
- Not verified: vault integration for directory passwords, native ODBC drivers and Windows Server 2025 equivalents. The on-premises IBM Security Verify Access is the closer SiteMinder match; the file names IBM Security Verify generically.
- Sentiment: added a one-sentence summary of general market sentiment at the start of the Key Product Capability Statement. Existing statement text was not changed.
- Sources: https://www.ibm.com/products/verify; https://www.ibm.com/support/pages/system/files/inline-files/verifyaccess_productoverview_3.pdf
