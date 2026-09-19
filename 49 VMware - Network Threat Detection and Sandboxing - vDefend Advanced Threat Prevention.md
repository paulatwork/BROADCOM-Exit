# vDefend Advanced Threat Prevention

## Status 

Draft

## Broadcom Software Type

VMware

## Broadcom Product Category

Network Threat Detection & Sandboxing

## Broadcom Product Name

vDefend Advanced Threat Prevention

## Broadcom Product Description (Key Features) (This is important to get right)

vDefend Advanced Threat Prevention combines IDS/IPS, malware prevention (sandbox) and network traffic analysis with NDR correlation. Version 4.2 documentation and 9.x feature guides are current.

Key features:

1. **Multi-layer detection** - IDS/IPS, MPS, NTA.
2. **On-premises sandbox** - No file upload to cloud.
3. **NDR campaigns** - Condenses alerts into campaigns.
4. **AI Assistant** - Explains events and suggests remediation.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

Independent, product-specific analyst criticism of vDefend Advanced Threat Prevention is limited. The most substantial third-party evaluation identified is an SE Labs test report assessing its threat-detection efficacy, which is a technical performance assessment rather than a commercial or lock-in critique; a Forrester Total Economic Impact study also exists but was commissioned by Broadcom/VMware and should be read as vendor-sponsored material rather than independent analyst research. The applicable, verifiable caution is architectural: vDefend Advanced Threat Prevention operates as an extension of the NSX network fabric, so its threat-inspection scope is limited to traffic traversing NSX-managed segments, and it does not natively extend coverage to non-VMware hypervisors or bare-metal environments, consistent with the broader NSX lock-in concerns documented for this product family. Palo Alto Networks Cortex/Prisma Cloud and Cisco Secure Network Analytics are established NDR alternatives with platform-agnostic deployment models; Red Hat Advanced Cluster Security is a Kubernetes-native container security tool and is not a direct substitute for network-level NDR and sandboxing, so it should be positioned as a complementary control for containerised workloads rather than a replacement for this specific capability.

Sources: SE Labs, 'Advanced Security Test Report: VMware vDefend Advanced Threat Prevention' (2025); Forrester Consulting, 'The Total Economic Impact of Broadcom VMware vDefend' (commissioned by Broadcom, February 2025).

## IBM Replacement Strength

Yes

## IBM Replacement Strategy - Why IBM over Broadcom

Red Hat

## PRIMARY - Key Product - IBM Alternative

Red Hat Advanced Cluster Security for Kubernetes

## PRIMARY - Key Product Capability Statement - IBM Alternative

(not provided)

## PRIMARY - IBM Product Page URL

https://www.redhat.com/en/technologies/cloud-computing/openshift/advanced-cluster-security

## Customer Reference
(not provided)
## SECONDARY - Product Name - Supporting Product From any vendor - ONLY Where needed to for FULL Capability match for Broadcom. Extend the IBM Key Product.

(not provided)

## SECONDARY - Product Description - From any vendor - A Secondary Support Product.

(not provided)

## SECONDARY - Product Page(s) URL

https://www.redhat.com/en/technologies/cloud-computing/openshift/advanced-cluster-security

## Sources: Analyst reviews and exist strategy

Corrected the framing so vendor-commissioned Forrester research is clearly labelled as such rather than presented as independent analyst commentary, and flagged that Red Hat Advanced Cluster Security is not a like-for-like replacement for network-level NDR, which affects the realism of the column G/H alternative.

## General Sources:

- vDefend Advanced Threat Prevention 4.2: https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend/vdefend-atp/4-2.html
- vDefend Advanced Threat Prevention Overview 9.0: https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend/vdefend-atp/9-0/vdefend-advanced-threat-prevention-overview.html
- VMware vDefend Advances Multi-Layer Lateral Security: https://blogs.vmware.com/security/2026/08/vdefend-ssp-for-frontier-ai-era.html
- SE Labs test report: https://selabs.uk/reports/reports-advanced-security-test-report-vmware-vdefend-advanced-threat-prevention-ndr-protection-2025-q1/

## Change history:

### 2026-09-19 - Broadcom product information review
- Product description: Added on-premises sandbox and AI assistant.
- Summary and numbered list of four key features rewritten from current Broadcom sources.
- General Sources: 4 sources recorded (Broadcom TechDocs, product pages, press releases where available).
