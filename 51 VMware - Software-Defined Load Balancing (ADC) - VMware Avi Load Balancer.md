# VMware Avi Load Balancer

## Status 

Draft

## Broadcom Software Type

VMware

## Broadcom Product Category

Software-Defined Load Balancing (ADC)

## Broadcom Product Name

VMware Avi Load Balancer

## Broadcom Product Description - Key Features

VMware Avi Load Balancer is a software-defined Layer 4-7 application delivery controller. Releases include 31.2.3 (3 August 2026) and 32.1.3.

Key features:

1. **Load balancing and ADC** - Layer 4-7.
2. **Post-quantum cryptography** - 31.2.1.
3. **Crypto offload** - Intel QAT.
4. **WAF** - Evaluation mode.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

The evidence base for organisations actively exiting Avi Load Balancer specifically is thinner than for the core hypervisor, storage and networking layers of the VMware stack. Most available trade and vendor documentation in 2025-2026 in fact describes migration activity moving in the opposite direction, from F5 BIG-IP to Avi, reflecting Broadcom's active promotion of Avi as an F5 replacement within VCF rather than customers leaving Avi. Broadcom has restructured Avi licensing tiers and discontinued the Basic edition, which is a genuine, documented commercial change increasing minimum spend for smaller deployments, but this should not be characterised as an active exodus from the product. Where organisations do reconsider Avi, it is typically as part of a broader VCF exit decision rather than a standalone one. The alternative currently listed, IBM Cloud Load Balancer/VPC Load Balancer, is a hyperscaler-native service tied to IBM Cloud and is not a realistic on-premises or private-cloud ADC substitute for Avi; genuine like-for-like alternatives are F5 BIG-IP/NGINX, Citrix ADC, HAProxy Enterprise, or Kemp, and the recommended alternative in columns G and H should be reconsidered.

Sources: Broadcom Knowledge Base, 'VMware Avi Load Balancer Basic Edition: End of Availability & End of General Support Notice'; Broadcom TechDocs, 'F5 to Avi Load Balancer Migration Workflow', which documents inbound rather than outbound migration activity.

## IBM Replacement Strength

Yes

## IBM Replacement Strategy - Why IBM over Broadcom

IBM

## IBM PRIMARY - Product Name (The Replacement)

IBM Cloud Load Balancer / VPC Load Balancer

## IBM PRIMARY - Product Description 

(not provided)

## IBM PRIMARY - IBM Product Page URL

https://www.ibm.com/cloud/load-balancer

## Customer Reference

(not provided)
## IBM SECONDARY - Product Name (Supporting Product, where recommended to compliment the Primary capability)

(not provided)

## IBM SECONDARY - Product Description

(not provided)

## IBM SECONDARY - Product Page(s) URL

https://www.ibm.com/cloud/load-balancer

# Sources:

## Sources: Analyst reviews and exist strategy

Corrected the row's overall framing: available evidence shows migration activity is predominantly moving toward Avi from F5, not away from it, and flagged that IBM Cloud Load Balancer in column H is not a credible on-premises substitute for this capability.

## General Sources:

- Release Notes for Avi 31.2.1: https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/avi-load-balancer/avi-load-balancer/31-2/vmware-avi-load-balancer-release-notes/release-notes-for-avi-load-balancer-version-31-2-1.html
- Release Notes for Avi 32.1.3: https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/avi-load-balancer/avi-load-balancer/32-1/vmware-avi-load-balancer-release-notes/release-notes-for-avi-load-balancer-version-32-1-3.html
- Avi release notifications: https://knowledge.broadcom.com/external/article/312808/vmware-avi-load-balancer-release-notific.html

## Change history:

### 2026-09-19 - Broadcom product information review
- Product description: Updated to 31.2.x and 32.1.x.
- Summary and numbered list of four key features rewritten from current Broadcom sources.
- General Sources: 3 sources recorded (Broadcom TechDocs, product pages, press releases where available).
