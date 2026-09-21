# VMware vSphere

## Page Status 

Draft

## Broadcom Software Type

VMware

## Broadcom Product Category

Hypervisor Compute Virtualization

## Broadcom Product Name

VMware vSphere

## Broadcom Product Description - Key Features

VMware vSphere is the hypervisor (ESX, renamed from ESXi in 9.0) and vCenter management layer. vSphere 9.1 was released 12 May 2026.

Key features:

1. **ESX hypervisor** - Virtualises compute; ESXi was renamed ESX in 9.0.
2. **vCenter management** - Central management, with a new resize API and quick patch in 9.1.
3. **Live patching and zero-touch provisioning** - 9.1 applies kernel patches to running memory on TPM-enabled hosts and bootstraps ESX on bare metal by network imaging.
4. **NVMe memory tiering and AI certification** - Enhanced NVMe memory tiering in 9.1, and NVIDIA-Certified Hypervisor status for vSphere 9.1.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

Standalone perpetual vSphere/ESXi licences were discontinued in 2023 in favour of subscription-only, per-core licensing with a 16-core-per-CPU minimum, meaning older hosts with fewer cores per socket are billed as though fully populated. Organisations continuing to run vSphere on expired perpetual licences without an active subscription lose access to security patches and CVE remediation, a risk consistently flagged in trade press covering the Broadcom transition. Broadcom's restriction, in 2025, of public access to the VDDK software development kit, on which third-party migration and backup tools including Microsoft Azure Migrate, Red Hat's Migration Toolkit and Nutanix Move depend, has added practical friction to vSphere exit projects. Gartner's September 2025 guidance projected that more than one-third of VMware workloads will move to other platforms by 2028, but stated that full hypervisor migrations typically take three or more years, and ranked Nutanix and public cloud as more mature migration destinations than Red Hat virtualisation, a consideration relevant to the Red Hat-centric alternative proposed for this row. As a real-world example, Nutanix has reported, as a vendor claim, migrating Western Union off vSphere across 900 to 1,200 applications and 3,900 cores within six months.

Sources: Network World, 'Broadcom hampers VMware migration by blocking downloads of key SDK'; The Register, 'VMware to lose 35 percent of workloads in three years' (September 2025); Slashdot/Ars Technica coverage of Nutanix .NEXT conference claims (April 2026).

## IBM PRIMARY - Product Name (The Replacement)

OpenShift Virtualization

## IBM PRIMARY - IBM Product Page URL

https://www.redhat.com/en/technologies/cloud-computing/openshift/virtualization-engine

## IBM Replacement Strength

Yes

## IBM Replacement Strategy (Short)

Red Hat OpenShift Virtualization replaces the vSphere hypervisor, running virtual machines on Red Hat's platform.

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

https://www.redhat.com/en/technologies/cloud-computing/openshift/virtualization-engine

# Sources:

## Sources: Analyst reviews and exist strategy

Tightened column D for precision (ESXi/vCenter naming). Replaced generic caution language with the verified VDDK-blocking finding and the Western Union migration example, and added the Gartner alternative-ranking caveat.

## General Sources:

- What's New with vSphere in VCF 9.1: https://blogs.vmware.com/cloud-foundation/2026/05/12/whats-new-with-vsphere-9-1/
- vSphere What's New 9.0: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vsphere.html
- VMware Cloud Foundation 9.1 What's New: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/vmware-cloud-foundation-9-1-0-0-release-notes/what-s-new.html

## Change history:
