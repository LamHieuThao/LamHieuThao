---
title: "Week 5 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.5. </b> "
---

### Week 5 Objectives:

* AWS security services.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Security is Job Zero <br> - Shared Responsibility Model | 18/05/2026 | 18/05/2026 | Module 05-01 - Share Responsibility Model |
| 3 | - AWS Identity and Access Management <br>&emsp; + Root Account <br>&emsp; + IAM Policy <br>&emsp; + IAM Role | 19/05/2026 | 19/05/2026 | Module 05-02 - Amazon Identity and access management |
| 4 | - Amazon Cognito <br> - AWS Organization <br> - AWS Identity Center (SSO) <br> - Amazon Key Management Service (KMS) <br> - AWS Security Hub | 20/05/2026 | 20/05/2026 | Module 05-03 - Amazon Cognito <br> Module 05-04 - AWS Organization <br> Module 05-05 - AWS Identity Center <br> Module 05-06 - Amazon Key Management Service <br> Module 05-07 - AWS Security Hub |
| 5 | - Hands-on practice | 21/05/2026 | 21/05/2026 | Create IAM Group :: IAM ROLE & CONDITION |
| 6 | - Hands-on practice | 22/05/2026 | 22/05/2026 | |

### Week 5 Achievements:

#### **Monday**

* Learned the **Security is Job Zero** principle: security is always the top priority in AWS.
* Learned the **Shared Responsibility Model:**
    * AWS is responsible for securing the Cloud infrastructure.
    * Customers are responsible for configuration, data management, and access control.
* Understood that security responsibilities vary depending on the type of AWS service.

#### **Tuesday**

**A) Amazon Identity and access management**

**a) Root Account**

* Learned about the Root Account in AWS: this account has full access to all AWS services and resources, including managing billing information and account registration data.
* Understood security principles for the Root Account:
    * Create an IAM Administrator User for daily use.
    * Limit use of the Root User and secure login credentials.
    * Ensure the email and domain linked to the Root Account are maintained.
* Learned about IAM (Identity and Access Management) for managing access in AWS.
* Understood the IAM Principal concept including: Root User, IAM User, Federated User, IAM Role, AWS Services.
* Learned about IAM User:
    * Not a separate AWS account.
    * Can sign in with a password or Access Key/Secret Key.
    * By default, has no access to AWS resources.
    * Requires an IAM Policy to grant service usage permissions.
* Learned about IAM Group:
    * Used to manage multiple IAM Users more easily.
    * An IAM Group cannot be nested inside another Group.

**b) IAM Policy**

* Learned about IAM Policy for granting access in AWS, written in JSON format.
* Distinguished policy types:
    * AWS Managed Policy
    * Customer Managed Policy
    * Inline Policy
* Learned the 2 main types:
    * Identity-based Policy attached to IAM User/Group/Role.
    * Resource-based Policy attached directly to AWS resources.
* Understood IAM evaluation principles:
    * Explicit Deny always takes precedence over Allow.
* Practiced an example restricting Amazon S3 access:
    * Allow operations on a specific S3 Bucket.
    * Deny access to other AWS services using Explicit Deny.

**c) IAM Role**

* Learned about IAM Role: used to grant access to AWS resources through IAM Policy without fixed credentials.
* Learned the AssumeRole mechanism:
    * An IAM User or AWS Service can assume a Role to receive temporary permissions.
    * AWS STS provides temporary credentials when assuming a role.
    * When assuming a role, the user's current permissions are replaced by the Role's permissions.
* Learned about Trust Policy used to define who is allowed to assume an IAM Role.
* Understood practical applications of IAM Role:
    * Implement the principle of least privilege.
    * Support access across multiple AWS Accounts (Cross-account access).
* Learned how to use IAM Role for applications running on EC2:
    * Attach an IAM Role directly to EC2 instead of hardcoding Access Key/Secret Key.
    * AWS automatically provides and rotates temporary credentials to enhance security.

#### **Wednesday**

**B) Amazon Cognito**

* Learned about Amazon Cognito: an AWS-managed service for authentication, authorization, and user management for web and mobile applications. Users can sign in directly with a username and password or through a third party such as Facebook, Amazon, or Google.
* Learned the two main components of Cognito:
    * **User Pool:** manages user registration and sign-in.
    * **Identity Pool:** grants access to AWS services.
* Learned authentication methods:
    * Direct sign-in with username/password.
    * Federated sign-in via Google, Facebook, or other third-party services.
* Learned the workflow when combining User Pool and Identity Pool to authenticate users and authorize access to AWS resources securely.
    * **User Pool:**
        * A directory that stores and manages user information.
        * Provides sign-up and sign-in options for users to access the application.
    * **Identity Pool:**
        * Stores mappings between access to AWS services/resources and user information.

**C) AWS Organization**

* Learned about AWS Organizations – a service that helps centrally manage multiple AWS Accounts in an enterprise.
* Understood the organizational model including:
    * Management Account
    * Organization Unit (OU)
    * Member Account
* Learned about Consolidated Billing for centralized billing management across multiple AWS accounts.
* Learned about Service Control Policies (SCP):
    * Used to set maximum permission limits for IAM Users and IAM Roles.
    * Can be applied to Root, OU, or individual AWS Accounts.
    * Supports deny-based policies for strict security control.
* Understood the role of AWS Organizations in reducing blast radius during incidents and supporting large-scale AWS system management.

**D) AWS Identity Center (SSO)**

* Learned about AWS Identity Center (formerly AWS SSO) for centralized access management across multiple AWS Accounts and external applications.
* Learned about Identity Source for managing Users and Groups, usable directly on AWS or linked with Active Directory.
* Learned about Permission Sets for defining User/Group access to AWS Accounts through IAM Roles.
* Understood the authorization workflow:
    * Create Users and Groups
    * Create Permission Sets.
    * Assign access to each AWS Account.
* Learned about Single Sign-On (SSO), allowing users to access multiple AWS Accounts from a single login portal.

**E) Amazon Key Management Service (KMS)**

* Learned about Amazon KMS (Key Management Service) for creating and managing encryption keys on AWS for data encryption and decryption.
* Understood the role of KMS in protecting data with Encryption at Rest and the FIPS 140-2 security standard.
* Learned the two main key types:
    * CMK (Customer Master Key) used to manage and encrypt Data Keys.
    * Data Key used to directly encrypt data.
* Learned the encryption and decryption process through CMK and Data Key in AWS KMS.
* Understood the importance of Master Key access in protecting data from unauthorized access.

**F) AWS Security Hub**

* Learned about AWS Security Hub – a service that supports automated security checks for AWS resources and services.
* Understood how Security Hub works in checking configurations based on AWS Best Practices and security standards such as PCI DSS.
* Learned common check areas:
    * Firewall configuration
    * Data encryption with KMS
    * IAM authorization
    * MFA and CloudTrail
* Learned about Dashboard and Findings for assessing security posture, displaying Pass/Fail status and risk level for each resource.
* Understood the role of Security Hub in monitoring and improving security for AWS systems.

#### **Thursday & Friday**

Hands-on lab practice.

Lab link: <https://docs.google.com/document/d/1wZdmeSouU-_2RQX7embfRbY9oR2vWcrR/edit?usp=sharing&ouid=110146210370887604643&rtpof=true&sd=true>
