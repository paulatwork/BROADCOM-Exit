# VCF Automation

## Page Status 

Draft

## Broadcom Software Type

VMware

## Broadcom Product Category

Cloud Infrastructure Lifecycle Automation

## Broadcom Product Name

VCF Automation

## Broadcom Product Description - Key Features

VCF Automation (formerly Aria Automation) is the self-service private cloud layer in VCF 9.x. 9.1.0.0200 was released 13 July 2026.

Key features:

1. **Self-service cloud services** - VMs, Kubernetes, volumes, databases and more.
2. **Multi-tenancy** - Central quotas and networks.
3. **Declarative VM Service** - Cloud-init and sysprep.
4. **VLAN-backed VPCs** - From 9.1.1.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

Broadcom confirmed in a published knowledge base notice the deprecation of VCF Automation Pipelines from VCF Automation 9, removing a CI/CD-oriented capability some customers had built processes around; this is a specific, verifiable instance of functional discontinuity within the Broadcom product portfolio. Standalone Aria Automation licensing was eliminated in the 2023 restructuring, consistent with the wider pattern across the VCF product family. Independent trade press on organisations specifically exiting VCF/Aria Automation is less extensive than coverage of the hypervisor and networking layers, so specific migration volumes should not be cited for this product without further verification. Red Hat Ansible Automation Platform combined with OpenShift, and HashiCorp Terraform/OpenTofu, are genuine, widely adopted alternatives for infrastructure-as-code and orchestration and represent a realistic replacement path, though migrating existing vRA/vRO blueprints requires genuine re-authoring effort rather than direct import, since the underlying automation models differ substantially.

Sources: Broadcom Knowledge Base article confirming deprecation of VCF Automation Pipelines (knowledge.broadcom.com, article 378424); Broadcom TechDocs on the Aria-to-VCF Automation rebrand and upgrade path.

## IBM PRIMARY - Product Name (The Replacement)

Red Hat Ansible Automation Platform + OpenShift

## IBM PRIMARY - IBM Product Page URL

https://www.redhat.com/en/technologies/management/ansible

## IBM Replacement Strength

Yes

## IBM Replacement Strategy (Short)

Red Hat Ansible Automation Platform with OpenShift replaces VCF Automation for infrastructure automation and orchestration.

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

https://www.redhat.com/en/technologies/management/ansible

# Sources:

## Sources: Analyst reviews and exist strategy

Verified the specific Automation Pipelines deprecation claim against a real Broadcom knowledge base article rather than leaving it as an unsourced assertion, and added an honest note on the thinner evidence base for product-specific exit volumes.

## General Sources:

- VCF Automation What's New 9.0: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-automation.html
- VCF Automation 9.1.0.0200 Release Notes: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/patch-releases-9-1-0-x/vcf-automation/vcfautomation-9-1-0-0200-release-notes.html
- VCF Automation 9.1.1.0 Release Notes: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/vmware-cloud-foundation-9-1-1-0-release-notes/vcfautomation-9-1-1-0-release-notes.html

## Change history:
