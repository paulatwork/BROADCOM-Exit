# Application Performance Management

## Page Status 

Draft

## Broadcom Software Type

Enterprise Software

## Broadcom Product Category

AIOps and Observability

## Broadcom Product Name

Application Performance Management

## Broadcom Product Description - Key Features

DX APM (formerly CA APM and Wily Introscope) provides application performance monitoring within DX Operational Observability. The agent release line is current (26.8.1 in 2026), with centralised agent management and Kubernetes operator support.

Key features:

1. **Code-level application monitoring** - Agents instrument Java, .NET and other stacks for transaction tracing and performance diagnostics.
2. **Centralised agent management** - Agent Controller (ACC) bundles deliver agent versions, and CloudProxy log improvements aid troubleshooting agents behind load balancers.
3. **Kubernetes and container support** - The Universal Monitoring Agent (UMA) operator has a CLI upgrade method that synchronises agent version and status into DX O2.
4. **Platform coverage** - Release 26.8.1 certifies WebSphere and WebSphere Liberty on z/OS 3.2.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

Reviewers of DX Application Performance Management on PeerSpot describe a product that is expensive and ageing. Licensing is 'based on agent count rather than usage', renewal increases are 'reportedly ~20%+', and the product is 'generally perceived as expensive versus modern alternatives'. They also point to missing AI and machine learning features compared with Dynatrace, limited cloud and container support, including OpenShift 4 compatibility problems, and support that varies in quality through the ticketing system.

Broadcom's own lifecycle notices add urgency. Technical support for DX APM 23.3 ended on 30 December 2025, and Broadcom recommends moving to DX Operational Observability 24.2, so customers are being pushed onto a new licensing model whether they want to move or not.

The analyst picture has faded. As CA Technologies, Broadcom was last named a Leader in Gartner's Magic Quadrant for application performance monitoring suites in 2019, the final edition under that name. Gartner has since replaced it with a report on application performance monitoring and observability, and vendor summaries of the 2025 and 2026 research name Datadog, Dynatrace, Elastic, New Relic and Grafana as Leaders, not Broadcom. The full report was not seen, so this is an indicator and not a confirmed ranking.

No named organisation has publicly described leaving DX APM. Broadcom, for its part, runs a customer-research page titled 'Customers Applaud CA APM over Dynatrace', which is vendor-commissioned and should be read that way. IBM Instana, Dynatrace, Datadog and New Relic remain the realistic destinations for automated, agentless monitoring.

## IBM PRIMARY - Product Name (The Replacement)

IBM Instana Observability (APM)

## IBM PRIMARY - IBM Product Page URL

https://www.ibm.com/products/instana/application-performance-monitoring

## IBM Replacement Strength

Strong Replacement, with improved outcomes

## IBM Replacement Strategy (Short)

Instana replaces agent-heavy DX APM with zero-touch, unsampled tracing, Kubernetes support and lower licensing costs.

## IBM Replacement Strategy (Description - Why IBM over Broadcom)

IBM Instana Observability replaces Broadcom DX APM (legacy CA Wily Introscope) with a modern, zero-touch application performance monitoring solution. Broadcom DX APM imposes heavy agent maintenance overhead, per-agent licensing penalties with 20%+ renewal increases, and lagging support for containerized cloud platforms. IBM Instana eliminates manual agent configuration through automated discovery and continuous code profiling, captures unsampled end-to-end transactions, and provides deep mainframe-to-cloud visibility at a significantly lower operational and commercial footprint.

## IBM PRIMARY - Product Description

IBM Instana Observability is IBM's automated Application Performance Monitoring (APM) and full-stack observability solution. It continuously monitors, traces, and profiles distributed microservices, legacy monoliths, and enterprise middleware with 1-second metric resolution and zero manual instrumentation.

- **Code-level application monitoring** — IBM Instana automatically injects runtime sensors into Java, .NET, Node.js, Python, Go, and PHP applications, capturing 100% of distributed transactions and profiling code-level execution down to exact method calls and database statements without sampling.
- **Centralised agent management** — IBM Instana utilizes a single, lightweight host agent with automated dynamic sensor loading and centralized over-the-air version management, eliminating manual agent installation, bundle updates, and proxy configuration.
- **Kubernetes and container support** — IBM Instana features an automated Kubernetes operator and OpenShift Certified Operator that instantly discovers containerized pods, microservice dependencies, and dynamic cluster topologies without manual tagging.
- **Platform coverage** — IBM Instana provides industry-leading platform coverage from modern public clouds and Kubernetes clusters to enterprise middleware, including deep tracing for IBM WebSphere, WebSphere Liberty on z/OS, and mainframe transactions.

## Customer Reference

(not provided)
## IBM SECONDARY - Product Name (Supporting Product, where recommended to compliment the Primary capability)

(not provided)

## IBM SECONDARY - Product Description

(not provided)

## IBM SECONDARY - Product Page(s) URL

(not provided)

# Sources:

## IBM Instana Observability (APM)

- IBM Instana Application Performance Monitoring Product Overview: https://www.ibm.com/products/instana/application-performance-monitoring
- IBM Instana Mainframe and z/OS Tracing Capabilities: https://medium.com/ibm-cloud/enabling-instana-tracing-for-websphere-and-liberty-on-z-os-environment-278d30684b8b
- Gartner Peer Insights — IBM Instana Observability Reviews: https://www.gartner.com/reviews/market/observability-platforms/vendor/ibm/product/ibm-instana-observability

## Sources: Analyst reviews and exist strategy

- PeerSpot, "Broadcom DX Application Performance Management Reviews" (peerspot.com)
- Broadcom Support Portal, DX APM end-of-life announcement (support.broadcom.com)
- Broadcom/GlobeNewswire, "Broadcom Named a Leader in the Gartner Magic Quadrant for Application Performance Monitoring Suites for Second Consecutive Year" (globenewswire.com, 2019), cited to establish the last confirmed Leader placement
- Broadcom, 'DX Application Performance Management (APM)' customer success page (https://www.broadcom.com/info/aiops/customer-success-dx-application-performance-management) [vendor-published]
- TechValidate, 'Customers Applaud CA APM over Dynatrace' (https://www.techvalidate.com/portals/customers-applaud-ca-apm-over-dynatrace) [vendor-commissioned]

## General Sources:

- DX APM Agents 26.8.1 Release Notes: https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/dx-apm-agents/26-8-1/release-notes/26-8-1.html
- DX APM Agents SaaS Release Notes: https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/dx-apm-agents/SaaS/release-notes.html
- DX Operational Observability SaaS Release Notes: https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/dx-operational-observability/saas/release-notes.html

## Change history:
