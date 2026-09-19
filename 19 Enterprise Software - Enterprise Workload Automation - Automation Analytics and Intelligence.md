# Automation Analytics and Intelligence

## Status 

Draft

## Broadcom Software Type

Enterprise Software

## Broadcom Product Category

Enterprise Workload Automation

## Broadcom Product Name

Automation Analytics and Intelligence

## Broadcom Product Description (Key Features) (This is important to get right)

Automation Analytics and Intelligence (AAI) is Broadcom's analytics and observability layer for workload automation. AAI v26 reached general availability on 14 September 2026, adding financial intelligence, a conversational AI interface and an AI-led security scan-and-remediate process.

Key features:

1. **Financial intelligence** - Calculates total cost of ownership of automation by mapping job executions to internal cost centres.
2. **Conversational AI** - Natural-language queries over workload data provide fast operational insight.
3. **Predictive SLA and trend analytics** - Flags likely SLA breaches, with an 18-month SLA trend view and improved dependency tracking.
4. **Modern deployment and security** - Official OpenShift container images, secure Airflow proxy support and an AI-led security scan-and-remediate process.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

The original Column D for this row consisted largely of unedited marketing copy, including claims about aligning "compute, storage, network and GPU resources with live demand," Kubernetes pod scaling and VMware VM placement. Based on Broadcom's own product documentation, AAI's actual function is analytics and SLA prediction for job and workload scheduling across multiple automation engines, not infrastructure resource right-sizing or placement; that latter function is a distinct capability more closely associated with application resource management and FinOps tools such as IBM Turbonomic (branded IBM Concert Optimize). This distinction matters for this review: the alternative already proposed in column H, IBM Concert Optimize (Turbonomic), is a resource-optimisation and FinOps platform, not a direct functional equivalent of AAI's workload-scheduling analytics. It may be a reasonable adjacent recommendation if the organisation is separately seeking infrastructure right-sizing, but it should not be presented as a like-for-like replacement for AAI. IBM's own workload automation analytics, or an SLA/analytics layer such as those offered by ServiceNow ITOM, Stonebranch or Redwood, should be evaluated as more direct functional alternatives.

No independent analyst coverage (Gartner, Forrester, IDC) specific to AAI as a standalone product was found in this review; this is stated plainly rather than assumed to exist. Broadcom's own marketing materials cite customer-reported outcomes of a 68 per cent reduction in missed SLAs, 70 per cent less monitoring time, and 200 per cent return on investment within three months; these are vendor-supplied figures, not independently verified, and should not be repeated to the client as confirmed benchmarks.

Commercial pressure: AAI is licensed as an add-on analytics layer bundled with Broadcom's wider workload automation portfolio, consistent with the bundled-commit pattern documented for Automic Automation and AutoSys elsewhere in this schedule.

Sources: Broadcom (automation.broadcom.com), "AAI: Advanced Analytics for Workload Automation" blog post, used to establish AAI's actual functional scope and the vendor-supplied performance figures. No independent analyst report specific to AAI was located.

## IBM Replacement Strength

Yes

## IBM Replacement Strategy - Why IBM over Broadcom

Migrate.

## PRIMARY - Key Product - IBM Alternative

IBM Concert Optimize (Turbonomic)

## PRIMARY - Key Product Capability Statement - IBM Alternative

General sentiment: Positive – rated about 4.5 stars from 77 Gartner Peer Insights reviews for removing capacity-planning guesswork and reducing over-provisioned cloud cost.

Application Resource Management and FinOps platform that uses advanced analytics and automation to optimize performance, reduce costs of ICT across hybrid, and multicloud environments. By dynamically aligning application demand with infrastructure resources, rovides continuous, real-time resource allocation, to impove ROI while ensuring optimal application performance and business-level SLA.

## PRIMARY - IBM Product Page URL

(not provided)

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

- Broadcom Unveils AAI v26 - Broadcom Automation blog: https://automation.broadcom.com/blog/broadcom-unveils-aai-v26-media-alert
- Broadcom Unveils AAI v26 - SD Times: https://sdtimes.com/data-analytics/broadcom-unveils-aai-v26-bringing-financial-accountability-and-ai-driven-insights-to-workload-automation/
- Announcing AAI v26: https://automation.broadcom.com/blog/announcing-aai-v26-transforming-automation-into-a-strategic-business-asset
- Broadcom Advances AAI with 24.4: https://automation.broadcom.com/blog/broadcom-advances-automation-analytics-intelligence-with-aai-24-4-impact-brief

## Change history:

### 2026-09-19 - Broadcom product information verification (WebFetch pass, files 02-39)
- Verified: AAI v26 general availability on 14 September 2026. The v26 announcement contains no customer outcome figures, so the vendor-supplied figures in Analyst Cautions (68 per cent fewer missed SLAs and similar) come from an older source and were not re-confirmed; the text already labels them as unverified vendor figures. No changes.

### 2026-09-19 - Broadcom product information review
- Product description: Updated to AAI v26 (GA 14 September 2026). The multi-vendor scheduler statement (IBM and BMC) was not re-verified in this review and was removed.
- Summary and numbered list of four key features rewritten from current Broadcom sources.
- General Sources: 4 sources recorded (Broadcom TechDocs, product pages, press releases where available).

### 2026-09-19 - IBM alternative product verification and sentiment (WebFetch and WebSearch pass, files 02-39)
- Requirement match against the Key Features section: Weak functional match.
- Confirmed (IBM product page): automated, application-aware resource optimisation, cost optimisation, SLO alignment and Kubernetes and OpenShift support. Gartner lists Turbonomic as part of the Concert platform; the 'Concert Optimize' name was not confirmed on the page fetched.
- Gap: Automation Analytics and Intelligence analyses the cost, SLA and dependencies of workload automation jobs, whereas Turbonomic optimises infrastructure resources. Cost mapping of job executions to cost centres, predictive SLA breach flags and conversational AI were not found. IBM Workload Automation analytics (file 17) should be assessed alongside.
- Sentiment: added a one-sentence summary of general market sentiment at the start of the Key Product Capability Statement. Existing statement text was not changed.
- Sources: https://www.ibm.com/products/turbonomic; https://www.gartner.com/reviews/product/ibm-turbonomic-platform
