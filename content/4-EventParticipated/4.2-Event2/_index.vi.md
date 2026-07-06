---
title: "Event 2"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 4.2. </b> "
---



### Event Objectives

- Hiểu đúng vai trò và phạm vi công việc thực tế của một DevOps Engineer trong doanh nghiệp.
- Nắm được cách thiết kế một hệ thống ứng dụng có khả năng mở rộng (scalable system) trên nền tảng AWS thông qua case study thực tế.
- Tìm hiểu hành trình phát triển từ một sinh viên mới bắt đầu tìm hiểu Cloud đến khi trở thành AWS Partner / AWS Community Builder.
- Khám phá công việc thực tế của một Data Analytics Engineer và những kỹ năng cần thiết để phát triển sự nghiệp.
- Hiểu văn hóa làm việc và quy trình tuyển dụng chuẩn tại các tập đoàn đa quốc gia (MNC).

---

### Agenda Overview

**Thời gian:** 9:00 AM – 12:00 PM, Thứ Bảy, ngày 13 tháng 6 năm 2026  
**Địa điểm:** AWS Vietnam Office

---

## Điểm nổi bật

### 1. Chào mừng & Giới thiệu

- Check-in và networking giữa người tham dự.
- Giới thiệu mục tiêu, nội dung trọng tâm.
- Tổng quan nội dung sự kiện

---

### 2. Tổng quan về các dịch vụ có trong buổi Workshop

Buổi meetup tập trung vào 4 phần chia sẻ chính:

- Thực tế công việc của DevOps Engineer
- Thiết kế hệ thống scalable trên AWS (case study thực tế)
- Hành trình phát triển cùng cộng đồng AWS (từ sinh viên đến AWS Partner/Community Builder)
- Thực tế công việc Data Analytics Engineer và văn hóa làm việc tại tập đoàn đa quốc gia, nhằm giúp người tham dự có góc nhìn toàn diện hơn về nghề nghiệp công nghệ, kỹ năng cần thiết và con đường phát triển sự nghiệp trong lĩnh vực Cloud và Data.

---

## Nội dung chính của Workshop

### 1. WHAT DOES A DEVOPS ENGINEER REALLY DO? (Thực tế công việc của một DevOps Engineer)

**Diễn giả:** Trọng H. Truong  
**Vị trí:** DevOps Engineer @ Endava Vietnam

#### **Nội dung chính**

- Chỉ ra sự khác biệt giữa những gì mọi người thường nghĩ về DevOps (người viết CI/CD pipeline, người dùng Docker/Kubernetes, cloud/platform engineer...) và công việc thực tế mà một DevOps Engineer đảm nhận. Phạm vi công việc của DevOps thực chất phụ thuộc rất nhiều vào bối cảnh cụ thể: quy mô công ty, cấu trúc đội nhóm, mức độ trưởng thành về hạ tầng/cloud và độ phức tạp của sản phẩm. Chia sẻ cũng đề cập đến việc AI đang thay đổi tốc độ làm việc của kỹ sư (thời gian debug rút ngắn đáng kể từ khi có các công cụ AI hỗ trợ lập trình) và những công cụ nền tảng nên học đầu tiên khi theo đuổi con đường DevOps.

#### **Kiến thức tiếp thu**

- Hiểu đúng vai trò và phạm vi công việc thực tế của một DevOps Engineer, tránh những ngộ nhận phổ biến.
- Nhận biết các yếu tố (quy mô công ty, cấu trúc team, độ trưởng thành hạ tầng...) ảnh hưởng đến phạm vi công việc DevOps.
- Nắm được các công cụ/kỹ năng nền tảng cần học đầu tiên và cách AI đang hỗ trợ, tăng tốc công việc của kỹ sư.

---

### 2. A SCALABLE URL SHORTENING SERVICE ON AWS (Thiết kế hệ thống rút gọn URL có khả năng mở rộng)

**Diễn giả:** Đinh Trung Kiên & Nguyễn Minh Thọ  
**Vị trí:** Lead Developer tại startup & Student

#### **Nội dung chính**

- Trình bày quá trình thiết kế một dịch vụ rút gọn URL (URL Shortener) có khả năng mở rộng trên AWS. Nhóm phân tích ưu và nhược điểm của mô hình đơn giản ban đầu (dễ triển khai, chi phí thấp nhưng dễ gặp single point of failure, độ trễ đọc cao và khó mở rộng), từ đó xây dựng kiến trúc hoàn chỉnh gồm: tầng Frontend (Amazon CloudFront, AWS WAF, AWS Amplify), Key Generation Service (KGS) sử dụng Amazon ECS kết hợp Amazon ElastiCache (Redis) để sinh sẵn các mã rút gọn, và Backend Service với hai luồng xử lý riêng biệt — luồng tạo mới (create flow: ECS/Spring Boot ghi vào cache và Amazon DynamoDB) và luồng chuyển hướng (forward flow: ưu tiên đọc từ cache, truy vấn DynamoDB khi cache miss).

#### **Kiến thức tiếp thu**

- Hiểu quy trình thiết kế một hệ thống có khả năng chịu tải cao và mở rộng linh hoạt.
- Nắm được cách kết hợp CloudFront, WAF và Amplify để tối ưu và bảo vệ tầng frontend.
- Hiểu vai trò của ElastiCache (Redis) trong việc sinh mã trước (KGS) và giảm tải truy vấn cho DynamoDB.
- Phân biệt được thiết kế luồng tạo (create) và luồng chuyển hướng (forward) trong một hệ thống backend thực tế.

---

### 3. FROM FIRST CLOUD AI JOURNEY TO AWS PARTNER (Hành trình từ First Cloud AI Journey đến AWS Partner)

**Diễn giả:** Danh Hoàng Hiếu Nghị  
**Vị trí:** Ex Engineer, AWS Community Builder, AWS Student Builder Group Leader

#### **Nội dung chính**

- Chia sẻ hành trình cá nhân qua 8 giai đoạn: từ sự tò mò của một sinh viên (Student Curiosity), tham gia First Cloud Journey, workshop & cộng đồng, thực hành hands-on labs, các dự án ở trường, xây dựng portfolio, trở thành AWS Partner và cuối cùng là chia sẻ lại kiến thức cho cộng đồng (Share Back).
- Chia sẻ giới thiệu chương trình AWS Student Builder Group (kế thừa từ AWS Cloud Clubs Program) cùng lộ trình tham gia, các quyền lợi và badge nhận được khi tham gia sự kiện (Student Community Day, credit/voucher AWS...), cũng như chương trình AWS Community Builder dành cho những thành viên tích cực đóng góp cho cộng đồng.

#### **Kiến thức tiếp thu**

- Hiểu lộ trình phát triển từ một sinh viên mới tìm hiểu Cloud đến khi trở thành AWS Partner/Community Builder.
- Biết đến chương trình AWS Student Builder Group và các quyền lợi (badge, credit, voucher) khi tham gia các sự kiện cộng đồng.
- Nhận thấy tầm quan trọng của việc chủ động xây dựng portfolio và "viết nên lịch sử của riêng mình" trong sự nghiệp công nghệ.

---

### 4. CÂU CHUYỆN THỰC TẾ ĐẾN VĂN HÓA TẠI TẬP ĐOÀN ĐA QUỐC GIA

**Diễn giả:** Mr. Dat Pham & Mr. Cường Nguyễn  
**Vị trí:** Data Analytics Engineer & Process Engineer

#### **Nội dung chính**

- **Data Analytics Engineer:** chia sẻ công việc thực tế của một Data Analytics Engineer qua các case study tại doanh nghiệp (Kamereo, Colgate-Palmolive), cùng những kỹ năng cần thiết như tư duy phản biện, kỹ năng giao tiếp, kể chuyện bằng dữ liệu (data storytelling) và giải quyết vấn đề — minh họa qua các ví dụ thực tế như Operation Performance, Backup Performance, Fill Rate Performance. Bài chia sẻ cũng trình bày lộ trình phát triển tư duy nghề nghiệp qua các giai đoạn: Follower (người thực thi) → Learner (người học chủ động) → Problem Solver (người giải quyết vấn đề), tiến tới System Thinker (người tư duy hệ thống) và Super Star (người dẫn dắt).
- **Process Engineer:** giới thiệu quy trình tuyển dụng chuẩn tại các tập đoàn đa quốc gia gồm 4 bước: Sàng lọc & Sơ vấn → Test năng lực → Phỏng vấn chuyên môn → Đánh giá sự hòa hợp văn hóa. Phần chia sẻ khép lại bằng những trăn trở về tinh thần đổi mới, dám nghĩ dám làm của thế hệ trẻ Việt Nam trong hành trình xây dựng những "Steve Jobs/Elon Musk của Việt Nam".

#### **Kiến thức tiếp thu**

- Hiểu công việc thực tế của một Data Analytics Engineer tại doanh nghiệp đa quốc gia.
- Nắm được các kỹ năng mềm cần thiết: tư duy phản biện, giao tiếp, kể chuyện bằng dữ liệu, giải quyết vấn đề.
- Hiểu lộ trình phát triển tư duy nghề nghiệp từ người thực thi đến người tư duy hệ thống/dẫn dắt.
- Nắm được quy trình tuyển dụng chuẩn tại các tập đoàn đa quốc gia và yếu tố văn hóa doanh nghiệp cần lưu ý khi ứng tuyển.
- Nhận thức rõ hơn về tinh thần đổi mới, dám nghĩ dám làm trong phát triển sự nghiệp công nghệ tại Việt Nam.

----

### Minh chứng đã tham gia event:

![Minh chứng đã tham gia event](/images/4-EventParticipated/4.2-Event2/01.png)

![Minh chứng đã tham gia event](/images/4-EventParticipated/4.2-Event2/02.png)

![Minh chứng đã tham gia event](/images/4-EventParticipated/4.2-Event2/03.png)

----

> Thông qua các phần chia sẻ, em đã có cơ hội tiếp cận góc nhìn thực tế và đa chiều về các vị trí công việc trong ngành công nghệ — từ DevOps Engineer, kỹ sư thiết kế hệ thống trên AWS, đến Data Analytics Engineer. Đặc biệt, em nhận thấy tầm quan trọng của việc chủ động học hỏi, xây dựng portfolio và tham gia cộng đồng (như AWS Student Builder Group) trong việc phát triển sự nghiệp. Bên cạnh kiến thức kỹ thuật, buổi meetup còn giúp em hiểu rõ hơn về văn hóa làm việc, quy trình tuyển dụng tại các tập đoàn đa quốc gia và tinh thần đổi mới cần có để phát triển bản thân trong lĩnh vực Cloud và Data.
