# Test Data Manager

## Status 

Draft

## Broadcom Software Type

Enterprise Software

## Broadcom Product Category

Application Development - Continuous Testing

## Broadcom Product Name

Test Data Manager

## Broadcom Product Description (Key Features) (This is important to get right)

Test Data Manager (formerly CA Test Data Manager) creates, masks and provisions fit-for-purpose test data across the development lifecycle. Version 5.0 is the latest documented in TechDocs (version list 5.0, 4.11, 4.10, 4.9). Its documented components include a Database Virtualization Engine (DAVE), the Javelin automation tool and mainframe data source support. Virtual Test Data Management (vTDM) has been deprecated since version 4.11.

Key features:

1. **Data masking and PII discovery** - Discovers and masks personally identifiable information to protect test environments.
2. **Synthetic data generation** - Generates realistic synthetic data that covers test scenarios without exposing production data.
3. **Data subsetting** - Creates smaller, referentially intact data sets from production sources.
4. **Self-service provisioning** - A portal lets testers request, reserve and provision data on demand without database scripting.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

Analyst commentary: Broadcom was recognised as a 2022 Gartner Peer Insights Customers' Choice for Data Masking, the category Test Data Manager sits within, but no 2025-2026 Gartner, Forrester, or IDC ranking specific to this product was located in this review; none should be assumed. Independent PeerSpot user reviews rate the self-service portal, masking, and subsetting functions positively but flag slow data delivery against large platforms such as Teradata and gaps in native cloud (AWS/Azure) and DevOps toolchain (Jira) integration.

Broadcom/CA commercial pressures: Test Data Manager sits in the same CA-Technologies-era Continuous Testing bundle subject to Broadcom's shift from perpetual to consolidated subscription licensing and reduced flexibility to purchase individual modules outside bundled agreements.

Exit strategy findings (2025-2026): Engineering teams are consolidating test-data provisioning into broader shift-left platforms, including Broadcom's own newly announced unified continuous testing platform (2025), IBM's DevOps Test/Engineering Lifecycle Management line, and specialist data vendors such as Delphix and K2view. Cross-check: the alternative currently listed in column H (IBM DevOps Deploy) is a release-automation product, not a test-data-management product, and does not map to this row's function; this mismatch is noted for the reviewer but is not corrected here as it falls outside this review's scope.

Sources: PeerSpot, 'Broadcom Test Data Manager: Pros and Cons' (peerspot.com); Broadcom Academy blog, 'Broadcom Is a 2022 Customers' Choice for Data Masking on Gartner Peer Insights' (academy.broadcom.com); Broadcom TechDocs, Test Data Manager 4.10 (techdocs.broadcom.com).

## IBM Replacement Strength

(not provided)

## IBM Replacement Strategy - Why IBM over Broadcom

(not provided)

## PRIMARY - Key Product - IBM Alternative

IBM DevOps Deploy

## PRIMARY - Key Product Capability Statement - IBM Alternative

General sentiment: Mixed to positive – praised for deployment orchestration and IBM tool integration, but reviewers cite slow support resolution and burdensome agent management.

IBM DevOps Deploy (formerly UrbanCode Deploy) provides enterprise application release automation and continuous deployment orchestration. It delivers multi-tier deployment modeling, automated quality gates, push-button rollbacks, full inventory governance, and native integration with Jenkins, GitOps (Argo CD), and Red Hat OpenShift across hybrid cloud and mainframe estates.

## PRIMARY - IBM Product Page URL

https://www.ibm.com/products/devops-deploy

## Customer Reference
(not provided)
## SECONDARY - Product Name - Supporting Product From any vendor - ONLY Where needed to for FULL Capability match for Broadcom. Extend the IBM Key Product.

IBM DevOps Test

## SECONDARY - Product Description - From any vendor - A Secondary Support Product.

IBM DevOps Test provides a comprehensive continuous testing suite covering automated API testing, functional UI testing, enterprise performance load testing, and service virtualization. It integrates directly into CI/CD pipelines, enabling shift-left quality gates, AI-driven test script maintenance, and realistic protocol/workload simulation without expensive proprietary per-virtual-user fees.

## SECONDARY - Product Page(s) URL

https://www.ibm.com/products/devops-test/performance

## Sources: Analyst reviews and exist strategy

Column D expanded from a one-line fragment into a full, sourced capability summary. Column E replaces generic claims with a verified 2022 Gartner Peer Insights recognition, sourced PeerSpot customer feedback, an honest statement that no 2025-2026 analyst ranking was found, and a flag that column H's listed alternative does not match this row's product category.

## General Sources:

- CA Test Data Manager 5.0 - Broadcom TechDocs: https://techdocs.broadcom.com/us/en/ca-enterprise-software/devops/test-data-management/5-0.html
- Release Notes - Test Data Manager 4.11: https://techdocs.broadcom.com/us/en/ca-enterprise-software/devops/test-data-management/4-11/release-notes.html
- Test Data Manager (product page): https://www.broadcom.com/products/software/app-dev/test-data-manager
- Broadcom Delivers World's First AI Driven Unified Shift-Left Continuous Testing Platform: https://investors.broadcom.com/news-releases/news-release-details/broadcom-delivers-worlds-first-ai-driven-unified-shift-left

## Change history:

### 2026-09-19 - Broadcom product information verification (WebFetch pass, files 02-39)
- Product description: confirmed vTDM deprecation (quoted from the 4.11 release notes) and version 5.0. Added DAVE, Javelin and mainframe data sources from the 5.0 documentation; Javelin had been removed in the previous pass as unverified and is now confirmed.
- Analyst Cautions: the source line cites Test Data Manager 4.10 documentation, which is no longer the latest (5.0); the citation is unchanged. Broadcom's 2025 unified continuous testing platform announcement (BlazeMeter Continuous Testing Platform) is confirmed.

### 2026-09-19 - Broadcom product information review
- Product description: Corrected the earlier description: Virtual Test Data Management (vTDM) is deprecated from 4.11 and is no longer listed as a key feature. Updated to version 5.0. The Javelin migration engine statement was removed because it was not re-verified.
- Summary and numbered list of four key features rewritten from current Broadcom sources.
- General Sources: 3 sources recorded (Broadcom TechDocs, product pages, press releases where available).

### 2026-09-19 - IBM alternative product verification and sentiment (WebFetch and WebSearch pass, files 02-39)
- Requirement match against the Key Features section: Does not meet.
- Gap (IBM product page): IBM DevOps Deploy is an application release and deployment automation product (deployment automation, quality gates, inventory control, workflow customisation). It offers no data masking, PII discovery, synthetic data generation, subsetting or self-service test data provisioning.
- An IBM test data management product would be needed to meet the functional requirements; none was researched in this pass.
- Sentiment: added a one-sentence summary of general market sentiment at the start of the Key Product Capability Statement. Existing statement text was not changed.
- Sources: https://www.ibm.com/products/devops-deploy; https://www.trustradius.com/products/ibm-urbancode-deploy/reviews?qs=pros-and-cons
