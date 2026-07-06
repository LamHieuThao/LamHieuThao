---
title: "Blog 2"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 3.2. </b> "
---

# [SECURITY/Web3] Building secure, verifiable blockchain key management on AWS Nitro Enclaves at Turnkey

### Topic Concept

- AWS Nitro Enclaves is AWS's hardware-based virtualization technology that enables the creation of fully isolated compute partitions (Enclaves) to protect and process highly sensitive data. When applied to Web3, Turnkey's Enclave-Native Key Management architecture moves all core tasks such as key initialization, digital signing, and policy enforcement inside this isolated environment. This solution transforms the key management system from a "black box" (requiring blind trust) into a transparent model that can be cryptographically verified and is absolutely protected against memory extraction attacks.

### Key Points to Understand

- **Challenges in traditional architecture:** The conventional transaction signing process always involves a trade-off between security and operational performance. Building infrastructure in-house is costly and carries high compliance risks; entrusting third parties (Custodians) reduces direct control. Meanwhile, conventional software infrastructure risks exposing raw keys through memory dumps or log files when the system is compromised.
- **Absolute hardware isolation mechanism:** The enclave environment has no persistent storage, no interactive access support (no SSH), and no Internet connectivity. Communication data must go through the internal virtual VSOCK channel. Configuration keys are only decrypted in RAM at signing time and are immediately deleted, making them inaccessible to both Turnkey administrators and AWS.
- **HD Wallet standard initialization and storage process:** The key management system is derived according to a hierarchical wallet model. The root data chain (Seed) is generated from the secure random number generator of the Nitro Security Module (NSM) hardware, then symmetrically encrypted via the Quorum Key before being stored in the database. When signing transactions, the ciphertext is loaded into the enclave, temporarily decrypted in RAM for signing, then immediately erased, never written to disk.
- **State and data flow separation architecture:** The system is divided into two distinct partitions to optimize security:
  - **Outside (AWS Cloud Infrastructure - Not absolutely secure):** API Gateway receives requests, EC2 servers (Coordinator) handle orchestration. State data and encrypted root keys reside in Aurora Database. Auxiliary components (Async Queue, Redis, Updater, Heartbeat, Notifier/Webhook Targets) only perform synchronization and notification tasks, completely unaware of what the raw keys are.
  - **Inside (AWS Nitro Enclave - Absolutely secure):** Sensitive commands are transferred to the Enclave via gRPC/VSOCK and processed in a closed loop through 5 steps: (1) TLS Fetcher establishes a secure network connection; (2) Parser extracts data; (3) Policy Engine checks rules (limits, blocklists); (4) Notarizer signs valid certifications; (5) Signer decrypts keys in RAM, digitally signs transactions, and wipes all traces.
- **Mathematical remote verification mechanism (Verifiable Model):** Instead of absolute trust, the system allows verification through Remote Attestation (AWS signs cryptographic documents with hardware to ensure execution code is not tampered with) and Reproducible Builds (running on minimal QuorumOS, allowing independent parties to recompile source code from scratch to verify integrity).

### Practical Applications

- **Embedded Wallets:** Enables direct integration of non-custodial wallets into decentralized applications with enterprise-grade security standards.
- **AI Agent Transactions:** Supports artificial intelligence agents (AI Agents) to safely execute automated on-chain transactions according to pre-established policies without exposing configuration keys.

### Summary

Turnkey's solution leverages AWS Nitro Enclaves to establish a closed key processing workflow in RAM that automatically releases memory after use. The complete separation between state storage (State) and hardware-isolated execution environment (Execution) helps protect digital assets even when virtual server infrastructure is compromised. At the same time, thanks to remote attestation and source code reproducibility, the system allows users to verify the integrity and transparency of the entire cryptographic process.

### Images

![Building secure blockchain key management on AWS Nitro Enclaves at Turnkey](/images/3-BlogsPosted/3.2-Blog2/01.jpeg)

### Links

* Original article link: [Building secure, verifiable blockchain key management on AWS Nitro Enclaves at Turnkey | AWS Web3 Blog](https://aws.amazon.com/blogs/web3/building-secure-verifiable-blockchain-key-management-on-aws-nitro-enclaves-at-turnkey/)
* Updated article on Facebook group: [AWS Study Group VN | **[SECURITY/Web3] Building secure, verifiable blockchain key management on AWS Nitro Enclaves at Turnkey** | Facebook](https://www.facebook.com/groups/awsstudygroupfcj)
