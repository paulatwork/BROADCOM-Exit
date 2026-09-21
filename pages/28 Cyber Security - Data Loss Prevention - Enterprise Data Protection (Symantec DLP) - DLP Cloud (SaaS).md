# Enterprise Data Protection (Symantec DLP) - DLP Cloud (SaaS)

## Page Status 

Draft

## Broadcom Software Type

Cyber Security

## Broadcom Product Category

Data Loss Prevention

## Broadcom Product Name

Enterprise Data Protection (Symantec DLP) - DLP Cloud (SaaS)

## Broadcom Product Description - Key Features

Symantec DLP Cloud extends Symantec DLP policies to cloud and AI channels, integrating with CloudSOC to protect data in more than 100 sanctioned and unsanctioned cloud apps. 26.1 raises the large file extraction limit from 30 MB to 150 MB.

Key features:

1. **Cloud application coverage** - Data in motion and at rest in cloud apps such as Office 365, Google Workspace, Box, Dropbox and Salesforce.
2. **Generative AI controls** - Real-time inspection of data sent to AI applications such as ChatGPT.
3. **Agentic AI protection** - Integration with Google Cloud Agent Gateway inspects agent traffic.
4. **Shared policy engine** - Uses the same detection technologies as on-premises DLP; 26.1 supports files up to 150 MB.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

The cloud-delivered DLP line lives under the same commercial rules as the on-premises product. Broadcom's focus on its largest accounts and its multi-product bundling apply, so a customer who wants only the cloud service may find it sold as part of something larger.

Independent commentary is missing. No analyst coverage specific to the cloud product was found, and Gartner and others generally treat Symantec's on-premises and cloud DLP as one product family, so it would be wrong to suggest a separate body of analysis exists. No named organisation has publicly described leaving the cloud service.

The wider industry observation is worth including, with care. Agent-based DLP architectures tend to produce more false positives and slower remediation than newer data security posture management tools in cloud, SaaS and generative AI settings. That is a general view about legacy architecture and not a finding about Broadcom specifically.

This assessment does not cover cloud-hosted or cloud-access services in scope for replacement, so no IBM alternative is proposed for the service itself. Organisations replacing cloud DLP are generally choosing Microsoft Purview DLP, Forcepoint ONE, Netskope, Nightfall AI or Strac, and IBM Guardium Data Security Center is the IBM option for the data security posture component.

## IBM PRIMARY - Product Name (The Replacement)

IBM Guardium Data Security Center (Guardium DSPM)

## IBM PRIMARY - IBM Product Page URL

https://www.ibm.com/products/guardium-data-security-center

## IBM Replacement Strength

Strong Replacement, with improved outcomes

## IBM Replacement Strategy (Short)

Guardium DSPM offers agentless cloud discovery and generative AI monitoring, replacing costly Symantec DLP Cloud.

## IBM Replacement Strategy (Description - Why IBM over Broadcom)

IBM Guardium Data Security Center (with Guardium DSPM) replaces Symantec DLP Cloud by providing modern, cloud-native data security posture management and AI governance across multi-cloud SaaS and IaaS environments. Broadcom's Symantec DLP Cloud relies on legacy CASB/DLP policy frameworks that produce high false-positive rates and incur substantial subscription overhead. IBM Guardium DSPM continuously discovers sensitive data across cloud repositories (M365, Google Workspace, Box, AWS, Azure, GCP), monitors generative AI prompts and agentic AI pipelines, and automates compliance without heavy proxy infrastructure.

## IBM PRIMARY - Product Description

IBM Guardium Data Security Center (incorporating Guardium Data Security Posture Management - DSPM) is IBM's cloud-native data protection platform. It provides automated data discovery, shadow data detection, generative AI monitoring, and continuous data risk mitigation across cloud applications and AI pipelines.

- **Cloud application coverage** — IBM Guardium DSPM provides agentless, automated data discovery, classification, and vulnerability assessment across cloud SaaS applications (Microsoft 365, Google Workspace, Box, Salesforce) and cloud storage buckets (AWS S3, Azure Blob, Google Cloud Storage).
- **Generative AI controls** — IBM Guardium DSPM actively inspects data flows and user interactions with enterprise generative AI applications (such as ChatGPT, Microsoft Copilot, and custom LLMs) to prevent proprietary data leakage and enforce privacy guardrails.
- **Agentic AI protection** — IBM Guardium DSPM integrates with cloud AI gateways and agentic frameworks, providing real-time data tracing, payload inspection, and policy enforcement across automated autonomous AI agents.
- **Shared policy engine** — IBM Guardium Data Security Center provides a unified, centralized policy engine that enforces consistent data classification rules, contextual access policies, and high-capacity content scanning across hybrid cloud and on-premises environments.

## Customer Reference

(not provided)
## IBM SECONDARY - Product Name (Supporting Product, where recommended to compliment the Primary capability)

N/A

## IBM SECONDARY - Product Description

N/A

## IBM SECONDARY - Product Page(s) URL

N/A

# Sources:

## IBM Guardium Data Security Center

- IBM Guardium Data Security Center Overview: https://www.ibm.com/products/guardium-data-security-center
- IBM Data Security Posture Management (DSPM): https://www.ibm.com/products/guardium-data-security-center/dspm
- Gartner Magic Quadrant for Data Security Platforms (IBM Leader): https://www.gartner.com/reviews/market/data-security-platforms/vendor/ibm/product/ibm-guardium

## Sources: Analyst reviews and exist strategy

- Redress Compliance, 'Symantec Enterprise Software Licensing Under Broadcom: A CIO Playbook' for the general Broadcom commercial pattern

## General Sources:

- Detection Features in DLP 26.1: https://techdocs.broadcom.com/us/en/symantec-security-software/information-security/data-loss-prevention/25-1/detection-features-in-dlp-26-1.html
- Symantec DLP Cloud (product page): https://www.broadcom.com/products/cybersecurity/information-protection/data-loss-prevention-cloud
- Stopping Data Leaks at the Speed of AI: https://www.security.com/feature-stories/symantec-dlp-google-agent-gateway-agentic-ai-security

## Change history:
