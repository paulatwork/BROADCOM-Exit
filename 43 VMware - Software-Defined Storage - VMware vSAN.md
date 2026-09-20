# VMware vSAN

## Status 

Draft

## Broadcom Software Type

VMware

## Broadcom Product Category

Software-Defined Storage

## Broadcom Product Name

VMware vSAN

## Broadcom Product Description - Key Features

VMware vSAN is hyperconverged software-defined storage. In 9.x, Express Storage Architecture (ESA) is the focus; global deduplication is available in 9.1.

Key features:

1. **vSAN ESA** - NVMe-optimised architecture.
2. **Global deduplication** - Cluster-wide with encryption (9.1).
3. **Native snapshot replication** - 200-deep snapshots.
4. **Site Maintenance Mode** - One-click site maintenance.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

Standalone vSAN licensing was discontinued in 2023; capacity is now bundled per physical core (0.25 TiB per core under VVF, confirmed by Broadcom TechDocs), with additional capacity requiring supplementary licensing or a step-up to full VCF. Storage-dense clusters, common in environments running large databases or backup repositories, can incur materially higher licensing costs than under the previous per-CPU or per-terabyte models, a pattern documented across multiple VMware licensing analyses published during 2025 and 2026. Industry commentary on VMware exit strategies generally treats storage as more tractable to replatform than networking, since data can be migrated using standard storage migration tooling; however, replicating vSAN's tight integration with vSphere HA/DRS requires a genuinely hyperconverged replacement rather than a bolt-on array. Red Hat OpenShift Data Foundation, built on Ceph, and Nutanix AOS are realistic alternatives, though OpenShift Data Foundation is primarily oriented toward container-native and OpenShift Virtualization workloads rather than general-purpose VM storage, so a mixed VM and container estate may require complementary tooling such as IBM Storage Fusion for VM-centric use cases.

Sources: Broadcom TechDocs, 'VMware vSphere Foundation Capacity License for vSAN'; general VMware/Broadcom licensing analyses published by Network World and CIO Dive through 2025-2026 covering per-core vSAN capacity bundling.

## IBM Replacement Strength

Yes

## IBM Replacement Strategy - Why IBM over Broadcom

Red Hat + IBM

## IBM PRIMARY - Product Name (The Replacement)

OpenShift Data Foundation + IBM Fusion

## IBM PRIMARY - Product Description 

(not provided)

## IBM PRIMARY - IBM Product Page URL

https://www.redhat.com/en/resources/add-capabilities-enterprise-deployments-datasheet

## Customer Reference
(not provided)
## IBM SECONDARY - Product Name (Supporting Product, where recommended to compliment the Primary capability)

(not provided)

## IBM SECONDARY - Product Description

(not provided)

## IBM SECONDARY - Product Page(s) URL

https://www.redhat.com/en/resources/add-capabilities-enterprise-deployments-datasheet

# Sources:

## Sources: Analyst reviews and exist strategy

Added the verified 0.25 TiB/core capacity figure and a caution that OpenShift Data Foundation is container-oriented rather than a direct general-purpose VM storage equivalent, which affects the realism of the column G/H alternative for mixed estates.

## General Sources:

- What's new for vSAN in 9.1? - Yellow Bricks: https://www.yellow-bricks.com/2026/05/07/whats-new-for-vsan-in-9-1/
- vSAN What's New 9.1: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/vmware-cloud-foundation-9-1-0-0-release-notes/what-s-new/whats-new-vsan.html

## Change history:

### 2026-09-19 - Broadcom product information review
- Product description: Updated to 9.1 features. Yellow Bricks is an independent expert blog.
- Summary and numbered list of four key features rewritten from current Broadcom sources.
- General Sources: 2 sources recorded (Broadcom TechDocs, product pages, press releases where available).
