---
title: "Week 6 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.6. </b> "
---

### Week 6 Objectives:

* Database services on AWS.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Database Concepts | 25/05/2026 | 25/05/2026 | Module 06-01 - Database Concepts review - YouTube |
| 3 | - Amazon RDS & Amazon Aurora | 26/05/2026 | 26/05/2026 | Module 06-02 - Amazon RDS & Amazon Aurora - YouTube |
| 4 | - Redshift - Elasticache | 27/05/2026 | 27/05/2026 | (4998) Module 06-03 - Redshift - Elasticache - YouTube |
| 5 | - Hands-on practice | 28/05/2026 | 28/05/2026 | |
| 6 | - Hands-on practice | 29/05/2026 | 29/05/2026 | |

### Week 6 Achievements:

#### **Monday**

* Learned basic database concepts such as Database, Session, Primary Key, Foreign Key, Index, Partition, Buffer, and Database Log.
* Understood the role of Primary Key and Foreign Key in linking data between tables and ensuring data integrity.
* Learned about Index for faster data queries and Partition for optimizing performance when processing large tables.
* Learned about Execution Plan to analyze how the database executes queries and support system optimization.
* Learned about Database Log and Buffer in supporting data recovery, system synchronization, and faster read/write operations.
* Learned the differences between relational database management systems (RDBMS/SQL) and non-relational (NoSQL):
    * RDBMS uses table structures, supports ACID, and is suitable for tightly related data.
    * NoSQL has flexible schemas, supports horizontal scaling, and optimizes performance for large-scale data processing.
* Learned about OLTP and OLAP models:
    * OLTP focuses on high-speed online transaction processing and ensures data consistency.
    * OLAP serves historical data analysis, reporting, and data mining in a Data Warehouse.

#### **Tuesday**

* Learned about Amazon RDS – an AWS-managed relational database service supporting MySQL, PostgreSQL, SQL Server, Oracle, and MariaDB.
* Understood key RDS features:
    * Automatic backup and Point-in-Time Recovery support.
    * Read Replica support to reduce read query load and serve reporting.
    * Multi-AZ support for automatic failover and high system availability.
    * Encryption at rest and in transit, using Security Groups and NACLs for security.
    * Support for changing instance size and Storage Auto Scaling.
* Learned the differences between Multi-AZ and Read Replica:
    * Multi-AZ is used for High Availability with synchronous data replication.
    * Read Replica is used to scale read capacity with asynchronous replication.
* Learned about Amazon Aurora – an AWS-developed database engine based on MySQL and PostgreSQL with high read/write performance.
* Understood standout Aurora features:
    * Shared Storage reduces replication lag.
    * Backtrack supports fast data recovery.
    * Global Database supports multi-Region deployment.
    * Clone and Multi-Master support for large enterprise environments.

#### **Wednesday**

* Learned about Amazon Redshift – an AWS-managed Data Warehouse service using a PostgreSQL core, optimized for OLAP systems and large-scale data analytics.
* Understood Redshift's MPP (Massively Parallel Processing) architecture:
    * Data is split and stored across Compute Nodes.
    * The Leader Node receives, coordinates, and aggregates queries.
* Learned about Columnar Storage:
    * Data is stored by column instead of by row.
    * Speeds up analytical and statistical queries on large datasets.
* Learned about Redshift cost and performance optimization features:
    * Transient Cluster supports temporary scaling to increase processing performance.
    * Redshift Spectrum allows querying data directly on Amazon S3 to reduce storage costs.
* Learned about Amazon ElastiCache – an AWS-managed caching service with two engines: Redis and Memcached.
* Understood the role of ElastiCache in a system:
    * Placed in front of the Database layer to cache frequently accessed data.
    * Reduces Database load and improves application response time.
    * AWS automatically detects and replaces failed nodes to ensure high availability.
* Learned the differences between Redis and Memcached, with Redis often preferred for supporting more features and data structures.
* Learned about caching logic in applications:
    * Identify data to cache and cache expiration time.
    * Manage cache updates or invalidation to keep data in sync with the Database.


