---
title: "Week 1 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.1. </b> "
---



### **Week 1 Objectives**

* Start participating, connecting, and integrating into the community; get to know other First Cloud Journey members.
* Understand what AWS is and what First Cloud AI Journey (FCAJ) is.
* Understand AWS services and AWS Free Tier account levels.

---

### **Tasks to be carried out this week**

| Day | Task | Start Date | Completion Date | Reference/Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 (Tue) | Receive internship Gmail; join the community WhatsApp group; get to know FCAJ members | 20/04/2026 | 20/04/2026 | |
| 3 (Wed) | Read the code of conduct and regulations required during the AWS internship | 21/04/2026 | 21/04/2026 | Internship Code of Conduct & Regulations :: Internship Report |
| 4 (Thu) | Study learning materials and create an AWS account (Free Tier, AWS Console, complete 5 post-sign-up tasks) | 22/04/2026 | 22/04/2026 | AWS Free Tier 2025: The Revolution! :: Create an AWS Account |
| 5 (Fri) | Learn what AWS and FCAJ are; explore AWS services and cloud computing; study AWS management tools | 23/04/2026 | 23/04/2026 | First Cloud Journey Bootcamp 2025 - YouTube; AWS Study Group |
| 6 (Sat) | Complete hands-on labs: Kiro (Lab 000180), Create admin group and admin user, Budget | 24/04/2026 | 24/04/2026 | Kiro Spec Driven Development; https://000002.awsstudygroup.com/; https://000007.awsstudygroup.com/ |

---

### **Week 1 Achievements**

#### **Tuesday**

* Received the Gmail account for the AWS internship program.
* Joined the community WhatsApp group and met many new peers.

![Community WhatsApp group](/images/1-Worklog/1.1-Week1/01-whatsapp-community.png)

![Internship code of conduct and regulations](/images/1-Worklog/1.1-Week1/02-internship-rules.jpeg)

#### **Wednesday**

* Code of conduct and required practices during the internship:

**1. Attendance and check-in:** Over 3 months, participate in at least 10 full-time office sessions plus 4 events to qualify for the completion badge. Office days do not have to be every day, but at least one day per week on-site is required. Check-in is recorded through the office registration system, and the internship project must be completed as required. Attend regularly and follow your registered schedule to stay on track and meet evaluation criteria.

**2. Working hours:** 09:00–17:00 (Mon–Fri); arrive by 08:45. Lunch break: 12:00–13:30. Workplace: Floor 26 or Floor 46, Bitexco Financial Tower.

**3. Dress code and conduct:** Wear AWS uniform (or school uniform if AWS uniform is not yet available). Long pants, formal shoes, and ID badge required. Maintain order; no personal work during office hours.

**4. Access and workspace:** Check in at the main entrance (Floor 26); do not change work areas without permission. Take care of equipment and turn off devices when leaving.

**5. Food and drinks:** Eat only in designated areas. Do not bring colored food or drinks into the office; plain water only, due to high cleaning fees.

#### **Thursday**

1. **Study materials and AWS account setup:**
    * Following the provided guide, I created an AWS account under the **AWS Free Tier 2025** program.
    * After successful account creation, I received **$100** in credits.
    * I then read the guide and completed 5 tasks to earn an additional **$100** in credits:
        * Launch EC2 Instance - $20 credit
        * Amazon Bedrock Playground - $20 credit
        * Set up AWS Budgets - $20 credit
        * Create Lambda Web App - $20 credit
        * Create RDS Database - $20 credit
    * Completed all 5 tasks and received a total of **$200** in credits.

![Screenshot: $200 in credits received](/images/1-Worklog/1.1-Week1/04-credits-200-received.png)

2. **AWS Management Console overview:**
    * The **AWS Console (AWS Management Console)** is the web interface for managing all AWS cloud services on a single platform.
    * It is similar to a Control Panel or Dashboard. Through the Console you can:
        * Create servers
        * Store data
        * Deploy websites
        * Manage databases
        * View costs
    * After signing in, the home page includes a service search bar, recently used services, and key areas such as Billing and Security.
    * Key services:
        * **EC2:** Create and manage virtual servers
        * **S3:** Store files such as images and videos
        * **RDS:** Manage databases (MySQL, PostgreSQL)
        * **IAM:** Manage accounts and permissions
        * **VPC:** Configure private networks
        * **Billing:** Monitor and control costs

#### **Friday**

1. **AWS and FCAJ overview:**
    * AWS has been the leading cloud infrastructure provider for 13 consecutive years (as of 2023). Key differentiators: vision and culture.
    * **AWS pricing philosophy:** The more customers use AWS services, features, and resources, the more AWS reduces service prices over time.
    * AWS philosophy and culture are reflected through its leadership.
    * **FCAJ** is a learning community where members support one another and grow together.
    * **FCAJ direction:** AWS Study Group courses go beyond passive theory or mechanically repeating pre-built step-by-step labs.
    * **Six core principles:**
        * Proactive hands-on practice (Builder & Troubleshooter): Build products and handle incidents independently without waiting to be reminded.
        * Teamwork: Collaborate to bridge knowledge gaps and expand relationships.
        * Resilience: Persist under pressure to meet demanding job requirements.
        * Hands-on practice & knowledge sharing: Competence is measured by real work and the ability to share knowledge, not certificates alone.
        * Invest in yourself: Spend time and money to upgrade yourself.
        * Lifelong learning: Keep learning throughout a long-term journey.
    * **FCAJ internship path:**
        * Path: 3 months of self-driven practice during the internship.
        * Practice: Complete labs from basics to understand Cloud.
        * Outcome: Finish the graduation project.

2. **AWS services and cloud computing:**
    * **Journey:**
        * AWS is a Cloud provider with a vast number of courses. You can become a Cloud expert by completing your own learning path — connect with peers first, then work together toward becoming Cloud experts.
        * Cloud environment difference: Unlike traditional IT split by specialty, Cloud requires broad, cross-cutting system knowledge.
        * Large service ecosystem: AWS services and features grow very quickly (~12,000); services interact and support one another. Self-study alone is less effective — learn with the community.
    * **AWS infrastructure:**
        * **Data Center:** Houses tens of thousands of servers at large scale. All AWS data centers use hardware optimized specifically for AWS. Use benchmarking tools to measure real performance due to hardware optimization differences across providers.
        * **Availability Zone (AZ):** A logical cluster of one or more data centers. AZs are designed with independent power and networking so disasters affect only one AZ. AZs are linked by AWS high-speed private networks. Deploy across at least 2 AZs (Active-Active) for High Availability.
        * **Region:** Contains at least 3 Availability Zones. 25+ Regions worldwide, connected via the AWS backbone. Data stays within the Region where it is stored. Choose a Region by proximity (e.g., users in Vietnam often choose Singapore), service availability, and cost.
        * **Edge Location (PoP - Point of Presence):** Low-latency network nodes. Main services: **CloudFront** (CDN), **WAF** (layer 7 firewall, DDoS protection), **Route 53** (DNS). Edge locations are available in Hanoi and Ho Chi Minh City.

3. **AWS management tools:**
    * **AWS Management Console:** Web interface to operate, search, and access AWS services.
    * Two sign-in mechanisms:
        * **Root User:** The first account created when registering AWS; sign in with email and password. Highest privilege — use only for initial setup and MFA, not daily work.
        * **IAM User:** Sub-accounts for access control; requires a 12-digit Account ID when signing in.
        * **Support Center:** Open Support Cases for AWS assistance.
    * **AWS CLI:** Open-source command-line tool using Access Key and Secret Access Key for API requests.
    * **AWS SDK:** Multi-language libraries that handle authentication, retries, and serialization — simplifying application development.
    * **Cost optimization:** Right sizing; On-Demand / Reserved / Spot Instances; turn off unused resources; serverless; optimal architecture design; AWS Budgets; cost allocation tags; AWS Pricing Calculator.
    * **AWS Support:** Basic (free), Developer, Business (recommended for production), Enterprise (includes TAM).

#### **Saturday**

* Completed the following hands-on labs:

1. **Kiro — Modules 01–03** (Kiro Spec Driven Development)

![Kiro installation in progress](/images/1-Worklog/1.1-Week1/06-kiro-installing.jpeg)

![Kiro installed successfully](/images/1-Worklog/1.1-Week1/07-kiro-installed.jpeg)

**Evolution of AI in software development (SDLC):**

* **AI Assistant (2024):** Helps write code faster (autocomplete only).
* **AI Agents (2025):** Can complete tasks end-to-end, but still require human review.
* **Autonomous Agents (present/future):** AI can work fully autonomously and coordinate with other agents without humans.

**Spec Driven Development:**

* To address the limitations above, developers should return to the Spec Driven Development model.
* Before coding, prepare business requirements, system design, and test & deploy plans.
* Compile them into a specification (Spec) so AI coding tools can understand and build larger products.

**Main components and features of AWS Kiro:**

* **Kiro IDE:** App development environment from basics to production; supports Vibe Coding and Spec Driven workflows.
* **Agent Hook:** Automatically runs tasks on triggers (e.g., save file → update changelog, run tests).
* **Context & Steering File:** Helps AI understand the system via databases and docs; auto-generates orientation files such as product and architecture.
* **Checkpoint & PBT:** Saves code state for rollback; AI creates and runs tests to verify requirements.
* **Kiro CLI:** Use AI in the terminal with natural language; supports custom agents (DevOps, DB, etc.).
* **Kiro Power:** Loads tools only when needed → less lag, fewer AI errors, toward an open ecosystem.
* **Autonomous Agent:** AI plans, designs, and codes from descriptions; can learn from feedback.
* **Team Governance & pricing:** Team management and permissions; credit-based billing with 50 free credits per month.

2. **Create admin group and admin user — Module 01-Lab01-03** (https://000002.awsstudygroup.com/)

![IAM User Group created successfully](/images/1-Worklog/1.1-Week1/08-iam-user-group.jpeg)

![Admin User created successfully](/images/1-Worklog/1.1-Week1/09-admin-user-created.jpeg)

![Successful sign-in as User_Admin](/images/1-Worklog/1.1-Week1/10-admin-user-login.png)


