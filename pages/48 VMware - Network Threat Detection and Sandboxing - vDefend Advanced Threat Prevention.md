# vDefend Advanced Threat Prevention

## Status 

Draft

## Broadcom Software Type

VMware

## Broadcom Product Category

Network Threat Detection & Sandboxing

## Broadcom Product Name

vDefend Advanced Threat Prevention

## Broadcom Product Description - Key Features

vDefend Advanced Threat Prevention combines IDS/IPS, malware prevention (sandbox) and network traffic analysis with NDR correlation. Version 4.2 documentation and 9.x feature guides are current.

Key features:

1. **Multi-layer detection** - IDS/IPS, MPS, NTA.
2. **On-premises sandbox** - No file upload to cloud.
3. **NDR campaigns** - Condenses alerts into campaigns.
4. **AI Assistant** - Explains events and suggests remediation.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

Independent, product-specific analyst criticism of vDefend Advanced Threat Prevention is limited. The most substantial third-party evaluation identified is an SE Labs test report assessing its threat-detection efficacy, which is a technical performance assessment rather than a commercial or lock-in critique; a Forrester Total Economic Impact study also exists but was commissioned by Broadcom/VMware and should be read as vendor-sponsored material rather than independent analyst research. The applicable, verifiable caution is architectural: vDefend Advanced Threat Prevention operates as an extension of the NSX network fabric, so its threat-inspection scope is limited to traffic traversing NSX-managed segments, and it does not natively extend coverage to non-VMware hypervisors or bare-metal environments, consistent with the broader NSX lock-in concerns documented for this product family. Palo Alto Networks Cortex/Prisma Cloud and Cisco Secure Network Analytics are established NDR alternatives with platform-agnostic deployment models; Red Hat Advanced Cluster Security is a Kubernetes-native container security tool and is not a direct substitute for network-level NDR and sandboxing, so it should be positioned as a complementary control for containerised workloads rather than a replacement for this specific capability.

Sources: SE Labs, 'Advanced Security Test Report: VMware vDefend Advanced Threat Prevention' (2025); Forrester Consulting, 'The Total Economic Impact of Broadcom VMware vDefend' (commissioned by Broadcom, February 2025).

## IBM PRIMARY - Product Name (The Replacement)

Red Hat Advanced Cluster Security for Kubernetes

## IBM PRIMARY - IBM Product Page URL

https://www.redhat.com/en/technologies/cloud-computing/openshift/advanced-cluster-security

## IBM Replacement Strength

Yes

## IBM Replacement Strategy (Short)

Advanced Cluster Security replaces vDefend Advanced Threat Prevention with Kubernetes-native container security from Red Hat.

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

https://www.redhat.com/en/technologies/cloud-computing/openshift/advanced-cluster-security

# Sources:

## Sources: Analyst reviews and exist strategy

Corrected the framing so vendor-commissioned Forrester research is clearly labelled as such rather than presented as independent analyst commentary, and flagged that Red Hat Advanced Cluster Security is not a like-for-like replacement for network-level NDR, which affects the realism of the column G/H alternative.

## General Sources:

- vDefend Advanced Threat Prevention 4.2: https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend/vdefend-atp/4-2.html
- vDefend Advanced Threat Prevention Overview 9.0: https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend/vdefend-atp/9-0/vdefend-advanced-threat-prevention-overview.html
- VMware vDefend Advances Multi-Layer Lateral Security: https://blogs.vmware.com/security/2026/08/vdefend-ssp-for-frontier-ai-era.html
- SE Labs test report: https://selabs.uk/reports/reports-advanced-security-test-report-vmware-vdefend-advanced-threat-prevention-ndr-protection-2025-q1/

## Change history:
