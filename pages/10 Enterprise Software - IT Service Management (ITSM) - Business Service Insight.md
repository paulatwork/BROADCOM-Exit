# Business Service Insight

## Status 

Draft

## Broadcom Software Type

Enterprise Software

## Broadcom Product Category

IT Service Management (ITSM)

## Broadcom Product Name

Business Service Insight

## Broadcom Product Description - Key Features

Business Service Insight (BSI, formerly CA Business Service Insight and Oblicore Guarantee) is a service level management tool that models service agreements, monitors operational level agreements against business SLAs and reports on service performance and penalty exposure. Version 9.0.0.0 is the current release documented in Broadcom TechDocs (previous line 8.3.5).

Key features:

1. **SLA and OLA modelling** - Captures contract terms, service definitions and commitments in a central model.
2. **Service level monitoring** - Measures actual service performance against agreed targets using data from multiple sources.
3. **Service Level Insight reporting** - Reports on compliance, trends and penalty exposure for service owners and business stakeholders.
4. **Integration** - Integrates with ITSM and monitoring tools; version 9.0.0.0 documentation covers integrations, administration and design guidance.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

Business Service Insight is one of the quietest products in the portfolio. No Gartner Peer Insights, Forrester or IDC coverage specific to it was found, and none appears to exist. That should be stated plainly, not read as a good or bad sign. Broadcom's documentation confirms it is on a legacy, non-SaaS architecture, and a claim that its reporting depends on Jaspersoft components could not be confirmed from current documentation, so it should be checked with Broadcom before anyone relies on it.

The wider context is a company that has openly redirected research and development spending away from products outside its core accounts, as The Register reported in 2022. Small, legacy CA-derived modules like this one are the obvious candidates for reduced investment, though Broadcom still maintains version 9.0.0.

No named organisation has publicly described leaving Business Service Insight. Customers who do move are generally changing the way they work, not just the tool. IBM Instana, Dynatrace and Datadog are actively developed observability platforms with service level objective and error-budget tracking, which shifts SLA reporting from a periodic exercise to a continuous one. ServiceNow Service Level Management is a real if less commonly deployed standalone alternative. Because this is a change of tooling category, the client's contractual SLA and OLA reporting requirements should be tested against whichever platform is chosen before Business Service Insight is switched off.

## IBM PRIMARY - Product Name (The Replacement)

IBM Instana Observability

## IBM PRIMARY - IBM Product Page URL

https://www.ibm.com/products/instana

## IBM Replacement Strength

Partial Match

## IBM Replacement Strategy (Short)

Instana replaces periodic SLA reporting with continuous real-time SLO monitoring, error budgets and proactive alerting.

## IBM Replacement Strategy (Description - Why IBM over Broadcom)

IBM Instana Observability shifts service level management from Broadcom BSI's static, batch-oriented, periodic SLA reporting to continuous, real-time Service Level Objective (SLO) monitoring and automated error-budget management. Broadcom BSI is a legacy on-premises product receiving minimal active innovation and subject to expensive bundling renewals. IBM Instana provides immediate time-to-value with automated discovery, 1-second metric resolution, and proactive SmartAlerts that prevent service degradation before contractual penalties occur.

## IBM PRIMARY - Product Description

IBM Instana Observability is IBM's real-time enterprise observability and automated Application Performance Monitoring (APM) solution. It monitors cloud-native, hybrid, and on-premises applications, translating raw performance and telemetry data into actionable Service Level Objectives (SLOs), error budgets, and health insights.

- **SLA and OLA modelling** — IBM Instana enables engineering and operations teams to model technical Service Level Objectives (SLOs) and Service Level Indicators (SLIs) based on latency, throughput, error rates, and synthetic uptime transactions across business services.
- **Service level monitoring** — IBM Instana provides real-time, continuous service level tracking with 1-second metric granularity and unsampled end-to-end distributed tracing, replacing static periodic batch evaluation.
- **Service Level Insight reporting** — IBM Instana generates real-time error-budget burn rate analytics, executive reliability dashboards, and automated breach notifications via SmartAlerts to visualize SLA risks and performance trends.
- **Integration** — IBM Instana natively integrates with modern ITSM, alerting, and incident management platforms (including IBM Maximo IT, ServiceNow, Slack, and PagerDuty) through bidirectional REST APIs and webhooks.

## Customer Reference

(not provided)
## IBM SECONDARY - Product Name (Supporting Product, where recommended to compliment the Primary capability)

(not provided)

## IBM SECONDARY - Product Description

(not provided)

## IBM SECONDARY - Product Page(s) URL

(not provided)

# Sources:

## IBM Instana Observability

- IBM Instana Observability Product Overview: https://www.ibm.com/products/instana
- IBM Instana Documentation — Service Level Objectives (SLOs) and SmartAlerts: https://www.ibm.com/docs/en/instana-observability?topic=instana-service-level-objectives-slos
- Gartner Peer Insights — IBM Instana Observability Reviews: https://www.gartner.com/reviews/market/observability-platforms/vendor/ibm/product/ibm-instana-observability

## Sources: Analyst reviews and exist strategy

- Broadcom TechDocs, CA Business Service Insight 9.0.0 release documentation, confirming the product remains under active version maintenance (techdocs.broadcom.com/us/en/ca-enterprise-software/business-management/clarity-business-service-insight/9-0-0.html)
- The Register, 'Broadcom's stated strategy ignores most VMware customers', 2022 (https://www.theregister.com/software/2022/05/30/broadcoms-strategy-ignores-most-vmware-customers/1194871)

## General Sources:

- CA Business Service Insight 9.0.0.0 - Broadcom TechDocs: https://techdocs.broadcom.com/us/en/ca-enterprise-software/business-management/clarity-business-service-insight/9-0-0.html
- CA Business Service Insight 9.0.0 Services - Broadcom TechDocs: https://techdocs.broadcom.com/us/en/ca-enterprise-software/business-management/clarity-business-service-insight/9-0-0/ca-business-service-insight-services.html

## Change history:
