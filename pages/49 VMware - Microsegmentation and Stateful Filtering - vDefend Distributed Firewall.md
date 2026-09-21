# vDefend Distributed Firewall

## Page Status 

Draft

## Broadcom Software Type

VMware

## Broadcom Product Category

Microsegmentation & Stateful Filtering

## Broadcom Product Name

vDefend Distributed Firewall

## Broadcom Product Description - Key Features

vDefend Distributed Firewall is a hypervisor-enforced stateful firewall for east-west micro-segmentation. vDefend 9.1 (May 2026) raises throughput and adds federated identity firewalling.

Key features:

1. **Hypervisor-level microsegmentation** - Enforced at each vNIC.
2. **Higher throughput** - Vendor claims up to 22 Gbps per host with 25GbE and 75 Gbps with 100GbE.
3. **Layer 7 App ID** - More than 5,000 App IDs.
4. **Federated identity firewalling** - Multi-site.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

This is consistently identified in independent migration guidance as one of the hardest VMware capabilities to exit. Distributed firewall rules are expressed as policy objects tied to VMware-specific constructs, including security groups, tags and applied-to scopes; specialist microsegmentation vendor ColorTokens notes that these cannot be replaced with another infrastructure-specific tool without redesigning the underlying security model, and that there is no automated, vendor-neutral export of these policies, meaning migration requires manually reconstructing years of accumulated segmentation logic. Gartner's 2025 guidance similarly frames network security re-architecture as one of the higher-effort components of any VMware exit and recommends a platform-agnostic microsegmentation approach rather than a like-for-like swap. Calico Enterprise and Illumio are genuine, purpose-built microsegmentation platforms designed specifically to operate across hypervisors, cloud and bare metal, and are realistic alternatives for this capability; Red Hat Advanced Cluster Security and OpenShift network policy only cover containerised workloads running on OpenShift and do not, by themselves, provide microsegmentation for remaining VM-based workloads, so a mixed estate will likely require both a container-native control and a VM-capable microsegmentation platform during transition.

Sources: ColorTokens, 'Rethinking Microsegmentation During a VMware NSX Exit'; The Register, 'VMware to lose 35 percent of workloads in three years' (Gartner Symposium coverage, September 2025).

## IBM PRIMARY - Product Name (The Replacement)

OpenShift network policy + Advanced Cluster Security

## IBM PRIMARY - IBM Product Page URL

https://www.redhat.com/en/technologies/cloud-computing/openshift/security

## IBM Replacement Strength

Yes

## IBM Replacement Strategy (Short)

OpenShift network policy with Advanced Cluster Security replaces vDefend Distributed Firewall using Red Hat controls.

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

https://www.redhat.com/en/technologies/cloud-computing/openshift/security

# Sources:

## Sources: Analyst reviews and exist strategy

Verified the migration-complexity claim against a genuine, specific source as requested and flagged that the OpenShift-based portion of the recommended alternative only covers containerised workloads, not remaining VM-based estate, which is a material caveat for the column G/H recommendation.

## General Sources:

- VMware vDefend 9.1 Release Notes: https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend/vdefend-firewall/9-1/release-notes/vmware-vdefend-91-release-notes.html
- vDefend for VCF 9.1: https://blogs.vmware.com/security/2026/05/vdefend-vcf-9-1-zero-trust.html
- StorageReview: vDefend 75Tbps: https://www.storagereview.com/news/vmware-vdefend-75tbps-distributed-firewall-vcf-9-1-update

## Change history:
