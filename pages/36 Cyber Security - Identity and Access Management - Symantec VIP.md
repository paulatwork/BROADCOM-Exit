# Symantec VIP

## Page Status 

Draft

## Broadcom Software Type

Cyber Security

## Broadcom Product Category

Identity and Access Management

## Broadcom Product Name

Symantec VIP

## Broadcom Product Description - Key Features

Symantec VIP is a cloud MFA and risk-based authentication service. VIP Authentication Services 2026.March.01 was the latest release located.

Key features:

1. **Multi-factor authentication** - Push, OTP tokens and FIDO2.
2. **Risk-based access** - Adaptive risk evaluation and device fingerprinting.
3. **Microsoft ecosystem MFA** - 2026.March.01 updates for Azure and Entra ID MFA.
4. **Standards** - Improved SAML validation and updated endpoint certificates.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

Symantec VIP is better liked than most of the portfolio. Gartner Peer Insights gives it a strong 4.5 out of 5 from 80 reviews, with users praising reliable, fast two-factor authentication and easy integration, though some report occasional session timeouts and missed push notifications. An earlier draft claimed limited passwordless FIDO2 support, but Broadcom's own documentation lists FIDO2 support, so that claim has been dropped. No independent Magic Quadrant or Forrester Wave covers VIP as a standalone product.

The reason to leave is architectural, not a complaint about quality. Enterprises are folding standalone multi-factor authentication into their main cloud identity provider and cutting the number of authentication vendors and licences they manage. One university shows how that looks in practice. Michigan State University announced in October 2021 that Okta Verify would replace the Symantec VIP mobile app, which would stop working for most of its applications on 5 December 2021. The announcement does not give reasons, so it should be read as an example of the consolidation trend and not as a verdict on VIP.

Broadcom's bundled licensing and core-account strategy apply to VIP as they do across the Symantec identity portfolio. There is a practical incentive as well. An organisation already leaving SiteMinder, IDSP or Carbon Black has reason to retire VIP at the same time to reduce the number of Broadcom contracts coming up for renewal.

The destinations are Microsoft Entra ID with Authenticator and FIDO2 keys, Cisco Duo Security, Okta Verify and IBM Security Verify.

## IBM PRIMARY - Product Name (The Replacement)

IBM Security Verify (Adaptive MFA & Passwordless)

## IBM PRIMARY - IBM Product Page URL

https://www.ibm.com/products/security-verify

## IBM Replacement Strength

Strong Replacement, with improved outcomes

## IBM Replacement Strategy (Short)

Verify consolidates MFA, passkeys, adaptive risk and SSO in one platform, ending standalone VIP renewals.

## IBM Replacement Strategy (Description - Why IBM over Broadcom)

IBM Security Verify replaces Broadcom Symantec VIP by providing modern, cloud-native multi-factor authentication (MFA) and adaptive access integrated into a unified Identity-as-a-Service (IDaaS) platform. Rather than maintaining Symantec VIP as a standalone MFA silo subject to Broadcom's bundled renewal increases, migrating to IBM Security Verify consolidates MFA, passwordless FIDO2 passkeys, adaptive AI risk signals, and SSO into a single manageable platform, lowering administrative complexity and per-user subscription costs.

## IBM PRIMARY - Product Description

IBM Security Verify delivers enterprise Multi-Factor Authentication (MFA), passwordless passkeys, and risk-based adaptive access controls designed to secure workforce and customer identities across hybrid cloud and on-premises environments.

- **Multi-factor authentication** — IBM Security Verify supports comprehensive MFA methods including push notifications via IBM Verify mobile app, time-based one-time passwords (TOTP), SMS/voice OTP, and FIDO2-certified biometric passkeys and security keys.
- **Risk-based access** — IBM Security Verify incorporates AI-powered adaptive risk engines that evaluate user context, device fingerprinting, IP reputation, behavioral anomalies, and geolocation in real time to challenge or grant access dynamically.
- **Microsoft ecosystem MFA** — IBM Security Verify provides native integration and identity federation with Microsoft Azure / Entra ID, Windows Hello for Business, and Microsoft 365 environments to enforce conditional MFA.
- **Standards** — IBM Security Verify adheres to industry standards with robust SAML 2.0, OpenID Connect, OAuth 2.0 validation, and automated PKI certificate management.

## Customer Reference

(not provided)
## IBM SECONDARY - Product Name (Supporting Product, where recommended to compliment the Primary capability)

(not provided)

## IBM SECONDARY - Product Description

(not provided)

## IBM SECONDARY - Product Page(s) URL

(not provided)

# Sources:

## IBM Security Verify (Adaptive MFA)

- IBM Security Verify Authentication & MFA Overview: https://www.ibm.com/products/security-verify
- IBM Documentation — Multifactor Authentication in IBM Security Verify: https://www.ibm.com/docs/en/security-verify
- Gartner Magic Quadrant for Access Management (IBM Leader): https://www.gartner.com/reviews/market/access-management/vendor/ibm/product/ibm-verify

## Sources: Analyst reviews and exist strategy

- Gartner Peer Insights, 'Symantec VIP Reviews & Ratings' (gartner.com/reviews)
- Broadcom Symantec VIP product documentation (for FIDO2 capability)
- Michigan State University Technology, 'New MFA mobile app: Okta Verify to replace Symantec VIP' (https://tech.msu.edu/news/2021/10/new-mfa-mobile-app-okta-verify-to-replace-symantec-vip)

## General Sources:

- VIP Authentication Services 2026.March.01 announcement: https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/ReleaseAnnouncements/General-Availability-Announcement---Symantec-VIP-Authentication-Services-2026-March-01/37328
- Symantec VIP (product page): https://www.broadcom.com/products/identity/vip
- About FIDO authenticators - Symantec VIP: https://techdocs.broadcom.com/us/en/symantec-security-software/identity-security/vip/cloud/vip-web-services-and-apis-v127046027-d2278e2328/VIP-User-Services-Developer-s-Guide/about-vip-v99979554-d2386e8/about-fido-authenticators.html

## Change history:
