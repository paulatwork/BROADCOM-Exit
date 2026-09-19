# Application Performance Management

## Status 

Draft

## Broadcom Software Type

Enterprise Software

## Broadcom Product Category

AIOps and Observability

## Broadcom Product Name

Application Performance Management

## Broadcom Product Description (Key Features) (This is important to get right)

DX APM (formerly CA APM and Wily Introscope) provides application performance monitoring within DX Operational Observability. The agent release line is current (26.8.1 in 2026), with centralised agent management and Kubernetes operator support.

Key features:

1. **Code-level application monitoring** - Agents instrument Java, .NET and other stacks for transaction tracing and performance diagnostics.
2. **Centralised agent management** - Agent Controller (ACC) bundles deliver agent versions, and CloudProxy log improvements aid troubleshooting agents behind load balancers.
3. **Kubernetes and container support** - The Universal Monitoring Agent (UMA) operator has a CLI upgrade method that synchronises agent version and status into DX O2.
4. **Platform coverage** - Release 26.8.1 certifies WebSphere and WebSphere Liberty on z/OS 3.2.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

PeerSpot user reviews of DX Application Performance Management provide specific, verifiable evidence. Reviewers cite a licensing model "based on agent count rather than usage," with annual renewal increases "reportedly ~20%+," and describe the product as "generally perceived as expensive versus modern alternatives." Reported technical limitations include missing AI/ML capabilities compared with Dynatrace, limited cloud and container support (including OpenShift 4 compatibility issues), and inconsistent support quality through the ticketing system. Broadcom's own support portal has issued an end-of-life notice for legacy DX APM versions (including 23.3), confirming the lifecycle-deadline pressure already noted in this row. Broadcom's announcement gives 30 December 2025 as the date technical support for DX APM 23.3 ended and recommends migrating to DX Operational Observability 24.2.

Analyst standing: Broadcom (as CA Technologies) was last named a Leader in Gartner's Magic Quadrant for Application Performance Monitoring Suites in 2019, the final edition of that named research. Gartner has since replaced it with the Magic Quadrant for Application Performance Monitoring and Observability, and Broadcom does not appear among the vendors publicly named as Leaders in current vendor-published summaries of the 2025-2026 research, which instead cite Datadog, Dynatrace, Elastic, New Relic and Grafana. This is treated as an indicator of declining analyst visibility rather than a confirmed ranking, since the full current Magic Quadrant document itself was not sighted.

Exit strategy: the alternatives already listed in this row (IBM Instana, Dynatrace, Datadog, New Relic) are consistent with the vendors organisations are independently reported to be adopting for automated, agentless APM, and are realistic.

Sources: PeerSpot, "Broadcom DX Application Performance Management Reviews" (peerspot.com); Broadcom Support Portal, DX APM end-of-life announcement (support.broadcom.com); Broadcom/GlobeNewswire, "Broadcom Named a Leader in the Gartner Magic Quadrant for Application Performance Monitoring Suites for Second Consecutive Year" (globenewswire.com, 2019), cited to establish the last confirmed Leader placement.

## IBM Replacement Strength

Yes

## IBM Replacement Strategy - Why IBM over Broadcom

(not provided)

## PRIMARY - Key Product - IBM Alternative

IBM Instana Observability (APM)

## PRIMARY - Key Product Capability Statement - IBM Alternative

General sentiment: Positive – rated about 4.3 stars from roughly 265 Gartner Peer Insights reviews for easy dashboards and automatic discovery, with no consistent criticism surfaced in this pass.

Traditional Application Performance Management (APM) solutions often fall short in delivering the visibility needed to fix problems before they impact the end user. IBM Instana Observability delivers an automated, zero-touch Application Performance Monitoring (APM) platform designed to replace legacy Wily Introscope agents. It captures 100% of end-user transactions without sampling, profiles code-level execution in real time, maps dynamic microservice topologies, and isolates offending code lines automatically without manual agent configuration.

## PRIMARY - IBM Product Page URL

https://www.ibm.com/products/instana/application-performance-monitoring

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

- DX APM Agents 26.8.1 Release Notes: https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/dx-apm-agents/26-8-1/release-notes/26-8-1.html
- DX APM Agents SaaS Release Notes: https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/dx-apm-agents/SaaS/release-notes.html
- DX Operational Observability SaaS Release Notes: https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/dx-operational-observability/saas/release-notes.html

## Change history:

### 2026-09-19 - Broadcom product information verification (WebFetch pass, files 02-39)
- Analyst Cautions: added the verified date (30 December 2025) and recommended migration target (DX Operational Observability 24.2) from Broadcom's DX APM 23.3 end-of-life announcement.

### 2026-09-19 - Broadcom product information review
- Product description: Corrected the earlier statement that the product relies on manual agent deployment: ACC bundles and the UMA operator provide managed deployment and upgrade. Added 26.8.1 release detail.
- Summary and numbered list of four key features rewritten from current Broadcom sources.
- General Sources: 3 sources recorded (Broadcom TechDocs, product pages, press releases where available).

### 2026-09-19 - IBM alternative product verification and sentiment (WebFetch and WebSearch pass, files 02-39)
- Requirement match against the Key Features section: Meets most requirements.
- Confirmed: Kubernetes monitoring, OpenTelemetry, and tracing for WebSphere and Liberty on z/OS; Gartner-listed strengths include tracing each request and profiling every process.
- Not verified: '100 percent unsampled' capture (not stated on the IBM page fetched), centralised agent management and WebSphere on z/OS 3.2 certification.
- Sentiment: added a one-sentence summary of general market sentiment at the start of the Key Product Capability Statement. Existing statement text was not changed.
- Sources: https://www.ibm.com/products/instana; https://medium.com/ibm-cloud/enabling-instana-tracing-for-websphere-and-liberty-on-z-os-environment-278d30684b8b; https://www.gartner.com/reviews/product/ibm-instana-observability
