---
title: "Week 11 Worklog"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 1.11. </b> "
---


### Week 11 Goals:

- Create project diagram on draw.io
- Describe the project

### Summary of tasks completed during the week:

| Day | Task | Start Date | End Date | Source |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ----------------------------------------- |
| 2, 3, 4 & 5 | - Create project diagram on draw.io | 29/06/2026 | 07/02/2026 | |
| 6 | - Make revisions after Admin feedback <br> - Project description | 03/07/2026 | 03/02/2026 | |

### Day 2 -> Day 6:

- Create "Cloud Computing Architecture on AWS Platform" diagram on Draw.io
![AWS Architecture Diagram](/images/1-Worklog/1.11-Week11/01-aws-architecture.png)
### Project Description:

- Project Name: GEN AI
- Description: A project that enables users with no prior knowledge of computer networks or attack/defense to understand clearly by simply entering one prompt.

#### Phase 1: Architecture Initialization (Provisioning & AI Generation)

The process begins when user access traffic is routed and DNS-resolved to the web application interface (Frontend). Here, users provide an input prompt requesting a basic network diagram. This request is packaged into API calls, passes through firewall layers and identity-verifying routers, and is then forwarded to a serverless compute environment. The central logic processor communicates with a Large Language Model (LLM) to analyze the semantics and, from there, generates a standard network architecture in JSON format and returns it to be visually rendered on the user's Drag-Drop interface.

#### Phase 2: Refinement and Configuration Validation (Modification & Validation)

Based on the AI-proposed architecture, users have full control to refine it by adding, editing, or removing network devices (nodes such as IPS, IDS, Firewall) or readjusting connection flows (edges) from the toolbar. As soon as the save operation is executed, the latest state of the network diagram (network topology) is pushed to the backend system. Here, AI acts as a configuration validator, automatically reviewing the entire diagram to detect irregularities (misconfigurations) or violations of secure network design principles. If risks are found, the system returns detailed warnings together with remediation recommendations directly on the interface for user awareness.

#### Phase 3: Asynchronous Attack Simulation and Defense Optimization (Async Attack Simulation & Defensive Remediation)

This is the heavy-workload processing subsystem designed with an asynchronous architecture. When the "Scan Attack" feature is activated, AI reviews the diagram to extract a list of feasible attack vectors. The user selects a scenario, and that command is immediately pushed into a message queue for background orchestration, completely decoupled from Frontend operations. The system automatically simulates each step of the attack, calculates damage, and returns a result report. Based on the event logs of that attack, AI continues to propose mitigation strategies. Users can update these defensive devices into the diagram and re-test the original attack scenario, allowing visual verification of the effectiveness of the applied security measures.

#### Phase 4: Observability and Notification (Observability & Notification)

Throughout the system's lifecycle, all versions of network diagrams and risk analysis reports are maintained in persistence via databases and secure object storage. When background simulation chains complete or when the system detects critical vulnerabilities, the event-driven mechanism automatically triggers a messaging service to push real-time alerts to user devices. At the same time, all communication behavior between microservices in the system is bound by the least privilege principle and measured, centrally logged to support performance monitoring.

### Service Functions:

- **Amazon Route 53**: Acts as the Domain Name System (DNS), responsible for routing access traffic from user browsers to content delivery endpoints.
- **Amazon CloudFront**: Functions as a Content Delivery Network (CDN), caching interface resources at edge locations to optimize latency for static content delivery.
- **AWS WAF (Web Application Firewall)**: Acts as an Application Layer firewall, enforcing security rules to detect and block common web attacks such as DDoS, SQL Injection, and XSS.
- **Amazon S3 (Frontend Bucket)**: Object Storage service configured as Static Website Hosting, used to store the entire Frontend source code (HTML, CSS, JS) of the network diagram drag-and-drop tool.
- **Amazon API Gateway**: Central entry point for all API (RESTful API) communication, responsible for receiving, routing, and rate limiting request streams from client to server.
- **Amazon Cognito**: Handles Identity and Access Management (IAM) at the end-user level, responsible for identity authentication and issuing secure JSON Web Tokens (JWT).
- **AWS Lambda (API Handlers)**: Serverless Compute environment, responsible for executing all business logic in the system, from calling external APIs and processing data streams to communicating with databases.
- **Google Gemini API**: Artificial Intelligence (LLM) platform, acting as the core "brain" to analyze text prompts, generate topology diagrams, validate network integrity, and create attack/defense simulation scenarios.
- **Amazon SQS (Simple Queue Service)**: Message Queuing service, acting as a buffer to decouple tasks. This service is extremely important for retaining "Scan Attack" commands and preventing system bottlenecks during long-running simulations.
- **AWS Step Functions**: Workflow Orchestration service, responsible for state machine management to coordinate and control the execution order of Lambda functions in the attack kill chain simulation.
- **Amazon DynamoDB**: NoSQL database with millisecond latency, specialized for storing and continuously reading/writing the current state of network topology (Topology JSON) records while users edit.
- **Amazon S3 (Results Bucket)**: Secure dedicated object storage, used to permanently store vulnerability scan result reports and large-scale structure data in PDF or JSON format.
- **Amazon SNS (Simple Notification Service)**: Pub/Sub messaging service, responsible for distributing notifications upon completion of background simulations or urgent alerts via Email/SMS to administrators.
- **AWS IAM (Identity and Access Management)**: Core access control policy service, applying the Least Privilege Principle to ensure cloud services interact only within their authorized functions.
- **Amazon CloudWatch**: Observability service, responsible for resource monitoring, collecting performance metrics, and centrally storing activity logs for debugging and system tracing.


