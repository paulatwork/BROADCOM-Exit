# VCF Private AI Services

## Status 

Draft

## Broadcom Software Type

VMware

## Broadcom Product Category

Private AI & ML Infrastructure Stack

## Broadcom Product Name

VCF Private AI Services

## Broadcom Product Description - Key Features

VCF Private AI Services runs AI model serving on VCF. VCF 9.1.1 (3 September 2026) adds shared models across tenants; an AI gateway is preview only and other capabilities are reserved for future releases.

Key features:

1. **Model Runtime** - Serves models on-premises.
2. **Multi-tenant model sharing** - 9.1.1.
3. **GPU support** - AMD DirectPath I/O and NVIDIA-certified hypervisor.
4. **AI gateway (preview)** - Access to over 150 models, preview only.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

This is a genuinely current Broadcom product, confirmed by Broadcom's technical documentation and 2025-2026 product announcements around VCF 9.1's AI capabilities; it should not be conflated with VMware Private AI Foundation with NVIDIA, a related but separate offering. Because it requires full VCF licensing plus specialised GPU host configurations, it inherits the same subscription and minimum-core cost structure as the rest of VCF. Independent, product-specific commentary on customers exiting this particular capability is minimal given how recently it has been introduced; the applicable evidence is the general VCF licensing and lock-in concerns documented elsewhere in this review rather than AI-specific migration case studies. Red Hat OpenShift AI is a genuine, actively developed competing platform for container-native AI and machine learning workloads, and IBM watsonx addresses foundation model governance and lifecycle management; both are realistic alternatives, though GPU driver and hardware-partner support parity should be confirmed before treating this as a like-for-like substitution, since Broadcom has published multi-vendor GPU and CPU partnership announcements, including with NVIDIA, specific to VCF 9.1.

Sources: Broadcom VCF 9.1 product announcements and TechDocs on VCF Private AI Services and Private AI Foundation with NVIDIA (blogs.vmware.com/cloud-foundation, techdocs.broadcom.com).

## IBM PRIMARY - Product Name (The Replacement)

Red Hat OpenShift AI + IBM watsonx

## IBM PRIMARY - IBM Product Page URL

https://www.redhat.com/en/technologies/ai/openshift-ai

## IBM Replacement Strength

Yes

## IBM Replacement Strategy (Short)

OpenShift AI and IBM watsonx replace VCF Private AI Services, combining Red Hat and IBM.

## IBM Replacement Strategy (Description - Why IBM over Broadcom)

Red Hat + IBM

## IBM PRIMARY - Product Description 

(not provided)

## Customer Reference

(not provided)
## IBM SECONDARY - Product Name (Supporting Product, where recommended to compliment the Primary capability)

(not provided)

## IBM SECONDARY - Product Description

(not provided)

## IBM SECONDARY - Product Page(s) URL

https://www.redhat.com/en/technologies/ai/openshift-ai

# Sources:

## Sources: Analyst reviews and exist strategy

Confirmed the product name and current status against Broadcom's own 2026 documentation, and added a distinction from the separately-branded Private AI Foundation with NVIDIA to avoid conflating the two offerings.

## General Sources:

- VCF 9.1: Private Cloud Platform for Production AI: https://blogs.vmware.com/cloud-foundation/2026/05/05/vcf-9-1-secure-cost-effective-private-cloud-platform-for-production-ai/
- Explore 2026: VMware AI Factory: https://blogs.vmware.com/cloud-foundation/2026/09/03/explore-2026-vmware-ai-factory-and-other-new-ai-innovations-in-vcf/
- VMware Private AI Services Release Notes: https://techdocs.broadcom.com/us/en/vmware-cis/private-ai/foundation-with-nvidia/9-0/private-ai-release-notes/vmware-private-ai-services-release-notes.html
- eWeek: VCF 9.1.1 Adds Shared AI Models: https://www.eweek.com/news/vmware-vcf-shared-ai-models/

## Change history:
