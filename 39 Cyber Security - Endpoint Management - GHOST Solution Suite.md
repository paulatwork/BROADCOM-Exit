# GHOST Solution Suite

## Status 

Draft

## Broadcom Software Type

Cyber Security

## Broadcom Product Category

Endpoint Management

## Broadcom Product Name

GHOST Solution Suite

## Broadcom Product Description - Key Features

Symantec Ghost Solution Suite handles imaging, deployment and migration of desktops, laptops and servers. Release 3.3.13 is the latest listed in TechDocs (page updated 9 June 2026). Its feature list could not be retrieved, so the features below are carried forward from Broadcom's product description.

Key features:

1. **Disk imaging** - Centralised imaging and cloning.
2. **OS deployment and migration** - Provisioning and migration across hardware.
3. **Remote command execution** - Run commands on managed machines.
4. **Recovery** - Restore devices from images.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

GHOST Solution Suite has no independent voice. No Gartner, Forrester or IDC coverage was found, and no dedicated Gartner Peer Insights page could be located, so nothing here should suggest analyst sentiment that has not been verified.

The product is not being wound down, whatever a lifecycle page might suggest. Broadcom publishes an end-of-life schedule for GHOST Solution Suite versions on its knowledge base, but the article lists no dates, and Broadcom is still releasing the product. Version 3.3.13 has documentation updated on 9 June 2026, with about one release a year.

The pressure on GHOST is a change in how endpoints are built, not a Broadcom decision. Thick-image, disk-cloning deployment is being retired across the industry in favour of cloud-native, zero-touch provisioning, because thick imaging suits neither remote and hybrid workforces nor modern hardware abstraction. That is a general trend in endpoint management, not a finding about Broadcom or about this product in particular.

No named organisation has publicly described leaving GHOST. Enterprises retiring it are adopting Windows Autopilot paired with Microsoft Intune, IBM MaaS360, Apple Business Manager for Apple estates, or Tanium Provision.

## IBM Replacement Strength

Strong Replacement, with improved outcomes

## IBM Replacement Strategy - Why IBM over Broadcom

IBM Security MaaS360 with Watson replaces Symantec GHOST Solution Suite by modernizing endpoint provisioning from legacy thick-image cloning to automated, cloud-native zero-touch deployment. Static disk cloning requires maintaining hardware-specific images and cannot service remote or hybrid workforces. IBM MaaS360 integrates with modern device provisioning frameworks (Windows Autopilot, Apple Device Enrollment, Android Zero-Touch) to automate over-the-air enrollment, configuration, and recovery, drastically reducing provisioning time, network overhead, and administrative costs.

## IBM PRIMARY - Product Name (The Replacement)

IBM Security MaaS360 with Watson (Modern Endpoint Provisioning)

## IBM PRIMARY - Product Description

IBM Security MaaS360 with Watson is IBM's cloud-native Unified Endpoint Management (UEM) solution that replaces legacy disk-imaging workflows with modern zero-touch OS enrollment, configuration deployment, and over-the-air device lifecycle management.

- **Disk imaging** — IBM MaaS360 replaces legacy sector-based thick disk cloning with dynamic, policy-based over-the-air profile provisioning and application bundle distribution directly from the cloud.
- **OS deployment and migration** — IBM MaaS360 integrates seamlessly with modern cloud enrollment programs (Windows Autopilot, Apple Business Manager, Android Zero-Touch) to provision and migrate operating systems without physical media or custom gold master images.
- **Remote command execution** — IBM MaaS360 enables IT administrators to push instant remote actions, custom PowerShell/Bash scripts, and configuration profiles to managed endpoints across corporate networks or the public internet.
- **Recovery** — IBM MaaS360 provides remote device wipe, enterprise data reset, automated self-healing policy re-enforcement, and cloud-initiated OS re-provisioning to rapidly restore compromised or malfunctioning devices.

## IBM PRIMARY - IBM Product Page URL

https://www.ibm.com/products/maas360

## Customer Reference
(not provided)
## IBM SECONDARY - Product Name (Supporting Product, where recommended to compliment the Primary capability)

(not provided)

## IBM SECONDARY - Product Description

(not provided)

## IBM SECONDARY - Product Page(s) URL

(not provided)

# Sources:

## IBM Security MaaS360 with Watson

- IBM Security MaaS360 Product Overview: https://www.ibm.com/products/maas360
- IBM MaaS360 Device Enrollment and Provisioning Guide: https://www.ibm.com/docs/en/maas360?topic=getting-started-device-enrollment
- Gartner Peer Insights — IBM Security MaaS360 Reviews: https://www.gartner.com/reviews/market/unified-endpoint-management-tools/vendor/ibm/product/ibm-security-maas360

## Sources: Analyst reviews and exist strategy

- Broadcom Knowledge Base, 'Ghost Solution Suite End of Life Schedules' (knowledge.broadcom.com)

## General Sources:

- Ghost Solution Suite 3.3.13 Release Notes: https://techdocs.broadcom.com/us/en/symantec-security-software/endpoint-security-and-management/ghost-solutions-suite/3-3/Release-Notes/Ghost-Solution-Suite-33-13-Release-Notes.html
- Download the latest version of Ghost Solution Suite: https://knowledge.broadcom.com/external/article/175846/download-the-latest-version-of-symantec.html
- Ghost Solution Suite End of Life Schedules (knowledge base): https://knowledge.broadcom.com/external/article/195893/ghost-solution-suite-end-of-life-schedul.html

## Change history:

### 2026-09-20 - Analyst Cautions and Industry Findings rewritten as a narrative
- Rewrote the section as a narrative and stated more clearly that Broadcom is still releasing the product.
- Recorded that no named organisation has publicly left GHOST.
- Moved all citations to the Sources: Analyst reviews and exist strategy section and removed the earlier column notes from that section.


### 2026-09-19 - Broadcom product information verification (WebFetch pass, files 02-39)
- Analyst Cautions: removed the claim that the product is 'on a formal wind-down lifecycle'. The Broadcom knowledge base article contains no dates, and release 3.3.13 was published in 2026, so the wind-down conclusion was not supported.

### 2026-09-19 - WebFetch verification pass
- Verified with WebFetch: 3.3.13 is the latest release listed. Detailed 3.3.13 features were not available from the fetched pages.

### 2026-09-19 - Broadcom product information review
- Product description: Added current release line 3.3 (RU13). Feature detail is carried forward from the earlier description.
- Summary and numbered list of four key features rewritten from current Broadcom sources.
- General Sources: 2 sources recorded (Broadcom TechDocs, product pages, press releases where available).
