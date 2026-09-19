# Business Service Insight

## Status 

Draft

## Broadcom Software Type

Enterprise Software

## Broadcom Product Category

IT Service Management (ITSM)

## Broadcom Product Name

Business Service Insight

## Broadcom Product Description (Key Features) (This is important to get right)

Business Service Insight (BSI, formerly CA Business Service Insight and Oblicore Guarantee) is a service level management tool that models service agreements, monitors operational level agreements against business SLAs and reports on service performance and penalty exposure. Version 9.0.0.0 is the current release documented in Broadcom TechDocs (previous line 8.3.5).

Key features:

1. **SLA and OLA modelling** - Captures contract terms, service definitions and commitments in a central model.
2. **Service level monitoring** - Measures actual service performance against agreed targets using data from multiple sources.
3. **Service Level Insight reporting** - Reports on compliance, trends and penalty exposure for service owners and business stakeholders.
4. **Integration** - Integrates with ITSM and monitoring tools; version 9.0.0.0 documentation covers integrations, administration and design guidance.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

Analyst cautions and commercial pressures: no Gartner Peer Insights, Forrester or IDC coverage specific to Business Service Insight was identified in this research, and none appears to currently exist; this should be stated plainly rather than treated as either a positive or negative signal. Broadcom technical documentation confirms the product remains on a legacy, non-SaaS architecture; the specific claim that reporting depends on Jaspersoft components could not be independently confirmed from current Broadcom documentation in this research and should be verified directly with Broadcom before being relied upon in the deliverable. Reduced investment in smaller, legacy CA-derived modules such as this one is consistent with Broadcom's disclosed pattern of reallocating research and development spend away from products outside its core-account portfolio, as reported by The Register in 2022.

Broadcom exit strategies and market alternatives: IBM Instana, Dynatrace and Datadog are genuine, actively developed observability platforms with SLO and error-budget tracking, representing a realistic architectural shift from static, periodic SLA reporting to continuous observability. ServiceNow SLM is a real, if less commonly deployed, standalone alternative. Moving from a dedicated SLM/OLA compliance tool to an observability platform represents a change in tooling category rather than a strict feature-for-feature replacement, and the client's specific contractual SLA/OLA reporting requirements should be validated against whichever platform is selected before decommissioning BSI.
Sources: Broadcom TechDocs, CA Business Service Insight 9.0.0 release documentation, confirming the product remains under active version maintenance (techdocs.broadcom.com/us/en/ca-enterprise-software/business-management/clarity-business-service-insight/9-0-0.html); The Register, 2022 Broadcom account-strategy analysis; no independent analyst report identified for Business Service Insight as at September 2026.

## IBM Replacement Strength

(not provided)

## IBM Replacement Strategy - Why IBM over Broadcom

(not provided)

## PRIMARY - Key Product - IBM Alternative

IBM Instana Observability

## PRIMARY - Key Product Capability Statement - IBM Alternative

General sentiment: Positive – rated about 4.3 stars from roughly 265 Gartner Peer Insights reviews for easy dashboards and automatic discovery, with no consistent criticism surfaced in this pass.

IBM Instana Observability delivers automated, real-time Service Level Management and SLO/SLA tracking across hybrid and cloud-native applications. It eliminates outdated static batch reporting with 1-second metric granularity, automated SmartAlerts, synthetic monitoring, and end-to-end transaction tracing to proactively protect business service agreements and contract SLAs.

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

- CA Business Service Insight 9.0.0.0 - Broadcom TechDocs: https://techdocs.broadcom.com/us/en/ca-enterprise-software/business-management/clarity-business-service-insight/9-0-0.html
- CA Business Service Insight 9.0.0 Services - Broadcom TechDocs: https://techdocs.broadcom.com/us/en/ca-enterprise-software/business-management/clarity-business-service-insight/9-0-0/ca-business-service-insight-services.html

## Change history:

### 2026-09-19 - Broadcom product information verification (WebFetch pass, files 02-39)
- Verified: BSI 9.0.0 documentation is published. The Jaspersoft reporting dependency noted in Analyst Cautions still could not be confirmed and remains flagged as unverified. No changes.

### 2026-09-19 - Broadcom product information review
- Product description: Confirmed version 9.0.0.0 as current and removed the low-profile remark. Feature detail carried forward from the earlier description.
- Summary and numbered list of four key features rewritten from current Broadcom sources.
- General Sources: 2 sources recorded (Broadcom TechDocs, product pages, press releases where available).

### 2026-09-19 - IBM alternative product verification and sentiment (WebFetch and WebSearch pass, files 02-39)
- Requirement match against the Key Features section: Partially meets – technical SLOs only.
- Confirmed (IBM documentation via search): Instana creates and manages service level objectives, Smart Alerts on SLO status, error budget and burn rate, and SLOs based on synthetic monitoring.
- Gap: no contractual SLA or OLA modelling and no penalty exposure reporting were found. Instana SLOs are technical reliability objectives, so the contract-centric functions of Business Service Insight are not replaced. The 1-second granularity claim was not re-verified.
- Sentiment: added a one-sentence summary of general market sentiment at the start of the Key Product Capability Statement. Existing statement text was not changed.
- Sources: https://www.ibm.com/docs/en/iofgs?topic=instana-service-level-objectives-slos; https://www.ibm.com/docs/en/iofgs?topic=slos-smart-alerts-service-level-objectives; https://www.ibm.com/products/instana/synthetic-monitoring
