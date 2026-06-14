---
title: "Worklog Tuần 4"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.4. </b> "
---

### Mục tiêu tuần 4:

* Dịch vụ lưu trữ AWS.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Dịch vụ lưu trữ trên AWS <br>&emsp; + Amazon Simple Storage Service (Amazon S3): <br>&emsp;&emsp; + S3 Access Point, S3 Storage Class <br>&emsp;&emsp; + S3 Object Lifecycle Management <br>&emsp;&emsp; + Static Website & Cors <br>&emsp;&emsp; + Control Access <br>&emsp;&emsp; + Endpoint & Versioning <br>&emsp;&emsp; + Object Key & Performance <br>&emsp;&emsp; + Glacier | 11/05/2026 | 11/05/2026 | Module 04-02 - Amazon Simple Storage Service (S3) - Access Point - Storage Class <br> Module 04-03 - S3 Static Website & CORS - Control Access - Object Key & Performance - Glacier |
| 3 | - Snow Family <br>&emsp; + Snowball <br>&emsp; + Snowball Edge (Snowball X) <br>&emsp; + Snowmobile <br> - Disaster Recovery on AWS | 12/05/2026 | 12/05/2026 | Module 04-04 - Snow Family - Storage Gateway - Backup |
| 4 | - Thực hành <br>&emsp; + S3 bucket (000057) <br>&emsp; + AWS Backup (000013) | 13/05/2026 | 13/05/2026 | Create S3 bucket :: Start with Amazon S3 <br> Deploy AWS Backup to the System :: DEPLOY AWS BACKUP TO THE SYSTEM |
| 5 | - Thực hành <br>&emsp; + VM Import/Export | 14/05/2026 | 14/05/2026 | AWS VM Import/Export :: VIRTUAL MACHINE (VM) IMPORT/EXPORT |
| 6 | - Thực hành | 15/05/2026 | 15/05/2026 | |

### Kết quả đạt được tuần 4:

#### **Thứ 2**

**A) S3 Access Point (Điểm truy cập):**

* Là tính năng cho phép tạo các điểm kết nối (hostname unique) dành cho ứng dụng, người dùng đơn lẻ hoặc theo nhóm.
* Chúng ta có thể cấu hình phân quyền khác nhau cho mỗi access point được tạo ra.

**CÂU HỎI:** Vì sao cần dùng Access Point?

* Vì ban đầu, khi nhiều ứng dụng cùng sử dụng chung một S3 Bucket, việc cấu hình quyền truy cập (Policy) rất phức tạp và dễ xảy ra lỗi như cấp dư hoặc thiếu quyền. Còn S3 Access Point giúp giải quyết vấn đề này bằng cách tạo các điểm truy cập riêng cho từng ứng dụng hoặc nhóm người dùng. Mỗi Access Point có policy riêng, giúp quản lý quyền truy cập rõ ràng, linh hoạt và dễ kiểm soát hơn. Ngoài ra, tính năng này còn tăng cường bảo mật nhờ kết hợp Identity Policy và Resource Policy để kiểm soát truy cập chặt chẽ hơn.

![Hình ảnh cách thức hoạt động của S3 Access Point](/images/1-Worklog/1.4-Week4/01.jpeg)

**B) S3 Storage Class (Các lớp lưu trữ):**

* Amazon S3 chia lưu trữ thành nhiều lớp để tối ưu chi phí.
* **Các cấp lưu trữ (S3 Storage Class):**
    * **S3 Standard (Chuẩn):** Dữ liệu được truy cập thường xuyên (Phí lưu trữ cao, nhưng gọi request rất rẻ).
    * **S3 Standard IA (Truy cập không thường xuyên):** Dữ liệu không truy cập thường xuyên (Phí lưu trữ rẻ hơn Standard nhưng phí Request rất cao).
    * **S3 Intelligent Tiering:** Tự động di chuyển các đối tượng giữa các cấp lưu trữ theo số ngày đối tượng không được truy cập. Cụ thể, nếu sau 60 ngày mà không đụng tới file này thì nó sẽ tự động đẩy xuống lớp rẻ hơn.
    * **S3 One Zone IA:** Dữ liệu có thể tái tạo lại, được lưu trữ dài hạn, không truy cập thường xuyên nhưng cần truy cập nhanh. Lớp giá rất rẻ. Dữ liệu chỉ lưu tại 1 AZ duy nhất (thay vì 3 AZ). Dành cho dữ liệu ít xài, nhưng nếu có lỡ mất thì vẫn có thể tái tạo lại được.
    * **Amazon Glacier / Deep Archive:** Lưu trữ dữ liệu ít truy cập. Giá của nó rất rẻ, và lưu trữ cực lạnh. Nó rất thích hợp giành cho những dữ liệu nhiều năm mới đụng tới 1 lần. (Lưu ý: Ta không thể đọc dữ liệu trực tiếp từ lớp nyaf, mà chúng ta phải "rả đông" ra trước rồi mới đẩy lên các lớp trên mới đọc được).
* Chúng ta có thể thiết lập tự động hóa vòng đời của dữ liệu (Object Life Cycle Management) được lưu trữ trong Amazon S3. Bằng cách sử dụng chính sách vòng đời, chúng ta có thể luân chuyển dữ liệu trong 1 S3 bucket giữa các cấp lưu trữ theo thời gian (ngày) tùy chỉnh.

![Hình ảnh sơ đồ vòng đời của Amazon S3](/images/1-Worklog/1.4-Week4/02.jpeg)

* Object Life Cycle Management sẽ di chuyển Object sau số ngày chúng ta quy định, được tính từ ngày Object được tạo.

**C) Static Website & Cors:**

* Amazon S3 có tính năng cho phép host các static website (html, media ...), phù hợp cho Single Page Application. (ứng dụng web hoặc trang web tương tác với người dùng bằng cách tự động viết lại trang web hiện tại với dữ liệu mới từ máy chủ web sử dụng javascript và các framework của nó như AngularJs, ReactJS, thay vì phương pháp mặc định của trình duyệt web tải toàn bộ trang mới).
* Amazon S3 hỗ trợ CORS. CORS là một cơ chế cho phép nhiều tài nguyên khác nhau (fonts, Javascript, v.v...) của một trang web có thể được truy vấn từ domain khác với domain của trang đó.
* CORS là viết tắt của từ Cross-origin resource sharing.
* **Chức năng:** Amazon S3 không chỉ dùng để lưu trữ file tĩnh (hình ảnh, video) mà còn có khả năng host (lưu trữ và chạy) nguyên một trang web tĩnh (Static Website).

![Hình ảnh cách thiết lập CORS cho Amazon S3](/images/1-Worklog/1.4-Week4/03.jpeg)

* Amazon S3 cho phép cấu hình chính sách CORS (Cross Origin Resource Sharing) cho phép client web applications tương tác với các tài nguyên nằm ở domain khác.
* Phải bật và cấu hình tính năng CORS trên S3 Bucket đó. Nếu không cấu hình CORS, hệ thống sẽ chặn truy cập và báo lỗi Access Denied.

**D) Control Access**

* Có cơ chế kiểm soát quyền truy cập tới Bucket:
    * **S3 Access Control List (ACL)** là một cơ chế kiểm soát truy cập cũ có trước IAM. Tuy nhiên, nếu bạn đã sử dụng S3 ACL và thấy đủ thì không cần thay đổi. ACL S3 được gắn bucket (thư mục gốc) và object (từng file lẻ) của S3. Nó xác định tài khoản hoặc nhóm AWS nào được cấp quyền truy cập và loại quyền truy cập.
    * **Nhược điểm:** Việc gán hàng trăm policy vụn vặt ở các cấp độ khác nhau khiến việc quản lý trở nên cực kỳ phức tạp và dễ nhầm lẫn.
    * **S3 Bucket Policy và IAM policy** xác định quyền cấp đối tượng bằng cách cung cấp các đối tượng đó trong phần Resource trong policy của bạn. Câu lệnh sẽ áp dụng cho các đối tượng đó trong bucket. Việc hợp nhất các quyền dành riêng cho đối tượng thành một chính sách (trái ngược với nhiều ACL S3) giúp bạn dễ dàng hơn trong việc xác định các quyền truy cập.
    * Đây là phương pháp hiện đại và nó thuộc loại Resource Policy.
    * **Ưu điểm:** Quản lý tầm trung, chỉ cần viết 1 cái Policy duy nhất gán thẳng vào S3 Bucket, quy định toàn bộ quyền hạn cho mọi file (object) nằm trong bucket đó.

**E) Endpoint & Versioning:**

* **Điểm truy cập Amazon S3 (S3 Endpoint)** là tính năng cho phép truy cập đến S3 bucket thông qua mạng riêng của AWS. Mặc định, việc truy cập tới S3 là thông qua internet.
    * Máy chủ EC2 và S3 đều là "gà cùng một mẹ" AWS. Nhưng mặc định, nếu EC2 muốn upload file lên S3, nó phải kết nối vòng ra mạng Internet công cộng rồi mới vòng lại S3. Vừa chậm vừa kém bảo mật. Vậy nên ta cần giải pháp sử dụng S3 VPC Gateway Endpoint.
    * **Lợi ích sử dụng:** Traffic (dữ liệu truyền tải) từ EC2 sang S3 sẽ đi qua đường ống mạng nội bộ (mạng Private ảo) của AWS mà không cần chạm tới Internet (dùng IP Private thay vì IP Public). Giúp nhanh hơn và an toàn tuyệt đối.
* Chúng ta có thể kích hoạt tính năng lập phiên bản (Versioning) cho phép bạn khôi phục đối tượng sau khi vô tình xóa hay ghi đè, có thể hỗ trợ trước việc bị tấn công ransomware / encryption attack.
    * Nếu xóa một đối tượng, thay vì xóa đối tượng đó, thì Amazon S3 sẽ đánh dấu tập tin đã xóa.
    * Nếu ghi đè đối tượng, thì một phiên bản đối tượng mới sẽ xuất hiện trong bucket.
    * Trong cả 2 trường hợp chúng ta đều có thể khôi phục phiên bản trước đó.

![Hình ảnh sơ đồ tổ chức public/private subnet trong VPC](/images/1-Worklog/1.4-Week4/04.jpeg)

* **Cơ chế khi xóa:** S3 thực chất không xóa hẳn file đó đi, mà nó dán một cái nhãn gọi là Delete Marker. Nếu truy cập bình thường sẽ báo không thấy file (lỗi 404), nhưng nếu gọi kèm theo ID của version cũ thì vẫn tải về bình thường.
* **Chống Ransomware:** Nếu bị hacker mã hóa tống tiền, nó sẽ ghi đè file hỏng lên file gốc. Nếu bật Versioning, file gốc vẫn nằm đó (phiên bản cũ), bạn chỉ việc khôi phục lại mà không cần trả tiền chuộc.
* **Chi phí:** Khi bật versioning lên, lưu bao nhiêu phiên bản sẽ bị tính tiền dung lượng cho bấy nhiêu phiên bản cộng gộp lại. Khi đã bật thì không thể tắt hoàn toàn (disable), chỉ có thể tạm ngưng (suspend) nó.

**F) Object Key & Performance:**

* Mỗi object trong S3 đều ngang hàng, không phân cấp (hierarchy) và được gán 1 object key. Ví dụ: /image/sample.jpg, sample.jpg.
* Sâu bên dưới S3 chia ra các Partitions, Partitions sẽ được chia ra tự động khi lượng request tăng cao hoặc số lượng S3 object keys lớn. (làm chậm tốc độ tìm kiếm object trong partition).
* S3 lưu trữ key map (key map cũng được chia ra nhiều partition và được hash bởi prefix – tiền tố của object key).
* Để tối ưu S3 performance có thể dùng random prefix (/fscd/img/sample.jpg thay vì /img/sample.jpg). Mục tiêu của việc làm này là khiến S3 lưu trữ các object trên nhiều partitions nhất có thể vì performance của S3 dựa trên số lượng partitions.

**G) Glacier**

* Là lựa chọn lưu trữ chi phí thấp (rẻ hơn S3 Standard tới 20 lần), phù hợp cho dữ liệu không cần truy cập trực tiếp và được lưu trữ lâu dài (từ 5-10 năm). Nếu ứng dụng cần truy cập dữ liệu thường xuyên hoặc nhanh chóng, nên chọn Amazon S3 thay vì Glacier.
* Khi lưu trữ dữ liệu trong Amazon S3 Glacier, không thể truy cập trực tiếp; dữ liệu phải được truy xuất về S3 Bucket.
* Có ba tùy chọn truy xuất với thời gian và chi phí khác nhau (mức độ rã đông):
    * **Truy xuất Nhanh (Expedited):** thường hoàn tất trong vòng 1 – 5 phút.
    * **Truy xuất Tiêu chuẩn (Standard):** thường hoàn tất trong vòng 3 – 5 giờ.
    * **Truy xuất Hàng loạt (Bulk):** thường hoàn tất trong vòng 5 – 12 giờ.
* **KHÔNG** thể đọc trực tiếp. Nếu muốn tải về xem, cần phải làm một thao tác gọi là Retrieve (rã đông/đưa dữ liệu từ Glacier trả về S3 Standard).
* Bạn không thể upload file lên Glacier qua giao diện web (Console) thông thường. Bắt buộc phải dùng Code (CLI hoặc SDK) hoặc dùng tính năng Object Lifecycle chuyển dần xuống. Các object nằm trong này được gọi là "Archive".

![Hình ảnh minh họa quy trình lưu trữ, truy xuất và quản lý dữ liệu giữa S3 và Glacier trong AWS](/images/1-Worklog/1.4-Week4/05.jpeg)

* Amazon S3 Glacier là lựa chọn lưu trữ có chi phí thấp, phù hợp với dữ liệu không yêu cầu truy suất trực tiếp, dữ liệu lưu trữ dài hạn.

#### **Thứ 3**

**A) Snow Family (Dịch vụ chuyển dữ liệu vật lý)**

* **Tổng quan:** Là giải pháp Offline Data Transfer (chuyển dữ liệu trạng thái lạnh) dùng khi băng thông internet không đủ để tải lượng dữ liệu khổng lồ (vài chục TB đến hàng trăm PB).
* **Nguyên lý:**

![Hình ảnh nguyên lý Snow Family](/images/1-Worklog/1.4-Week4/06.png)

**a) Snowball**

* Dịch vụ hỗ trợ migrate dữ liệu từ môi trường on-premise tới AWS ở quy mô lên đến PetaByte (PB). Mỗi Snowball có thể chứa tới 80 TeraByte (TB).
* Snowball sẽ được ship trở về AWS region mà chúng ta lựa chọn để lưu trữ dữ liệu và lưu trong dịch vụ chúng ta lựa chọn bao gồm S3 hoặc Glacier.
* Chúng ta sẽ cần cài Snowball Client tại máy local để thực hiện xác minh, nén, mã hóa và transfer dữ liệu.

**b) Snowball Edge (Snowball X)**

* Dịch vụ hỗ trợ migrate dữ liệu từ môi trường on-premise tới AWS ở quy mô lên đến PetaByte (PB). Mỗi Snowball Edge có thể chứa tới 100 TeraByte (TB).
* Snowball Edge sẽ được ship trở về AWS region mà chúng ta lựa chọn để lưu trữ dữ liệu và lưu trong dịch vụ chúng ta lựa chọn bao gồm S3 hoặc Glacier.
* Chúng ta sẽ cần cài Snowball Client tại máy local để thực hiện xác minh, nén, mã hóa và transfer dữ liệu.
* Snowball Edge là thiết bị đặc biệt có sẵn các tài nguyên tính toán để xử lý dữ liệu local trước khi import vào thiết bị.
* Có tích hợp tài nguyên tính toán (máy chủ bên trong) để tiền xử lý dữ liệu ngay tại chỗ trước khi gửi đi.

**c) Snowmobile**

* Dịch vụ hỗ trợ migrate dữ liệu từ môi trường on-premise tới AWS ở quy mô lên đến Exabyte. Nó là một xe tải chứng dữ liệu, mỗi Snowmobile có thể chứa tới 100 PB.
* Snowmobile sẽ trở về AWS region mà chúng ta lựa chọn để lưu trữ dữ liệu và lưu trong dịch vụ chúng ta lựa chọn bao gồm S3 hoặc Glacier.

**B) AWS Storage Gateway (Giải pháp lưu trữ Hybrid)**

* AWS Storage Gateway là giải pháp lưu trữ Hybrid, kết hợp dung lượng lưu trữ trên AWS với dung lượng lưu trữ vô hạn tại chỗ (on-premise).
* Chúng ta có thể tận dụng quy mô và giá thành hợp lý của các dịch vụ lưu trữ trên cloud để giúp lưu trữ các dữ liệu lớn có thời gian yêu cầu lưu trữ lâu.
* AWS Storage Gateway hỗ trợ ba phương thức lưu trữ chính: tập tin, ổ đĩa và băng từ.
    * **Cổng kết nối tập tin (File Gateway)** cho phép bạn lưu trữ và truy xuất đối tượng trong Amazon S3 bằng cách sử dụng các giao thức tệp NFS và SMB. Đối tượng được ghi thông qua cổng kết nối tập tin có thể được truy cập trực tiếp trong S3 (dưới dạng Object).
    * **Cổng kết nối ổ đĩa (Volume Gateway)** cung cấp lưu trữ dạng khối cho ứng dụng của bạn bằng cách sử dụng giao thức iSCSI. Dữ liệu trên ổ đĩa được lưu trữ trong Amazon S3. Để truy cập ổ đĩa iSCSI trong AWS, bạn có thể tạo EBS snapshot (tự động bằng AWS Backup) từ đó tạo ra thành EBS Volumes.
        * **Stored Volume:** Lưu 1 bản copy đầy đủ ở local và 1 bản trên AWS (dùng cho Disaster Recovery).
        * **Cached Volume:** Chỉ lưu dữ liệu hay dùng ở local, dữ liệu cũ đẩy lên AWS (tối ưu dung lượng local).
    * **Cổng kết nối băng từ (Tape Gateway)** cung cấp cho ứng dụng sao lưu của bạn một giao diện thư viện băng từ ảo (VTL) iSCSI, các ổ tape drive ảo và tape ảo. Dữ liệu tape ảo được lưu trữ trong Amazon S3 hoặc có thể được lưu trữ vào Amazon Glacier. Thay thế thư viện băng từ (Tape Library) truyền thống bằng thư viện ảo (VTL). Giúp backup dữ liệu cũ lên S3 hoặc Glacier với chi phí rẻ.

![Hình ảnh sơ đồ kiến trúc của AWS Storage Gateway](/images/1-Worklog/1.4-Week4/07.jpeg)

**C) Disaster Recovery on AWS (Chiến lược khắc phục thảm họa)**

**a) RTO (Recovery Time Objective)**

* Thời gian phục hồi mục tiêu (Recovery Time Objective RTO) là thời gian cần thiết để phục hồi một dịch vụ trở lại trạng thái hoạt động bình thường.
* Ví dụ: Nếu một thảm họa xảy ra lúc 2:00 giờ chiều và RTO là 4 giờ, quá trình DR phải phục hồi dịch vụ trễ nhất vào thời điểm 6:00 giờ tối.

**b) RPO (Recovery Point Objective)**

* Thời điểm phục hồi mục tiêu RPO (Recovery Point Objective): là khoảng thời gian tối đa mà dữ liệu có thể bị mất (Thời gian tối đa để hệ thống hoạt động trở lại bình thường).
* Ví dụ: Nếu chúng ta thực hiện backup mỗi ngày 1 lần thì trong trường hợp xấu nhất chúng ta có thể mất dữ liệu 24 giờ, RPO = 24 hours. (Khoảng thời gian tối đa chấp nhận việc mất dữ liệu).
* Các dịch vụ, ứng dụng có độ phức tạp khác nhau và có mức cam kết dịch vụ (Service Level Agreement - SLA) trong đó bao gồm RTO/RPO khác nhau. Tùy theo loại dịch vụ và mức cam kết chúng ta sẽ lựa chọn chiến lược phục hồi sau thảm họa tương ứng.
* Có 4 chiến lược phục hồi sau thảm họa trên AWS bao gồm:
    * **Sao lưu và khôi phục:** rẻ nhất nhưng RTO/RPO lâu nhất (bước bắt buộc cho mọi chiến lược).
    * **Pilot Light (Active – Standby):** Chi phí thấp. Hệ thống trên AWS chỉ chạy các thành phần cốt lõi (như Database), khi thảm họa mới bật các máy chủ khác lên.
    * **Low Capacity Active – Active:** Hệ thống trên AWS luôn chạy nhưng ở quy mô nhỏ hơn local (ví dụ 20% công suất).
    * **Full Capacity Active – Active:** Hai bên (Local và AWS) chạy song song 100%, có thể chuyển đổi ngay lập tức.

**D) AWS Backup**

* Là dịch vụ quản lý các tác vụ backup, cho phép cấu hình và lên lịch backup (backup schedule), chính sách backup (backup retention) và giám sát hoạt động backup cho các tài nguyên AWS.
    * Amazon EBS
    * Amazon EC2
    * Cơ sở dữ liệu Amazon RDS
    * Cơ sở dữ liệu DynamoDB
    * Amazon EFS
    * AWS Storage Gateway volumes

#### **Thứ 4 – Thứ 6**

Thực hành lab.

Link các bài lab: <https://docs.google.com/document/d/1iNnUbO9kMa4T13B-2wERHX2QJAniIzwO/edit?usp=sharing&ouid=110146210370887604643&rtpof=true&sd=true>
