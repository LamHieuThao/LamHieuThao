---
title: "Week 2 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.2. </b> "
---

### Week 2 Objectives:

* Explore the main networking services in AWS.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Amazon Virtual Private Cloud (VPC) <br>&emsp; + VPC – subnet <br>&emsp; + VPC – Route Table <br>&emsp; + VPC – Elastic Network Interface <br>&emsp; + VPC – Elastic IP address <br>&emsp; + VPC – Endpoint <br>&emsp; + VPC - Internet Gateway <br>&emsp; + VPC – NAT Gateway <br>&emsp; + VPC – Security Group <br>&emsp; + VPC - Network Access Control List <br>&emsp; + VPC - Flow Logs | 27/04/2026 | 27/04/2026 | <https://000003.awsstudygroup.com/> <br> <https://youtu.be/O9Ac_vGHquM?si=7p-6vhNNY4-RR4dF> |
| 3 | - VPC Peering & Transit Getway <br> - VPN & Dircet Connect | 28/04/2026 | 28/04/2026 | <https://000003.awsstudygroup.com/> <br> <https://youtu.be/O9Ac_vGHquM?si=7p-6vhNNY4-RR4dF> |
| 4 | - Elastic Load Balancing | 29/04/2026 | 29/04/2026 | |
| 5 | - Hands-on practice | 30/04/2026 | 30/04/2026 | Introduction :: WORK WITH AMAZON SYSTEM MANAGER - SESSION MANAGER |
| 6 | - Hands-on practice | 01/05/2026 | 01/05/2026 | Introduction :: Start with Amazon VPC and AWS VPN Site-to-Site. |

### Week 2 Achievements:

#### **Monday**

**1. Amazon Virtual Private Cloud (VPC)**

* **Overview:** A core service that creates a logically isolated private virtual network. It covers how to configure a VPC, create Subnets, Route Tables, Internet Gateways, NAT Gateways, and associated firewall services.
* **Concept:** A service that provides a private virtual network environment that is fully logically isolated from other networks on the AWS cloud platform.
* It allows you to launch AWS resources into a virtual network that you define. For example, you can choose a virtual network with an IP range of 10.10.0.0/16.
* A VPC resides within a single Region. When creating a VPC, you must declare an IPv4 CIDR block (required) and IPv6 (optional).
* The current VPC limit is 5 VPCs per AWS Region per AWS Account.
* The main purpose of using a VPC is typically to separate environments (Production / Dev / Test / Staging).
* **Note:** If you want resources to be completely isolated (users cannot see a specific resource), you need to separate them across multiple AWS accounts; multiple VPCs alone cannot solve this problem.

**a) VPC – subnet:** Amazon VPC allows you to create multiple virtual networks and divide them into subnets.

* **Characteristics:** A VPC Subnet resides within a specific Availability Zone. Once a Subnet is created, you assign a CIDR block for that subnet, which is a subset of the VPC CIDR block.
* **Reserved IP rule:** In each Subnet, AWS reserves 5 IP addresses. For example, if a Subnet has a CIDR of 10.10.1.0/24:
    * Network address (10.10.1.0)
    * Broadcast address (10.10.1.255)
    * Address for the router (10.10.1.1)
    * Address for DNS (10.10.1.2)
    * Address reserved for future use (10.10.1.3)
* **Public Subnet vs Private Subnet:** They are essentially the same. However, by convention, if a Subnet is configured so that instances inside it can reach the Internet, it is called a Public Subnet. Otherwise, it is a Private Subnet.

**b) VPC – Route Table:** A collection of routes used to determine network traffic paths.

* When you create a VPC, AWS creates a Default Route Table (Main). The Default Route Table cannot be deleted and contains only one route that allows all Subnets within the VPC to communicate with each other.
* When you create a VPC, a Default Route Table (Main) is automatically created and cannot be deleted. It contains one default rule (Local) that allows all resources in every Subnet within the VPC to communicate with each other.
* Route tables are associated with Subnets.
* Depending on the Internet traffic path, you can create a Custom Route Table; however, the default route (VPC CIDR - Local) cannot be deleted.

**c) VPC – Elastic Network Interface (ENI):** A virtual network card, similar to a physical Network Interface Card (NIC) on a computer, which can be moved to other EC2 Instances.

* When you launch an EC2 instance, AWS automatically creates an ENI and attaches it to that instance. The Private IP address is assigned to this ENI rather than directly to the instance.
* **Characteristics:** When moved to a new instance, a virtual network card retains:
    * Private IP address
    * Elastic IP address
    * MAC address

**d) VPC – Elastic IP address (EIP) — Paid service:** A static public IPv4 address that can be associated with an Elastic Network Interface.

* This address does not change even when the instance is restarted.
* When not in use, you will be charged (avoid waste).

**e) VPC – Endpoint:** Allows resources within a VPC to connect to supported AWS services (via AWS PrivateLink over AWS's private network) without going through the Internet.

* There are 2 types of VPC Endpoint:
    * **Interface Endpoint:** Uses an Elastic Network Interface within the VPC along with a Private IP address to connect to a supported service. Simply put: use a virtual network card (ENI) within the VPC with a Private IP to communicate with the external service.
    * **Gateway Endpoint:** Uses a route table to route traffic to the endpoint of a supported service (S3 and DynamoDB). Simply put: it works based on Route Tables. Currently, it only supports connections to Amazon S3 and DynamoDB.

**Question:** How does a server reach the Internet?

**f) VPC - Internet Gateway:** A component of Amazon VPC that scales horizontally and allows EC2 Instances within a VPC to communicate with the Internet.

* Internet Gateway is managed by AWS; you do not need to configure autoscaling or high availability.
* **Requirements for a server to reach the Internet:**
    * The EC2 instance must have a Public IP address (e.g., an EIP) assigned to its ENI.
    * An Internet Gateway must be created and attached to the VPC.
    * A Custom Route Table must be associated with the Public Subnet.
    * In that Custom Route Table, add a route entry: Destination: 0.0.0.0/0 (all IP addresses) -> Target: the Internet Gateway ID.

**g) VPC – NAT Gateway:** Allows EC2 instances in a subnet to access the Internet or other AWS services. It only accepts outbound connections and does not accept inbound connections.

* In practice, for security, applications are often placed in Private Subnets. However, they still need one-way Internet access to download patches or call APIs (e.g., a gold price API) without allowing the Internet to initiate connections back in. In that case, you use a NAT Gateway.
* **NAT Gateway architecture:**
    * Create a NAT Gateway. Important note: the NAT Gateway must be placed in a Public Subnet (where Internet access is available).
    * Assign an Elastic IP address to the NAT Gateway.
    * Create a separate Custom Route Table and associate it with the Private Subnet.
    * In this Custom Route Table, add a route: Destination: 0.0.0.0/0 -> Target: NAT Gateway ID.
* **Traffic flow diagram:**

![Traffic flow diagram](/images/1-Worklog/1.2-Week2/01.png)

**h) VPC – Security Group (SG):** A stateful virtual firewall that controls inbound and outbound traffic to AWS resources.

* Security Group rules are restricted by protocol, source address, port, or another Security Group.
* Security Group rules only allow "allow" rules.
* Security Groups are applied to Elastic Network Interfaces.
* **Stateful behavior:** If you configure an Inbound rule (e.g., open Port 80 for web access), AWS automatically allows the corresponding Outbound traffic (the response back to the user) within the same session. You do not need to configure a separate Outbound rule.
* **How it works:**
    * Only supports "Allow" rules; there are no "Deny" rules.
    * By default, when a new Security Group is created: all Inbound traffic is blocked, and all Outbound traffic is allowed.

![Security Group operation diagram](/images/1-Worklog/1.2-Week2/02.png)

* **Source configuration:** The source does not have to be a fixed IP; you can specify another Security Group as the source.

**i) VPC - Network Access Control List (NACL):** A stateless virtual firewall that controls inbound and outbound traffic to AWS resources. Because it is stateless, you must configure both directions explicitly. To configure correctly, you need to understand the port flow (which port traffic enters on and which port it exits on).

* NACLs are restricted by protocol, source address, and port.
* NACLs are applied to Amazon VPC Subnets.
* By default, a NACL allows all inbound and outbound traffic.
* **How to read rules:** Rules must be read from top to bottom; the first matching rule is applied.

![Rule table diagram](/images/1-Worklog/1.2-Week2/03.jpeg)

* **Stateless behavior:** When configuring, you must create explicit rules for both directions: Inbound and Outbound, based on the ports used by the application.
* **Operations:**
    * Supports both "Allow" and "Deny" rules.
    * Rules are numbered in order (e.g., Rule 100, 200...). The system evaluates them sequentially from top to bottom. The first matching rule is applied.
    * By default, when a VPC is created, the Network ACL has default rules that Allow All inbound and outbound traffic for easier initial setup.

![NACL operation diagram](/images/1-Worklog/1.2-Week2/04.jpeg)

* **Scope of impact:** Because NACLs are associated with Subnets, changing NACL configuration affects all instances within that Subnet (unlike Security Groups, which only affect instances with the associated ENI).

**j) VPC - Flow Logs:** A feature that allows you to capture information about IP traffic to and from network interfaces in your VPC.

* **Data destination:** Log files can be published to Amazon CloudWatch Logs or Amazon S3.
* VPC Flow Logs do not capture packet content.
* **Characteristics:** VPC Flow Logs only record packet headers (including: source IP, destination IP, port, protocol, send time, Allow or Reject, etc.). They do NOT record the content inside the packet.
* **Practical use:** Widely used in security to detect anomalous behavior, port scanning, or malware sending packets to a command-and-control server in the early morning hours.

#### **Tuesday**

**2. VPC Peering & Transit Getway**

* **Overview:** Methods for connecting multiple VPCs together. VPC Peering allows connecting 2 VPCs; Transit Gateway connects a large number of VPCs easily and efficiently.

**a) VPC Peering:** A feature that connects two or more VPCs so that resources within those VPCs can communicate directly without going through the Internet, enhancing VPC security.

* VPC Peering requires a 1:1 connection between two member VPCs and does not support transitive routing.
* VPC Peering is not supported when the two VPCs have overlapping IP address spaces.
* **Key characteristics:**
    * Supports connections between VPCs in different Regions or different AWS Accounts.
    * Does NOT support Transitive Routing: If VPC A is peered with VPC B, and VPC B is peered with VPC C, A cannot reach C through B. A must create a separate Peering connection directly to C.
    * VPC Peering cannot be established if the CIDR blocks of the two VPCs overlap.
* **Practical configuration:** Setting up Peering alone is not enough for connectivity. You must configure the Route Table on both ends of the Subnets in both VPCs to direct traffic. (You can configure the Destination to point to a specific Subnet or a specific instance IP).
* **Limitation:** If an organization has dozens or thousands of VPCs, using VPC Peering creates an extremely complex "spider web" of connections (e.g., 30 VPCs would require 435 Peering connections).

**b) Transit Gateway:**

* Transit Gateway is used to connect VPCs and on-premises networks through a central hub. This simplifies the network and eliminates complex routing relationships.
* A Transit Gateway Attachment is used to attach the subnets of each VPC that needs connectivity to a provisioned TGW. Transit Gateway Attachments operate at the Availability Zone (AZ) level.
* Within a VPC, when a subnet in an AZ has a Transit Gateway Attachment to a TGW, other subnets in the same AZ can also connect to that TGW.
* **How it works:**
    * Instead of VPCs connecting directly to each other, all VPCs only need to connect to a single central Transit Gateway hub.
    * Use Transit Gateway Attachments: to connect a VPC to a Transit Gateway, you create Attachments associated with Subnets.
* **Scale note:** Attachments operate at the AZ level. Each AZ only needs one Transit Gateway Attachment (even if there are multiple Subnets in that AZ). If a VPC spans 3 AZs, you will need 3 Attachments.

![Transit Gateway operation diagram](/images/1-Worklog/1.2-Week2/05.png)

* **Routing configuration:** Similar to VPC Peering, you must configure Route Tables in the VPC to direct necessary traffic to the Transit Gateway, and the Transit Gateway itself has its own Route Table to distribute traffic to the appropriate destination VPC.

**3. VPN & Dircet Connect**

* **Overview:** Solutions for securely and reliably connecting the AWS environment to on-premises data centers.

**a) Site-to-Site VPN:** Used in hybrid architectures to establish a persistent connection between traditional on-premises data centers and AWS VPC environments. Setting up the connection requires two endpoints on the AWS side and the customer side:

* **Virtual Private Gateway:** Fully managed by AWS (with 2 endpoints across 2 AZs).
* **Customer Gateway:** The customer-side endpoint, which can be a hardware device or a software appliance.
* <https://docs.aws.amazon.com/vpn/latest/s2svpn/your-cgw.html> — this link provides a list of devices/software appliances supported by AWS and guidance for setting up Site-to-Site VPN from the customer environment to AWS.

**b) Client-to-Site VPN:** Allows a host to access resources within a VPC using internal IPs without connecting over the public Internet.

* **Recommendation:**
    * Use Client-to-Site VPN solutions from AWS Marketplace (third-party).
    * AWS does offer a Client-to-Site VPN service, but the cost is relatively high and billed hourly, which is not very practical at this time.

**c) AWS Direct Connect:** A service that allows you to create a dedicated connection from on-premises data centers to AWS.

* It is a dedicated connection at a low layer (Layer 2/3) for customers.
* Latency in Vietnam for Direct Connect is approximately 20 ms – 30 ms (when connecting from Ho Chi Minh City; from Hanoi it may be slightly higher).
* AWS Direct Connect in Vietnam currently goes through AWS Direct Connect partners (e.g., Viettel, FPT, CMC) and operates as Hosted Connections (bandwidth in Vietnam currently supports up to approximately 2 Gbps). A direct connection to AWS would be a Dedicated Connection (higher bandwidth allowed, but not currently available in Vietnam).
* Direct Connect bandwidth can be scaled up or down as needed. During initial large-scale migration, bandwidth can be increased. After replication is complete, bandwidth can be reduced to save costs.
* In practice, Cloud Engineers rarely configure Direct Connect themselves; most work is done through partner teams for setup and configuration — we mainly use the connection.
* **Important note:** Direct Connect does not encrypt data. Therefore, after establishing a Direct Connect connection, you still need to configure a Site-to-Site VPN over Direct Connect to encrypt the data.

#### **Wednesday**

**4. Elastic Load Balancing**

* **Overview:** A service that distributes traffic (load balancing) across multiple target servers, ensuring fault tolerance, performance, and scalability.
* **Concept:** Elastic Load Balancing (ELB) is a managed load balancing service from AWS that distributes traffic across multiple EC2 Instances or Containers.
* **Characteristics:**
    * Uses HTTP, HTTPS, TCP, and SSL (secure TCP) protocols.
    * Can be placed in Public or Private subnets: In practice (best practice), the Load Balancer is placed in a Public Subnet to receive user requests, then the Load Balancer connects to EC2 instances in Private Subnets.
    * Each ELB is assigned a DNS name and is accessed only through DNS. The exception is Network Load Balancer (NLB), which supports static IP assignment.
    * **Health Check:** ELB has a health check feature to verify whether backend Instances are still "healthy." Traffic is not sent to Instances that fail the health check.
* **There are 4 types in total:**
    * **Application Load Balancer:** A managed load balancing service from AWS that operates at Layer 7 (Application layer in the OSI model).
        * Primary protocols: HTTP, HTTPS.
        * Supports Path-based routing: requests can be routed based on URL path. For example: URL /mobile routes to a target group with mobile servers; URL /desktop routes to a target group for desktop servers.
        * Allows routing traffic to targets outside the VPC (using IP addresses), EC2, serverless functions such as Lambda, and Containers (ECS, EKS).
    * **Network Load Balancer:** A managed load balancing service from AWS that operates at Layer 4. Automatically auto-scales when traffic increases.
        * Protocols: TCP, TLS.
        * Supports static IP assignment.
        * Offers the highest performance among Load Balancer types, capable of handling millions of requests per second (extreme performance).
        * Allows routing traffic to targets outside the VPC (IP address), EC2, Containers (ECS, EKS). (Note: does not support Lambda and does not support Path-based routing like ALB).
    * **Classic Load Balancer:** A legacy load balancing service that operates at both Layer 4 and Layer 7.
        * Protocols: HTTP, HTTPS, TCP, TLS.
        * Higher cost than ALB and NLB; currently rarely used and gradually being phased out.
        * Only allows routing traffic to EC2 instances.
    * **Gateway Load Balancer:** Operates at Layer 3, commonly used in security-related architectures. GWLB listens to all IP packets and forwards them to a designated target group.
        * Uses the GENEVE protocol on port 6081.
        * Allows routing traffic to AWS-supported virtual appliances (such as Next Generation Firewalls from third-party security vendors to inspect packet content for safety).
        * Here is the link to the list of AWS-supported vendors: <https://aws.amazon.com/vi/elasticloadbalancing/partners/>

* This is the architecture you will commonly see when using Gateway Load Balancer.

![Gateway Load Balancer architecture diagram](/images/1-Worklog/1.2-Week2/06.jpeg)

**a) Sticky session (session affinity):**

* A feature that binds connections to a specific target. This ensures that requests from a user within a session are sent to the same target. Sticky sessions are necessary when application servers store user session state locally. If a request is routed to a different server, the user loses session state (e.g., being logged out).
    * Works on: Network Load Balancer, Application Load Balancer, Classic Load Balancer.
* ELB provides access log storage; you can use access logs to analyze traffic and troubleshoot. Access logs are stored in Amazon S3 (Simple Storage Service).
* **Access Logs feature:**
    * ELB provides access log storage.
    * Used to analyze traffic and troubleshoot issues.
    * Access logs are stored in Amazon S3 (Simple Storage Service).

#### **Thursday and Friday**

**Lab03 _ Module 02-Lab03:** ( Amazon VPC and AWS Site-to-Site VPN Workshop :: Start with Amazon VPC and AWS VPN Site-to-Site. )

![VPC created successfully](/images/1-Worklog/1.2-Week2/07.png)

![Subnet created successfully](/images/1-Worklog/1.2-Week2/08.png)

![Internet Gateway created successfully](/images/1-Worklog/1.2-Week2/09.jpeg)

![Route table created successfully](/images/1-Worklog/1.2-Week2/10.png)

![Security Group created successfully (Public)](/images/1-Worklog/1.2-Week2/11.jpeg)

![Security Group created successfully (Private)](/images/1-Worklog/1.2-Week2/12.jpeg)

![EC2 created successfully](/images/1-Worklog/1.2-Week2/13.png)

![Elastic IP created successfully](/images/1-Worklog/1.2-Week2/14.png)

![NAT Gateway created successfully](/images/1-Worklog/1.2-Week2/15.jpeg)

![Security Group for EIC Endpoint created successfully](/images/1-Worklog/1.2-Week2/16.jpeg)

![EC2 Endpoint created successfully](/images/1-Worklog/1.2-Week2/17.jpeg)

**Lab03 _ Module 02-Lab20** ( Set up AWS Transit Gateway :: SET UP AWS TRANSIT GATEWAY )

![Key Pairs created successfully](/images/1-Worklog/1.2-Week2/18.png)

![CloudFormation created successfully](/images/1-Worklog/1.2-Week2/19.png)

![Transit Gateway created successfully](/images/1-Worklog/1.2-Week2/20.jpeg)

![Transit Gateway Attachments created successfully](/images/1-Worklog/1.2-Week2/21.jpeg)

![EC2 connection successful](/images/1-Worklog/1.2-Week2/22.png)

![Transit Gateway Route Tables created successfully](/images/1-Worklog/1.2-Week2/23.png)

![Association successful](/images/1-Worklog/1.2-Week2/24.jpeg)

![Association successful](/images/1-Worklog/1.2-Week2/25.jpeg)
