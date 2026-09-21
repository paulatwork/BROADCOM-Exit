# Workload Automation Advanced Integration for Hadoop

## Page Status 

Complete

## Broadcom Software Type

Enterprise Software

## Broadcom Product Category

Enterprise Workload Automation

## Broadcom Product Name

Workload Automation Advanced Integration for Hadoop

## Broadcom Product Description - Key Features

Workload Automation Advanced Integration for Hadoop lets Hadoop big-data jobs be defined and scheduled from Broadcom workload automation products. 

Key features:

1. **Hive and Pig jobs** - Runs HiveQL queries against HDFS data and Pig scripts, which generate MapReduce programs.
2. **Oozie workflows and coordinators** - Runs Oozie workflows and time or data-triggered coordinator jobs.
3. **Sqoop data transfer** - Imports data from relational databases to HDFS and exports it back, with the ability to terminate a running job.
4. **Single scheduling console** - Hadoop jobs are managed alongside enterprise workloads from AutoSys (and other Broadcom schedulers) rather than a separate Hadoop scheduler.

## Analyst Cautions and Industry Findings - Related to the Legacy Broadcom Product. Include newest findings on Broadcom exist strategies

This product is a plug-in for the AutoSys and ESP schedulers, built for a world in which Hadoop was the centre of enterprise data. That world has been shrinking for years. Organisations have been moving off on-premises Hadoop towards cloud object storage, managed Spark and distributed microservices, and that shift began before Broadcom bought CA and has nothing to do with Broadcom's commercial behaviour. Investment in Hadoop-specific scheduler integrations is limited by the decline of the market itself.

So the exit story here is mostly a story about Hadoop. No analyst firm covers the product, and no named organisation has publicly described leaving it, although the market trend away from Hadoop toward platforms such as Databricks is widely reported. Customers who leave AutoSys will find that the integration has little value without it.

The IBM suggestion needs care. IBM Spectrum Conductor is a supported IBM product, but it is a multi-tenant cluster manager for Spark, Anaconda and Dask, aimed at machine learning workloads. It is not a general-purpose enterprise job scheduler, and it replaces only part of what the scheduling console does. Apache Airflow with Astronomer, and Kubernetes-native Argo Workflows, are closer to the job of orchestrating data pipelines alongside other enterprise workloads, and they are the options most often cited in commentary on moving Hadoop-adjacent scheduling.

## IBM PRIMARY - Product Name (The Replacement)

IBM Spectrum Conductor

## IBM PRIMARY - IBM Product Page URL

https://www.ibm.com/products/spectrum-conductor

## IBM Replacement Strength

Partial

## IBM Replacement Strategy (Short)

Spectrum Conductor offers an alternative for common Spark workloads, excluding Hive and Oozie scheduling.

## IBM Replacement Strategy (Description - Why IBM over Broadcom)

For specialised workloads, IBM offers a suppier alterantive matching more common requirements.

## IBM PRIMARY - Product Description 

Spectrum Conductor is an enterprise-class, multi-tenant platform for deploying and managing Apache Spark (plus Anaconda, Dask and other frameworks) on shared resources, providing higher utilization, and lower TCO for infrastructure. Spectrum Conductor runs common jobs for Spark, Anaconda and Dask. It does not run Hive, Pig, Oozie or Sqoop job scheduling but these have limited uptake in government.

Scaling Machine Learning - A multi-stage workflow process to scale machine learning, across data preparation, feature engineering, model training, and model scoring. An enterprise-class, multi-tenant platform for deploying and managing Apache Spark, Anaconda, Dask and other application frameworks and services on a common shared cluster of resources. 

Note - Offers supperior solution to Cloudera cluster software. So, may allow improved use of infrastructure and consolidation of dozens of heterogeneous applications and environments into a centrally-managed Spark environment to improve costs. 

Independent benchmarking finds Conductor delivered 25–88% higher Spark throughput than other resource managers across interactive, batch and mixed workloads. 

Simply complex Hadoop stacks - Solve the inability to efficiently run multiple versions of Spark on the same infrastructure.
Improved ROI - Get reduction in SaaS Cloudera costs / Infrastructure for on-prem.
Improved Performance - Get imporved performance while reducing spend, with low risk swap, requires no change to applications.

## Customer Reference

Wells Fargo Bank, considered one of the "Big Four Banks" in the United States, is building deep learning models to comply with requests from US Comprehensive Capital Analysis and Review (CCAR) regulators. CCAR is a United States regulatory framework to regulate large banks and financial institutions. There are many data scientists at Wells Fargo who build, enhance, and validate hundreds of models each day and speed is critical, as well as scalability, as they deal with greater amounts of data and more complicated models.

Wells Fargo needed to replace legacy Hortonworks Data Platform (HDP) cluster on Intel data lake and were building out a data science practice; and solve the core problem with a classic HDP/Hadoop cluster is siloing and low utilization. Each line of business, each Spark version, each dev/test/prod environment tends to get its own carved-off set of nodes. 


## IBM SECONDARY - Product Name (Supporting Product, where recommended to compliment the Primary capability)

None 

## IBM SECONDARY - Product Description

None 

## IBM SECONDARY - Product Page(s) URL

None 

# Sources:

## Sources: Analyst reviews and exist strategy

- Broadcom TechDocs, Workload Automation Advanced Integration for Hadoop product documentation (techdocs.broadcom.com)

## General Sources:

- Workload Automation Advanced Integration for Hadoop 24.1: https://techdocs.broadcom.com/us/en/ca-enterprise-software/intelligent-automation/workload-automation-for-hadoop/24-1.html
- Define a Sqoop Job - AutoSys 24.2: https://techdocs.broadcom.com/us/en/ca-enterprise-software/intelligent-automation/autosys-workload-automation/24-2-00/scheduling/ae-scheduling/ca-wa-advanced-integration-for-hadoop/define-a-sqoop-job.html
- Define Oozie Jobs - AutoSys 24.2: https://techdocs.broadcom.com/us/en/ca-enterprise-software/intelligent-automation/autosys-workload-automation/24-2-00/scheduling/ca-wcc-scheduling/manage-the-advanced-integration-for-hadoop-using-ca-wa/define-oozie-jobs.html

## Change history:
