# PAM (CA Privileged Access Manager, Symantec PAM)

## Status 

Draft

## Broadcom Software Type

Cyber Security

## Broadcom Product Category

Identity and Access Management

## Broadcom Product Name

PAM (CA Privileged Access Manager, Symantec PAM)

## Broadcom Product Description - Key Features

Symantec Privileged Access Manager (PAM, formerly CA PAM) manages privileged accounts. TechDocs lists version 4.3.2 as the newest (versions 4.3.2, 4.3.1, 4.3 and 4.2.x); the 4.3.1 landing page was updated on 14 September 2026. Version 4.3 added VMware Cloud Foundation credential integration.

Key features:

1. **Credential vaulting and rotation** - Central management and automated password rotation for privileged accounts.
2. **VCF integration** - 4.3 centralises VCF credential management and enforces privileged access controls.
3. **Threat analytics** - PAM Threat Analytics is documented for 4.3.1.
4. **Operational tooling** - Upgrade Utility for hotfixes and service packs, and Azure password composition policies.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

The strongest verified fact in this entry belongs to a competitor. Gartner has named Delinea a Leader in its Magic Quadrant for privileged access management for seven consecutive years, including 2025. Several independent wire services carried Delinea's announcement, though the Gartner report itself could not be opened, so the claim is well supported but second-hand.

Broadcom's own position is harder to pin down. Earlier drafts called Symantec PAM a 'Niche Player or Challenger', but that could only be partly confirmed. In the 2021 and 2022 quadrants, the years with a full vendor list to check, Broadcom's Symantec was placed as a Niche Player and not a Challenger, and one 2022 analysis described it as holding 'pole position' among niche players thanks to its privileged elevation and delegation capability across Windows, Linux, UNIX and mainframe. Searches for the 2024 and 2025 quadrants did not find Broadcom or Symantec in the vendor lists published by BeyondTrust, Segura or other participants, which suggests it may no longer be included at all. That is an open point that could not be confirmed against the Gartner report.

Users are more generous than the analysts. Gartner Peer Insights gives Symantec Privileged Access Manager 4.2 out of 5 from 78 reviews, with reviewers valuing session monitoring and audit logging but marking down support responsiveness and integration. PeerSpot reviewers say support was good under CA and has slipped under Broadcom, with tickets often answered by pointing to documentation, and some rate Delinea and BeyondTrust as stronger on features.

No named organisation has publicly described leaving Symantec PAM, and searches for migration case studies to CyberArk, Delinea or BeyondTrust found none. Broadcom's core-account strategy and bundled licensing apply as elsewhere in the Symantec portfolio. Enterprises replacing Symantec and CA PAM are choosing Delinea, CyberArk, BeyondTrust or, for machine and non-human credentials, HashiCorp Vault.

## IBM Replacement Strength

Strong Replacement, with improved outcomes

## IBM Replacement Strategy - Why IBM over Broadcom

IBM Security Verify Privilege Vault (powered by Delinea Secret Server, a 7-time consecutive Gartner Magic Quadrant Leader) alongside IBM HashiCorp Vault replaces Broadcom Symantec PAM (CA PAM). Broadcom has relegated Symantec PAM to niche status with declining analyst standing, complex appliance upgrades, and steep renewal pricing. IBM delivers an enterprise-proven privileged access platform for human admins and non-human machine secrets, providing automated credential rotation, session recording, and multi-cloud infrastructure governance at lower operational complexity and total cost.

## IBM PRIMARY - Product Name (The Replacement)

IBM Security Verify Privilege Vault (with IBM HashiCorp Vault)

## IBM PRIMARY - Product Description

IBM Security Verify Privilege Vault (built on Delinea technology) and IBM HashiCorp Vault provide an enterprise Privileged Access Management (PAM) and secrets management solution for securing privileged credentials, administrative sessions, and machine identities across hybrid IT environments.

- **Credential vaulting and rotation** — IBM Security Verify Privilege Vault provides automated discovery, encrypted vaulting, and scheduled or check-in/check-out password rotation for domain admin, database, and service accounts.
- **VCF integration** — IBM Security Verify Privilege Vault centrally manages and enforces privileged credentials and API keys across virtualized environments (including VMware Cloud Foundation, Red Hat OpenShift, and public clouds).
- **Threat analytics** — IBM Security Verify Privilege Vault delivers real-time behavioral analytics, monitoring privileged user session activities, detecting anomalous credential usage, and automatically terminating suspicious sessions.
- **Operational tooling** — IBM Security Verify Privilege Vault provides streamlined automated update mechanisms, granular password complexity policy enforcement, and comprehensive audit reporting across on-premises and multi-cloud estates.

## IBM PRIMARY - IBM Product Page URL

https://www.ibm.com/products/verify-privilege-vault

## Customer Reference
(not provided)
## IBM SECONDARY - Product Name (Supporting Product, where recommended to compliment the Primary capability)

IBM HashiCorp Vault

## IBM SECONDARY - Product Description

Solving Non-Human Identity PAM.

## IBM SECONDARY - Product Page(s) URL

https://www.ibm.com/products/security-verify

# Sources:

## IBM Security Verify Privilege Vault

- IBM Security Verify Privilege Vault Product Overview: https://www.ibm.com/products/verify-privilege-vault
- IBM Security Verify Privilege Solutions Guide: https://www.ibm.com/downloads/documents/us-en/107a02e94dc8f96e
- Gartner Magic Quadrant for Privileged Access Management (Delinea Leader): https://www.gartner.com/reviews/market/privileged-access-management/vendor/delinea

## Sources: Analyst reviews and exist strategy

- Delinea, 'Delinea Named a Leader in 2025 Gartner Magic Quadrant for Privileged Access Management for Seventh Consecutive Time' (delinea.com; globenewswire.com)
- SolutionsReview, 'What's Changed: 2022 Magic Quadrant for Privileged Access Management' and 'Analysis: the 2021 Gartner Magic Quadrant for Privileged Access Management'
- Gartner Peer Insights, Symantec Privileged Access Management product page (4.2/5, 78 reviews)
- PeerSpot, 'Symantec Privileged Access Manager Reviews, Competitors and Pricing' (https://www.peerspot.com/products/symantec-privileged-access-manager-reviews)
- PeerSpot, 'Symantec Privileged Access Manager: Pros and Cons 2026' (https://www.peerspot.com/products/symantec-privileged-access-manager-pros-and-cons)

## General Sources:

- New Features and Enhancements in 4.3: https://techdocs.broadcom.com/us/en/symantec-security-software/identity-security/privileged-access-manager/4-3/release-information/new-features-and-enhancements-in-4-3.html
- Symantec PAM v4.3 GA Announcement: https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/ReleaseAnnouncements/Symantec-Privileged-Access-Manager-v4-3-GA-Announcement/36165
- Symantec Privileged Access Manager 4.3.1: https://techdocs.broadcom.com/us/en/symantec-security-software/identity-security/privileged-access-manager/4-3-1.html
- Symantec Privileged Access Manager 4.3.1 (version list): https://techdocs.broadcom.com/us/en/symantec-security-software/identity-security/privileged-access-manager/4-3-1.html

## Change history:

### 2026-09-20 - Analyst Cautions and Industry Findings rewritten as a narrative
- Rewrote the section as a narrative.
- Added PeerSpot reviewer commentary on support since the Broadcom acquisition.
- Searched for named organisations that replaced Symantec PAM (2026-09-20). None was found, and the text now says so.
- Moved all citations to the Sources: Analyst reviews and exist strategy section and removed the earlier column notes from that section.


### 2026-09-19 - Broadcom product information verification (WebFetch pass, files 02-39)
- Corrected the current version: TechDocs lists 4.3.2, so 4.3.1 was not the newest. The 4.3.2 feature list was not retrieved, so the key features are unchanged.

### 2026-09-19 - Broadcom product information review
- Product description: Added 4.3 features. Session recording detail was not reconfirmed in this review.
- Summary and numbered list of four key features rewritten from current Broadcom sources.
- General Sources: 3 sources recorded (Broadcom TechDocs, product pages, press releases where available).

### 2026-09-19 - IBM alternative product verification and sentiment (WebFetch and WebSearch pass, files 02-39)
- Requirement match against the Key Features section: Meets requirements.
- Confirmed: credential vaulting, password rotation and expiry with check-in and check-out, session recording (SessionConnector), and management of human, machine and AI identities. Verify Privilege Vault is the IBM-resold Delinea Secret Server, and Delinea was named a Leader in the 2025 Gartner Magic Quadrant for PAM for the seventh consecutive time.
- Not verified: VMware Cloud Foundation credential integration, and the file's claim that Broadcom is positioned as a Niche Player or Challenger. Analytics is offered as an optional extension (Privilege Vault Analytics).
- Sentiment: added a one-sentence summary of general market sentiment at the start of the Key Product Capability Statement. Existing statement text was not changed.
- Sources: https://www.ibm.com/products/verify-privilege-vault; https://www.ibm.com/downloads/documents/us-en/107a02e94dc8f96e; https://www.gartner.com/reviews/market/privileged-access-management/vendor/delinea
