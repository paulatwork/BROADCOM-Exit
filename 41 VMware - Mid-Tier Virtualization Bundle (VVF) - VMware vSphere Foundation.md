# VMware vSphere Foundation

## Status 

Draft

## Broadcom Software Type

VMware

## Broadcom Product Category

Mid-Tier Virtualization Bundle (VVF)

## Broadcom Product Name

VMware vSphere Foundation

## Broadcom Product Description - Key Features

VMware vSphere Foundation (VVF) 9.x is the mid-tier bundle. Documentation is now part of VCF documentation. Each licensed core includes 0.25 TiB of vSAN capacity. The 9.1 FAQ confirms that vSphere, vSAN and VCF Operations are included, and that NSX, VCF Automation, Kubernetes (VKS), HCX, Live Recovery and Avi Load Balancer are offered separately.

Key features:

1. **vSphere virtualisation** - Core compute layer.
2. **vSAN entitlement** - 0.25 TiB per licensed core, pooled.
3. **VCF Operations** - Included operations tooling.
4. **Unified licensing** - Licensed through a VCF Operations instance and the VCF Business Services console.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

Broadcom TechDocs confirms VVF licensing includes 0.25 TiB of vSAN capacity per physical core, with additional storage requiring a separate add-on licence or a step-up to full VCF. Because VVF and VCF are both licensed on total physical cores with a 16-core-per-CPU minimum, customers with smaller or older, lower-core-count clusters can see a disproportionate increase in licensed core counts relative to previous per-CPU or per-VM entitlements, a pattern widely reported across trade press covering the 2023-2024 licensing transition. A February 2026 CloudBolt survey of 302 North American IT decision-makers found 86 percent of organisations actively reducing VMware footprint, with most reporting cost increases in the 25-49 percent band, materially lower than initial expectations of price doubling, indicating that outcomes vary significantly by account size and negotiating position rather than following a single multiplier. Gartner has advised against wholesale migration for stable environments, recommending selective modernisation instead, and ranked Nutanix and public cloud ahead of Red Hat virtualisation as VMware migration destinations, a relevant consideration given the Red Hat-centric alternative proposed for this row.

Sources: Broadcom TechDocs, 'VMware vSphere Foundation Capacity License for vSAN'; CIO Dive, 'VMware customers shrink deployments in lieu of full-scale migrations' (CloudBolt survey, February 2026); The Register, 'VMware to lose 35 percent of workloads in three years' (September 2025).

## IBM Replacement Strength

Yes

## IBM Replacement Strategy - Why IBM over Broadcom

Red Hat

## IBM PRIMARY - Product Name (The Replacement)

OpenShift Virtualization Engine / OpenShift Platform Plus

## IBM PRIMARY - Product Description 

(not provided)

## IBM PRIMARY - IBM Product Page URL

https://www.redhat.com/en/technologies/cloud-computing/openshift/virtualization-engine

## Customer Reference

(not provided)
## IBM SECONDARY - Product Name (Supporting Product, where recommended to compliment the Primary capability)

(not provided)

## IBM SECONDARY - Product Description

(not provided)

## IBM SECONDARY - Product Page(s) URL

https://www.redhat.com/en/technologies/cloud-computing/openshift/virtualization-engine

# Sources:

## Sources: Analyst reviews and exist strategy

Corrected column D, which incorrectly stated VVF includes Tanzu Standard; current Broadcom documentation confirms VVF bundles vSphere, capacity-limited vSAN, the vSphere IaaS Control Plane and VCF Operations only. Added the verified 0.25 TiB/core figure and the CloudBolt/Gartner evidence to column E.

## General Sources:

- vSphere Foundation 9.0 Documentation: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vsphere-foundation/9-0/vvf-getting-started.html
- 9.0 Product Subscription and Licensing: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/licensing-overview/offerings-and-components.html
- VVF 9.1 FAQ: https://www.vmware.com/docs/vmware-vsphere-foundation-faqs

## Change history:

### 2026-09-19 - WebFetch verification pass
- Verified with WebFetch: 9.1 exclusions confirmed (NSX, Automation, VKS, HCX, Live Recovery, Avi).

### 2026-09-19 - Broadcom product information review
- Product description: Updated to 9.x. Older exclusions confirmed for 9.1 in the later verification pass.
- Summary and numbered list of four key features rewritten from current Broadcom sources.
- General Sources: 3 sources recorded (Broadcom TechDocs, product pages, press releases where available).
