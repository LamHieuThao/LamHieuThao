---
title: "Week 8 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.8. </b> "
---

### Week 8 Objectives:

* Complete hands-on lab exercises.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 & 3 | - Hands-on practice (Lab 24) | 08/06/2026 | 09/06/2026 | Using AWS Storage Gateway :: USING FILE STORAGE GATEWAY |
| 4 & 5 & 6 | - Translate blog post | 10/06/2026 | 12/06/2026 | |

### Week 8 Achievements:

#### **Monday & Tuesday**

**Lab 24 — Using AWS Storage Gateway**

**Concepts:**

* **AWS Storage Gateway:** A hybrid storage service connecting on-premises systems with AWS Cloud, enabling seamless data access and synchronization. There are 3 main types of Storage Gateway:
    * File Gateway
    * Volume Gateway
    * Tape Gateway
* **File Gateway (SMB):** A Storage Gateway component that enables file sharing on Windows via the SMB protocol and stores data on Amazon S3.
* **Amazon S3:** A highly durable object storage service that serves as the primary storage for data synchronized from File Gateway.
* **Amazon EC2:** An AWS virtual server used to deploy and operate Storage Gateway in the cloud environment.
* **AWS Security Group:** A virtual firewall that controls network traffic, ensuring secure connections between the system and Storage Gateway.

**Benefits:**

* **Enterprise:**
    * Flexibly expand storage capacity at low cost with Amazon S3.
    * Easy integration with existing systems without changing applications.
    * High access performance through local caching.
    * Enhanced data protection and Disaster Recovery support.
    * Supports Hybrid Cloud deployment between on-premises infrastructure and AWS.
    * Simplifies backup and long-term storage with automated policies on S3.
    * Ensures data safety through encryption during transfer and storage.

**Lab objectives:**

* Understand Hybrid Cloud Storage architecture and the role of AWS Storage Gateway in connecting on-premises systems with AWS Cloud.
* Deploy and configure File Gateway on Amazon EC2.
* Create and manage an SMB File Share connected to Amazon S3.
* Mount the File Share on a Windows machine via the SMB protocol.
* Verify data synchronization between the on-premises environment and Amazon S3.

**Lab steps**

![Lab 24 steps diagram](/images/1-Worklog/1.8-Week8/01.png)

**Results achieved:**

* Successfully created S3.
* Successfully created EC2 for Storage Gateway.

![S3 and EC2 creation success screenshot](/images/1-Worklog/1.8-Week8/02.png)

![Data sync verification and Cache Gateway configuration screenshot](/images/1-Worklog/1.8-Week8/03.jpeg)

* Successfully verified data synchronization between the on-premises environment and Amazon S3 through AWS Storage Gateway.
* Successfully configured Cache Gateway to optimize access performance for frequently used data.
* Set up SMB security with Guest Access and authentication password to control File Share access.
* Gained a solid understanding of AWS resource management and cleanup to avoid unnecessary costs.
* Completed the full Hybrid Cloud Storage model, building a foundation for deploying real-world enterprise storage solutions.

#### **Thursday – Saturday**

* Translated and studied the blog post: [SECURITY] SOFTWARE SUPPLY CHAIN SECURITY ACCORDING TO AWS WELL-ARCHITECTED STANDARDS.
* Original blog link: [Well-architected best practices for software supply chain security | AWS Security Blog](https://aws.amazon.com/blogs/security/well-architected-best-practices-for-software-supply-chain-security/)
