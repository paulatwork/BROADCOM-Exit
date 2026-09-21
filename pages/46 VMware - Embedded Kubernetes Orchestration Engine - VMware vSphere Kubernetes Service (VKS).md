# VMware vSphere Kubernetes Service (VKS)

## Page Status 

Draft

## Broadcom Software Type

VMware

## Broadcom Product Category

Embedded Kubernetes Orchestration Engine

## Broadcom Product Name

VMware vSphere Kubernetes Service (VKS)

## Broadcom Product Description - Key Features

vSphere Kubernetes Service (VKS) is the Kubernetes runtime in vSphere. VKS 3.7.0 (Kubernetes 1.36) was released on 18 June 2026, with 3.7.1 on 13 August 2026. VKS is not included in vSphere Foundation.

Key features:

1. **Native Kubernetes on vSphere** - Clusters run beside VMs on the same infrastructure, with up to 250 worker nodes per cluster in 3.7.
2. **Networking flexibility** - Supported CNI plugins, an option to disable kube-proxy, Multus and SR-IOV virtual function support.
3. **Security and identity** - Configurable TLS profiles, FIPS on Ubuntu nodes without a Canonical subscription, native OIDC and workload identity federation.
4. **Operations** - 5-node control planes, in-place node updates, TuneD profiles (3.6) and VKS and VM fast-deploy in VCF 9.1.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

Because VKS is deployed as a Supervisor-level capability of vSphere, it creates a direct dependency on vSphere and VCF/VVF licensing, with no way to run VKS independently of the underlying VMware hypervisor licence; this is a verifiable architectural characteristic rather than a general assertion. Independent analysis of VMware's container strategy identifies cost and licensing complexity, a steep operational learning curve, and reduced flexibility relative to vendor-neutral Kubernetes distributions as the principal reasons organisations are reconsidering VKS and Tanzu Kubernetes Grid, alongside the broader vendor lock-in concerns raised by the 2023-2024 licensing changes. Red Hat OpenShift Container Platform is a realistic, widely adopted enterprise alternative with a comparable enterprise support model; SUSE Rancher and the major hyperscaler managed Kubernetes services (Amazon EKS, Azure AKS, Google GKE) are also commonly cited migration destinations and should be considered alongside OpenShift depending on the organisation's cloud strategy.

Sources: Fairwinds, 'Are You Still Using VMware Tanzu? (And Is Now the Time to Migrate?)'; Broadcom TechDocs on vSphere IaaS Control Plane and VKS architecture.

## IBM PRIMARY - Product Name (The Replacement)

Red Hat OpenShift Container Platform

## IBM PRIMARY - IBM Product Page URL

https://www.redhat.com/en/technologies/cloud-computing/openshift

## IBM Replacement Strength

Yes

## IBM Replacement Strategy (Short)

Red Hat OpenShift Container Platform replaces vSphere Kubernetes Service (VKS) with an enterprise-supported Kubernetes platform.

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

https://www.redhat.com/en/technologies/cloud-computing/openshift

# Sources:

## Sources: Analyst reviews and exist strategy

Added a genuine independent source (Fairwinds) for the migration-driver claims and broadened the realistic alternative set beyond OpenShift alone, consistent with what that source actually recommends.

## General Sources:

- VKS 3.7 Release Notes: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-service-administration-and-development/9-1/release-notes/vks-release-notes/vmware-tanzu-kubernetes-grid-service-37-release-notes.html
- VKS 3.6 Release Notes: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-service-administration-and-development/9-1/release-notes/vks-release-notes/vmware-tanzu-kubernetes-grid-service-36-release-notes.html
- VKS 3.6 blog: https://blogs.vmware.com/cloud-foundation/2026/02/11/vmware-vsphere-kubernetes-service3-6-making-enterprise-kubernetes-safer-more-flexible-and-easier-to-operate/
- VMware Cloud Foundation 9.1 What's New: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/vmware-cloud-foundation-9-1-0-0-release-notes/what-s-new.html

## Change history:
