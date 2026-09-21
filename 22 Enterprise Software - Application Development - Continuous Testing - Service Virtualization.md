# Service Virtualization

## Status 

Draft

## Broadcom Software Type

Enterprise Software

## Broadcom Product Category

Application Development - Continuous Testing

## Broadcom Product Name

Service Virtualization

## Broadcom Product Description - Key Features

Service Virtualization (part of DevTest Solutions, formerly LISA) emulates unavailable or costly dependent systems for testing. DevTest 10.9 is now the current release line (with 10.9.1 documentation also published), following 10.8.3.

Key features:

1. **Virtual service creation** - Creates virtual services by recording live traffic or from specifications such as WSDL and OpenAPI, with scripted logic and data-driven responses.
2. **Automated VSE scaling (10.9)** - Virtual Service Environment instances scale dynamically with workload in Kubernetes and OpenShift, provisioning Pods automatically for performance testing.
3. **Messaging protocol support** - 10.8.3 extended virtual service creation to Apache Kafka, JMS and IBM MQ, including Kafka SASL OAUTHBEARER authentication.
4. **Virtual Service Catalog and platform support (10.9)** - A new Virtual Service Catalog UI and simpler properties, more than 45 security fixes, and support for RHEL 10, Windows Server 2025, Amazon Linux 2023 and current databases.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

Service Virtualization comes with the kind of complaints that are hard to argue with, because they come from paying customers. On PeerSpot one enterprise reviewer cited close to USD 1 million for a three-year multi-licence agreement. Reviewers also describe a performance-testing add-on that is priced separately when competing tools include it, extra charges for higher support tiers, a drop in specialist technical expertise since the acquisition, and stability problems such as memory leaks and portal restarts. A Gartner Peer Insights page exists, but no 2025 or 2026 Gartner, Forrester or IDC ranking for the product was found.

The background is the same continuous testing bundle, with consolidated subscription licensing, capacity-based tiers and less freedom to buy on its own. It is also worth knowing where the product came from. It began as ITKO's LISA, which CA bought in 2011 and Broadcom inherited in 2018, and market commentary notes that development has slowed in recent years.

No named organisation has publicly described leaving Service Virtualization. Engineering teams that do leave are replacing heavyweight, appliance-style virtualisation with lighter, developer-friendly, API-first tools wired into CI/CD pipelines. WireMock, Parasoft Virtualize, Tricentis and IBM's Rational Test Workbench lineage are the alternatives cited most often. Commentary treats Broadcom DevTest and Parasoft Virtualize as the incumbents for deep legacy protocol stacks run by a central team, whereas WireMock suits API-first teams.

## IBM PRIMARY - Product Name (The Replacement)

IBM DevOps Test Virtualization

## IBM PRIMARY - IBM Product Page URL

https://www.ibm.com/products/devops-test/virtualization

## IBM Replacement Strength

Strong Replacement, with improved outcomes

## IBM Replacement Strategy (Short)

DevOps Test Virtualization offers CI/CD-ready virtualisation with broad messaging support, avoiding Broadcom's costly tiered licensing.

## IBM Replacement Strategy (Description - Why IBM over Broadcom)

IBM DevOps Test Virtualization (formerly Rational Integration Tester / RTVS) delivers a lightweight, developer-friendly, and enterprise-grade service virtualization platform that replaces Broadcom Service Virtualization (CA LISA). Broadcom Service Virtualization is notoriously expensive (with enterprise contracts approaching $1M+), suffers from stability issues and memory leaks, and charges extra for performance testing tiers. IBM DevOps Test Virtualization supports extensive enterprise messaging protocols (Kafka, MQ, JMS, REST, gRPC), integrates seamlessly into containerized CI/CD pipelines on OpenShift, and eliminates prohibitive per-virtual-user and tier licensing costs.

## IBM PRIMARY - Product Description

IBM DevOps Test Virtualization is IBM's continuous testing and service virtualization solution. It enables software engineering teams to model, simulate, and emulate unavailable, constrained, or third-party dependent services, APIs, databases, and messaging systems throughout the software development lifecycle.

- **Virtual service creation** — IBM DevOps Test Virtualization creates high-fidelity virtual services by recording live network traffic, importing OpenAPI/Swagger, WSDL, and JSON schemas, and applying programmable data-driven request-response logic.
- **Automated VSE scaling (10.9)** — IBM DevOps Test Virtualization deploys lightweight, containerized virtual test stubs on Red Hat OpenShift and Kubernetes that scale dynamically to handle high-throughput performance and load testing demands.
- **Messaging protocol support** — IBM DevOps Test Virtualization provides native, out-of-the-box virtualization for enterprise messaging and event streams, including Apache Kafka (with SASL/OAuth authentication), IBM MQ, JMS, MQTT, and RabbitMQ.
- **Virtual Service Catalog and platform support (10.9)** — IBM DevOps Test Virtualization offers a centralized web-based asset catalog for managing, sharing, and orchestrating virtual services, with modern cross-platform support across RHEL, Windows Server, and container environments.

## Customer Reference

(not provided)
## IBM SECONDARY - Product Name (Supporting Product, where recommended to compliment the Primary capability)

(not provided)

## IBM SECONDARY - Product Description

(not provided)

## IBM SECONDARY - Product Page(s) URL

(not provided)

# Sources:

## IBM DevOps Test Virtualization

- IBM DevOps Test Virtualization Product Overview: https://www.ibm.com/products/devops-test/virtualization
- IBM Documentation — DevOps Test Virtualization: https://www.ibm.com/docs/en/devops-test
- Gartner Peer Insights — IBM DevOps Test Reviews: https://www.gartner.com/reviews/market/automated-software-testing/vendor/ibm/product/ibm-devops-test

## Sources: Analyst reviews and exist strategy

- PeerSpot, 'Broadcom Service Virtualization reviews' (peerspot.com)
- Broadcom TechDocs, DevTest Solutions 10.7/10.8 Service Virtualization documentation (techdocs.broadcom.com)
- WireMock, 'The 10 Best Service Virtualization Tools in 2026' (wiremock.io)
- Parasoft, 'Parasoft vs. Broadcom - Service Virtualization Solutions' (parasoft.com)
- Speedscale, '7 Best Service Virtualization Tools in 2026' (https://speedscale.com/blog/service-virtualization-tools/), for the LISA and ITKO lineage and the slowing of development

## General Sources:

- New Features and Enhancements - DevTest 10.8: https://techdocs.broadcom.com/us/en/ca-enterprise-software/devops/devtest-solutions/10-8/release-notes/new-features-and-enhancements.html
- Post 10.8 Updates - DevTest: https://techdocs.broadcom.com/us/en/ca-enterprise-software/devops/devtest-solutions/10-9/post108updates.html
- Using Service Virtualization - DevTest 10.8: https://techdocs.broadcom.com/us/en/ca-enterprise-software/devops/devtest-solutions/10-8/using/using-service-virtualization.html
- 10.9 New Features and Enhancements: https://techdocs.broadcom.com/us/en/ca-enterprise-software/devops/devtest-solutions/10-9/release-notes/new-features-and-enhancements-109.html

## Change history:
