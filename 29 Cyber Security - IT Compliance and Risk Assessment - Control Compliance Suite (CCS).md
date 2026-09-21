# Control Compliance Suite (CCS)

## Status 

Draft

## Broadcom Software Type

Cyber Security

## Broadcom Product Category

IT Compliance & Risk Assessment

## Broadcom Product Name

Control Compliance Suite (CCS)

## Broadcom Product Description - Key Features

Control Compliance Suite (CCS) automates risk assessment, policy enforcement and compliance reporting. Version 12.8.0 (with Security Content Update 2025) is the latest documented release, and Broadcom publishes lifecycle dates for support.

Key features:

1. **Continuous assessment** - Scans to discover devices and assess security configuration.
2. **Regulatory coverage** - Evaluates systems against more than 100 regulations, mandates and best practices.
3. **Closed-loop remediation** - Integrates with ticketing systems to remediate failing controls.
4. **Content updates** - Security content updates keep standards and platform coverage current.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

Control Compliance Suite is still being built, but not with much enthusiasm. Broadcom delivered version 12.7.0 on 30 July 2024 and 12.8.0 on 10 October 2025 under its standard support policy, which keeps engineering on the latest generally available version and the one before it. No end-of-service or end-of-life dates have been published for either. The product has not been retired, yet it sits in a precarious spot in a portfolio that Broadcom has been consolidating hard since its US $61 billion purchase of VMware, completed in November 2023.

The pressure on customers arrives in three forms. The first is price. Broadcom removed perpetual licences across its enterprise software division and moved everything to annual subscription bundles, and customers who held perpetual CCS licences have had to renegotiate, with many reporting effective increases of two to five times their old maintenance cost. For mid-market customers that is the main reason to leave. The second is attention. Broadcom has said it will concentrate sales and support on its roughly 600 largest global accounts, and mid-tier organisations that used CCS as an affordable compliance platform no longer get the same engineering or go-to-market focus. Analyst commentary from Gartner and IT-Harvest in 2024 describes the security portfolio inherited from CA in 2018 and Symantec in 2019 as managed for cash extraction and not for development. The third is support. A long-tenured customer on PeerSpot rated the product 8 out of 10 yet warned that 'whenever we went to them with a problem, the support was very poor', and worried that Broadcom had deprioritised its future.

No Gartner Magic Quadrant or Forrester Wave covers CCS, so customers have no independent benchmark for judging lock-in risk, and no named organisation has publicly described leaving it. Those who go are folding compliance and vulnerability work into broader platforms, mainly Qualys VMDR, Tenable One or Rapid7 InsightVM, or, for IBM and Red Hat-aligned organisations, IBM Security QRadar Suite with Red Hat's compliance tools. One caution applies to the IBM route. IBM has ended service for its own QRadar Vulnerability Manager scanner, so compliance assessments on QRadar now depend on third-party scanning connectors.

There is also the matter of architecture. CCS runs on a multi-tier, on-premises design of application servers, manager nodes, SQL databases and scanners, and users cite heavy effort for database upgrades, agent re-registration during data centre moves and complicated patch cycles. For an organisation already facing higher licence costs, that burden strengthens the case for planning an exit.

## IBM PRIMARY - Product Name (The Replacement)

IBM Security QRadar SIEM & Risk Manager (with Red Hat Compliance)

## IBM PRIMARY - IBM Product Page URL

https://www.ibm.com/products/qradar-siem

## IBM Replacement Strength

Partial Match

## IBM Replacement Strategy (Short)

IBM QRadar with Red Hat tools replaces multi-tier CCS infrastructure, lowering cost and automating remediation.

## IBM Replacement Strategy (Description - Why IBM over Broadcom)

IBM Security QRadar (on-premises SIEM & Risk Manager) combined with the Red Hat Compliance Ecosystem (Red Hat Insights, OpenSCAP, and Ansible Automation Platform) replaces Broadcom Control Compliance Suite (CCS). Broadcom CCS imposes heavy multi-tier infrastructure maintenance and aggressive 2x to 5x subscription cost increases while deprioritizing mid-market accounts. The combined IBM and Red Hat architecture replaces legacy CCS agent infrastructure with OpenSCAP policy scanning, continuous network-level risk monitoring, and automated closed-loop Ansible remediation, significantly reducing total operational cost.

## IBM PRIMARY - Product Description

IBM Security QRadar (SIEM and Risk Manager with Policy Monitor), augmented by the Red Hat Compliance ecosystem (Insights, OpenSCAP, and Ansible Automation Platform), provides comprehensive IT asset risk assessment, configuration auditing, multi-regulatory compliance monitoring, and automated remediation.

- **Continuous assessment** — IBM QRadar SIEM automatically discovers network-connected assets, correlates risk posture across the estate, and works alongside Red Hat Insights and OpenSCAP to continuously scan managed hosts and verify security configuration baselines.
- **Regulatory coverage** — IBM QRadar Risk Manager Policy Monitor evaluates network device configurations against major regulatory standards (PCI DSS, HIPAA, SOX, ISO 27001, NERC CIP, NIST), generating automated offenses and notifications upon policy drift.
- **Closed-loop remediation** — IBM Security QRadar and Red Hat Ansible Automation Platform (AAP) execute automated playbooks triggered by non-compliant configuration alerts, resolving failing controls and updating enterprise ticketing systems (ServiceNow/Maximo) without manual intervention.
- **Content updates** — The Red Hat ComplianceAsCode project and IBM Security QRadar continuous content extensions deliver automated, regular updates to security baselines, compliance benchmarks, and threat rules.

## Customer Reference

(not provided)
## IBM SECONDARY - Product Name (Supporting Product, where recommended to compliment the Primary capability)

* IBM QRadar Risk Manager (Policy Monitor)
* IBM Security Randori Recon (Attack Surface Management)
* IBM MaaS360 Mobile Device Management (SaaS)
* Red Hat Satellite
* OpenSCAP / ComplianceAsCode
* Red Hat Insights Compliance
* Red Hat Ansible Automation Platform (AAP)

## IBM SECONDARY - Product Description

1. **IBM QRadar Risk Manager / Policy Monitor** — Provides compliance policy evaluation across regulatory frameworks (PCI DSS, HIPAA, SOX, ISO 27001, NERC CIP). Continuously monitors policy questions against device configuration, vulnerability, and network topology data. Generates offenses, email notifications, or syslog events when unapproved configurations are detected. Directly replaces CCS's multi-framework compliance assessment and reporting capability.

2. **IBM Security Randori Recon** — External attack surface management (EASM) that continuously discovers and monitors internet-facing assets, including unmanaged and shadow IT assets. Feeds discovery data into the QRadar Connected Assets and Risk service. Addresses the gap created by QRadar Vulnerability Manager's EOL for external asset discovery.

3. **IBM MaaS360 Mobile Device Management (SaaS)** — Discovers and manages enrolled endpoints (mobile, laptops, frontline/unattended devices) and assesses device posture. Enforces configuration/compliance policy, assesses device risk posture. Enterprise Mobility Management (EMM) with Mobile Threat Defence (MTD) and Mobile Device Management (MDM).

4. **Red Hat** — For systems under management: Continuous Discovery and Scanning with Red Hat Insights (predictive SaaS analytics) and Red Hat Satellite (lifecycle management) continuously discover and assess managed hosts. Comprehensive Policy and Regulatory Evaluation with Red Hat Insights Compliance (OpenSCAP). Closed-loop automated remediation via Red Hat Ansible Automation Platform (AAP).

## IBM SECONDARY - Product Page(s) URL

1. https://www.ibm.com/products/qradar-siem
2. https://www.ibm.com/docs/en/qradar-on-cloud
3. https://www.redhat.com/en/resources/ansible-automation-platform-beginners-guide-ebook
4. https://www.ibm.com/docs/en/maas360
5. https://www.ibm.com/support/pages/node/6853425 (QRadar Vulnerability Manager EOL notice)

# Sources:

## IBM Security QRadar SIEM & Risk Manager

- IBM Security QRadar SIEM Product Overview: https://www.ibm.com/products/qradar-siem
- IBM QRadar Risk Manager & Policy Monitor Guide: https://www.ibm.com/docs/en/qsip/7.5?topic=overview-qradar-risk-manager
- Red Hat Insights Compliance Documentation: https://docs.redhat.com/en/documentation/red_hat_insights/1-latest/html/assessing_and_monitoring_security_policy_compliance_of_rhel_systems/index

## Sources: Analyst reviews and exit strategy

- PeerSpot, 'Broadcom Control Compliance Suite Reviews' (peerspot.com), for support quality and product development concerns after the Broadcom acquisition
- Broadcom Support Portal, end-of-life and end-of-service dates for Control Compliance Suite (support.broadcom.com), confirming CCS 12.7.0 (30 July 2024) and 12.8.0 (10 October 2025)
- IBM Documentation, 'QRadar Risk Manager overview', for Policy Monitor templates covering PCI DSS, HIPAA, SOX, ISO 27001 and NERC CIP
- IBM Support, 'QRadar Vulnerability Manager: End of service product notification' (https://www.ibm.com/support/pages/node/6853425), confirming that the scanner is no longer supported in any QRadar version
- IBM Documentation, 'QRadar platform overview' (IBM Security QRadar Suite SIEM), for pre-built integrations and native SIEM, EDR, NDR and SOAR capabilities
- IBM Documentation, 'Connecting data sources to import assets and risk data' (IBM Security QRadar Suite SIEM), for third-party connectors including Qualys, Tenable, Tanium, CrowdStrike Falcon, RHACS, Randori, Guardium and IBM Security Verify Analytics
- IBM Documentation, 'IBM Security QRadar Compliance Content Extensions', for SOX, PCI DSS, HIPAA and ISO 27001 content
- Gartner and IT-Harvest industry commentary, 2024, characterising Broadcom's post-CA, post-Symantec and post-VMware portfolio strategy as concentrated on a reduced set of top-tier accounts
- Redress Compliance, 'Symantec Enterprise Software Licensing Under Broadcom: A CIO Playbook' (https://redresscompliance.com/symantec-enterprise-software-licensing-under-broadcom-a-cio-playbook.html)

## General Sources:

- Symantec Control Compliance Suite - 12.x: https://techdocs.broadcom.com/us/en/symantec-security-software/information-security/control-compliance-suite/12-x.html
- Releases and Support Lifecycle Dates: https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/ProductAdvisories/Symantec-Control-Compliance-Suite-Releases-and-Support-Lifecycle-Dates/16154
- Discontinued platforms - SCU 2025: https://techdocs.broadcom.com/us/en/symantec-security-software/information-security/control-compliance-suite/SCU-2025/System-requirements-and-compatibility/Deprecation.html
- End-of-Life and End-of-Service dates for Control Compliance Suite: https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/product-advisories/End-of-Life-and-End-of-Service-dates-for-Control-Compliance-Suite/16154

## Change history:
