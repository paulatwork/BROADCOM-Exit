

## Category

VMware Workload Migration Strategy

## Content

Following Broadcom's acquisition of VMware in November 2023, VMware licensing moved from perpetual licences to subscription bundles priced per core. Licence cost is therefore directly linked to the number of physical cores deployed. This creates two paths for managing the cost of existing workloads (virtual machines) hosted on the VMware estate: First, is to reduce the VMware footprint to lower subscription cost (optimisation); Second, is to move as much workloads as possible to an alternative platform (migration). Combined together, these two approaches form the basis of an effective mitigation strategy to protected against continued rising costs and an increasingly combatative vendor.

## Expansion

ITOM is a required component of a mature VMware migration strategy.

1. **Inventory and licence baseline**. Discovery and infrastructure monitoring establish the actual host, core, cluster and virtual machine count. This is the basis for validating subscription quotes and identifying unlicensed or idle capacity.
2. **Rightsizing**. Utilisation data (CPU, memory, storage) over a representative period identifies oversized virtual machines and underused hosts. Consolidating onto fewer hosts reduces the licensed core count.
3. **Dependency mapping**. Application topology from observability tools (for example, Instana or DX Operational Observability) shows which virtual machines communicate with each other. This determines migration wave groupings, so that dependent components are moved together.
4. **Network flow analysis**. Network performance data (SevOne or Network Observability by Broadcom) identifies traffic volumes and latency sensitivity between tiers. This determines whether workloads can be separated across data centres or cloud regions without performance impact.
5. **Workload automation dependencies**. Batch schedules in Workload Automation, AutoSys or Automic frequently reference specific hostnames, agents and file paths. These must be identified and updated before migration, or scheduled jobs will fail after cutover.
6. **Performance baseline and validation**. Pre migration performance measurements provide the reference point for confirming that migrated workloads meet the same service levels. Without a baseline, degradation cannot be measured or attributed.
7. **Operational control during transition**. During migration the estate runs across two platforms. Event correlation (Concert Operate or Operational Intelligence) consolidates alerts from both, reducing the risk that incidents are missed during cutover windows.
8. **Execution automation**. Runbooks and orchestration reduce manual effort and error rates in repeatable migration tasks such as pre checks, cutover steps and rollback.

Risk considerations specific to this use

- **Target platform coverage**. Confirm that the current monitoring and automation tools support the target platform (for example, Nutanix, Red Hat OpenShift Virtualization, Microsoft Hyper‑V or public cloud) before migration begins.
2. **Supplier dependency**. Several of the listed tools are Broadcom products. Where the objective is to reduce dependence on Broadcom, the plan should assess whether the monitoring and automation layer is also in scope for change, and sequence that change so that visibility is maintained throughout the migration.
3. **Data period**. Utilisation data should cover peak periods such as month end and year end processing. A short sample may understate capacity requirements.
