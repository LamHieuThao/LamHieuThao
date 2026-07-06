---
title: "Blog 1"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---

# [SECURITY] SOFTWARE SUPPLY CHAIN SECURITY ACCORDING TO AWS WELL-ARCHITECTED

### Topic Concept

- Software Supply Chain Security within the AWS Well-Architected framework is a set of design principles and technical practices aimed at protecting the entire software lifecycle — from managing third-party dependency packages, protecting developer identities, to verifying source code integrity before deployment. This model helps organizations build a defense-in-depth system, ensuring that even if one link or one credential is compromised, multi-layered control mechanisms will prevent the incident from spreading across the entire system.

### Key Points to Understand

- **Challenges of modern supply chain attacks:** Attacks targeting public registries such as the npm Registry (for example: Shai-Hulud malware, Chalk/Debug, or token abuse) are becoming increasingly sophisticated and occurring at large scale. Developers need mechanisms to prevent account takeover when credentials are stolen; meanwhile, package consumers need defensive layers to detect, block the deployment of malicious packages, and minimize damage.
- **Mitigating credential exposure risks:** To limit risk, systems must use temporary credentials by federating users from a central identity provider (IdP) into AWS and applying IAM roles. At the same time, the principle of least privilege must be strictly enforced, with regular auditing and key rotation. If interacting with third-party services that do not support temporary credentials, information must be stored centrally in AWS Secrets Manager with automatic rotation and dedicated audit logging.
- **Defense in Depth strategy:** Even when least privilege is applied, a compromised account can still distribute malicious source packages. Therefore, the system needs to establish strategic barriers such as: enabling multi-factor authentication (MFA), separating different IAM roles for each sensitive workload, and selectively applying approval workflows to balance deployment speed and security.
- **Artifact Signing and SBOM Management:** All software artifacts must be digitally signed to prove provenance. This, combined with centralized storage and creating Software Bills of Materials (SBOM), creates a layer of protection against forgery. At deployment time, admission controllers such as Kyverno on Amazon EKS or lifecycle hooks on Amazon ECS will verify and validate digital signatures before allowing any source code to run in the container cluster.
- **Centralized Dependency Management:** By centralizing the management of packages and dependency libraries, organizations can proactively verify and approve third-party libraries before they are embedded into applications. This mechanism allows security teams to quickly audit and scan the entire system to find compromised packages when incidents occur. For open-source packages (such as npm), checking provenance attestations before use is a low-cost signal that helps ensure integrity.
- **Continuous Monitoring and Centralized Log Analysis:** The system requires enabling logging for both applications and services, then aggregating to a central analysis hub to detect abnormal signing behaviors (such as signing from unfamiliar IPs, unusual time windows). AWS provides a powerful coordinated toolkit: Amazon GuardDuty continuously monitors malicious behavior and abnormal API calls; findings are centralized in AWS Security Hub; and AWS Config is responsible for enforcing and monitoring standard security configurations.

### Practical Applications

- **Secure CI/CD infrastructure:** Developers can enable provenance verification by running the `npm publish --provenance` command directly from supported CI/CD environments such as GitHub Actions or AWS CodePipeline to demonstrate source code transparency.
- **Automated container verification in Kubernetes:** Deploy Kyverno policies on Amazon EKS to automatically block container images that have not passed security scanning or lack valid signatures from the central Build system, preventing malware from entering the production runtime environment.

### SUMMARY

Software supply chain security on the Cloud is not limited to writing secure code; it is a comprehensive strategy: building multi-layered architecture (defense in depth), eliminating long-term privileges, and maintaining absolute control and monitoring over every artifact before it enters the operational system.

### Images

![Software supply chain security according to AWS Well-Architected](/images/3-BlogsPosted/3.1-Blog1/01.jpeg)

![Defense in depth for software supply chain](/images/3-BlogsPosted/3.1-Blog1/02.jpeg)

![Monitoring and controlling artifacts](/images/3-BlogsPosted/3.1-Blog1/03.jpeg)

### Links

* Original article link: [Well-architected best practices for software supply chain security | AWS Security Blog](https://aws.amazon.com/blogs/security/well-architected-best-practices-for-software-supply-chain-security/)
* Updated article on Facebook group: [AWS Study Group VN | # **[SECURITY] SOFTWARE SUPPLY CHAIN SECURITY ACCORDING TO AWS WELL-ARCHITECTED** | Facebook](https://www.facebook.com/groups/awsstudygroupfcj)
