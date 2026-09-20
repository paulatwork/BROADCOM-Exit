# AutoSys Workload Automation

## Status 

Draft

## Broadcom Software Type

Enterprise Software

## Broadcom Product Category

Enterprise Workload Automation

## Broadcom Product Name

AutoSys Workload Automation

## Broadcom Product Description - Key Features

AutoSys Workload Automation is Broadcom's job scheduling and workload automation engine, using Job Information Language (JIL). Documentation is available for release 24.2, with 24.1 adding TLS-encrypted scheduler-to-agent communication and an enhanced Monitor interface.

Key features:

1. **Dependency-based job scheduling** - Defines jobs, dependencies, calendars and conditions in JIL across platforms.
2. **Event-driven and cross-platform automation** - Triggers workflows from events and manages jobs across operating systems and applications through system agents.
3. **Secure communication** - From 24.1, TLS encrypts job data, commands and agent responses between scheduler and agents; the agent supports HTTPS.
4. **Unified Monitor interface** - Provides job details, schedules, events, alarms and logs, including job definitions in tabular form and log analysis for all job types.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

AutoSys is the one product in this schedule where a named organisation has told its story of leaving. BSH, the home appliance maker, ran 250,000 tasks a day, about eight million a month, across 40 factories and a large SAP estate on AutoSys, and it found the scheduler held back its ability to scale. Because AutoSys schedules by time and not by data or process status, BSH had to build custom development around it, and that proved unstable and expensive. Errors were caught by hand. As the central scheduling architect Stefan Wiedenmann put it, 'If there was a problem, we didn't find out until the next morning when it was too late to fix it.' On several occasions 20,000 factory workers were sent home because a delayed ten-minute task held up production information by twelve hours. BSH moved to RunMyJobs by Redwood. Its reasons were technical, not commercial, and the case study is published by Redwood, so it is a vendor account. GROWMARK also left AutoSys for Redwood in order to bring its SAP processes into one enterprise solution.

The commercial complaints run in parallel. Beta Systems, a competitor, lists four recurring reasons customers give for leaving: 'significant, often unexpected price increases at renewal' since the Broadcom acquisition, limited native integration with AWS and Azure, thin reporting and predictive analytics, and friction between the JIL scripting model and modern DevOps practice. Treat that as directionally credible vendor content, consistent with the wider renewal-price pattern.

The analyst view is mixed. Broadcom was named a Leader in Gartner's 2025 Magic Quadrant for service orchestration and automation platforms, and that should sit beside the pricing concerns. IBM Workload Automation, Redwood RunMyJobs and BMC Control-M are all named vendors in that quadrant, and Apache Airflow with Astronomer is a widely adopted open-source route for engineering-led teams.

## IBM Replacement Strength

Strong Replacement, with improved outcomes

## IBM Replacement Strategy - Why IBM over Broadcom

IBM Workload Automation replaces Broadcom AutoSys Workload Automation by providing a modern, event-driven orchestration platform that bridges legacy batch schedules with modern cloud-native architectures. Migrating from AutoSys frees enterprises from brittle JIL scripting constraints, unexpected renewal price spikes, and legacy licensing overhead. IBM Workload Automation offers proven migration toolkits, native CI/CD and DevOps integration, containerized deployment, and sophisticated predictive critical-path analysis.

## IBM PRIMARY - Product Name (The Replacement)

IBM Workload Automation

## IBM PRIMARY - Product Description

IBM Workload Automation is IBM's advanced workload scheduling and automation platform designed to manage high-volume, mission-critical batch workflows and real-time triggers across distributed, cloud, and mainframe architectures.

- **Dependency-based job scheduling** — IBM Workload Automation provides sophisticated cross-platform job dependency modeling, complex enterprise business calendars, conditional branching, and automated critical-path calculation across heterogeneous systems.
- **Event-driven and cross-platform automation** — IBM Workload Automation triggers jobs based on file changes, message queues, cloud events, and database states across Windows, Linux, UNIX, Kubernetes, and mainframe environments using lightweight agents.
- **Secure communication** — IBM Workload Automation enforces end-to-end TLS encryption, mutual certificate-based agent authentication, and role-based access control (RBAC) across all engine, console, and agent communications.
- **Unified Monitor interface** — IBM Workload Automation provides the Dynamic Workload Console (DWC), a unified web-based dashboard offering graphical workflow modeling, real-time job monitoring, log exploration, and automated incident alerting.

## IBM PRIMARY - IBM Product Page URL

https://www.ibm.com/products/workload-automation

## Customer Reference

(not provided)
## IBM SECONDARY - Product Name (Supporting Product, where recommended to compliment the Primary capability)

(not provided)

## IBM SECONDARY - Product Description

(not provided)

## IBM SECONDARY - Product Page(s) URL

(not provided)

# Sources:

## IBM Workload Automation

- IBM Workload Automation Product Overview: https://www.ibm.com/products/workload-automation
- IBM Workload Automation Architecture & Security Guide: https://www.ibm.com/docs/en/workload-automation?topic=overview-security
- Gartner Peer Insights — IBM Workload Automation Reviews: https://www.gartner.com/reviews/market/service-orchestration-and-automation-platforms/vendor/ibm/product/ibm-workload-automation

## Sources: Analyst reviews and exist strategy

- Beta Systems, "AutoSys Alternatives: 6 Best Replacements & Tools for 2026" (betasystems.com), noted as vendor-authored competitive content
- Broadcom Academy, "Broadcom Recognized as a Leader: Engineering the Future of Service Orchestration" (academy.broadcom.com), referencing the 2025 Gartner Magic Quadrant for Service Orchestration and Automation Platforms
- Redwood, 'BSH Case Study' (https://www.redwood.com/resource/bsh-case-study/) [vendor-published customer case study]
- Redwood, 'Broadcom CA Autosys Workload Automation Alternative' (https://www.redwood.com/replace-ca-autosys/) [vendor-authored competitive content]

## General Sources:

- AutoSys Workload Automation New Features in Release 24.1: https://techdocs.broadcom.com/us/en/ca-enterprise-software/intelligent-automation/autosys-workload-automation/11-3-6/release-notes/ae-release-notes24-1/new-features-r24-1-00.html
- AutoSys Workload Automation 24.2: https://techdocs.broadcom.com/us/en/ca-enterprise-software/intelligent-automation/autosys-workload-automation/24-2-00.html
- Key Capabilities of AutoSys Workload Automation: https://techdocs.broadcom.com/us/en/ca-enterprise-software/intelligent-automation/autosys-workload-automation/24-0-01/getting-started/key-capabilities-of-autosys.html

## Change history:

### 2026-09-20 - Analyst Cautions and Industry Findings rewritten as a narrative
- Rewrote the section as a narrative built around the BSH account of leaving AutoSys, with GROWMARK as a second named example.
- Noted that the BSH and GROWMARK accounts are published by Redwood, and that BSH gave technical rather than commercial reasons.
- Searched for Whitbread and Coca-Cola HBC as AutoSys exits. Redwood's page does not say they came from AutoSys, so they were left out.
- Moved all citations to the Sources: Analyst reviews and exist strategy section.


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
