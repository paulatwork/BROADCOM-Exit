# Identity Security Platform (Symantec Identity Security Platform, IDSP)

## Status 

Draft

## Broadcom Software Type

Cyber Security

## Broadcom Product Category

Identity and Access Management

## Broadcom Product Name

Identity Security Platform (Symantec Identity Security Platform, IDSP)

## Broadcom Product Description (Key Features) (This is important to get right)

Symantec Identity Security Platform (IDSP) is a cloud-native, container-based IAM platform (formerly VIP Authentication Hub). Version 4.0 was released on 12 January 2026 and existing deployments and APIs continue to work.

Key features:

1. **Passwordless and adaptive authentication** - FIDO2 biometrics, hardware keys and passkeys, alongside SMS and software authenticators, with adaptive risk evaluation in real time.
2. **Standards-based federation and identity store** - SAML 2.0, OpenID Connect, an integrated identity store with SCIM support and just-in-time provisioning for external identity providers.
3. **API-first policy-driven platform** - OAuth 2.0 authorisation server with custom scopes, personal access tokens, REST APIs and a policy-driven framework without hard-coded logic.
4. **Incremental migration** - Native integration with SiteMinder and other Broadcom products supports gradual modernisation; 4.0 adds an Identity Credential Verifier role.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

IDSP is the renamed VIP Authentication Hub (version 4.0, January 2026) on a cloud-native, container-based architecture. Broadcom documentation says it integrates natively with SiteMinder and other Broadcom solutions to allow gradual migration, rather than replacing them outright. A distinct Gartner Peer Insights or Magic Quadrant entry specific to 'Identity Security Platform' or 'IDSP' by name was not identified in this research; Gartner Peer Insights instead lists separate entries for related component products such as 'Symantec IGA,' which limits the ability to independently verify adoption or satisfaction levels for the consolidated IDSP platform itself. This should be stated plainly rather than implying broad analyst coverage exists.

Customers of Broadcom's identity portfolio more broadly report high administrative overhead from fragmented management consoles spanning multiple legacy products, and steep renewal pricing under Broadcom's bundled licensing model; this is consistent with Broadcom's documented general commercial pattern rather than an IDSP-specific finding.

Organisations modernising identity and access management away from Broadcom's identity portfolio are generally consolidating onto unified, cloud-native IAM/CIAM platforms with substantial independent analyst coverage and market share, including Microsoft Entra ID, Okta Workforce Identity Cloud, Ping Identity, and IBM Security Verify.

Sources: Broadcom TechDocs, 'About Symantec Identity Security Platform (IDSP)' (techdocs.broadcom.com); Redress Compliance, 'Symantec Enterprise Software Licensing Under Broadcom: A CIO Playbook'; no distinct Gartner or Forrester coverage of IDSP by name was located in this research.

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

Substantially expanded Column D with real, sourced product detail (AuthHub, FIDO2, OAuth, adaptive risk, SCIM identity store) drawn from Broadcom's own technical documentation, replacing the previous bare feature-name list. Corrected Column E to state plainly that no distinct analyst coverage of IDSP by name was found.

## General Sources:

- Release Notes - 4.0: https://techdocs.broadcom.com/us/en/symantec-security-software/identity-security/identity-security-platform/4-0/isp-release-notes/release-notes--4-0.html
- About Symantec Identity Security Platform: https://techdocs.broadcom.com/us/en/symantec-security-software/identity-security/identity-security-platform/4-0/Getting-Started.html
- Rebranding Announcement: https://techdocs.broadcom.com/us/en/symantec-security-software/identity-security/vip-authentication-hub/IDSP-Versions/information-about-idsp-releases.html
- About Symantec Identity Security Platform (4.0): https://techdocs.broadcom.com/us/en/symantec-security-software/identity-security/identity-security-platform/4-0/Getting-Started.html

## Change history:

### 2026-09-19 - Broadcom product information verification (WebFetch pass, files 02-39)
- Analyst Cautions: corrected the statement that IDSP consolidates SiteMinder and VIP components. Broadcom documentation says IDSP is the renamed VIP Authentication Hub and integrates natively with SiteMinder for gradual migration (integration, not replacement).
- Description: restored verified capabilities removed in the previous pass (SCIM identity store, adaptive risk, SAML 2.0 and OIDC, just-in-time provisioning) and reworded the migration statement.

### 2026-09-19 - Broadcom product information review
- Product description: Added rebrand from VIP Authentication Hub, version 4.0 and its features. Removed the unverified SCIM and adaptive-risk details.
- Summary and numbered list of four key features rewritten from current Broadcom sources.
- General Sources: 3 sources recorded (Broadcom TechDocs, product pages, press releases where available).

### 2026-09-19 - IBM alternative product verification and sentiment (WebFetch and WebSearch pass, files 02-39)
- Requirement match against the Key Features section: Meets most requirements.
- Confirmed: passwordless (FIDO2 and QR) authentication, adaptive risk evaluation, and containerised directory and OIDC provider options. SAML 2.0, OpenID Connect and OAuth 2.0 are supported by Verify Access; SCIM is referenced mainly through adjacent components.
- Not verified: a Broadcom-style incremental migration path from SiteMinder and an Identity Credential Verifier equivalent.
- Sentiment: added a one-sentence summary of general market sentiment at the start of the Key Product Capability Statement. Existing statement text was not changed.
- Sources: https://www.ibm.com/products/verify; https://www.ibm.com/support/pages/system/files/inline-files/verifyaccess_config_federation_2.pdf; https://www.gartner.com/reviews/market/access-management/vendor/ibm/product/ibm-verify
