# AutoSys Workload Automation

## Status 

Draft

## Broadcom Software Type

Enterprise Software

## Broadcom Product Category

Enterprise Workload Automation

## Broadcom Product Name

AutoSys Workload Automation

## Broadcom Product Description (Key Features) (This is important to get right)

AutoSys Workload Automation is Broadcom's job scheduling and workload automation engine, using Job Information Language (JIL). Documentation is available for release 24.2, with 24.1 adding TLS-encrypted scheduler-to-agent communication and an enhanced Monitor interface.

Key features:

1. **Dependency-based job scheduling** - Defines jobs, dependencies, calendars and conditions in JIL across platforms.
2. **Event-driven and cross-platform automation** - Triggers workflows from events and manages jobs across operating systems and applications through system agents.
3. **Secure communication** - From 24.1, TLS encrypts job data, commands and agent responses between scheduler and agents; the agent supports HTTPS.
4. **Unified Monitor interface** - Provides job details, schedules, events, alarms and logs, including job definitions in tabular form and log analysis for all job types.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

Beta Systems, a competing vendor, publishes a detailed comparison identifying four recurring reasons organisations cite for moving away from AutoSys: pricing volatility, with "significant, often unexpected price increases at renewal" since the Broadcom acquisition; limited native integration with AWS and Azure; a lack of the richer reporting, alerting and predictive analytics expected of modern platforms; and friction between the JIL scripting model and modern DevOps/CI/CD and infrastructure-as-code practices. As vendor-authored competitive content, these claims should be treated as directionally credible rather than independently verified, but they are consistent with the broader, independently documented Broadcom renewal-pricing pattern.

Analyst standing: AutoSys sits within Gartner's Service Orchestration and Automation Platforms category, where Broadcom was named a Leader in the 2025 Magic Quadrant. As with Automic Automation, this recognition should be read alongside customer pricing concerns rather than instead of them.

Exit strategy and alternatives check: the alternatives listed in this row (IBM Workload Automation, Redwood RunMyJobs, Astronomer/Apache Airflow, BMC Control-M) are realistic; all except Airflow appear as named vendors in the current Gartner Magic Quadrant for this category, and Apache Airflow/Astronomer is a widely adopted open-source alternative for engineering-led teams, consistent with Beta Systems' own comparison.

Sources: Beta Systems, "AutoSys Alternatives: 6 Best Replacements & Tools for 2026" (betasystems.com), noted as vendor-authored competitive content; Broadcom Academy, "Broadcom Recognized as a Leader: Engineering the Future of Service Orchestration" (academy.broadcom.com), referencing the 2025 Gartner Magic Quadrant for Service Orchestration and Automation Platforms.

## IBM Replacement Strength

(not provided)

## IBM Replacement Strategy - Why IBM over Broadcom

(not provided)

## PRIMARY - Key Product - IBM Alternative

IBM Workload Automation

## PRIMARY - Key Product Capability Statement - IBM Alternative

General sentiment: Positive but thinly evidenced – reviewers praise stability and plug-in breadth, while noting complex installation and upgrades and weak documentation (only two Gartner Peer Insights reviews were found).

IBM Workload Automation provides an enterprise batch scheduling engine designed to replace legacy AutoSys JIL architectures. It features advanced cross-platform dependency mapping, calendar and event-driven job triggers, centralized Dynamic Workload Console management, REST API orchestration, and automated critical-path SLA tracking.

## PRIMARY - IBM Product Page URL

https://www.ibm.com/products/workload-automation

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

- AutoSys Workload Automation New Features in Release 24.1: https://techdocs.broadcom.com/us/en/ca-enterprise-software/intelligent-automation/autosys-workload-automation/11-3-6/release-notes/ae-release-notes24-1/new-features-r24-1-00.html
- AutoSys Workload Automation 24.2: https://techdocs.broadcom.com/us/en/ca-enterprise-software/intelligent-automation/autosys-workload-automation/24-2-00.html
- Key Capabilities of AutoSys Workload Automation: https://techdocs.broadcom.com/us/en/ca-enterprise-software/intelligent-automation/autosys-workload-automation/24-0-01/getting-started/key-capabilities-of-autosys.html

## Change history:

### 2026-09-19 - Broadcom product information verification (WebFetch pass, files 02-39)
- Verified: AutoSys 24.2.00 is the latest version listed in TechDocs, and the 2025 Gartner Leader placement stands. No changes.

### 2026-09-19 - Broadcom product information review
- Product description: Added current release line (24.x) with TLS and Monitor features. Release 24.2 feature detail was not reviewed.
- Summary and numbered list of four key features rewritten from current Broadcom sources.
- General Sources: 3 sources recorded (Broadcom TechDocs, product pages, press releases where available).

### 2026-09-19 - IBM alternative product verification and sentiment (WebFetch and WebSearch pass, files 02-39)
- Requirement match against the Key Features section: Partially meets.
- Confirmed (IBM product page): event-driven processes, orchestration across platforms and a single monitoring point.
- Not confirmed on the page: explicit dependency and calendar scheduling, TLS-encrypted agent communication and a JIL conversion path. The JIL replacement claim and critical-path SLA tracking should be confirmed with IBM.
- Sentiment: added a one-sentence summary of general market sentiment at the start of the Key Product Capability Statement. Existing statement text was not changed.
- Sources: https://www.ibm.com/products/workload-automation; https://www.gartner.com/reviews/product/ibm-workload-automation
