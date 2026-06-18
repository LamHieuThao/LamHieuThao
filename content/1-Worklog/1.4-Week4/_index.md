---
title: "Week 4 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.4. </b> "
---

### Week 4 Objectives:

* AWS storage services.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - AWS storage services <br>&emsp; + Amazon Simple Storage Service (Amazon S3): <br>&emsp;&emsp; + S3 Access Point, S3 Storage Class <br>&emsp;&emsp; + S3 Object Lifecycle Management <br>&emsp;&emsp; + Static Website & Cors <br>&emsp;&emsp; + Control Access <br>&emsp;&emsp; + Endpoint & Versioning <br>&emsp;&emsp; + Object Key & Performance <br>&emsp;&emsp; + Glacier | 11/05/2026 | 11/05/2026 | Module 04-02 - Amazon Simple Storage Service (S3) - Access Point - Storage Class <br> Module 04-03 - S3 Static Website & CORS - Control Access - Object Key & Performance - Glacier |
| 3 | - Snow Family <br>&emsp; + Snowball <br>&emsp; + Snowball Edge (Snowball X) <br>&emsp; + Snowmobile <br> - Disaster Recovery on AWS | 12/05/2026 | 12/05/2026 | Module 04-04 - Snow Family - Storage Gateway - Backup |
| 4 | - Hands-on practice <br>&emsp; + S3 bucket (000057) <br>&emsp; + AWS Backup (000013) | 13/05/2026 | 13/05/2026 | Create S3 bucket :: Start with Amazon S3 <br> Deploy AWS Backup to the System :: DEPLOY AWS BACKUP TO THE SYSTEM |
| 5 | - Hands-on practice <br>&emsp; + VM Import/Export | 14/05/2026 | 14/05/2026 | AWS VM Import/Export :: VIRTUAL MACHINE (VM) IMPORT/EXPORT |
| 6 | - Hands-on practice | 15/05/2026 | 15/05/2026 | |

### Week 4 Achievements:

#### **Monday**

**A) S3 Access Point:**

* A feature that allows you to create connection endpoints (unique hostnames) for applications, individual users, or groups.
* You can configure different permissions for each access point created.

**QUESTION:** Why use Access Points?

* Initially, when multiple applications share the same S3 Bucket, configuring access permissions (Policies) is very complex and prone to errors such as granting excessive or insufficient permissions. S3 Access Point solves this by creating separate access points for each application or user group. Each Access Point has its own policy, making access management clearer, more flexible, and easier to control. In addition, this feature enhances security by combining Identity Policy and Resource Policy for stricter access control.

![S3 Access Point operation diagram](/images/1-Worklog/1.4-Week4/01.jpeg)

**B) S3 Storage Class:**

* Amazon S3 divides storage into multiple tiers to optimize costs.
* **Storage tiers (S3 Storage Class):**
    * **S3 Standard:** Frequently accessed data (high storage cost, but very low request cost).
    * **S3 Standard IA (Infrequent Access):** Infrequently accessed data (lower storage cost than Standard, but very high request cost).
    * **S3 Intelligent Tiering:** Automatically moves objects between storage tiers based on the number of days an object has not been accessed. Specifically, if a file is not touched for 60 days, it is automatically moved to a cheaper tier.
    * **S3 One Zone IA:** Reproducible data stored long-term, infrequently accessed but requiring fast access. Very low cost. Data is stored in only 1 AZ (instead of 3 AZs). For data that is rarely used but can be recreated if lost.
    * **Amazon Glacier / Deep Archive:** Stores infrequently accessed data. Very low cost and cold storage. Ideal for data that may only be accessed once every few years. (Note: You cannot read data directly from this tier; you must "thaw" it first before moving it to upper tiers to read.)
* You can set up automated data lifecycle (Object Life Cycle Management) for data stored in Amazon S3. Using lifecycle policies, you can move data within an S3 bucket between storage tiers over a custom time period (days).

![Amazon S3 lifecycle diagram](/images/1-Worklog/1.4-Week4/02.jpeg)

* Object Life Cycle Management moves objects after the number of days you specify, counted from the date the object was created.

**C) Static Website & Cors:**

* Amazon S3 has a feature that allows hosting static websites (html, media, etc.), suitable for Single Page Applications. (A web application or website that interacts with users by automatically rewriting the current page with new data from the web server using JavaScript and frameworks such as AngularJS and ReactJS, instead of the browser's default method of loading an entirely new page.)
* Amazon S3 supports CORS. CORS is a mechanism that allows different resources (fonts, JavaScript, etc.) of a website to be requested from a domain other than the page's domain.
* CORS stands for Cross-origin resource sharing.
* **Function:** Amazon S3 is not only used to store static files (images, videos) but can also host (store and run) an entire static website.

![Amazon S3 CORS configuration diagram](/images/1-Worklog/1.4-Week4/03.jpeg)

* Amazon S3 allows configuring CORS (Cross Origin Resource Sharing) policies so that client web applications can interact with resources on other domains.
* CORS must be enabled and configured on the S3 Bucket. Without CORS configuration, the system will block access and return an Access Denied error.

**D) Control Access**

* Mechanisms for controlling access to Buckets:
    * **S3 Access Control List (ACL)** is a legacy access control mechanism that predates IAM. However, if you are already using S3 ACLs and they meet your needs, there is no need to change. S3 ACLs are attached to the bucket (root folder) and objects (individual files). They define which AWS accounts or groups are granted access and what type of access.
    * **Disadvantage:** Assigning hundreds of granular policies at different levels makes management extremely complex and error-prone.
    * **S3 Bucket Policy and IAM policy** define object-level permissions by specifying those objects in the Resource section of your policy. The statement applies to those objects in the bucket. Consolidating object-specific permissions into a single policy (as opposed to many S3 ACLs) makes it easier to determine access rights.
    * This is the modern approach and is a type of Resource Policy.
    * **Advantage:** Mid-level management — you only need to write one Policy attached directly to the S3 Bucket, governing all permissions for every file (object) in that bucket.

**E) Endpoint & Versioning:**

* **Amazon S3 Endpoint (S3 Endpoint)** is a feature that allows access to an S3 bucket through AWS's private network. By default, access to S3 is through the internet.
    * EC2 servers and S3 are both "children of the same AWS parent." But by default, if EC2 wants to upload a file to S3, it must route out through the public Internet and back to S3. This is both slow and less secure. Therefore, we need the S3 VPC Gateway Endpoint solution.
    * **Benefits:** Traffic (data transfer) from EC2 to S3 travels through AWS's internal network (private virtual network) without touching the Internet (using Private IP instead of Public IP). Faster and more secure.
* You can enable Versioning, which allows you to recover objects after accidental deletion or overwrite, and can help protect against ransomware / encryption attacks.
    * If you delete an object, instead of deleting it, Amazon S3 marks the file as deleted.
    * If you overwrite an object, a new object version appears in the bucket.
    * In both cases, you can recover the previous version.

![Public/private subnet organization diagram in VPC](/images/1-Worklog/1.4-Week4/04.jpeg)

* **Deletion mechanism:** S3 does not actually delete the file; it attaches a label called a Delete Marker. Normal access returns a 404 (file not found), but if you request it with the old version ID, you can still download it normally.
* **Ransomware protection:** If encrypted by a hacker, the corrupted file overwrites the original. With Versioning enabled, the original file remains (old version) and you can restore it without paying a ransom.
* **Cost:** When Versioning is enabled, you are charged for the combined storage of all versions. Once enabled, it cannot be fully disabled — only suspended.

**F) Object Key & Performance:**

* Every object in S3 is flat, with no hierarchy, and is assigned one object key. For example: /image/sample.jpg, sample.jpg.
* Under the hood, S3 divides data into Partitions, which are automatically split when request volume increases or the number of S3 object keys grows. (This slows down object lookup within a partition.)
* S3 stores a key map (the key map is also divided into multiple partitions and hashed by prefix — the prefix of the object key).
* To optimize S3 performance, you can use a random prefix (/fscd/img/sample.jpg instead of /img/sample.jpg). The goal is to distribute objects across as many partitions as possible, since S3 performance depends on the number of partitions.

**G) Glacier**

* A low-cost storage option (up to 20 times cheaper than S3 Standard), suitable for data that does not need direct access and is stored long-term (5–10 years). If an application needs frequent or fast data access, choose Amazon S3 instead of Glacier.
* When storing data in Amazon S3 Glacier, you cannot access it directly; data must be retrieved to an S3 Bucket.
* There are three retrieval options with different times and costs (thaw levels):
    * **Expedited retrieval:** typically completes within 1–5 minutes.
    * **Standard retrieval:** typically completes within 3–5 hours.
    * **Bulk retrieval:** typically completes within 5–12 hours.
* **Cannot** read directly. To download and view data, you must perform a Retrieve operation (thaw/restore data from Glacier back to S3 Standard).
* You cannot upload files to Glacier through the standard web Console. You must use Code (CLI or SDK) or use Object Lifecycle to gradually move data down. Objects stored here are called "Archives."

![Diagram of storage, retrieval, and data management between S3 and Glacier in AWS](/images/1-Worklog/1.4-Week4/05.jpeg)

* Amazon S3 Glacier is a low-cost storage option suitable for data that does not require direct access and is stored long-term.

#### **Tuesday**

**A) Snow Family (Physical data transfer service)**

* **Overview:** An Offline Data Transfer (cold data transfer) solution used when internet bandwidth is insufficient to transfer massive amounts of data (tens of TB to hundreds of PB).
* **Principle:**

![Snow Family principle diagram](/images/1-Worklog/1.4-Week4/06.png)

**a) Snowball**

* A service that supports migrating data from on-premises environments to AWS at scales up to Petabytes (PB). Each Snowball can hold up to 80 Terabytes (TB).
* Snowball is shipped back to the AWS region you choose for data storage in your selected service, including S3 or Glacier.
* You need to install the Snowball Client on your local machine to perform verification, compression, encryption, and data transfer.

**b) Snowball Edge (Snowball X)**

* A service that supports migrating data from on-premises environments to AWS at scales up to Petabytes (PB). Each Snowball Edge can hold up to 100 Terabytes (TB).
* Snowball Edge is shipped back to the AWS region you choose for data storage in your selected service, including S3 or Glacier.
* You need to install the Snowball Client on your local machine to perform verification, compression, encryption, and data transfer.
* Snowball Edge is a special device with built-in compute resources to process data locally before importing it into the device.
* Integrates compute resources (internal server) to preprocess data on-site before shipping.

**c) Snowmobile**

* A service that supports migrating data from on-premises environments to AWS at Exabyte scale. It is a data transport truck; each Snowmobile can hold up to 100 PB.
* Snowmobile returns to the AWS region you choose for data storage in your selected service, including S3 or Glacier.

**B) AWS Storage Gateway (Hybrid storage solution)**

* AWS Storage Gateway is a Hybrid storage solution that combines AWS cloud storage with unlimited on-premises storage capacity.
* You can leverage the scale and reasonable pricing of cloud storage services to store large volumes of data with long retention requirements.
* AWS Storage Gateway supports three main storage methods: file, disk, and tape.
    * **File Gateway** allows you to store and retrieve objects in Amazon S3 using NFS and SMB file protocols. Objects written through the file gateway can be accessed directly in S3 (as Objects).
    * **Volume Gateway** provides block storage for your applications using the iSCSI protocol. Data on the disk is stored in Amazon S3. To access iSCSI disks in AWS, you can create EBS snapshots (automatically via AWS Backup) and then create EBS Volumes from them.
        * **Stored Volume:** Keeps a full copy locally and one copy on AWS (used for Disaster Recovery).
        * **Cached Volume:** Keeps only frequently used data locally; older data is pushed to AWS (optimizes local capacity).
    * **Tape Gateway** provides your backup application with a virtual tape library (VTL) iSCSI interface, virtual tape drives, and virtual tapes. Virtual tape data is stored in Amazon S3 or can be stored in Amazon Glacier. Replaces traditional Tape Libraries with a virtual library (VTL). Helps back up old data to S3 or Glacier at low cost.

![AWS Storage Gateway architecture diagram](/images/1-Worklog/1.4-Week4/07.jpeg)

**C) Disaster Recovery on AWS**

**a) RTO (Recovery Time Objective)**

* Recovery Time Objective (RTO) is the time required to restore a service to normal operating status.
* Example: If a disaster occurs at 2:00 PM and the RTO is 4 hours, the DR process must restore the service no later than 6:00 PM.

**b) RPO (Recovery Point Objective)**

* Recovery Point Objective (RPO) is the maximum amount of time for which data can be lost (the maximum time for the system to return to normal operation).
* Example: If we perform a backup once per day, in the worst case we could lose 24 hours of data, RPO = 24 hours. (The maximum acceptable data loss window.)
* Services and applications vary in complexity and have different Service Level Agreements (SLAs) that include different RTO/RPO values. Depending on the service type and commitment level, we choose the corresponding disaster recovery strategy.
* There are 4 disaster recovery strategies on AWS:
    * **Backup and restore:** cheapest but longest RTO/RPO (a mandatory step for every strategy).
    * **Pilot Light (Active – Standby):** Low cost. The AWS system runs only core components (such as Database); other servers are started when a disaster occurs.
    * **Low Capacity Active – Active:** The AWS system always runs but at a smaller scale than on-premises (e.g., 20% capacity).
    * **Full Capacity Active – Active:** Both sides (Local and AWS) run at 100% in parallel, with immediate failover.

**D) AWS Backup**

* A service that manages backup tasks, allowing you to configure and schedule backups (backup schedule), backup policies (backup retention), and monitor backup activity for AWS resources.
    * Amazon EBS
    * Amazon EC2
    * Amazon RDS databases
    * DynamoDB databases
    * Amazon EFS
    * AWS Storage Gateway volumes

#### **Thursday – Saturday**

Hands-on lab practice.

Lab links: <https://docs.google.com/document/d/1iNnUbO9kMa4T13B-2wERHX2QJAniIzwO/edit?usp=sharing&ouid=110146210370887604643&rtpof=true&sd=true>
