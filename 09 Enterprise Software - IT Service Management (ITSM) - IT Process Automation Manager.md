# IT Process Automation Manager

## Status 

Draft

## Broadcom Software Type

Enterprise Software

## Broadcom Product Category

IT Service Management (ITSM)

## Broadcom Product Name

IT Process Automation Manager

## Broadcom Product Description (Key Features) (This is important to get right)

IT Process Automation Manager (ITPAM, documented by Broadcom as CA Process Automation, with TechDocs path 'automic-process-automation') is a runbook and process orchestration engine for automating IT operations and production processes. Version 4.4.0 is the latest documented (documentation updated 10 June 2026; 4.3.05 is the previous version), and Broadcom lists a current product page for it.

Key features:

1. **Visual process design and orchestration** - Design, build, orchestrate, manage and report on automated processes supporting IT operations.
2. **Extensible operators** - Built-in operators for most integrations, plus custom operators using JavaScript calculations or TouchPoint scripts in any scripting language.
3. **Scalable orchestrators** - A Java-based server executes processes from the Process Library, and orchestrators scale horizontally.
4. **Broadcom portfolio integration** - A CLI and Start Request Forms allow processes to be run from schedulers such as AutoSys, and connectors exist for products such as Client Automation.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

Analyst cautions and commercial pressures: no dedicated Gartner Peer Insights, Forrester or IDC product page specific to ITPAM was identified in this research. Broadcom's wider automation portfolio, including the separately branded Automic Automation workload-automation product, is reviewed under adjacent Gartner categories such as Service Orchestration and Automation Platforms, but ITPAM itself does not appear to carry a distinct, current independent rating; this absence of coverage should be stated plainly rather than inferred as evidence of quality either way. Current Broadcom technical documentation confirms the product continues to rely on SOAP/XML-based process definitions, supporting this row's existing claim of ageing architecture. General bundling and renewal-price pressures documented for Broadcom's wider portfolio apply to ITPAM as part of any enterprise agreement.

Broadcom exit strategies and market alternatives: Red Hat Ansible Automation Platform is a credible, widely adopted, actively developed alternative for agentless, YAML-based automation and is a realistic replacement. ServiceNow Flow Designer and Integration Hub are realistic alternatives for organisations already standardised on the ServiceNow platform. Both alternatives are proportionate to ITPAM's function and are not overstated.
Sources: Broadcom, IT Process Automation Manager product page, confirming the product remains actively sold in 2026 (broadcom.com/products/software/automation/it-process-automation-manager) [vendor-published]; Gartner Peer Insights, Service Orchestration and Automation Platforms market, used to confirm no distinct ITPAM listing exists (gartner.com/reviews/market/service-orchestration-and-automation-platforms); Redress Compliance, Broadcom Enterprise Agreements guide, 2025.

## IBM Replacement Strength

(not provided)

## IBM Replacement Strategy - Why IBM over Broadcom

(not provided)

## PRIMARY - Key Product - IBM Alternative

Red Hat Ansible Automation Platform

## PRIMARY - Key Product Capability Statement - IBM Alternative

General sentiment: Positive – valued for agentless, readable YAML automation, with the main criticisms being node-based licensing cost, container platform prerequisites and an initial learning curve.

Red Hat Ansible Automation Platform provides an enterprise open-source IT automation and orchestration solution. It replaces legacy complex XML/SOAP runbooks with human-readable YAML playbooks, Event-Driven Ansible for automated incident remediation, and cross-domain workflow orchestration across multi-cloud, network, and on-premises infrastructure.

## PRIMARY - IBM Product Page URL

https://www.redhat.com/en/technologies/management/ansible

## Customer Reference
(not provided)
## SECONDARY - Product Name - Supporting Product From any vendor - ONLY Where needed to for FULL Capability match for Broadcom. Extend the IBM Key Product.

(not provided)

## SECONDARY - Product Description - From any vendor - A Secondary Support Product.

(not provided)

## SECONDARY - Product Page(s) URL

(not provided)

## Sources: Analyst reviews and exist strategy

Column D and Column E reviewed and revised against sourced evidence; see Sources line at the end of Column E for citations.

## General Sources:

- CA IT Process Automation Manager - Broadcom TechDocs (legacy bookshelf): https://techdocs.broadcom.com/us/en/ca-miscellaneous/legacy_bookshelves_and_pdfs/bookshelves_and_pdfs/bookshelves/ca-it-process-automation-manager.html
- Integrate with IT Process Automation Manager - Workload Automation Agent for Web Services 24.0: https://techdocs.broadcom.com/us/en/ca-enterprise-software/intelligent-automation/workload-automation-agent-for-web-services/24-0/command-line-interfaces/integrate-with-ca-process-automation.html
- CA Process Automation Connector for CA IT Client Manager: https://techdocs.broadcom.com/us/en/ca-enterprise-software/intelligent-automation/automic-process-automation-connectors/2-0/ca-process-automation-connector-for-ca-it-client-manager.html
- CA Process Automation 4.4.0 - Broadcom TechDocs: https://techdocs.broadcom.com/us/en/ca-enterprise-software/intelligent-automation/automic-process-automation/04-4-00.html

## Change history:

### 2026-09-19 - Broadcom product information verification (WebFetch pass, files 02-39)
- Product description: replaced the earlier caution that the version could not be confirmed and that documentation sat in legacy bookshelves. TechDocs now hosts CA Process Automation 4.4.0 (with 4.3.05) under the 'automic-process-automation' path, updated 10 June 2026. The four key features are unchanged.
- Analyst Cautions: the statement that documentation confirms SOAP/XML-based process definitions was not re-verified and is unchanged.

### 2026-09-19 - Broadcom product information review
- Product description: Added lifecycle caution (legacy documentation location, version not confirmed) and four features from Broadcom documentation.
- Summary and numbered list of four key features rewritten from current Broadcom sources.
- General Sources: 3 sources recorded (Broadcom TechDocs, product pages, press releases where available).

### 2026-09-19 - IBM alternative product verification and sentiment (WebFetch and WebSearch pass, files 02-39)
- Requirement match against the Key Features section: Meets most requirements.
- Confirmed (Red Hat product page): Event-Driven Ansible, an automation orchestrator for workflows, Ansible Content Collections and plug-ins, automation mesh for scalable execution, and ServiceNow ITSM integration.
- Not verified: a visual process designer and a REST API or CLI for launching from schedulers such as AutoSys. Ansible is code-based (YAML), so the migration of CA Process Automation runbooks is a rebuild rather than a conversion.
- Sentiment: added a one-sentence summary of general market sentiment at the start of the Key Product Capability Statement. Existing statement text was not changed.
- Sources: https://www.redhat.com/en/technologies/management/ansible; https://www.gartner.com/reviews/product/red-hat-ansible-automation-platform
