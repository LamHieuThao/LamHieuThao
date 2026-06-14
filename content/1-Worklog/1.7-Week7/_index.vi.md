---
title: "Worklog Tuần 7"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.7. </b> "
---

### Mục tiêu tuần 7:

* Làm các bài lab thực hành.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Thực hành Lab 18 (Enable Security Hub) | 01/06/2026 | 01/06/2026 | Getting Started with AWS Security Hub :: Enable AWS Security Hub |
| 3 & 4 & 5 & 6 | - Thực hành Lab 117 (Build a Complete serverless Chat Website) | 02/06/2026 | 03/06/2026 | Build a Complete serverless Chat Website :: Start with Amazon VPC and AWS VPN Site-to-Site. |

### Kết quả đạt được tuần 7:

#### **Thứ 2**

**Lab 18 — Enable Security Hub**

**Khái niệm:**

* AWS Security Hub là dịch vụ quản lý tư thế bảo mật đám mây, đóng vai trò như một "trung tâm chỉ huy" giúp tổng hợp, tổ chức và ưu tiên các cảnh báo bảo mật (findings) từ nhiều dịch vụ AWS khác nhau vào một bảng điều khiển duy nhất.

**Mục tiêu thực hành lab:**

* Thiết lập giám sát bảo mật tập trung bằng AWS Security Hub.
* Kích hoạt các tiêu chuẩn kiểm tra bảo mật tự động.
* Đánh giá mức độ tuân thủ bảo mật của tài nguyên AWS.
* Làm quen với việc phát hiện các vấn đề bảo mật.

**Lợi ích**

* **Doanh nghiệp:**
    * Tăng khả năng giám sát bảo mật.
    * Phát hiện sớm lỗi cấu hình và giảm rủi ro rò rỉ dữ liệu.
    * Giảm chi phí xử lý sự cố.

**Các bước thực hiện lab:**

* **Bước 1:** Truy cập AWS Security Hub từ AWS Management Console và bắt đầu kích hoạt.
* **Bước 2:** Xác nhận quyền truy cập để Security Hub thu thập dữ liệu bảo mật từ các dịch vụ AWS liên quan.
* **Bước 3:** Kích hoạt tiêu chuẩn AWS Foundational Security Best Practices.
* **Bước 4:** Xác nhận cấu hình và hoàn tất kích hoạt Security Hub.
* **Bước 5:** Kiểm tra Dashboard và các Findings để đánh giá tình trạng tuân thủ bảo mật của tài nguyên AWS.

**Sơ đồ tóm tắt AWS Security Hub**

![Sơ đồ tóm tắt AWS Security Hub](/images/1-Worklog/1.7-Week7/01.jpeg)

**Kết quả đạt được:**

![Hình ảnh kết quả Lab 18 Security Hub](/images/1-Worklog/1.7-Week7/02.jpeg)

* Hệ thống Security Hub đã vận hành thành công. Đã nắm vững cách kết nối dịch vụ, kích hoạt tiêu chuẩn bảo mật tự động và đọc hiểu các báo cáo phát hiện rủi ro từ hệ thống.

#### **Thứ 3 & 4 & 5 & 6**

**Lab 117 — Build a Complete serverless Chat Website**

**Khái niệm các dịch vụ:**

* **Amazon S3:** Dùng lưu trữ và phân phối các tệp tĩnh của ứng dụng.
* **AWS Lambda:** Xử lý logic nghiệp vụ của ứng dụng theo mô hình serverless.
* **Amazon API Gateway:** Tiếp nhận yêu cầu từ người dùng và kết nối với Lambda.
* **Amazon DynamoDB:** Lưu trữ dữ liệu ứng dụng với hiệu năng cao.
* **Amazon Cognito:** Quản lý đăng ký, đăng nhập và xác thực người dùng.
* **Amazon CloudFront:** Tăng tốc độ truy cập nội dung thông qua mạng CDN.
* **AWS IAM:** Quản lý quyền truy cập tài nguyên AWS theo nguyên tắc quyền tối thiểu.

**Lợi ích:**

* **Doanh nghiệp:**
    * Tiết kiệm chi phí.
    * Tự động mở rộng.
    * Bảo mật cao.
    * Triển khai nhanh.
    * Hiệu năng tốt.
    * Giảm gánh nặng quản trị.

**Mục tiêu thực hiện lab:**

* Xây dựng ứng dụng web serverless trên AWS.
* Triển khai website bằng S3, Lambda và API Gateway.
* Lưu trữ dữ liệu với DynamoDB.
* Xác thực người dùng bằng Cognito.
* Tăng hiệu năng với CloudFront.
* Quản lý và dọn dẹp tài nguyên AWS.

**Các bước thực hiện lab:**

![Hình ảnh các bước thực hiện Lab 117](/images/1-Worklog/1.7-Week7/03.jpeg)

**Kết quả đạt được:**

* Build lên được trang web chat.
* API

![Hình ảnh kết quả trang web chat](/images/1-Worklog/1.7-Week7/04.png)

![Hình ảnh kết quả API](/images/1-Worklog/1.7-Week7/05.png)
