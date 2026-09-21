# ValueOps by Broadcom - ConnectALL (SaaS or On-prem)

## Status 

Complete

## Broadcom Software Type

Enterprise Software

## Broadcom Product Category

Integration & Workflow Automation

## Broadcom Product Name

ValueOps by Broadcom - ConnectALL (SaaS or On-prem)

## Broadcom Product Description - Key Features

ConnectALL is the value stream integration platform in ValueOps by Broadcom (added to the ValueOps portfolio in a Broadcom acquisition June 2023). It synchronises work items bi-directionally across Agile, DevOps, ALM and ITSM tools without custom coding, so teams keep their existing systems of record. ConnectALL 4.0 (2026) adds enhanced self-service, scalability and intelligent automation support.

Key features:

1. **Bi-directional work item synchronisation** - Keeps requirements, stories, defects and test cases consistent across tools from multiple vendors, removing manual handoffs.
2. **Out-of-the-box integrations** - Prebuilt connectors across a wide range of Agile, DevOps, ITSM and business tools, delivered without custom coding.
3. **Data transformation and mapping intelligence layer** - Captures, transforms and synchronises data accurately in near real time across the software delivery ecosystem, from portfolio planning through to operations.
4. **Native ValueOps integration** - Works with Clarity, Rally and Insights, so integrated data feeds portfolio planning and value stream metrics end to end.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

ConnectALL is a supporting services of the Broadcom ValueOps suite. Replacing one, means replacing the other. ConnectALL is not a widely used service on its own. It has no user reviews on Gartner Peer Insights as at 2026, and no Forrester or IDC specific coverage. 

Broadcom bought the company in 2023, and next to Clarity or Rally it is a modest acquisition that has attracted little independent attention. The commercial pressures that apply to the rest of the ValueOps bundle apply here too: Portfolio Licensing Agreement bundling, minimum commitments and steep renewals. Because ConnectALL is usually bought as part of that bundle, customers tend to feel those pressures through the bundle rather than through anything specific to the integration engine.

No named organisation has publicly described leaving ConnectALL. Refer to independent comparison sites, which compare Planview Hub (formerly Tasktop) against ConnectALL again and again. That makes it the most likely destination.

## IBM PRIMARY - Product Name (The Replacement)

IBM Engineering Lifecycle Management (ELM) Suite

## IBM PRIMARY - IBM Product Page URL

https://www.ibm.com/docs/en/engineering-lifecycle-management-suite/lifecycle-management/7.2.0?topic=integrating-oslc-integrations

## IBM Replacement Strength

Strong Replacement, with improve outcomes.

## IBM Replacement Strategy (Short)

Replace as part of migration to IBM Digital Engineering Products & Services.

## IBM Replacement Strategy (Description - Why IBM over Broadcom)

When replacing Broadcom, native ValueOps integration is not required, it is replaced. IBM ELM's equivalent is its own Engineering Insights / reporting and optimisation layer, which builds document-style reports and dashboards across the ELM environment and third-party tools for compliance, contractual and ad-hoc review

This allows portfolio/value-stream reporting to be based on an open, vendor-neutral foundation rather than one welded to Clarity/Rally.

**Outcome: Lower total cost of ownership, broader connector coverage for exsting Third Party Applcations on-prem, and improved use of agile planning**

## IBM PRIMARY - Product Description

IBM’s integrated suite .. across the Systems ‘V’ lifecycle.

IBM's differentiator is Model-Based Integration — described as unique in the industry — which goes beyond brittle point-to-point mappings to scale to hundreds of projects across multiple tools using linked-data specifications. This offers real enterprise 'scalability, becuase model-based scaling is architecturally stronger than replicating point-to-point connections.

ELM is built around industry integration standard, the Open Service for Lifecycle Collaboration (OSLC). The Engineering Integration Hub provides bi-directional synchronisation out of the box, for requirements, stories, defects and test cases stay consistent across multi-vendor tools, with point-and-click project and field mapping rather than a services engagement. ELM doesn't just sync work items between 3rd Party tools, it is itself a system of record for requirements (DOORS Next), workflow (EWM) and test (ETM), all linked by a native OSLC digital thread with full traceability and impact analysis. (ConnectALL keeps data in scattered systems and mirrors it; ELM can be the authoritative source and federate the rest).

The ELM Hub ships over 60 prebuilt connectors across the Agile and DevOps lifecycle — including Jira, Azure DevOps, Jama and ServiceNow — configured through point-and-click, not custom code. 

End-to-End Traceability is the 'digital thread' of the organisation. Unlike standalone lightweight agile tools, ELM connects high-level requirements (via DOORS Next) directly to agile work items, system models, and test cases. For instance, if a requirement changes during a sprint, you can instantly see the downstream impact on testing and code. 

## Customer Reference

(not provided)

## IBM SECONDARY - Product Name (Supporting Product, where recommended to compliment the Primary capability)

IBM App Connect

## IBM SECONDARY - Product Description

Where needed for additional integration to compliment IBM ELM, then IBM App Connect Enterprise (ACE) provide 'any-to-any' integration. It connects applications, data sources, and services across hybrid cloud environments using an event-driven, low-code flow designer and a rich connector library covering enterprise SaaS, DevOps, ITSM, and messaging systems.

IBM Concert is an application resilience and dependency-mapping tool, not a bi-directional synchronisation engine for ALM and DevOps tools, so it is not a like-for-like replacement on its own. For IBM-native toolchain users (EWM, IBM Engineering Lifecycle Management), App Connect provides a documented integration path with IBM's own portfolio, offering a coherent end-to-end data flow from planning to delivery for wider integrations.

- **Bi-directional work item synchronisation** — Yes. App Connect supports event-driven flows triggered by changes in a source application (e.g., a new or updated issue in Jira) that push updates to a target application (e.g., ServiceNow or Azure DevOps), and vice versa. Documented native connectors exist for Jira (Cloud and Server), ServiceNow (incidents, problems, tickets, assets), Jenkins, GitLab, and GitHub, enabling bi-directional synchronisation patterns — though these must be configured explicitly as paired flows rather than being enabled by a single toggle as in ConnectALL.

- **Out-of-the-box integrations** — Yes. App Connect ships with a curated catalog of basic and premium connectors accessible directly from the Designer UI without custom coding; basic connectors (HTTP, JDBC, REST, LDAP, email) are included at no extra cost, while premium connectors covering enterprise applications such as SAP, Salesforce, Workday, ServiceNow, and Jira are licensed in packs of three. The IBM Automation Explorer community further extends the catalog with importable connectors, and OpenAPI, GraphQL, and SOAP imports are natively supported.

- **Data transformation and mapping intelligence layer** — Yes. App Connect includes a visual data-mapping canvas with auto-mapping of matching nodes, JSONata expression support for complex field transformations, XSLT stylesheet execution, and XML/flat-file schema handling. The AI-assisted mapping feature uses IBM's automation intelligence to suggest field mappings across dissimilar schemas — functionally equivalent to ConnectALL's transformation layer and applicable across portfolio-planning, delivery, and operations data flows.

- **Native ValueOps integration** — Partial. App Connect does not have pre-built connectors labelled specifically for Broadcom Clarity, Rally, or Insights. However, it can integrate with these tools via their published REST/SOAP APIs using the HTTP or imported-OpenAPI connector capability.

IBM App Connect Enterprise can do the underlying integration work, but it lacks ConnectALL's ready-made connectors for ALM, DevOps and ITSM tools. It should be adopted along with a deployment approach aligned to use of IBM ELM. 

Use with IBM ELM Suite. IBM App Connect Enterprise covers the underlying integration engine, data transformation, and connector breadth, but does not deliver ConnectALL's purpose-built, zero-code value stream synchronisation model out of the box. Additional flow design effort is required to replicate bi-directional ALM/DevOps/ITSM work-item sync. The match strengthens significantly where App Connect's native Jira, ServiceNow, Jenkins, and GitLab connectors already exist and are documented.

## IBM SECONDARY - Product Page(s) URL

https://www.ibm.com/docs/en/app-connect/13.0.x?topic=overview-app-connect-enterprise-introduction

# Sources:

## IBM App Connect Enterprise

- IBM App Connect Enterprise as a Service — product overview and connector catalog: https://www.ibm.com/products/app-connect
- IBM Docs — App Connect SaaS: How-to guides for applications (connector catalog, including Jira, ServiceNow, Jenkins, GitLab): https://www.ibm.com/docs/en/app-connect/saas
- IBM Docs — App Connect: Connecting to Jira (Cloud and Server) — authentication, events, and actions: https://www.ibm.com/docs/en/app-connect/saas?topic=apps-jira
- IBM Docs — App Connect: ServiceNow events and actions (incidents, problems, tickets, assets): https://www.ibm.com/docs/en/app-connect/saas?topic=apps-servicenow
- IBM Docs — App Connect: Connecting to Jenkins for CI/CD workflow integration: https://www.ibm.com/docs/en/app-connect/saas?topic=apps-jenkins
- IBM Docs — App Connect: How to use IBM App Connect with GitLab (DevOps CI/CD connector): https://www.ibm.com/docs/en/app-connect/saas?topic=apps-gitlab
- IBM Docs — App Connect: IBM App Connect components and resources — Connectors (basic vs premium, connector packs of three): https://www.ibm.com/docs/en/app-connect/saas?topic=overview-app-connect-components-resources
- IBM Docs — App Connect: Creating event-driven flows from scratch (event-trigger and action model for bi-directional sync): https://www.ibm.com/docs/en/app-connect/saas?topic=flows-creating-event-driven-flows-from-scratch
- IBM Docs — App Connect Professional: Mapping — data transformation, auto-mapping, JSONata, XSLT, and schema handling: https://www.ibm.com/docs/en/app-connect/professional
- IBM Docs — App Connect Enterprise as a Service: What's new — connector additions (2023–2024 release history): https://www.ibm.com/docs/en/app-connect/saas?topic=whats-new-in-ibm-app-connect-enterprise-as-a-service
- IBM Automation Explorer (community connectors for App Connect): https://explorer.automation.ibm.com/
- Gartner Peer Insights — IBM App Connect Enterprise reviews and ratings: https://www.gartner.com/reviews/market/enterprise-integration-platform-as-a-service/vendor/ibm/product/ibm-app-connect

## Sources: Analyst reviews and exist strategy

- Gartner Peer Insights, ConnectALL Value Stream Management Platform (no reviews recorded) (gartner.com/reviews/product/connectall-value-stream-management-platform)
- PeerSpot, ConnectALL vs Planview Hub comparison (peerspot.com/products/comparisons/connectall_vs_planview-tasktop-hub)
- Broadcom Academy, ConnectALL acquisition announcement (academy.broadcom.com/connectall) [vendor-published]
- Redress Compliance, Broadcom Enterprise Agreements guide, 2025
- The Register, 'Broadcom's stated strategy ignores most VMware customers', 2022 (https://www.theregister.com/software/2022/05/30/broadcoms-strategy-ignores-most-vmware-customers/1194871)

## General Sources:

- Introducing ConnectALL 4.0 (ValueOps blog): https://valueops.broadcom.com/blog/introducing-connectall-4-0
- Value Stream Integration - ValueOps ConnectALL (product page): https://valueops.broadcom.com/products/connectall
- ValueOps ConnectALL Capabilities - Broadcom TechDocs: https://techdocs.broadcom.com/us/en/ca-enterprise-software/valueops/valueops-solution/ValueOps-Solution/n-valueops-capabilities/valueops-connectall-capabilities.html
- Broadcom acquires ConnectALL - SD Times: https://sdtimes.com/vsm/broadcom-acquires-connectall/
- Broadcom Adds ConnectALL's Technology to its ValueOps VSM Portfolio (6 June 2023): https://academy.broadcom.com/blog/valueops/broadcom-adds-connectall

## Change history:
