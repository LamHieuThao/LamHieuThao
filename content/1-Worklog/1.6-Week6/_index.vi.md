---
title: "Worklog Tuần 6"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.6. </b> "
---

### Mục tiêu tuần 6:

* Dịch vụ Cơ sở dữ liệu trên AWS.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Database Concepts | 25/05/2026 | 25/05/2026 | Module 06-01 - Database Concepts review - YouTube |
| 3 | - Amazon RDS & Amazon Aurora | 26/05/2026 | 26/05/2026 | Module 06-02 - Amazon RDS & Amazon Aurora - YouTube |
| 4 | - Redshift - Elasticache | 27/05/2026 | 27/05/2026 | (4998) Module 06-03 - Redshift - Elasticache - YouTube |
| 5 | - Thực hành | 28/05/2026 | 28/05/2026 | |
| 6 | - Thực hành | 29/05/2026 | 29/05/2026 | |

### Kết quả đạt được tuần 6:

#### **Thứ 2**

* Tìm hiểu các khái niệm cơ bản trong cơ sở dữ liệu như Database, Session, Primary Key, Foreign Key, Index, Partition, Buffer và Database Log.
* Hiểu vai trò của Primary Key và Foreign Key trong việc liên kết dữ liệu giữa các bảng và đảm bảo tính toàn vẹn dữ liệu.
* Tìm hiểu về Index giúp tăng tốc độ truy vấn dữ liệu và Partition giúp tối ưu hiệu năng khi xử lý bảng dữ liệu lớn.
* Tìm hiểu Execution Plan để phân tích cách cơ sở dữ liệu thực thi câu truy vấn và hỗ trợ tối ưu hệ thống.
* Tìm hiểu Database Log và Buffer trong việc hỗ trợ phục hồi dữ liệu, đồng bộ hệ thống và tăng tốc độ đọc/ghi dữ liệu.
* Tìm hiểu sự khác nhau giữa hệ quản trị cơ sở dữ liệu quan hệ (RDBMS/SQL) và phi quan hệ (NoSQL):
    * RDBMS sử dụng cấu trúc bảng, hỗ trợ ACID và phù hợp cho dữ liệu có quan hệ chặt chẽ.
    * NoSQL có schema linh hoạt, hỗ trợ mở rộng ngang và tối ưu hiệu năng xử lý dữ liệu lớn.
* Tìm hiểu mô hình OLTP và OLAP:
    * OLTP tập trung xử lý giao dịch trực tuyến với tốc độ cao và đảm bảo tính nhất quán dữ liệu.
    * OLAP phục vụ phân tích dữ liệu lịch sử, báo cáo và khai thác dữ liệu trong Data Warehouse.

#### **Thứ 3**

* Tìm hiểu về Amazon RDS – dịch vụ cơ sở dữ liệu quan hệ được AWS quản lý, hỗ trợ MySQL, PostgreSQL, SQL Server, Oracle và MariaDB.
* Hiểu các tính năng chính của RDS:
    * Tự động backup và hỗ trợ Point-in-Time Recovery.
    * Hỗ trợ Read Replica để giảm tải truy vấn đọc và phục vụ báo cáo.
    * Hỗ trợ Multi-AZ giúp tự động failover và tăng tính sẵn sàng cao cho hệ thống.
    * Hỗ trợ mã hóa dữ liệu at rest và in transit, sử dụng Security Group và NACL để bảo mật.
    * Hỗ trợ thay đổi instance size và Storage Auto Scaling.
* Tìm hiểu sự khác nhau giữa Multi-AZ và Read Replica:
    * Multi-AZ dùng cho High Availability với cơ chế đồng bộ dữ liệu.
    * Read Replica dùng để mở rộng khả năng đọc với cơ chế bất đồng bộ.
* Tìm hiểu về Amazon Aurora – hệ quản trị cơ sở dữ liệu do AWS phát triển dựa trên MySQL và PostgreSQL với hiệu năng đọc/ghi cao.
* Hiểu các tính năng nổi bật của Aurora:
    * Shared Storage giúp giảm replication lag.
    * Backtrack hỗ trợ khôi phục dữ liệu nhanh.
    * Global Database hỗ trợ triển khai hệ thống đa Region.
    * Hỗ trợ Clone và Multi-Master cho môi trường doanh nghiệp lớn.

#### **Thứ 4**

* Tìm hiểu về Amazon Redshift – dịch vụ Data Warehouse được AWS quản lý, sử dụng lõi PostgreSQL và tối ưu cho hệ thống OLAP, phân tích dữ liệu lớn.
* Hiểu kiến trúc MPP (Massively Parallel Processing) của Redshift:
    * Dữ liệu được chia nhỏ và lưu trên các Compute Node.
    * Leader Node chịu trách nhiệm nhận, điều phối và tổng hợp truy vấn.
* Tìm hiểu cơ chế lưu trữ Columnar Storage:
    * Dữ liệu được lưu theo cột thay vì theo hàng.
    * Giúp tăng tốc các truy vấn phân tích và thống kê dữ liệu lớn.
* Tìm hiểu các tính năng tối ưu chi phí và hiệu năng của Redshift:
    * Transient Cluster hỗ trợ mở rộng tạm thời để tăng hiệu năng xử lý.
    * Redshift Spectrum cho phép truy vấn dữ liệu trực tiếp trên Amazon S3 nhằm giảm chi phí lưu trữ.
* Tìm hiểu về Amazon ElastiCache – dịch vụ caching được AWS quản lý với hai engine Redis và Memcached.
* Hiểu vai trò của ElastiCache trong hệ thống:
    * Đặt trước lớp Database để cache dữ liệu thường truy cập.
    * Giảm tải cho Database và tăng tốc độ phản hồi ứng dụng.
    * AWS tự động phát hiện và thay thế node bị lỗi để đảm bảo tính sẵn sàng cao.
* Tìm hiểu sự khác nhau giữa Redis và Memcached, trong đó Redis thường được ưu tiên nhờ hỗ trợ nhiều tính năng và cấu trúc dữ liệu hơn.
* Tìm hiểu về caching logic trong ứng dụng:
    * Xác định dữ liệu cần cache và thời gian hết hạn cache.
    * Quản lý việc cập nhật hoặc xóa cache để đồng bộ dữ liệu với Database.

#### **Thứ 5 & Thứ 6**

Thực hành.
