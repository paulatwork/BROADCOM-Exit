# VCF Networking, NSX

## Status 

Draft

## Broadcom Software Type

VMware

## Broadcom Product Category

Software-Defined Networking & Security

## Broadcom Product Name

VCF Networking, NSX

## Broadcom Product Description - Key Features

VCF Networking (NSX) provides VPC-based networking, transit gateways, and distributed security. VCF 9.1 adds multiple transit gateways per tenant, a virtual network appliance and native EVPN VXLAN.

Key features:

1. **VPC networking** - Consumed from vCenter, VKS and VCF Automation.
2. **Transit gateway flexibility** - Multiple gateways per tenant (9.1).
3. **Native EVPN VXLAN** - Route controller VM.
4. **Direct hardware access** - NVIDIA ConnectX and BlueField adapters.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

NSX is widely regarded, including in independent security commentary, as one of the most difficult layers of the VMware stack to exit. Distributed firewall policy objects, tags, groups and overlay network configurations are tightly coupled to the VMware control plane; specialist microsegmentation vendor ColorTokens describes these policies as encoding years of accumulated knowledge about application dependencies, trust boundaries and risk tolerance, with no automated cross-vendor export path, requiring manual policy re-authoring during migration. Standalone NSX licensing was eliminated in 2023, so customers who want NSX at all must purchase full VCF. Genuine like-for-like alternatives for VM-centric microsegmentation and network virtualisation include Cisco ACI, Illumio and Calico Enterprise; Red Hat's OpenShift networking stack (OVN-Kubernetes, Cilium) is Kubernetes-native and only replaces NSX's function where workloads are also being containerised onto OpenShift, so it should not be presented as a direct substitute for NSX in VM-only environments. Gartner's September 2025 guidance recommended selective, application-by-application replatforming over wholesale network re-architecture given the effort involved.

Sources: ColorTokens, 'Rethinking Microsegmentation During a VMware NSX Exit'; The Register, 'VMware to lose 35 percent of workloads in three years' (Gartner Symposium coverage, September 2025); Broadcom TechDocs migration guidance on distributed firewall configuration.

## IBM PRIMARY - Product Name (The Replacement)

OpenShift networking + partner networking

## IBM PRIMARY - IBM Product Page URL

https://www.redhat.com/en/technologies/cloud-computing/openshift/platform-plus

## IBM Replacement Strength

Yes

## IBM Replacement Strategy (Short)

Red Hat OpenShift networking, with partner networking, replaces VCF Networking and NSX for Kubernetes-based workloads.

## IBM Replacement Strategy (Description - Why IBM over Broadcom)

Red Hat

## IBM PRIMARY - Product Description 

(not provided)

## Customer Reference

(not provided)
## IBM SECONDARY - Product Name (Supporting Product, where recommended to compliment the Primary capability)

(not provided)

## IBM SECONDARY - Product Description

(not provided)

## IBM SECONDARY - Product Page(s) URL

https://www.redhat.com/en/technologies/cloud-computing/openshift/platform-plus

# Sources:

## Sources: Analyst reviews and exist strategy

Replaced the direct quotation with a paraphrase per style guidance, added a genuine source (ColorTokens) for the migration-complexity claim as requested, and flagged that OpenShift networking only substitutes for NSX where workloads move to containers, a limitation on the column G/H alternative.

## General Sources:

- NSX What's New 9.0: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-nsx.html
- Network World: VCF 9.1 updates: https://www.networkworld.com/article/4218303/vmware-cloud-foundation-9-1-adds-transit-gateway-flexibility-segmentation-and-native-evpn-vxlan-support.html
- Simplify Workload Connectivity with VCF 9.1: https://blogs.vmware.com/cloud-foundation/2026/05/05/simplify-workload-connectivity-and-enhance-network-scale-and-performance-with-vcf-9-1/

## Change history:
