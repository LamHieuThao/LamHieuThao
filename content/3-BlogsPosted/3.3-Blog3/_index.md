---
title: "Blog 3"
date: 2024-01-01
weight: 3
chapter: false
pre: " <b> 3.3. </b> "
---

# [How AWS DevOps Agent uses multi-agent reasoning to find root causes]

### Topic Concept

- AWS DevOps Agent is an autonomous agent designed to automate operations and incident handling in distributed systems. The core of this technology is the Multi-Agent Reasoning architecture. Instead of blindly searching through telemetry or making assumptions based on confirmation bias, the system decomposes operational activities into multiple specialized agents. These agents work in parallel to simultaneously generate multiple competing hypotheses, proactively validating with both supporting and refuting evidence, thereby converging accurately on the root cause of incidents.

### Key Points to Understand

- **Challenges of traditional investigation methods:** When alerts occur, on-call engineers often fall into the trap of "confirmation bias" — forming hypotheses based on initial experience, finding one piece of supporting evidence, then stopping, missing the actual root cause buried in another service. Modern systems do not lack monitoring data (telemetry) but lack reasoning capability to process that data objectively at scale.
- **Topology Architecture Map — The foundation of all operations:** Before investigation, the system builds a "Learned Topology" (dynamic architecture map) through 4 sources: AWS CloudFormation/CDK stack analysis, tag-based discovery via AWS Resource Explorer, runtime behavior charting from CloudWatch Application Signals (or Datadog, Dynatrace), and CI/CD pipeline integration (GitHub Actions, GitLab CI/CD). This map helps agents understand dependency relationships, communication flows, and code change history to scope the blast radius instead of blind searching. All these activities are safely isolated in separate Agent Spaces.
- **Triage Phase — Optimized for speed:** When receiving signals from CloudWatch, PagerDuty, ServiceNow, or Grafana, Triage activates immediately. The core mechanism here is automatically grouping and correlating alerts related to the same event. This significantly reduces noise for engineers, preventing a single incident from creating numerous fragmented investigation tasks. Operators retain full control to unlink alerts if the system groups them incorrectly.
- **Investigation Reasoning Engine — The processing center:** The engine's deep analysis process runs in a closed loop through strict steps:
  - **Context and data collection:** Identify affected resources, scan the topology graph, pull metric indicators (compared against standard baselines), logs (CloudWatch, Splunk), and distributed traces.
  - **Parallel hypothesis generation:** The system proposes multiple reasons simultaneously (due to new deployment errors, metric anomalies, resource bottlenecks such as connection pool, CPU...).
  - **Evaluation and elimination:** For example, in a slow checkout application incident, the system checks 3 hypotheses simultaneously. It eliminates configuration errors (because only log level was changed), eliminates third-party payment gateway issues (because the gateway was detected as slow after the application had already slowed), and accurately validates the cause as database connection pool exhaustion (connection pool reached 94%) thanks to perfectly matching temporal data.
- **Closed data flow architecture (5-step Enclave):** To ensure absolute security, the processing flow inside the compute environment is divided into 5 subsystems:
  - **TLS Fetcher:** Establishes secure network connections from within.
  - **Parser:** Extracts and parses incident data.
  - **Policy Engine:** Verifies whether transactions/incidents violate preset rules.
  - **Notarizer:** Signs valid transaction/result certifications.
  - **Signer:** Processes and digitally signs, then wipes all temporary data in RAM.
- **Mitigation — Safety first:** Incident mitigation plans are automatically generated including: patching strategies, step-by-step procedures, system validation checks, success criteria, and rollback procedures. To ensure production environment safety, AWS DevOps Agent only has write permissions to create tickets/support cases and does not autonomously execute patch code; the decision to apply configuration or modification commands remains entirely with humans.
- **Prevention — Continuous improvement loop:** The system clusters historical incidents sharing the same core nature (despite different outward symptoms) to provide proactive recommendations. These recommendations include: filling monitoring blind spots, fine-tuning alerts, infrastructure optimization (autoscaling, right-sizing), and establishing control barriers (deployment gates, chaos engineering). Operators can accept or respond in natural language to train the agent to become smarter over time.

### Practical Applications

- **Embedded Wallets & System Keys:** Ensures tasks inspecting sensitive application partitions or cryptographic key infrastructure (such as Turnkey/Nitro Enclaves solutions) are monitored, recorded in immutable journals, and do not expose configuration when the system encounters errors.
- **AI Agent Transactions:** Supports safe monitoring, approval, and reasoning for AI agents performing automated on-chain or cloud infrastructure transactions. When an AI Agent encounters execution failures, DevOps Agent automatically steps in to analyze and find policy bottlenecks or connection errors.

### Summary

AWS DevOps Agent is changing how we operate systems. By delegating log review, architecture mapping, and evidence cross-referencing to AI, Backend and DevOps engineers can escape sleepless nights of manual debugging. You will enter the bug-fixing process with greater confidence, because every hypothesis has been validated with real data, along with a safe escape route.

### Images

![How AWS DevOps Agent uses multi-agent reasoning to find root causes](/images/3-BlogsPosted/3.3-Blog3/01.jpeg)

### Links

* Original article link: [How AWS DevOps Agent uses multi-agent reasoning to find root causes | AWS DevOps & Developer Productivity Blog](https://aws.amazon.com/blogs/devops/how-aws-devops-agent-uses-multi-agent-reasoning-to-find-root-causes/)
* Updated article on Facebook group: [AWS Study Group VN | **[How AWS DevOps Agent uses multi-agent reasoning to find root causes]** | Facebook](https://www.facebook.com/groups/awsstudygroupfcj)
