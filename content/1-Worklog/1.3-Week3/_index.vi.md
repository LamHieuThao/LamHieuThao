---
title: "Worklog Tuần 3"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.3. </b> "
---

### Mục tiêu tuần 3:

* Dịch vụ compute VM trên AWS.
* Dịch vụ lưu trữ AWS.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Amazon Elastic Compute Cloud (EC2) & EBS (Elastic Block Store) <br> - Amazon Lightsail | 04/05/2026 | 04/05/2026 | <https://youtu.be/e7XeKdOVq40?si=z4QEhZbtv5Fw_og8> |
| 3 | - Amazon EFS / FSX <br> - AWS Application Migration Service (MGN) | 05/04/2026 | 05/04/2026 | <https://youtu.be/hFVYG8WqfU0?si=QxwYCFD9nqa0VAW7> |
| 4 | - Thực hành <br>&emsp; + Manage Resources Using Tags and Resource Groups (Lab 27) | 06/04/2026 | 06/04/2026 | Using Tags :: MANAGE RESOURCES USING TAGS AND RESOURCE GROUPS |
| 5 | - Thực hành: <br>&emsp; + Deploying FCJ Management Application with Auto Scaling Group (Lab 06) | 07/04/2026 | 07/04/2026 | Deploying FCJ Management with Auto Scaling Group :: DEPLOYING FCJ MANAGEMENT APPLICATION WITH AUTO SCALING GROUP. |
| 6 | - Dịch vụ lưu trữ trên AWS <br>&emsp; + Amazon Simple Storage Service (Amazon S3): Khái niệm, các đặc tính nổi bật. | 08/04/2026 | 08/04/2026 | <https://youtu.be/_yunukwcAwc?si=EVCC-mNqdaYyj052> |

### Kết quả đạt được tuần 3:

#### **Thứ 2**

**1. Amazon Elastic Compute Cloud (EC2) & EBS (Elastic Block Store)**

* **Tổng quan:**
    * **Amazon Elastic Compute Cloud (EC2):** Đây là dịch vụ máy chủ ảo cốt lõi trên AWS.
    * **EBS (Elastic Block Store):** Là một dịch vụ lưu trữ gắn liền với EC2. Vì EBS không có quá nhiều thông tin phức tạp để học tách biệt, nên trong chương trình này, nó sẽ được gom chung và trình bày cùng với Amazon EC2.

**A) Amazon Elastic Compute Cloud (EC2):** Nó giống với máy chủ ảo hoặc máy chủ vật lý truyền thống. EC2 có khả năng khởi tạo nhanh, khả năng co dãn tài nguyên mạnh mẽ, linh hoạt.

* Amazon EC2 có thể hỗ trợ các workload như lưu trữ web, ứng dụng, cơ sở dữ liệu, dịch vụ xác thực và bất cứ công việc nào khác mà máy chủ thông thường có thể đáp ứng.
* **Điểm khác biệt & Ưu điểm vượt trội của EC2:**
    * **Khởi tạo siêu tốc (Provisioning):** Tốc độ tạo ra một máy chủ mới nhanh hơn rất nhiều so với máy chủ truyền thống.
    * **Linh hoạt thay đổi cấu hình:** Người dùng có thể dễ dàng thêm hoặc bớt tài nguyên cho máy ảo, không bị cố định chết như phần cứng vật lý.
    * **Nâng cấp dễ dàng với chi phí rẻ hơn:** Giống như việc "đi thuê nhà", AWS sẽ tự động nâng cấp CPU, chipset lên các phiên bản mạnh mẽ hơn sau vài năm, nhưng chi phí cho các phiên bản mới này lại thấp hơn phiên bản cũ. Đây là cam kết của AWS: chi phí theo thời gian chỉ có giảm chứ không tăng.

![Hình ảnh điểm khác biệt & ưu điểm vượt trội của EC2](/images/1-Worklog/1.3-Week3/01.png)

* **Elasticity (Độ co giãn):** Tự động tăng tài nguyên khi tải cao, giảm khi tải thấp.
* **Scalability:** Chỉ tập trung mở rộng hệ thống.
* **Khác biệt:** Elasticity = mở rộng + thu hẹp linh hoạt theo nhu cầu thực tế.
* **Lợi ích:** Tiết kiệm chi phí nhờ mô hình pay-as-you-go.
* **Ứng dụng:** Phù hợp cho web, database, xác thực và nhiều workload khác.
* **Instance Type:** Cấu hình của Amazon EC2 không được tùy chọn tùy ý, mà lựa chọn cấu hình thông qua việc lựa chọn các EC2 Instance type. (<https://aws.amazon.com/ec2/instance-types/?ncl=h_ls>)
* **Instance type quyết định các yếu tố:**
    * **CPU (Intel / AMD / ARM (Graviton 1 / 2 / 3) / GPU**
        * **Intel:** Có mức chi phí sử dụng cao nhất.
        * **AMD:** Tiết kiệm hơn khoảng 10% so với Intel.
        * **ARM (Chip AWS Graviton 1, 2, 3):** Có kiến trúc tương tự chip Apple M1/M2/M3. Dòng chip này mang lại tỷ lệ Hiệu năng / Giá thành (Performance/Price) cao nhất, giúp tiết kiệm chi phí lên tới 40%. (Chỉ hỗ trợ trên LINUX và chưa có trên WINDOWS)
    * **Memory**
    * **Network**
    * **Storage**
* **Sơ đồ kiến trúc của máy chủ ảo EC2:**

![Sơ đồ kiến trúc của máy chủ ảo EC2](/images/1-Worklog/1.3-Week3/02.jpeg)

**a) AMI / Backup / Key Pair**

* **AMI (Amazon Machine Image):** Là một template (bản mẫu) được sử dụng để khởi tạo (provision) một hoặc nhiều máy chủ ảo EC2 instance cùng một lúc.
* Sử dụng AMI (Amazon Machine Image) có thể provision ra một hoặc nhiều EC2 Instances cùng lúc. AMI có sẵn của AWS, trên AWS Market Place và custom AMI tự tạo từ EC2 Instances.

![Hình ảnh các loại AMI](/images/1-Worklog/1.3-Week3/03.jpeg)

* **AWS Marketplace:** Một "chợ ứng dụng" (tương tự App Store hay CH Play) nơi có thể mua các AMI chứa sẵn giải pháp từ các tổ chức hoặc nhà cung cấp phần mềm bên thứ 3.
* **Custom AMI (AMI tự tạo):** Có thể tự tạo một AMI từ chính máy chủ EC2 đang chạy của mình.
* AMI bao gồm root OS volumes, quyền sử dụng AMI quy định tài khoản AWS được sử dụng và mapping EBS volume sẽ được tạo và gán vào EC2 Instances.
* **Thành phần của AMI:**

![Hình ảnh thành phần của AMI](/images/1-Worklog/1.3-Week3/04.png)

* EC2 instance có thể được backup bằng cách tạo snapshot.
* Key pair (public key và private key) dùng để mã hóa thông tin đăng nhập cho EC2 Instance.
* **Cách thức hoạt động:**

![Hình ảnh cách thức hoạt động Key Pair](/images/1-Worklog/1.3-Week3/05.jpeg)

![Sơ đồ Key Pair mã hóa](/images/1-Worklog/1.3-Week3/06.jpeg)

**B) EBS (Elastic Block Store):** Là một dịch vụ lưu trữ gắn liền với EC2. Vì EBS không có quá nhiều thông tin phức tạp để học tách biệt, nên trong chương trình này, nó sẽ được gom chung và trình bày cùng với Amazon EC2.

* Elastic Block Store (EBS) là khi chúng ta nhắc đến "ổ đĩa gắn vào máy chủ EC2" hoặc "Block device mapping", đó chính là dịch vụ lưu trữ dạng khối (Block Storage).
* Amazon EBS cung cấp block storage và được gắn trực tiếp vào EC2 Instance, tuy được gắn trực tiếp như 1 RAW device, EBS về bản chất hoạt động độc lập với EC2 và được kết nối thông qua mạng riêng của EBS.
* **Mạng riêng biệt (EBS Network):** Đây là điểm khác biệt và lợi thế cực lớn của AWS so với các Cloud khác.
* **Bản chất:** EBS hoạt động độc lập với EC2 và không được kết nối thông qua mạng riêng của EBS trong cùng 1 AZ. EC2 không thể hoạt động mà không có EBS.
    * **EBS Network:** Mạng riêng kết nối giữa EBS và EC2 (không dùng chung mạng Internet).
    * **Điểm mạnh:** Là lợi thế nổi bật của AWS so với nhiều Cloud khác.
    * **Cách hoạt động:** Dữ liệu Storage (EBS) đi kênh riêng, tách biệt với Network thông thường.
    * **Lợi ích:** Tránh nghẽn mạng, không ảnh hưởng lẫn nhau khi truyền dữ liệu.
    * **Kết quả:** Đảm bảo hiệu năng lưu trữ ổn định, chính xác khi test hiệu năng.
* **Phân loại ổ đĩa:**

![Hình ảnh phân loại ổ đĩa EBS](/images/1-Worklog/1.3-Week3/07.png)

* EBS có hai nhóm đĩa chính là HDD và SSD, được thiết kế để đạt độ sẵn sàng 99.999% bằng cách replicate dữ liệu giữa 3 Storage Node trong 1 AZ.
* Có một số EC2 Instances đặc thù được tối ưu hóa hiệu năng của EBS. (Optimized EBS Instances)
* EBS volumes, mặc định chỉ được gắn vào 1 EC2 Instances, EC2 Instances chạy trên Hypervisor Nitro có thể dùng 1 EBS volume gắn vào nhiều EC2 Instances. (EBS Multi attach)
* EBS được backup bằng cách thực hiện snapshot vào S3 (Simple Storage Storage)
    * Snapshot đầu tiên là full, tất cả các snapshot tiếp theo là incremental.

**a) Instance Store:** Là vùng đĩa NVME tốc độ cực cao, nằm trên physical node chạy các máy ảo EC2.

* Instance store sẽ bị xóa hết dữ liệu khi chúng ta thực hiện stop EC2 instance.
* Instance store không bị xóa dữ liệu khi chúng ta thực hiện restart máy, hoặc bị crash.
* Instance store không replicate dữ liệu dự phòng nên thường không khuyến khích lưu trữ dữ liệu quan trọng.
    * Sử dụng trong các trường hợp cần hiệu năng cực cao lên tới hàng triệu IOPS.
    * Khi sử dụng thường được replicate dữ liệu vào một EBS volume để bảo đảm an toàn.
* **Rủi ro và khuyến cáo:**
    * **Không replication:** Instance Store không sao chép/dự phòng dữ liệu như EBS.
    * **Rủi ro cao:** Hỏng phần cứng ⇒ mất toàn bộ dữ liệu, không thể khôi phục.
    * **Khuyến cáo từ AWS:** Không lưu dữ liệu quan trọng trên Instance Store.
    * **Giải pháp:** Dữ liệu quan trọng nên lưu trên EBS.
* **Các trạng thái làm mất và không làm mất dữ liệu:**

![Hình ảnh các trạng thái làm mất và không làm mất dữ liệu](/images/1-Worklog/1.3-Week3/08.jpeg)

* Sử dụng trong các trường hợp cần hiệu năng cực cao lên tới hàng triệu IOPS:
    * swap
    * paging
    * ………

**b) User Data:** là đoạn script chạy một lần khi provision EC2 Instance từ AMI. Nó dễ hiểu nó là một đoạn mật mã kịch bản (Script).

* Tùy hệ điều hành mà chúng ta sẽ sử dụng bash shell scripts (Linux) / powershell (Windows).
* **Sự phụ thuộc vào hệ điều hành:**

![Hình ảnh sự phụ thuộc vào hệ điều hành](/images/1-Worklog/1.3-Week3/09.jpeg)

**CÂU HỎI:** Tại sao lại cần User Data trong thực tế?

* **Golden Image:** AMI chuẩn đã cấu hình sẵn (bảo mật, tối ưu) dùng làm bản gốc.
* **Vấn đề:** Nếu không dùng User Data → phải tạo nhiều AMI riêng (Web, App, DB…).
* **User Data:** Script chạy khi EC2 khởi tạo để cấu hình thêm.
* **Giải pháp:** Dùng 1 Golden Image + User Data để "biến" EC2 thành nhiều vai trò khác nhau.
* **Lợi ích:**

![Hình ảnh lợi ích của User Data](/images/1-Worklog/1.3-Week3/10.png)

* Giảm số lượng AMI cần quản lý.
* Tăng tự động hóa triển khai.
* Linh hoạt trong môi trường doanh nghiệp.

**c) EC2 Auto Scaling:** Là tính năng hỗ trợ tăng giảm số lượng EC2 Instance dựa theo các điều kiện cụ thể (scaling policy).

* Có thể tự đăng ký các EC2 Instance vào Elastic Load Balancer.
* Hoạt động trên nhiều AWS Availability Zone.
* Có thể hỗ trợ nhiều Pricing options khác nhau.
* **Vai trò cốt lõi của EC2 Auto Scaling:**
    * **Vai trò chính:** EC2 Auto Scaling giúp hiện thực hóa Elasticity (co giãn) trên Cloud.
    * **Chức năng:** Tự động tăng/giảm số lượng EC2 instances theo điều kiện thiết lập.
    * **Scaling Policy:** Tập hợp các quy tắc quyết định khi nào scale up / scale down.
    * **Ý nghĩa:** Đảm bảo hiệu năng hệ thống và tối ưu chi phí vận hành.
* **Tích hợp với Cân bằng tải và Độ sẵn sàng:**
    * **Tích hợp ELB:** Khi tạo EC2 mới, Auto Scaling tự động register vào Load Balancer.
    * **Lợi ích:** Traffic được phân phối đều ngay lập tức, không cần cấu hình thủ công.
    * **Multi-AZ:** Hoạt động trên nhiều Availability Zone (AZ).
    * **Ý nghĩa:** Tăng độ sẵn sàng (High Availability), tránh downtime khi 1 AZ gặp sự cố.
* **Tối ưu hóa chi phí:**
    * **Mục tiêu:** Tối ưu chi phí khi dùng EC2 Auto Scaling.
    * **Cách làm:** Kết hợp nhiều Pricing Options trong cùng hệ thống.
    * **On-Demand:** Trả tiền theo nhu cầu (linh hoạt, dễ dùng).
    * **Spot Instances:** Giá rẻ, dùng tài nguyên dư thừa (có thể bị thu hồi).
    * **Reserved / Savings Plans:** Cam kết dài hạn để được giảm giá.
    * **Lợi ích:** Cân bằng giữa chi phí – hiệu năng – độ ổn định.

**d) Pricing options**

* EC2 bao gồm 4 tùy chọn giá:
    * **On-demand:** Trả theo giờ / phút / giây, xài nhiều tính nhiều, mắc nhất. Phù hợp cho các workload chạy lên tới 6 tiếng 1 ngày.
    * **Reserved Instance:** Cam kết sử dụng theo kì hạn 1–3 năm để lấy discount, tuy nhiên bị giới hạn theo EC2 Instance type / family.
    * **Saving Plans:** Cam kết sử dụng theo kì hạn 1–3 năm để lấy discount, có thể không bị giới hạn bởi EC2 Instance type family.
    * **Spot Instance:** Tận dụng tài nguyên dư, giá rẻ tuy nhiên khi cần thì AWS sẽ terminate instance trong 2 phút.

**e) Amazon Lightsail:**

* Là dịch vụ tính toán có chi phí thấp (giá tính theo tháng chỉ bắt đầu từ 3,5 $/tháng) ngoài ra mỗi Instance Lightsail tạo ra cũng sẽ có một mức data transfer đi kèm. (data transfer này có mức giá rẻ hơn data transfer từ EC2 tương đối nhiều)
* Nó phù hợp cho các workload nhẹ, môi trường test dev, không yêu cầu tải CPU cao liên tục > hơn 2 giờ mỗi ngày.
* Cũng có khả năng backup bằng snapshot tương tự như EC2.
* Chạy trong một VPC đặc biệt, có thể kết nối tới VPC thông thường qua 1 click VPC Peering.

#### **Thứ 3**

**2. Amazon EFS / FSX**

* **Tổng quan:**
    * Đây là các dịch vụ dùng để tạo ra không gian lưu trữ và chia sẻ dữ liệu chung cho nhiều máy chủ khác nhau thông qua mạng (Network).
    * AWS cung cấp hai dịch vụ chính cho mục đích này là: Elastic File System (EFS) và FSx.

**a) EFS (Elastic File System)** cho phép tạo các NFSv4 Network volume và gắn vào nhiều EC2 Instances cùng lúc, quy mô lưu trữ lên đến hàng petabyte. EFS chỉ support Linux.

* Sử dụng EFS chỉ tính chi phí theo dung lượng sử dụng (trong khi EBS tính phí theo dung lượng cấp phát).
* EFS có thể được cấu hình để mount vào môi trường on-premise qua DX hoặc VPN.

**b) FSX:** Cho phép tạo các NTFS volume và gắn vào nhiều EC2 Instances cùng lúc sử dụng giao thức SMB (Server Message Block), FSx support Windows và Linux.

* Sử dụng FSx chỉ tính chi phí theo dung lượng sử dụng (trong khi EBS tính phí theo dung lượng cấp phát).
* FSx hỗ trợ tính năng deduplication, giúp giảm chi phí 30–50% cho các trường hợp sử dụng thông thường.

**3. AWS Application Migration Service (MGN)**

* **Tổng quan:**
    * Đây là dịch vụ chuyên hỗ trợ quá trình Migration (Dịch chuyển). Nó giúp bạn di chuyển các ứng dụng và dịch vụ từ môi trường máy chủ cục bộ (On-premise / Local) lên nền tảng đám mây AWS.
    * MGN còn đóng vai trò hỗ trợ Disaster Recovery (Khắc phục và phục hồi sự cố sau thảm họa).
* MGN: dùng để migrate và replicate phục vụ mục đích xây dựng Disaster Recovery Site cho các máy chủ thực, ảo lên môi trường AWS.
* Nó liên tục sao chép các máy chủ nguồn sang EC2 Instance trên tài khoản AWS (asynchronous / synchronous).
* MGN trong quá trình sao chép sẽ sử dụng các máy staging có số lượng và quy mô cấu hình nhỏ hơn máy chủ gốc rất nhiều.
* Khi thực hiện cut-over MGN sẽ tự động tạo và chạy các máy chủ EC2 trên AWS.

#### **Thứ 4 – Thứ 6**

Thực hiện các bài Lab.

Link các bài lab: <https://docs.google.com/document/d/1_NX-S0mg1et47c4ePoq0SdbkQLCLsN3NYFsMrnoKdng/edit?usp=sharing>
