---
title: "Worklog Tuần 5"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.5. </b> "
---

### Mục tiêu tuần 5:

* Dịch vụ bảo mật AWS.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Security is Job Zero <br> - Shared Responsibility Model | 18/05/2026 | 18/05/2026 | Module 05-01 - Share Responsibility Model |
| 3 | - AWS Identity and Access Management <br>&emsp; + Root Account <br>&emsp; + IAM Policy <br>&emsp; + IAM Role | 19/05/2026 | 19/05/2026 | Module 05-02 - Amazon Identity and access management |
| 4 | - Amazon Cognito <br> - AWS Organization <br> - AWS Identity Center (SSO) <br> - Amazon Key Management Service (KMS) <br> - AWS Security Hub | 20/05/2026 | 20/05/2026 | Module 05-03 - Amazon Cognito <br> Module 05-04 - AWS Organization <br> Module 05-05 - AWS Identity Center <br> Module 05-06 - Amazon Key Management Service <br> Module 05-07 - AWS Security Hub |
| 5 | - Thực hành | 21/05/2026 | 21/05/2026 | Create IAM Group :: IAM ROLE & CONDITION |
| 6 | - Thực hành | 22/05/2026 | 22/05/2026 | |

### Kết quả đạt được tuần 5:

#### **Thứ 2**

* Tìm hiểu nguyên tắc **Security is Job Zero:** bảo mật luôn là ưu tiên hàng đầu trong AWS.
* Tìm hiểu mô hình **Shared Responsibility Model:**
    * AWS chịu trách nhiệm bảo mật hạ tầng Cloud.
    * Khách hàng chịu trách nhiệm cấu hình, quản lý dữ liệu và quyền truy cập.
* Hiểu được trách nhiệm bảo mật sẽ khác nhau tùy theo từng loại dịch vụ AWS.

#### **Thứ 3**

**A) Amazon Identity and access management**

**a) Root Account**

* Tìm hiểu về Root Account trong AWS: đây là tài khoản có toàn quyền truy cập tất cả dịch vụ và tài nguyên AWS, bao gồm quản lý thông tin thanh toán và dữ liệu đăng ký tài khoản.
* Nắm được các nguyên tắc bảo mật cho Root Account:
    * Tạo IAM Administrator User để sử dụng hằng ngày.
    * Hạn chế sử dụng Root User và bảo mật thông tin đăng nhập.
    * Đảm bảo duy trì email và domain liên kết với Root Account.
* Tìm hiểu dịch vụ IAM (Identity and Access Management) dùng để quản lý quyền truy cập trong AWS.
* Hiểu khái niệm IAM Principal gồm: Root User, IAM User, Federated User, IAM Role, AWS Services.
* Tìm hiểu về IAM User:
    * Không phải là tài khoản AWS riêng biệt.
    * Có thể đăng nhập bằng mật khẩu hoặc Access Key/Secret Key.
    * Mặc định không có quyền truy cập tài nguyên AWS.
    * Cần gán IAM Policy để cấp quyền sử dụng dịch vụ.
* Tìm hiểu về IAM Group:
    * Dùng để quản lý nhiều IAM User dễ dàng hơn.
    * Một IAM Group không thể nằm trong Group khác.

**b) IAM Policy**

* Tìm hiểu về IAM Policy dùng để cấp quyền truy cập trong AWS, được viết dưới dạng JSON.
* Phân biệt các loại Policy:
    * AWS Managed Policy
    * Customer Managed Policy
    * Inline Policy
* Tìm hiểu 2 loại chính:
    * Identity-based Policy gắn với IAM User/Group/Role.
    * Resource-based Policy gắn trực tiếp với tài nguyên AWS.
* Hiểu nguyên tắc hoạt động của IAM:
    * Explicit Deny luôn được ưu tiên hơn Allow.
* Thực hành ví dụ giới hạn quyền truy cập Amazon S3:
    * Cho phép thao tác trên một S3 Bucket cụ thể.
    * Từ chối truy cập các dịch vụ AWS khác bằng Explicit Deny.

**c) IAM Role**

* Tìm hiểu về IAM Role: dùng để cấp quyền truy cập tài nguyên AWS thông qua IAM Policy nhưng không có credentials cố định.
* Tìm hiểu cơ chế AssumeRole:
    * IAM User hoặc AWS Service có thể assume Role để nhận quyền tạm thời.
    * AWS STS sẽ cấp temporary credentials khi assume role.
    * Khi assume role, quyền hiện tại của user sẽ được thay bằng quyền của Role.
* Tìm hiểu về Trust Policy dùng để quy định ai được phép assume IAM Role.
* Hiểu ứng dụng thực tế của IAM Role:
    * Thực hiện nguyên tắc cấp quyền tối thiểu.
    * Hỗ trợ truy cập giữa nhiều AWS Account (Cross-account access).
* Tìm hiểu cách dùng IAM Role cho ứng dụng chạy trên EC2:
    * Gắn IAM Role trực tiếp vào EC2 thay vì hardcode Access Key/Secret Key.
    * AWS tự động cấp và xoay vòng credentials tạm thời giúp tăng bảo mật.

#### **Thứ 4**

**B) Amazon Cognito**

* Tìm hiểu về Amazon Cognito: Là dịch vụ được quản lý bởi AWS có chức năng xác thực, cấp phép và quản lý người dùng cho các ứng dụng web và di động. Người dùng có thể đăng nhập trực tiếp bằng tên người dùng và mật khẩu hoặc thông qua một bên thứ ba như Facebook, Amazon hoặc Google.
* Tìm hiểu hai thành phần chính của Cognito:
    * **User Pool:** quản lý đăng ký và đăng nhập người dùng.
    * **Identity Pool:** cấp quyền truy cập đến các dịch vụ AWS.
* Tìm hiểu các phương thức xác thực:
    * Đăng nhập trực tiếp bằng username/password.
    * Đăng nhập liên kết qua Google, Facebook hoặc các dịch vụ bên thứ ba.
* Tìm hiểu luồng hoạt động khi kết hợp User Pool và Identity Pool để xác thực người dùng và phân quyền truy cập tài nguyên AWS một cách an toàn.
    * **User Pool:**
        * Là một thư mục chứa và quản lý thông tin người dùng.
        * Cung cấp các tùy chọn đăng ký (Sign-up) và đăng nhập (Sign-in) cho người dùng vào ứng dụng.
    * **Identity Pool:**
        * Là nơi lưu trữ các mapping (ánh xạ) giữa quyền truy cập vào các dịch vụ/tài nguyên của AWS với thông tin của người dùng.

**C) AWS Organization**

* Tìm hiểu về AWS Organizations – dịch vụ giúp quản lý tập trung nhiều AWS Account trong doanh nghiệp.
* Hiểu mô hình tổ chức gồm:
    * Management Account
    * Organization Unit (OU)
    * Member Account
* Tìm hiểu tính năng Consolidated Billing giúp quản lý thanh toán tập trung cho nhiều tài khoản AWS.
* Tìm hiểu về Service Control Policies (SCP):
    * Dùng để thiết lập giới hạn quyền tối đa cho IAM User và IAM Role.
    * Có thể áp dụng cho Root, OU hoặc từng AWS Account.
    * Hỗ trợ deny-based policy để kiểm soát bảo mật chặt chẽ.
* Hiểu vai trò của AWS Organizations trong việc giảm phạm vi ảnh hưởng khi xảy ra sự cố và hỗ trợ quản lý hệ thống AWS quy mô lớn.

**D) AWS Identity Center (SSO)**

* Tìm hiểu về AWS Identity Center (trước đây là AWS SSO) dùng để quản lý truy cập tập trung cho nhiều AWS Account và ứng dụng bên ngoài.
* Tìm hiểu Identity Source dùng để quản lý Users và Groups, có thể sử dụng trực tiếp trên AWS hoặc liên kết với Active Directory.
* Tìm hiểu Permission Sets dùng để định nghĩa quyền truy cập của User/Group đối với các AWS Account thông qua IAM Roles.
* Hiểu quy trình phân quyền:
    * Tạo User và Group
    * Tạo Permission Sets.
    * Gán quyền truy cập cho từng AWS Account.
* Tìm hiểu cơ chế đăng nhập một lần (SSO), giúp người dùng truy cập nhiều AWS Account từ một cổng đăng nhập duy nhất.

**E) Amazon Key Management Service (KMS)**

* Tìm hiểu về Amazon KMS (Key Management Service) dùng để tạo và quản lý encryption key trên AWS nhằm phục vụ mã hóa và giải mã dữ liệu.
* Hiểu vai trò của KMS trong bảo vệ dữ liệu Encryption at Rest và tiêu chuẩn bảo mật FIPS 140-2.
* Tìm hiểu hai loại khóa chính:
    * CMK (Customer Master Key) dùng để quản lý và mã hóa Data Key.
    * Data Key dùng để mã hóa trực tiếp dữ liệu.
* Tìm hiểu quy trình mã hóa và giải mã dữ liệu thông qua CMK và Data Key trong AWS KMS.
* Hiểu tầm quan trọng của quyền truy cập vào Master Key trong việc bảo vệ dữ liệu khỏi truy cập trái phép.

**F) AWS Security Hub**

* Tìm hiểu về AWS Security Hub – dịch vụ hỗ trợ kiểm tra bảo mật tự động cho các tài nguyên và dịch vụ AWS.
* Hiểu cơ chế hoạt động của Security Hub trong việc kiểm tra cấu hình dựa trên AWS Best Practices và các tiêu chuẩn bảo mật như PCI DSS.
* Tìm hiểu các nội dung kiểm tra phổ biến:
    * Cấu hình Firewall
    * Mã hóa dữ liệu bằng KMS
    * Phân quyền IAM
    * MFA và CloudTrail
* Tìm hiểu Dashboard và Findings giúp đánh giá mức độ bảo mật, hiển thị trạng thái Pass/Fail và mức độ rủi ro của từng tài nguyên.
* Hiểu vai trò của Security Hub trong việc theo dõi và cải thiện bảo mật cho hệ thống AWS.

#### **Thứ 5 & Thứ 6**

Thực hành các bài lab.

Link lab: <https://docs.google.com/document/d/1wZdmeSouU-_2RQX7embfRbY9oR2vWcrR/edit?usp=sharing&ouid=110146210370887604643&rtpof=true&sd=true>
