---
title: "Week 3 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.3. </b> "
---

### Week 3 Objectives:

* AWS compute VM services.
* AWS storage services.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Amazon Elastic Compute Cloud (EC2) & EBS (Elastic Block Store) <br> - Amazon Lightsail | 04/05/2026 | 04/05/2026 | <https://youtu.be/e7XeKdOVq40?si=z4QEhZbtv5Fw_og8> |
| 3 | - Amazon EFS / FSX <br> - AWS Application Migration Service (MGN) | 05/04/2026 | 05/04/2026 | <https://youtu.be/hFVYG8WqfU0?si=QxwYCFD9nqa0VAW7> |
| 4 | - Hands-on practice <br>&emsp; + Manage Resources Using Tags and Resource Groups (Lab 27) | 06/04/2026 | 06/04/2026 | Using Tags :: MANAGE RESOURCES USING TAGS AND RESOURCE GROUPS |
| 5 | - Hands-on practice: <br>&emsp; + Deploying FCJ Management Application with Auto Scaling Group (Lab 06) | 07/04/2026 | 07/04/2026 | Deploying FCJ Management with Auto Scaling Group :: DEPLOYING FCJ MANAGEMENT APPLICATION WITH AUTO SCALING GROUP. |
| 6 | - AWS storage services <br>&emsp; + Amazon Simple Storage Service (Amazon S3): Concepts and key features. | 08/04/2026 | 08/04/2026 | <https://youtu.be/_yunukwcAwc?si=EVCC-mNqdaYyj052> |

### Week 3 Achievements:

#### **Monday**

**1. Amazon Elastic Compute Cloud (EC2) & EBS (Elastic Block Store)**

* **Overview:**
    * **Amazon Elastic Compute Cloud (EC2):** This is the core virtual server service on AWS.
    * **EBS (Elastic Block Store):** A storage service attached to EC2. Because EBS does not have enough complex content to learn separately, in this program it is grouped together and presented alongside Amazon EC2.

**A) Amazon Elastic Compute Cloud (EC2):** It is similar to a virtual server or a traditional physical server. EC2 offers fast provisioning, strong resource elasticity, and flexibility.

* Amazon EC2 can support workloads such as web hosting, applications, databases, authentication services, and any other tasks that a regular server can handle.
* **Key differences & advantages of EC2:**
    * **Rapid provisioning:** Creating a new server is much faster than with traditional servers.
    * **Flexible configuration changes:** Users can easily add or remove resources for a virtual machine, without being locked in like physical hardware.
    * **Easy upgrades at lower cost:** Like "renting a house," AWS automatically upgrades CPUs and chipsets to more powerful versions over the years, but the cost for these newer versions is lower than the older ones. This is AWS's commitment: costs decrease over time rather than increase.

![Diagram of EC2 key differences and advantages](/images/1-Worklog/1.3-Week3/01.png)

* **Elasticity:** Automatically increases resources when load is high and decreases when load is low.
* **Scalability:** Focuses on expanding the system.
* **Difference:** Elasticity = flexible scale-out and scale-in based on actual demand.
* **Benefit:** Cost savings through the pay-as-you-go model.
* **Use cases:** Suitable for web, database, authentication, and many other workloads.
* **Instance Type:** Amazon EC2 configuration cannot be chosen arbitrarily; configuration is selected through EC2 Instance types. (<https://aws.amazon.com/ec2/instance-types/?ncl=h_ls>)
* **Instance type determines the following factors:**
    * **CPU (Intel / AMD / ARM (Graviton 1 / 2 / 3) / GPU**
        * **Intel:** Has the highest usage cost.
        * **AMD:** Saves approximately 10% compared to Intel.
        * **ARM (AWS Graviton 1, 2, 3 chips):** Has an architecture similar to Apple M1/M2/M3 chips. This chip line delivers the highest Performance/Price ratio, helping save costs by up to 40%. (Supported on LINUX only; not yet available on WINDOWS)
    * **Memory**
    * **Network**
    * **Storage**
* **EC2 virtual server architecture diagram:**

![EC2 virtual server architecture diagram](/images/1-Worklog/1.3-Week3/02.jpeg)

**a) AMI / Backup / Key Pair**

* **AMI (Amazon Machine Image):** A template used to provision one or more EC2 instances at the same time.
* Using an AMI (Amazon Machine Image), you can provision one or more EC2 Instances at once. AMIs are available from AWS, on AWS Marketplace, or as custom AMIs created from EC2 Instances.

![Diagram of AMI types](/images/1-Worklog/1.3-Week3/03.jpeg)

* **AWS Marketplace:** An "app store" (similar to the App Store or Google Play) where you can purchase AMIs with pre-built solutions from organizations or third-party software vendors.
* **Custom AMI:** You can create an AMI from your own running EC2 instance.
* An AMI includes root OS volumes, AMI usage permissions that define which AWS accounts can use it, and EBS volume mappings that will be created and attached to EC2 Instances.
* **Components of an AMI:**

![Diagram of AMI components](/images/1-Worklog/1.3-Week3/04.png)

* An EC2 instance can be backed up by creating a snapshot.
* A key pair (public key and private key) is used to encrypt login information for an EC2 Instance.
* **How it works:**

![Key Pair operation diagram](/images/1-Worklog/1.3-Week3/05.jpeg)

![Key Pair encryption diagram](/images/1-Worklog/1.3-Week3/06.jpeg)

**B) EBS (Elastic Block Store):** A storage service attached to EC2. Because EBS does not have enough complex content to learn separately, in this program it is grouped together and presented alongside Amazon EC2.

* Elastic Block Store (EBS) is what we refer to when we talk about "disks attached to an EC2 server" or "Block device mapping" — that is block storage.
* Amazon EBS provides block storage and is attached directly to an EC2 Instance. Although it is attached like a RAW device, EBS operates independently from EC2 and is connected through the dedicated EBS network.
* **Dedicated network (EBS Network):** This is a major differentiator and advantage of AWS compared to other cloud providers.
* **Nature:** EBS operates independently from EC2 and is connected through the dedicated EBS network within the same AZ. EC2 cannot operate without EBS.
    * **EBS Network:** A dedicated network connecting EBS and EC2 (does not share the Internet network).
    * **Strength:** A standout advantage of AWS compared to many other cloud providers.
    * **How it works:** Storage data (EBS) travels through a dedicated channel, separate from the regular network.
    * **Benefit:** Avoids network congestion; data transfer does not affect each other.
    * **Result:** Ensures stable, accurate storage performance when testing performance.
* **Disk classification:**

![EBS disk classification diagram](/images/1-Worklog/1.3-Week3/07.png)

* EBS has two main disk groups: HDD and SSD, designed to achieve 99.999% availability by replicating data across 3 Storage Nodes within 1 AZ.
* Some specific EC2 Instances are optimized for EBS performance. (Optimized EBS Instances)
* EBS volumes, by default, can only be attached to 1 EC2 Instance. EC2 Instances running on the Nitro Hypervisor can use 1 EBS volume attached to multiple EC2 Instances. (EBS Multi-Attach)
* EBS is backed up by taking snapshots to S3 (Simple Storage Service)
    * The first snapshot is full; all subsequent snapshots are incremental.

**a) Instance Store:** A very high-speed NVMe disk area located on the physical node running EC2 virtual machines.

* Instance store data is completely deleted when we stop an EC2 instance.
* Instance store data is not deleted when we restart the machine or when it crashes.
* Instance store does not replicate data for backup, so storing important data on it is generally not recommended.
    * Used in cases requiring extremely high performance up to millions of IOPS.
    * When used, data is often replicated to an EBS volume to ensure safety.
* **Risks and recommendations:**
    * **No replication:** Instance Store does not copy/backup data like EBS.
    * **High risk:** Hardware failure ⇒ complete data loss with no recovery.
    * **AWS recommendation:** Do not store important data on Instance Store.
    * **Solution:** Important data should be stored on EBS.
* **States that cause and do not cause data loss:**

![Diagram of states that cause and do not cause data loss](/images/1-Worklog/1.3-Week3/08.jpeg)

* Used in cases requiring extremely high performance up to millions of IOPS:
    * swap
    * paging
    * ………

**b) User Data:** A script that runs once when provisioning an EC2 Instance from an AMI. Simply put, it is a script.

* Depending on the operating system, we use bash shell scripts (Linux) / PowerShell (Windows).
* **Operating system dependency:**

![Operating system dependency diagram](/images/1-Worklog/1.3-Week3/09.jpeg)

**QUESTION:** Why is User Data needed in practice?

* **Golden Image:** A standard pre-configured AMI (security, optimization) used as the base image.
* **Problem:** Without User Data → you must create multiple separate AMIs (Web, App, DB…).
* **User Data:** A script that runs when EC2 is launched to apply additional configuration.
* **Solution:** Use 1 Golden Image + User Data to "transform" EC2 into different roles.
* **Benefits:**

![User Data benefits diagram](/images/1-Worklog/1.3-Week3/10.png)

* Reduces the number of AMIs to manage.
* Increases deployment automation.
* Flexibility in enterprise environments.

**c) EC2 Auto Scaling:** A feature that supports increasing or decreasing the number of EC2 Instances based on specific conditions (scaling policy).

* Can automatically register EC2 Instances with an Elastic Load Balancer.
* Operates across multiple AWS Availability Zones.
* Can support multiple Pricing options.
* **Core role of EC2 Auto Scaling:**
    * **Main role:** EC2 Auto Scaling helps implement Elasticity (scaling) on the Cloud.
    * **Function:** Automatically increases/decreases the number of EC2 instances based on configured conditions.
    * **Scaling Policy:** A set of rules that determine when to scale up / scale down.
    * **Meaning:** Ensures system performance and optimizes operational costs.
* **Integration with Load Balancing and Availability:**
    * **ELB integration:** When new EC2 instances are created, Auto Scaling automatically registers them with the Load Balancer.
    * **Benefit:** Traffic is distributed evenly immediately, with no manual configuration required.
    * **Multi-AZ:** Operates across multiple Availability Zones (AZs).
    * **Meaning:** Increases High Availability and avoids downtime when 1 AZ encounters an issue.
* **Cost optimization:**
    * **Goal:** Optimize costs when using EC2 Auto Scaling.
    * **Approach:** Combine multiple Pricing Options within the same system.
    * **On-Demand:** Pay as needed (flexible, easy to use).
    * **Spot Instances:** Low cost, uses spare capacity (may be reclaimed).
    * **Reserved / Savings Plans:** Long-term commitment for discounted pricing.
    * **Benefit:** Balances cost, performance, and stability.

**d) Pricing options**

* EC2 includes 4 pricing options:
    * **On-Demand:** Billed by the hour / minute / second; the more you use, the more you pay; most expensive. Suitable for workloads running up to 6 hours per day.
    * **Reserved Instance:** Commit to usage for 1–3 years to get a discount; however, limited by EC2 Instance type / family.
    * **Savings Plans:** Commit to usage for 1–3 years to get a discount; may not be limited by EC2 Instance type family.
    * **Spot Instance:** Uses spare capacity at a low price; however, AWS may terminate the instance within 2 minutes when capacity is needed.

**e) Amazon Lightsail:**

* A low-cost compute service (monthly pricing starting from $3.5/month). Each Lightsail Instance also includes a data transfer allowance. (This data transfer is significantly cheaper than data transfer from EC2.)
* Suitable for lightweight workloads and test/dev environments that do not require sustained high CPU load for more than 2 hours per day.
* Also supports backup via snapshots, similar to EC2.
* Runs in a special VPC and can connect to a regular VPC through one-click VPC Peering.

#### **Tuesday**

**2. Amazon EFS / FSX**

* **Overview:**
    * These are services used to create shared storage space for multiple servers over the network.
    * AWS provides two main services for this purpose: Elastic File System (EFS) and FSx.

**a) EFS (Elastic File System)** allows you to create NFSv4 network volumes and attach them to multiple EC2 Instances at the same time, with storage scale up to petabytes. EFS supports Linux only.

* EFS is billed only for used capacity (while EBS is billed for provisioned capacity).
* EFS can be configured to mount in on-premises environments via DX or VPN.

**b) FSx:** Allows you to create NTFS volumes and attach them to multiple EC2 Instances at the same time using the SMB (Server Message Block) protocol. FSx supports Windows and Linux.

* FSx is billed only for used capacity (while EBS is billed for provisioned capacity).
* FSx supports deduplication, helping reduce costs by 30–50% for typical use cases.

**3. AWS Application Migration Service (MGN)**

* **Overview:**
    * This is a service dedicated to supporting the Migration process. It helps you move applications and services from on-premises / local server environments to the AWS cloud platform.
    * MGN also supports Disaster Recovery.
* MGN is used to migrate and replicate for the purpose of building a Disaster Recovery Site for physical and virtual servers to the AWS environment.
* It continuously replicates source servers to EC2 Instances on an AWS account (asynchronous / synchronous).
* During replication, MGN uses staging machines that are much smaller in number and configuration than the source servers.
* When performing cut-over, MGN automatically creates and runs EC2 servers on AWS.

#### **Thursday – Saturday**

Complete the Lab exercises.

Lab links: <https://docs.google.com/document/d/1_NX-S0mg1et47c4ePoq0SdbkQLCLsN3NYFsMrnoKdng/edit?usp=sharing>
