---
title: "Worklog Tuần 8"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.8. </b> "
---

### Mục tiêu tuần 8:

* Thực hành các bài lab.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 & 3 | - Thực hành (Lab 24) | 08/06/2026 | 09/06/2026 | Using AWS Storage Gateway :: USING FILE STORAGE GATEWAY |
| 4 & 5 & 6 | - Dịch bài blog |10/06/2026 |12/06/2026 | |

### Kết quả đạt được tuần 8:

#### **Thứ 2 & Thứ 3**

**Lab 24 — Using AWS Storage Gateway**

**Khái niệm:**

* **AWS Storage Gateway:** Dịch vụ lưu trữ hybrid kết nối hệ thống on-premises với AWS Cloud, cho phép truy cập và đồng bộ dữ liệu liền mạch. Có 3 loại Storage Gateway chính:
    * File Gateway
    * Volume Gateway
    * Tape Gateway
* **File Gateway (SMB):** Thành phần của Storage Gateway giúp chia sẻ file trên Windows thông qua giao thức SMB và lưu trữ dữ liệu trên Amazon S3.
* **Amazon S3:** Dịch vụ lưu trữ đối tượng có độ bền cao, đóng vai trò lưu trữ chính cho dữ liệu được đồng bộ từ File Gateway.
* **Amazon EC2:** Máy chủ ảo AWS dùng để triển khai và vận hành Storage Gateway trong môi trường đám mây.
* **AWS Security Group:** Tường lửa ảo kiểm soát lưu lượng mạng, đảm bảo kết nối an toàn giữa hệ thống và Storage Gateway.

**Lợi ích:**

* **Doanh nghiệp:**
    * Mở rộng dung lượng lưu trữ linh hoạt với chi phí thấp nhờ Amazon S3.
    * Tích hợp dễ dàng với hệ thống hiện có mà không cần thay đổi ứng dụng.
    * Đảm bảo hiệu năng truy cập cao thông qua cơ chế cache cục bộ.
    * Tăng cường bảo vệ dữ liệu và hỗ trợ khôi phục sau thảm họa (Disaster Recovery).
    * Hỗ trợ triển khai mô hình Hybrid Cloud giữa hạ tầng on-premises và AWS.
    * Đơn giản hóa việc sao lưu và lưu trữ dài hạn bằng các chính sách tự động trên S3.
    * Đảm bảo an toàn dữ liệu thông qua cơ chế mã hóa khi truyền tải và lưu trữ.

**Mục tiêu thực hiện lab:**

* Hiểu kiến trúc Hybrid Cloud Storage và vai trò của AWS Storage Gateway trong việc kết nối hệ thống on-premises với AWS Cloud.
* Triển khai và cấu hình File Gateway trên Amazon EC2.
* Tạo và quản lý File Share SMB kết nối với Amazon S3.
* Thực hiện mount File Share trên máy Windows thông qua giao thức SMB.
* Kiểm tra quá trình đồng bộ dữ liệu giữa môi trường on-premises và Amazon S3.

**Các bước thực hiện bài lab**

![Hình ảnh các bước thực hiện Lab 24](/images/1-Worklog/1.8-Week8/01.png)

**Kết quả đạt được:**

* Tạo thành công S3.
* Tạo EC2 for Storage Gateway thành công.

![Hình ảnh tạo S3 và EC2 thành công](/images/1-Worklog/1.8-Week8/02.png)

![Hình ảnh kiểm chứng đồng bộ dữ liệu và cấu hình Cache Gateway](/images/1-Worklog/1.8-Week8/03.jpeg)

* Kiểm chứng thành công cơ chế đồng bộ dữ liệu giữa môi trường on-premises và Amazon S3 thông qua AWS Storage Gateway.
* Cấu hình Cache Gateway thành công, giúp tối ưu hiệu năng truy cập dữ liệu thường xuyên sử dụng.
* Thiết lập bảo mật SMB với Guest Access và mật khẩu xác thực để kiểm soát quyền truy cập File Share.
* Nắm vững quy trình quản lý và dọn dẹp tài nguyên AWS nhằm tránh phát sinh chi phí không cần thiết.
* Thực hành đầy đủ mô hình Hybrid Cloud Storage, tạo nền tảng cho việc triển khai các giải pháp lưu trữ thực tế trong doanh nghiệp.

#### **Thứ 4 – Thứ 6**

* Dịch và tìm hiểu bài Blog: [SECURITY] BẢO MẬT CHUỖI CUNG ỨNG PHẦN MỀM THEO CHUẨN AWS WELL-ARCHITECTED.
* Link bài blog gốc: [Well-architected best practices for software supply chain security | AWS Security Blog](https://aws.amazon.com/blogs/security/well-architected-best-practices-for-software-supply-chain-security/)
