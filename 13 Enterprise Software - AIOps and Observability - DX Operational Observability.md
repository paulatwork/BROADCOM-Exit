# DX Operational Observability

## Status 

Draft

## Broadcom Software Type

Enterprise Software

## Broadcom Product Category

AIOps and Observability

## Broadcom Product Name

DX Operational Observability

## Broadcom Product Description (Key Features) (This is important to get right)

DX Operational Observability (DX O2) is Broadcom's unified AIOps and observability platform, delivered as SaaS and on-premises (26.1 on-premises documentation is current). It consolidates application, infrastructure, network and log data with OpenTelemetry support, generative AI summarisation and CI-based alarm enrichment. Native synthetics monitoring for the SaaS edition was announced in May 2026.

Key features:

1. **Unified observability** - Brings APM, infrastructure, network and log analytics into one platform for cross-domain correlation.
2. **OpenTelemetry support** - Collects metrics and traces using the industry standard OpenTelemetry.
3. **Generative AI summarisation** - Uses a large language model to accelerate diagnostics, and tenant administrators can substitute their own Google Vertex AI project.
4. **Alarm enrichment and ITSM integration** - Enrichment rules add configuration item attributes to matched alarms, and the platform integrates with ServiceNow (Xanadu).

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

Commercial pressure: Broadcom's consolidation of the former DX APM, DX Operational Intelligence and Application Experience Analytics products into DX Operational Observability moves customers onto a single bundled licence. Independent user reviews of the predecessor product lines (see the DX APM and DX Operational Intelligence rows in this schedule) describe minimum-commitment thresholds and renewal increases consistent with Broadcom's core-account pricing approach across its enterprise software portfolio.

Analyst standing: independent review volume for this product is thin. Gartner Peer Insights lists Broadcom within its Observability Platforms market category, compared against Dynatrace and LogicMonitor, but with limited published review volume. In Forrester's Q2 2025 Wave for AIOps Platforms, Dynatrace and Datadog were the vendors publicly announced as Leaders; Broadcom was not identified among the leaders named in public vendor announcements of that report. This should be treated as an indicator of lower current analyst visibility for DX Operational Observability rather than a comprehensive assessment, since the full Forrester participant list was not independently sighted.

Exit strategy: organisations are moving toward cloud-native, unified observability platforms with broader ecosystem support and shorter time-to-value, principally IBM Instana, Dynatrace, Datadog and New Relic, all of which hold current independent analyst leader positions in observability and AIOps. The alternatives listed in this row are realistic and consistent with the wider market direction.

Sources: Gartner Peer Insights, Observability Platforms market, Broadcom vendor page (gartner.com); Dynatrace and Datadog public announcements of the Forrester Wave: AIOps Platforms, Q2 2025 (dynatrace.com; datadoghq.com); Broadcom TechDocs, DX Operational Observability product documentation (techdocs.broadcom.com).

## IBM Replacement Strength

Yes

## IBM Replacement Strategy - Why IBM over Broadcom

(not provided)

## PRIMARY - Key Product - IBM Alternative

IBM Instana Observability

## PRIMARY - Key Product Capability Statement - IBM Alternative

General sentiment: Positive – rated about 4.3 stars from roughly 265 Gartner Peer Insights reviews for easy dashboards and automatic discovery, with no consistent criticism surfaced in this pass.

Next-generation AIOps and Observability. IBM Instana Observability provides full-stack automated observability and enterprise AIOps with 1-second metric granularity and unsampled end-to-end distributed tracing. It automatically discovers, monitors, and maps dependencies across multi-cloud, containerized microservices, on-premises systems, and IBM zSystems mainframes to provide immediate AI-powered root cause analysis.

## PRIMARY - IBM Product Page URL

https://www.ibm.com/products/instana

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

- DX Operational Observability SaaS Release Notes: https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/dx-operational-observability/saas/release-notes.html
- DX Operational Observability 26.1 (on-premises): https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/dx-operational-observability-onprem/26-1.html
- Office Hours: Native Synthetics Monitoring Coming to DX Operational Observability (SaaS): https://community.broadcom.com/discussion/upcoming-event-office-hours-aiops-may-26-2026-native-synthetics-monitoring-coming-to-dx-operational-observability-saas
- DX Operational Observability (product page): https://www.broadcom.com/products/software/aiops-observability/operational-observability
- DX APM 23.3 End of Life Announcement: https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/ReleaseAnnouncements/DX-APM-23-3-End-of-Life-Announcement/25286

## Change history:

### 2026-09-19 - Broadcom product information verification (WebFetch pass, files 02-39)
- Verified: Broadcom's DX APM 23.3 end-of-life announcement describes DX Operational Observability as combining application, digital experience and infrastructure monitoring with integrated AIOps, which supports the consolidation statement in Analyst Cautions. No changes.

### 2026-09-19 - Broadcom product information review
- Product description: Added GenAI summarisation, alarm enrichment, ServiceNow integration, on-premises 26.1 and native synthetics announcement. The WatchTower mainframe reference was not re-verified and was removed.
- Summary and numbered list of four key features rewritten from current Broadcom sources.
- General Sources: 4 sources recorded (Broadcom TechDocs, product pages, press releases where available).

### 2026-09-19 - IBM alternative product verification and sentiment (WebFetch and WebSearch pass, files 02-39)
- Requirement match against the Key Features section: Meets most requirements; network and log analytics via other products.
- Confirmed (IBM product page): OpenTelemetry integration, Kubernetes and infrastructure monitoring, over 300 supported technologies and GenAI workflow discovery. Tracing for WebSphere and Liberty on z/OS was confirmed through IBM community material.
- Not confirmed: log analytics, ServiceNow integration and LLM summarisation of diagnostics. Network monitoring is not an Instana function (see SevOne, file 12).
- Sentiment: added a one-sentence summary of general market sentiment at the start of the Key Product Capability Statement. Existing statement text was not changed.
- Sources: https://www.ibm.com/products/instana; https://medium.com/ibm-cloud/enabling-instana-tracing-for-websphere-and-liberty-on-z-os-environment-278d30684b8b; https://www.gartner.com/reviews/product/ibm-instana-observability
