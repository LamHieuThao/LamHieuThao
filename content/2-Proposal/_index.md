---
title: "Proposal"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 2. </b> "
---


# Cloud Nexus  
  

## 1. Project Overview

**Cloud Nexus** is a network security simulation and analysis platform (Threat Modeling Platform) built for cybersecurity professionals and infrastructure architects. The system lets users design network diagrams visually, then uses AI (Google Gemini) to automatically detect vulnerabilities, simulate attack paths, and recommend defensive measures.

| Component | Technology |
|-----------|-----------|
| Frontend | React + Vite + ReactFlow + Tailwind CSS |
| Backend | FastAPI on AWS Lambda + API Gateway |
| AI | Google Gemini API (Gemini 2.0 Flash) |
| Infrastructure | AWS CDK (TypeScript), Python 3.12 ARM64 |
| AWS Services | S3, API Gateway, Lambda, Cognito, DynamoDB, SQS, SNS, Step Functions, Secrets Manager |

---

## 2. Objectives

### General Objective
Build a serverless platform on AWS that automates the network security assessment workflow—from drawing topology to vulnerability detection and attack simulation.

### Specific Objectives
- **Output:** REST API endpoints + Web Dashboard (React)
- **AI Integration:** Google Gemini generates topology, analyzes vulnerabilities, and simulates attacks
- **Alert:** SNS notification when a critical attack is detected
- **Serverless:** Entire backend runs on Lambda + API Gateway
- **Infra as Code:** AWS CDK — deploy and destroy with a single command

### Success Criteria
1. Web dashboard loads from S3 static hosting
2. API Gateway returns `{"status":"ok"}` at `/api/health`
3. Lambda successfully calls Google Gemini and returns valid topology JSON
4. Entire infrastructure can be deployed with `cdk deploy` and removed with `cdk destroy`

---

## 3. Problems to Solve

| Problem | Solution |
|---------|----------|
| Manual network vulnerability detection is time-consuming | AI automatically scans topology |
| Attack paths are difficult to visualize | Visual simulation on ReactFlow |
| Test environment setup is complex | Serverless on AWS with no server management |
| No tool for evaluating defenses | Compare attack paths before and after adding defenses |

### Target Users
- Security Analysts
- Cloud Architects
- Cybersecurity Students

---

## 4. Solution Architecture

![Cloud Nexus Solution Architecture](/images/2-Proposal/architecture.png?width=100pc)

---

## 5. Timeline (Jun 1 → Jul 4)

| Phase | Scope | Period |
|-------|-------|--------|
| **Kickoff** | Environment setup, IAM policy, AWS CLI | 06/01 → 06/04 |
| **Frontend** | Build UI with React + ReactFlow | 06/05 → 06/09 |
| **Backend** | FastAPI + AI service + Gemini integration | 06/10 → 06/14 |
| **Infrastructure** | AWS CDK stacks (Simulation, API, Frontend, Auth) | 06/15 → 06/19 |
| **Deployment** | Build Lambda Layer, deploy stacks | 06/20 → 06/23 |
| **Integration** | Connect frontend and backend, configure API key | 06/24 → 06/27 |
| **Testing** | End-to-end system testing and bug fixes | 06/28 → 06/30 |
| **Finalization** | Report, documentation, resource cleanup | 07/01 → 07/04 |

---

## 6. Budget

### Estimated AWS Costs (Monthly)

| Service | Cost |
|---------|------|
| S3 Static Hosting | ~$0.01 |
| API Gateway | $0 (free tier) |
| Lambda | $0 (free tier) |
| Cognito | $0 (free tier) |
| DynamoDB | $0 (free tier) |
| SQS | $0 (free tier) |
| SNS | $0 (free tier) |
| Step Functions | $0 (free tier) |
| Secrets Manager | ~$0.40 |
| **Total** | **~$0.41/month** |

### Google Gemini API Costs
- Gemini 2.0 Flash: free tier with low rate limits
- Costs apply only when usage exceeds the free tier

### Summary
The project fits entirely within the AWS Free Tier and Google Gemini Free Tier, with virtually no operating costs.

---

## 7. Risks

| Risk | Description | Level | Mitigation |
|------|-------------|-------|------------|
| **API Key Exposure** | Google API key committed to Git | High | Secrets Manager + .gitignore |
| **Unexpected Costs** | Lambda invoked continuously or abused | Medium | CloudWatch Alarm, budget alert |
| **Invalid AI Response** | Gemini returns invalid JSON | Medium | Retry logic (2 attempts), fallback |
| **Lambda Timeout** | AI response too slow (>30s) | Low | Increase timeout, use async SQS |
| **CDK Deploy Failure** | AWS CDK version mismatch | Low | Pin version, verify before deploy |
| **CORS** | Browser blocks cross-origin requests | Low | CORS middleware pre-configured |
| **Data Loss** | DynamoDB accidentally deleted | Medium | Backup, Point-in-Time Recovery |

---

*Project Proposal — Cloud Nexus*
