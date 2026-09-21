# Automation Analytics and Intelligence

## Status 

Draft

## Broadcom Software Type

Enterprise Software

## Broadcom Product Category

Enterprise Workload Automation

## Broadcom Product Name

Automation Analytics and Intelligence

## Broadcom Product Description - Key Features

Automation Analytics and Intelligence (AAI) is Broadcom's analytics and observability layer for workload automation. AAI v26 reached general availability on 14 September 2026, adding financial intelligence, a conversational AI interface and an AI-led security scan-and-remediate process.

Key features:

1. **Financial intelligence** - Calculates total cost of ownership of automation by mapping job executions to internal cost centres.
2. **Conversational AI** - Natural-language queries over workload data provide fast operational insight.
3. **Predictive SLA and trend analytics** - Flags likely SLA breaches, with an 18-month SLA trend view and improved dependency tracking.
4. **Modern deployment and security** - Official OpenShift container images, secure Airflow proxy support and an AI-led security scan-and-remediate process.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

The earlier description of this product was mostly marketing copy, with claims about aligning 'compute, storage, network and GPU resources with live demand', Kubernetes pod scaling and VMware virtual machine placement. Broadcom's documentation says otherwise. Automation Analytics and Intelligence analyses and predicts service levels for job and workload scheduling across several automation engines. It does not right-size or place infrastructure.

That matters for the IBM suggestion. IBM Concert Optimize, which is Turbonomic, is a resource-optimisation and FinOps platform. It is a sensible adjacent recommendation if the organisation also wants infrastructure right-sizing, but it is not a like-for-like replacement for this product. More direct alternatives are IBM's own workload automation analytics, or the service-level analytics layers offered by ServiceNow ITOM, Stonebranch and Redwood.

No independent Gartner, Forrester or IDC coverage of the product was found, and no named organisation has publicly described leaving it. Broadcom's marketing cites customer outcomes of a 68 per cent reduction in missed SLAs, 70 per cent less monitoring time and a 200 per cent return on investment within three months. Those figures are supplied by the vendor and have not been verified, so they should not be repeated to the client as benchmarks.

Commercially, the product is an add-on analytics layer sold with Broadcom's wider workload automation portfolio, so it follows the bundled-commit pattern described for Automic Automation and AutoSys. A customer who leaves the schedulers will almost certainly leave this product as well.

## IBM PRIMARY - Product Name (The Replacement)

IBM Workload Automation (Analytics & Predictive SLA Management)

## IBM PRIMARY - IBM Product Page URL

https://www.ibm.com/products/workload-automation

## IBM Replacement Strength

Strong Replacement, with improved outcomes

## IBM Replacement Strategy (Short)

IBM Workload Automation includes native predictive SLA analytics and AI, avoiding Broadcom's costly add-on lock-in.

## IBM Replacement Strategy (Description - Why IBM over Broadcom)

IBM Workload Automation (Analytics & Workload AI) alongside IBM Concert delivers an intelligent, predictive workload observability and optimization platform that surpasses Broadcom AAI. Broadcom AAI v26 is sold as an expensive add-on to lock customers into Automic/AutoSys agreements. IBM Workload Automation natively integrates advanced predictive SLA modeling, automated historical trend forecasting, and AI-driven anomaly remediation directly into the core platform, while IBM Concert extends cross-system dependency mapping and financial accountability across enterprise workloads without forced add-on licensing.

## IBM PRIMARY - Product Description

IBM Workload Automation includes native advanced analytics, predictive SLA management, and AI-powered workload intelligence that continuously evaluates batch execution streams, forecasts SLA completion times, and pinpoints bottleneck dependencies across enterprise environments.

- **Financial intelligence** — IBM Workload Automation and IBM Apptio provide deep financial visibility and cost allocation, mapping workload runtimes and compute consumption back to business units and cost centers.
- **Conversational AI** — IBM Workload Automation integrates with IBM watsonx to provide natural-language workload querying, automated incident summarization, and interactive operational insights for schedulers and business analysts.
- **Predictive SLA and trend analytics** — IBM Workload Automation provides predictive critical-path calculation, automated early-warning alerts for SLA risks, and multi-month historical trend analysis to guarantee on-time processing.
- **Modern deployment and security** — IBM Workload Automation is fully containerized on Red Hat OpenShift, provides automated vulnerability scanning and remediation workflows, and integrates securely with open-source frameworks such as Apache Airflow.

## Customer Reference

(not provided)
## IBM SECONDARY - Product Name (Supporting Product, where recommended to compliment the Primary capability)

(not provided)

## IBM SECONDARY - Product Description

(not provided)

## IBM SECONDARY - Product Page(s) URL

(not provided)

# Sources:

## IBM Workload Automation (Analytics & Predictive SLA Management)

- IBM Workload Automation Analytics and Intelligence: https://www.ibm.com/products/workload-automation
- IBM Workload Automation Predictive SLA Management Guide: https://www.ibm.com/docs/en/workload-automation?topic=monitoring-managing-workload-slas
- Gartner Magic Quadrant for Service Orchestration and Automation Platforms: https://www.gartner.com/reviews/market/service-orchestration-and-automation-platforms/vendor/ibm/product/ibm-workload-automation

## Sources: Analyst reviews and exist strategy

- Broadcom, 'AAI: Advanced Analytics for Workload Automation' (automation.broadcom.com) [vendor-published, used for functional scope and the vendor-supplied figures]

## General Sources:

- Broadcom Unveils AAI v26 - Broadcom Automation blog: https://automation.broadcom.com/blog/broadcom-unveils-aai-v26-media-alert
- Broadcom Unveils AAI v26 - SD Times: https://sdtimes.com/data-analytics/broadcom-unveils-aai-v26-bringing-financial-accountability-and-ai-driven-insights-to-workload-automation/
- Announcing AAI v26: https://automation.broadcom.com/blog/announcing-aai-v26-transforming-automation-into-a-strategic-business-asset
- Broadcom Advances AAI with 24.4: https://automation.broadcom.com/blog/broadcom-advances-automation-analytics-intelligence-with-aai-24-4-impact-brief

## Change history:
