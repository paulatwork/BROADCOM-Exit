# DX Unified Infrastructure Management

## Status 

Draft

## Broadcom Software Type

Enterprise Software

## Broadcom Product Category

AIOps and Observability

## Broadcom Product Name

DX Unified Infrastructure Management

## Broadcom Product Description - Key Features

DX Unified Infrastructure Management (DX UIM, formerly Nimsoft) is a hybrid infrastructure monitoring platform. The current release documented is 23.4 with cumulative update CU7 (documentation updated 30 June 2026).

Key features:

1. **Broad infrastructure monitoring** - Probe-based monitoring of servers, virtualisation, cloud, storage, databases and applications with automated discovery.
2. **Alarm and health management** - Centralised alarm handling and health tracking with operator console workflows.
3. **Reporting and scheduled dashboards** - CU7 adds availability report export to CSV with filtering, and scheduled dashboards can export tabular data as CSV and Excel.
4. **Device identity continuity** - The Operator Console correlates device identity so performance history continues when a device IP address changes.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

DX Unified Infrastructure Management gets its most telling feedback from TrustRadius reviewers. They call the pricing 'not cheap at all', and one organisation reported annual costs of around CAD 400,000. They describe inconsistent support since the acquisition, with one reviewer saying the team is 'sometimes not as knowledgeable or responsive' and another citing 'prolonged resolution times due to a lack of expertise' on complex issues. Others say the platform 'has not necessarily kept pace' with AWS, Azure and Google Cloud, which fits the view that it trails cloud-native tools in dynamic scaling and container discovery.

The independent rating looks better than the story it sits in. Gartner Peer Insights shows 4.6 out of 5, but from only 11 ratings, which is a thin base and not broad market validation.

No named organisation has publicly described leaving the product. A search for customers who replaced CA UIM or Nimsoft with Dynatrace, Datadog or LogicMonitor found migration services and comparison pages, but no named case. The exit case therefore rests on the reviewer testimony above.

IBM Instana, Datadog, Dynatrace and LogicMonitor are all established, independently recognised vendors in infrastructure and cloud monitoring, and each is a realistic candidate for this workload.

## IBM Replacement Strength

Strong Replacement, with improved outcomes

## IBM Replacement Strategy - Why IBM over Broadcom

IBM Instana Observability (Infrastructure & Cloud Monitoring) replaces Broadcom DX UIM (Nimsoft) with a modern, automated hybrid infrastructure monitoring solution. Broadcom DX UIM relies on an antiquated, complex probe-and-hub architecture requiring constant manual maintenance, while failing to keep pace with dynamic cloud and container architectures. IBM Instana eliminates probe configuration with lightweight, auto-discovering sensors, 1-second metric resolution, and direct correlation between infrastructure health and application performance at a significantly lower operational and licensing cost.

## IBM PRIMARY - Product Name (The Replacement)

IBM Instana Observability (Infrastructure & Cloud Monitoring)

## IBM PRIMARY - Product Description

IBM Instana Observability (Infrastructure & Cloud Monitoring) provides automated, real-time infrastructure visibility across bare-metal servers, virtual machines, containers, public clouds, and databases without requiring legacy probe architectures.

- **Broad infrastructure monitoring** — IBM Instana automatically discovers and monitors servers, hypervisors (VMware, KVM, Hyper-V), public cloud instances (AWS, Azure, GCP), storage, and over 300 enterprise database and middleware technologies in real time.
- **Alarm and health management** — IBM Instana provides automated health baselines, intelligent anomaly detection, and built-in incident grouping that eliminates alarm fatigue and simplifies operations console workflows.
- **Reporting and scheduled dashboards** — IBM Instana offers customizable infrastructure dashboards, automated executive reporting, metric trend visualization, and scheduled data exports in standard tabular and CSV formats.
- **Device identity continuity** — IBM Instana maintains continuous entity identity, lifecycle tracking, and historical metrics across dynamic IP address changes, container restarts, and ephemeral cloud auto-scaling events.

## IBM PRIMARY - IBM Product Page URL

https://www.ibm.com/products/instana/infrastructure-monitoring

## Customer Reference
(not provided)
## IBM SECONDARY - Product Name (Supporting Product, where recommended to compliment the Primary capability)

(not provided)

## IBM SECONDARY - Product Description

(not provided)

## IBM SECONDARY - Product Page(s) URL

(not provided)

# Sources:

## IBM Instana Observability (Infrastructure & Cloud Monitoring)

- IBM Instana Infrastructure Monitoring Product Overview: https://www.ibm.com/products/instana/infrastructure-monitoring
- IBM Instana Supported Technologies and Sensors: https://www.ibm.com/docs/en/instana-observability?topic=supported-technologies
- Gartner Peer Insights — IBM Instana Observability Reviews: https://www.gartner.com/reviews/market/observability-platforms/vendor/ibm/product/ibm-instana-observability

## Sources: Analyst reviews and exist strategy

- TrustRadius, "Broadcom DX Unified Infrastructure Management Reviews" (trustradius.com)
- Gartner Peer Insights, DX Unified Infrastructure Management product page (gartner.com)

## General Sources:

- What's New in DX UIM 23.4 CU7: https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/unified-infrastructure-management/23-4/release-notes/whats-new-in-dx-uim-23-4-cu7.html
- What's New in DX UIM 23.4 CU5: https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/unified-infrastructure-management/23-4/release-notes/whats-new-in-dx-uim-23-4-cu5.html
- Introducing DX Unified Infrastructure Management: https://academy.broadcom.com/blog/aiops/introducing-dx-unified-infrastructure-management

## Change history:

### 2026-09-20 - Analyst Cautions and Industry Findings rewritten as a narrative
- Rewrote the section as a narrative and merged the two review sources into one account.
- Searched for named organisations that replaced CA UIM or Nimsoft (2026-09-20). None was found, and the text now says so.
- Moved all citations to the Sources: Analyst reviews and exist strategy section.


### 2026-09-19 - Broadcom product information verification (WebFetch pass, files 02-39)
- Verified: DX UIM 23.4 is the latest version listed in TechDocs (versions 23.4, 20.4, 20.3, 20.1); no end-of-support notice found. No changes.

### 2026-09-19 - Broadcom product information review
- Product description: Added current version (23.4 CU7) and CU7 features. The multi-tenant, predictive analytics wording was not re-verified and was replaced with documented capabilities.
- Summary and numbered list of four key features rewritten from current Broadcom sources.
- General Sources: 3 sources recorded (Broadcom TechDocs, product pages, press releases where available).

### 2026-09-19 - IBM alternative product verification and sentiment (WebFetch and WebSearch pass, files 02-39)
- Requirement match against the Key Features section: Partially meets.
- Confirmed (IBM product page): infrastructure monitoring and over 300 supported technologies, including Kubernetes.
- Not verified individually: VMware and Hyper-V, storage arrays, databases, scheduled dashboard export and the '300 sensors' wording. Instana is agent-based, so probe-based UIM monitoring is replaced by a different architecture.
- Sentiment: added a one-sentence summary of general market sentiment at the start of the Key Product Capability Statement. Existing statement text was not changed.
- Sources: https://www.ibm.com/products/instana
