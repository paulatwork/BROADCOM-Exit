# Test Data Manager

## Status 

Draft

## Broadcom Software Type

Enterprise Software

## Broadcom Product Category

Application Development - Continuous Testing

## Broadcom Product Name

Test Data Manager

## Broadcom Product Description - Key Features

Test Data Manager (formerly CA Test Data Manager) creates, masks and provisions fit-for-purpose test data across the development lifecycle. Version 5.0 is the latest documented in TechDocs (version list 5.0, 4.11, 4.10, 4.9). Its documented components include a Database Virtualization Engine (DAVE), the Javelin automation tool and mainframe data source support. Virtual Test Data Management (vTDM) has been deprecated since version 4.11.

Key features:

1. **Data masking and PII discovery** - Discovers and masks personally identifiable information to protect test environments.
2. **Synthetic data generation** - Generates realistic synthetic data that covers test scenarios without exposing production data.
3. **Data subsetting** - Creates smaller, referentially intact data sets from production sources.
4. **Self-service provisioning** - A portal lets testers request, reserve and provision data on demand without database scripting.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

Test Data Manager earns real praise from the people who run it. Reviewers rate the self-service portal, data masking and subsetting well, and in 2022 Broadcom recorded a Customers' Choice recognition for data masking on Gartner Peer Insights. The complaints are about reach. Delivery of data from large platforms such as Teradata is slow, and native integration with AWS, Azure and Jira is thin. A competitor, K2view, goes further and describes the product as a legacy tool that pairs older Windows clients with a newer portal, leaving overlap between modules and upgrade risk. That is vendor content and should be weighed as such.

The commercial background is the usual one. Test Data Manager belongs to the continuous testing bundle inherited from CA Technologies, and Broadcom's move from perpetual to consolidated subscription licensing has reduced the freedom to buy single modules outside a bundled agreement.

No named organisation has publicly described leaving Test Data Manager, and no 2025 or 2026 analyst ranking was found. Teams that are consolidating test data provisioning are heading for broader shift-left platforms. Broadcom itself announced a unified continuous testing platform in 2025, which is a reminder that staying is also a moving target. Outside Broadcom, the options are IBM's DevOps Test and Engineering Lifecycle Management line and specialist data vendors such as Delphix and K2view.

## IBM Replacement Strength

Strong Replacement, with improved outcomes

## IBM Replacement Strategy - Why IBM over Broadcom

IBM InfoSphere Optim Test Data Management alongside IBM watsonx.data delivers a robust, enterprise-grade test data management platform that replaces Broadcom CA Test Data Manager. Broadcom TDM is locked into legacy CA continuous testing bundles, with deprecated virtual test data management (vTDM) and steep renewal pricing. IBM InfoSphere Optim provides high-performance data masking, automated PII discovery, referentially intact data subsetting, and synthetic test data generation across heterogeneous databases and mainframes, with self-service provisioning integrated directly into CI/CD pipelines at lower total cost of ownership.

## IBM PRIMARY - Product Name (The Replacement)

IBM InfoSphere Optim Test Data Management

## IBM PRIMARY - Product Description

IBM InfoSphere Optim Test Data Management is IBM's enterprise test data management, masking, and privacy solution. It discovers sensitive data, creates realistic de-identified and synthetic data sets, extracts referentially intact database subsets, and automates test data provisioning across hybrid cloud, distributed database, and mainframe environments.

- **Data masking and PII discovery** — IBM InfoSphere Optim automatically scans distributed databases and mainframes to discover sensitive PII, applying contextual, format-preserving masking algorithms to secure non-production environments while complying with global data privacy regulations (GDPR, HIPAA, CCPA).
- **Synthetic data generation** — IBM InfoSphere Optim (paired with watsonx.data synthetic generation capabilities) generates realistic synthetic test records and edge-case test payloads to fulfill boundary testing requirements without exposing real production records.
- **Data subsetting** — IBM InfoSphere Optim extracts referentially intact, right-sized data subsets across complex relational databases, legacy systems, and mainframe environments, drastically reducing non-production storage requirements.
- **Self-service provisioning** — IBM InfoSphere Optim provides intuitive web interfaces and RESTful APIs that allow developers and QA engineers to request, clone, reset, and provision sanitized test environments on demand directly within automated CI/CD workflows.

## IBM PRIMARY - IBM Product Page URL

https://www.ibm.com/products/infosphere-optim-test-data-management

## Customer Reference

(not provided)

## IBM SECONDARY - Product Name (Supporting Product, where recommended to compliment the Primary capability)

IBM DevOps Test

## IBM SECONDARY - Product Description

IBM DevOps Test provides a comprehensive continuous testing suite covering automated API testing, functional UI testing, enterprise performance load testing, and service virtualization. It integrates directly into CI/CD pipelines, enabling shift-left quality gates, AI-driven test script maintenance, and realistic protocol/workload simulation without expensive proprietary per-virtual-user fees.

IBM DevOps Deploy is a release-automation product, not a test-data-management product. It offers complimentary services. IBM DevOps Deploy (formerly UrbanCode Deploy) provides enterprise application release automation and continuous deployment orchestration. It delivers multi-tier deployment modeling, automated quality gates, push-button rollbacks, full inventory governance, and native integration with Jenkins, GitOps (Argo CD), and Red Hat OpenShift across hybrid cloud and mainframe estates.


## IBM SECONDARY - Product Page(s) URL

https://www.ibm.com/products/devops-test/performance

# Sources:

## IBM InfoSphere Optim Test Data Management

- IBM InfoSphere Optim Test Data Management Product Overview: https://www.ibm.com/products/infosphere-optim-test-data-management
- IBM Documentation — InfoSphere Optim Test Data Management: https://www.ibm.com/docs/en/infosphere-optim
- Gartner Peer Insights — IBM InfoSphere Optim Reviews: https://www.gartner.com/reviews/market/data-masking/vendor/ibm/product/ibm-infosphere-optim

## Sources: Analyst reviews and exist strategy

- PeerSpot, 'Broadcom Test Data Manager: Pros and Cons' (peerspot.com)
- Broadcom Academy blog, 'Broadcom Is a 2022 Customers' Choice for Data Masking on Gartner Peer Insights' (academy.broadcom.com)
- Broadcom TechDocs, Test Data Manager 4.10 (techdocs.broadcom.com)
- K2view, 'Broadcom TDM vs K2view: How TDM architecture impacts your delivery speed' (https://www.k2view.com/blog/broadcom-tdm-vs-k2view) [vendor-authored competitive content]

## General Sources:

- CA Test Data Manager 5.0 - Broadcom TechDocs: https://techdocs.broadcom.com/us/en/ca-enterprise-software/devops/test-data-management/5-0.html
- Release Notes - Test Data Manager 4.11: https://techdocs.broadcom.com/us/en/ca-enterprise-software/devops/test-data-management/4-11/release-notes.html
- Test Data Manager (product page): https://www.broadcom.com/products/software/app-dev/test-data-manager
- Broadcom Delivers World's First AI Driven Unified Shift-Left Continuous Testing Platform: https://investors.broadcom.com/news-releases/news-release-details/broadcom-delivers-worlds-first-ai-driven-unified-shift-left

## Change history:

### 2026-09-20 - Analyst Cautions and Industry Findings rewritten as a narrative
- Rewrote the section as a narrative.
- Searched for named organisations that replaced Test Data Manager with Delphix, K2view or Tonic (2026-09-20). None was found, and the text now says so.
- Added K2view's competitive description of the product, labelled as vendor content.
- Moved all citations to the Sources: Analyst reviews and exist strategy section and removed the earlier column notes from that section.


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
