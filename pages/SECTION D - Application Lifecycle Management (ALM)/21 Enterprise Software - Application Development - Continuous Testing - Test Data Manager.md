# Test Data Manager

## Category

Application Lifecycle Management (ALM)

## Page Status 

Complete

## Broadcom Software Type

Enterprise Software

## Broadcom Product Category

Application Development - Continuous Testing

## Broadcom Product Name

Test Data Manager

## Broadcom Product Description - Key Features

Test Data Manager (formerly CA Test Data Manager) creates, masks and provisions fit-for-purpose test data across the development lifecycle. By decoupling test data from production dependencies, it allows dev and QA teams to achieve complete test coverage without introducing privacy or compliance risks.

Version 5.0 is the latest documented in TechDocs (version list 5.0, 4.11, 4.10, 4.9). Its documented components include a Database Virtualization Engine (DAVE), the Javelin automation tool and mainframe data source support. Virtual Test Data Management (vTDM) has been deprecated since version 4.11.

Key features:

1. **Data masking and PII discovery** - Discovers and masks personally identifiable information to protect test environments.
2. **Synthetic data generation** - Generates realistic synthetic data that covers test scenarios without exposing production data. Automatically creates production-ready synthetic data that mimics real statistical distributions, data types, and value ranges. It goes beyond typical production data to automatically generate outlier scenarios, boundary conditions, and negative paths.
3. **Data subsetting** - Creates smaller, referentially intact data sets from production sources.
4. **Self-service provisioning** - A portal lets testers request, reserve and provision data on demand without database scripting.

## Analyst Cautions and Industry Findings

Broadcom Test Data Manager is liked by the people who run it. Reviewers rate the self-service portal, data masking and subsetting well, and in 2022 Broadcom recorded a Customers' Choice recognition for data masking on Gartner Peer Insights. 

However, Broadcom offers limited suppport. Delivery of data from large platforms such as Teradata is slow, and native integration with AWS, Azure and Jira is thin. A competitor, K2view, goes further and describes the product as "a legacy tool that pairs older Windows clients with a newer portal, leaving overlap between modules and upgrade risk".

The commercial background is the usual one. Test Data Manager belongs to the continuous testing bundle inherited from CA Technologies, and Broadcom's move from perpetual to consolidated subscription licensing has reduced the freedom to buy single modules outside a bundled agreement.

While limited organisations are documenated as publicly declaring they are leaving Test Data Manager, teams are consolidating test data provisioning into broader shift-left platforms. Broadcom itself announced a unified continuous testing platform in 2025, which represents the need for continued migration.

## IBM PRIMARY BRAND 

Automation

## IBM PRIMARY - Product Name (The Replacement)

IBM Optim

## IBM PRIMARY - IBM Product Page URL

https://www.ibm.com/products/optim

## IBM Replacement Strength

Strong Replacement

## IBM Replacement Strategy (Short)

IBM Optim delivers trusted data for testing, AI and DevOps. Masking, PII discovery, subsetting, synthetic data and CI/CD self-service, escaping Broadcom's bundled renewals.

## IBM Replacement Strategy (Why IBM over Broadcom)

IBM Optim offers test data management and data masking, as a robust, enterprise-grade test data management platform that replaces Broadcom CA Test Data Manager. 

Broadcom TDM is locked into legacy CA continuous testing bundles, with deprecated virtual test data management (vTDM) and steep renewal pricing. IBM Optim provides high-performance test data management, data masking, and referentially intact data subsetting across heterogeneous databases and mainframe data stores, with self-service provisioning integrated directly into CI/CD pipelines at lower total cost of ownership.

## IBM PRIMARY - Product Description

IBM Optim provides trusted data for testing, AI and DevOps. Allows organisations to provision trusted data across the enterprise, while preserving context and data integrity to enable compliant and scalable test data management across hybrid environments for development of applications and AI systems.

It provides a central control framework for structured data governance across the enterprise, connecting to multiple relational database management systems and enterprise applications to execute data extraction, masking, and archiving operations based on defined policy parameters.

It automates the provisioning of targeted, referentially intact and secure data across environments, leveraging API‑based execution, containerized cloud deployments, and advanced data de‑identification to accelerate release cycles, ensure data privacy, and reduce costs. Reusable workflow templates that can be shared across environments to standardize and accelerate data operations. Combined with business-aware virtual relationships and broader connectivity across modern and legacy data sources, 

The robust access and managment of test data seems triavl, but in fact it is the cause of many project delays. Many AI projects get delayed because they dont thave safe copies of production data. Meaning that teams quietly use unapproved production data causing potential for security breaches.

- **Data masking** — Create compliant training data for test cases, without manual redaction and data masking. Policy based, advanced data masking and de-identification. For both static masking (data at rest) and dynamic masking (data in motion), a policy-based data masking engine that supports text data. Protect sensitive information by replacing original values with masked values while preserving format, referential integrity, and compliance with data privacy rules. Provides advanced, cryptographically safe masking methods, including format-preserving encryption (FPE) and format-preserving tokenization (FPT), and allows users to define custom masking policies and formats. One interesting feature is 'SQL User Defined Functions (UDFs)', enforcing masking onto sensitive fields before data leaves the database engine.

- **Synthetic data generation** — With IBM Optim, generate masked test data based on production information. When masked production data is not available or desirable, use IBM DevOps Loop (Test stage) to create structured, configurable, reusable synthetic datasets for test/simulation scenarios and edge-case test payloads. Generates data using schema- and rules-driven fabrication engine, not a generative AI / LLM engine. So the prerequisite are less than needing an LLM in the environment. Continue with centralised, enterprise managed service for test data.

- **PII discovery** - This is provided through Guardium Discover and Classify as an enterprise-grade service. PII and senstive, classified data is everywhere, and almost no IT Ops team wil know where it all exists. Cloud sprawl, DevOps spinning up environments, and copies of sensitive data have proliferating daily mean most organisations have a proliferation of shadow 'dark data'; sensitive data whose location and type are simply unknown. Guardium Discover and Classify is a purpose-built engine for finding and cataloging sensitive data across the enterprise.
(1) It passively monitors network traffic to detect and list data repositories — including previously unknown ones. (2) It Scans repositories at rest to discover and classify sensitive data, then tracks how it flows across the network. (3) It Maintains a continuously updated catalog rather than a point-in-time snapshot, with high accuracy to cut the false positives that sank first-generation tools. Use IBM Guardium Discover and Classify to disover PII within the enterprise, or across sources of data used for testing purposes. 

- **Data subsetting** — Extracts referentially intact, right-sized data subsets across complex relational databases, legacy systems, and mainframe environments, drastically reducing non-production storage requirements.

- **Self-service provisioning** — An intuitive web interfaces and RESTful APIs that allow developers and QA engineers to request, clone, reset, and provision sanitized test environments on demand directly within automated CI/CD workflows. Optim is API-first and designed to plug into CI/CD and AI/ML pipelines, so its capability can be exposed to the entire organiation and future AI projects via an MCP service. This lets enterprise agents request governed, masked, production-like data on demand rather than a human filing a ticket. The privacy and compliance controls stay enforced in Optim; the MCP layer brokers the request under least-privilege and approval gates. 

## Customer Reference

(not provided)

## IBM SECONDARY - Product Name (Extended Capability)

IBM Devops Loop

## IBM SECONDARY - Product Page(s) URL

https://www.ibm.com/products/devops-loop
https://www.ibm.com/products/engineering-lifecycle-management

## IBM SECONDARY - Product Description

Compliement Optim Test Data Management with DevOps Loop to drive what and when to test across enterprise delivery pipelines. Its Test stage runs automated API, UI, performance and integration tests against that provisioned data, auto-generating and self-healing test cases and gating risky components before release.

When masked production data is not available or desirable, use IBM DevOps Loop (Test stage) create structured, configurable, reusable synthetic datasets for test/simulation scenarios and edge-case test payloads.

Addtional expansion would be to integrate with the DevOps Test automation suite to improve how software and AI systems move from idea to production with automation, governance and audit built into every step. Consolidates software and AI delivery tooling into a single platform.

With Test integrated, test results become direct inputs to the DevOp pipeline gates and compliance checkpoints. This links requirements, code changes, test evidence and release approvals in one traceable chain, supporting release decisions based on recorded quality data rather than manual attestation.

Where engineering governance and test governance is needed in the wider organisation, then adopt IBM Engineering Test Management (ETM), the test-management component of the Engineering Lifecycle Management (ELM) suite. A collaborative, web-based platform for planning, constructing, managing and executing tests with full traceability to requirements and defects. It will primarily ensure that test artefacts are managed and linked to requirements at the project level to deliver the traceable digital thread - test cases that link back to requirements (in systems such as DOORS/DOORS Next) and defects that flow into workflow management - and the verification chain to proove every requirement was tested.

# Sources:

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