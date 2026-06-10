---
title: "Worklog Tuần 2"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.2. </b> "
---

### Mục tiêu tuần 2:

* Khám phá các dịch vụ mạng chính trong AWS.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Amazon Virtual Private Cloud (VPC) <br>&emsp; + VPC – subnet <br>&emsp; + VPC – Route Table <br>&emsp; + VPC – Elastic Network Interface <br>&emsp; + VPC – Elastic IP address <br>&emsp; + VPC – Endpoint <br>&emsp; + VPC - Internet Gateway <br>&emsp; + VPC – NAT Gateway <br>&emsp; + VPC – Security Group <br>&emsp; + VPC - Network Access Control List <br>&emsp; + VPC - Flow Logs | 27/04/2026 | 27/04/2026 | <https://000003.awsstudygroup.com/> <br> <https://youtu.be/O9Ac_vGHquM?si=7p-6vhNNY4-RR4dF> |
| 3 | - VPC Peering & Transit Getway <br> - VPN & Dircet Connect | 28/04/2026 | 28/04/2026 | <https://000003.awsstudygroup.com/> <br> <https://youtu.be/O9Ac_vGHquM?si=7p-6vhNNY4-RR4dF> |
| 4 | - Elastic Load Balancing | 29/04/2026 | 29/04/2026 | |
| 5 | - Thực hành | 30/04/2026 | 30/04/2026 | Introduction :: WORK WITH AMAZON SYSTEM MANAGER - SESSION MANAGER |
| 6 | - Thực hành | 01/05/2026 | 01/05/2026 | Introduction :: Start with Amazon VPC and AWS VPN Site-to-Site. |

### Kết quả đạt được tuần 2:

#### **Thứ 2**

**1. Amazon Virtual Private Cloud (VPC)**

* **Tổng quát:** Là dịch vụ cốt lõi tạo ra mạng ảo riêng tư, được cô lập về mặt logic. Nó bao gồm cách thiết lập cấu hình VPC, tạo Subnet, Route Table, Internet Gateway, NAT Gateway và các dịch vụ tường lửa đi kèm.
* **Khái niệm:** là dịch vụ cung cấp môi trường mạng ảo riêng tư, được cô lập hoàn toàn về mặt logic khỏi các mạng khác trên nền tảng đám mây AWS.
* Nó cho phép khởi chạy các tài nguyên AWS vào 1 mạng ảo mà bạn đã xác định. Ví dụ: tự chọn một lớp mạng ảo có dải IP là 10.10.0.0/16
* VPC nằm trong 1 Region, khi tạo VPC cần khai báo 1 lớp mạng CIDR IPv4 (bắt buộc) và IPv6 (tùy chọn)
* Giới hạn của VPC hiện tại là 5 VPC trên 1 AWS Region trên 1 AWS Account.
* Mục đích chính sử dụng VPC thường dùng để phân tách các môi trường (Production / Dev / Test / Staging)
* **Lưu ý:** Nếu muốn các tài nguyên tách biệt hẳn (User không thể nhìn thấy một tài nguyên cụ thể thì cần tách thành nhiều AWS account, nhiều VPC không giải quyết được vấn đề này)

**a) VPC – subnet:** Amazon VPC cho phép tạo nhiều mạng ảo và chia các mạng ảo này thành các mạng con (subnet).

* **Tính chất:** VPC Subnet sẽ nằm trong 1 Availability Zone cụ thể. Một khi tạo Subnet, chúng ta chỉ định CIDR cho mạng con đó và đây là một tập hợp con của khối VPC CIDR.
* **Quy tắt bảo lưu IP:** Trong mỗi Subnet, AWS sẽ giữ 5 địa chỉ IP. Ví dụ nếu Subnet có CIDR là 10.10.1.0/24
    * Địa chỉ network (10.10.1.0)
    * Địa chỉ broadcast (10.10.1.255)
    * Địa chỉ cho bộ định tuyến (10.10.1.1)
    * Địa chỉ cho DNS (10.10.1.2)
    * Địa chỉ cho tính năng tương lai (10.10.1.3)
* **Public Subnet vs Private Subnet:** Về bản chất chúng giống nhau. Tuy nhiên theo "quy ước", nếu một Subnet được cấu hình để máy chủ bên trong nó có thể đi ra ngoài Internet, nó được gọi là Public Subnet. Ngược lại là Private Subnet.

**b) VPC – Route Table ( bảng định tuyến ):** Là tập hợp các Route, để xác định đường đi cho mạng.

* Khi tạo VPC, AWS sẽ tạo một Default Route table ( main ), Default Route table không thể bị xóa và chỉ chứa 1 Route duy nhất là Route cho phép tất cả các Subnet trong VPC liên lạc với nhau.
* Khi tạo VPC, có một Default Route Table (Main) tự sinh ra và không thể bị xóa. Trong đó chứa 1 rule mặc định (Local) cho phép tất cả các tài nguyên ở mọi Subnet trong VPC có thể kết nối liên lạc được với nhau.
* Route table sẽ được gán vào Subnet.
* Tùy vào tuyến đường đi của Internet, chúng ta có thể tạo Custom Route table (bảng định tuyến tùy chỉnh), tuy nhiên sẽ không thể xóa default route. (VPC CIDR - Local)

**c) VPC – Elastic Network Interface ( ENI ):** Là một card mạng ảo, nó giống như Card mạng (NIC) vật lý trên máy tính, chúng ta có thể chuyển sang các EC2 Instance khác.

* Khi khởi tạo 1 máy chủ EC2, AWS tự động tạo 1 ENI gán vào máy chủ đó, và địa chỉ Private IP cũng được gán lên ENI này chứ không gắn trực tiếp vào máy chủ.
* **Tính chất:** Khi chuyển sang một máy chủ mới, một card mạng ảo sẽ vẫn duy trì:
    * Địa chỉ IP Private
    * Địa chỉ Elastic IP address
    * Địa chỉ MAC

**d) VPC – Elastic IP address ( EIP )_ Có tính phí:** Là một địa chỉ public ipv4 tĩnh, có thể liên kết với một Elastic Network Interface.

* Địa chỉ này sẽ không bị thay đổi dù có khởi động lại (restart) máy chủ.
* Khi không sử dụng, sẽ bị Charge phí ( Tránh lãng phí ).

**e) VPC – Endpoint:** cho phép chúng ta kết nối các tài nguyên nằm trong VPC tới các dịch vụ AWS được hỗ trợ (AWS PrivateLink – đi qua mạng private của AWS) mà không cần thông qua kết nối internet.

* Có 2 kiểu VPC Endpoint:
    * **Interface Endpoint:** Sử dụng một Elastic Network Interface trong VPC cùng với một địa chỉ IP Private để kết nối tới 1 dịch vụ hỗ trợ. Nói đơn giản hơn là: Dùng 1 Card mạng ảo ENI nằm trong VPC kèm 1 Private IP để nói chuyện với dịch vụ ngoài.
    * **Gateway Endpoint:** Sử dụng một route table để định tuyến tới endpoint của dịch vụ hỗ trợ (S3 và Dynamo DB). Nói đơn giản hơn là : Dùng dựa trên Route Table. Hiện tại chỉ hỗ trợ kết nối tới 2 dịch vụ là Amazon S3 và DynamoDB.

**Câu hỏi:** Làm thế nào để máy chủ ra Internet

**f) VPC - Internet Gateway:** là một thành phần của Amazon VPC có khả năng mở rộng quy mô theo chiều ngang (scale out) cho phép các EC2 Instance trong VPC có thể truyền thông tin ra ngoài Internet.

* Internet Gateway được quản lý bởi AWS, chúng ta không cần cấu hình autoscale hoặc high availability.
* **Các điều kiện để máy chủ đi ra Internet:**
    * Máy chủ EC2 phải có 1 địa chỉ IP Public (Ví dụ EIP) gán vào ENI.
    * Phải tạo và gắn một Internet Gateway vào VPC.
    * Tạo 1 Custom Route Table gắn vào Public Subnet.
    * Trong Custom Route Table đó, thêm 1 Route entry định tuyến: Destination: 0.0.0.0/0 (Tất cả địa chỉ IP) -> Target: tới ID của Internet Gateway.

**g) VPC – NAT Gateway:** cho phép các EC2 instance trong subnet truy cập tới internet hoặc các dịch vụ AWS khác. Chỉ chấp nhận kết nối chiều ra và không chấp nhận kết nối chiều vào.

* Trong thực tế, để bảo mật, các ứng dụng thường đặt ở Private Subnet. Nhưng chúng vẫn cần ra internet (một chiều) để tải bản vá lỗi hoặc gọi API (ví dụ API giá vàng), mà không cho phép Internet chủ động gọi ngược vào. Khi đó ta dùng NAT Gateway.
* **Kiến trúc NAT Gateway:**
    * Khởi tạo một thiết bị NAT Gateway. Đặc biệt lưu ý: NAT Gateway phải được đặt ở Public Subnet (nơi có thể đi ra Internet).
    * Gắn địa chỉ Elastic IP cho NAT Gateway.
    * Tạo một Custom Route Table riêng biệt và gán nó cho Private Subnet.
    * Trong Custom Route Table này, thêm Route: Destination: 0.0.0.0/0 -> Target: ID của NAT Gateway.
* **Sơ đồ luồng đi ( Traffic ):**

![Hình ảnh sơ đồ Traffic](/images/1-Worklog/1.2-Week2/01.png)

**h) VPC – Security Group ( SG ):** Là một tường lửa ảo có lưu giữ trạng thái (stateful) giúp kiểm soát lượng truy cập đến và đi trong tài nguyên của AWS.

* Security Group rule được hạn chế theo giao thức, địa chỉ nguồn, cổng kết nối, hoặc một Security Group khác.
* Security Group rule chỉ cho phép rule allow.
* Security Group được áp dụng lên các Elastic Network Interface.
* **Tính chất State-ful (Lưu giữ trạng thái):** Nếu cấu hình cho phép kết nối luồng Inbound (chiều đến, ví dụ mở Port 80 cho người dùng truy cập web), AWS sẽ tự động cho phép luồng Outbound (chiều đi - phản hồi lại người dùng) trong cùng một phiên làm việc. Và không cần phải cấu hình mở rule cho Outbound nữa.
* **Cách hoạt động:**
    * Chỉ hỗ trợ thiết lập các quy tắc "Allow" (Cho phép), không có quy tắc "Deny" (Chặn).
    * Mặc định khi tạo mới 1 Security Group: Nó sẽ Chặn mọi truy cập đến (Inbound bị khóa trắng) và Cho phép mọi truy cập đi (Outbound mở toàn bộ).

![Hình ảnh cách hoạt động Security Group](/images/1-Worklog/1.2-Week2/02.png)

* **Cấu hình nguồn (Source):** Nguồn kết nối không nhất thiết phải là 1 IP cố định, bạn có thể gán nguồn là tên một Security Group khác.

**i) VPC - Network Access Control List (NACL):** Là một tường lửa ảo không lưu giữ trạng thái (stateless) giúp kiểm soát lượng truy cập đến và đi trong tài nguyên của AWS. Vì là tường lửa không lưu trữ trạng thái nên chúng ta cần phải cấu hình. Mà muốn cấu hình đúng thì ta cần biết được đường đi của Port ( Xem thử đi vào Port nào và đi ra Port nào ) để có thể cấu hình chính xác.

* NACL được hạn chế theo giao thức, địa chỉ nguồn, cổng kết nối.
* NACL được áp dụng lên các Amazon VPC Subnets
* Mặc định NACL cho phép mọi truy cập đến và đi.
* **Các đọc rule:** Là phải đọc từ trên xuống, nếu thỏa cái nào thì lấy cái đó.

![Hình ảnh bảng rule](/images/1-Worklog/1.2-Week2/03.jpeg)

* **Tính chất State-less (Không lưu giữ trạng thái):** Khi cấu hình, bạn bắt buộc phải tạo quy tắc rõ ràng cho cả 2 chiều: Inbound (Đến) và Outbound (Đi) dựa theo Port mà ứng dụng sử dụng.
* **Các hoạt động:**
    * Hỗ trợ thiết lập cả quy tắc "Allow" (Cho phép) và "Deny" (Chặn).
    * Các quy tắc được đánh số thứ tự (ví dụ: Rule 100, 200...). Hệ thống sẽ đọc tuần tự từ trên xuống dưới. Thỏa mãn Rule nào trước sẽ áp dụng luôn Rule đó.
    * Mặc định khi tạo VPC, Network ACL sẽ có Rule mặc định là Cho phép Mọi truy cập đến và đi (Allow All) để dễ dàng thiết lập ban đầu.

![Hình ảnh cách hoạt động của NACL](/images/1-Worklog/1.2-Week2/04.jpeg)

* **Tầm ảnh hưởng:** Vì được gắn vào Subnet nên khi thay đổi cấu hình NACL, nó sẽ tác động lên toàn bộ tất cả máy chủ bên trong Subnet đó (không như Security Group chỉ tác động lên máy chủ gắn đích danh ENI).

**j) VPC - Flow Logs:** Là một tính năng cho phép bạn nắm bắt thông tin về lưu lượng IP đến và đi từ các giao diện mạng trong VPC của bạn.

* **Nơi xuất dữ liệu:** Các tập tin logs có thể được xuất bản lên Amazon CloudWatch Logs hoặc Amazon S3.
* VPC Flow Logs không capture nội dung gói tin.
* **Đặc điểm:** VPC Flow Logs chỉ ghi lại Header của gói tin (Bao gồm: IP nguồn, IP đích, Port, giao thức, thời gian gửi, bị Allow hay Reject...). Nó KHÔNG ghi lại nội dung (content) bên trong gói tin.
* **Ứng dụng thực tế:** Được sử dụng rất nhiều trong bảo mật để phát hiện các hành vi bất thường, phát hiện luồng quét cổng hoặc mã độc (malware) gửi gói tin về máy chủ điều khiển lúc rạng sáng.

#### **Thứ 3**

**2. VPC Peering & Transit Getway**

* **Tổng quát:** Là cách thức kết nối nhiều VPC lại với nhau. VPC Peering cho phép kết nối 2 VPC, Transit Gateway kết nối số lượng lớn VPC dễ dàng và hiệu quả

**a) VPC Peering:** Là tính năng giúp kết nối hai hay nhiều VPC để các tài nguyên bên trong hai VPC đó có thể liên lạc trực tiếp với nhau không cần phải thông qua Internet, góp phần gia tăng tính bảo mật cho VPC.

* VPC Peering là kết nối cần tạo 1:1 giữa hai VPC thành viên, không hỗ trợ transitive routing.
* VPC Peering không hỗ trợ khi 2 VPC bị overlap IP address space.
* **Đặc điểm nổi bật:**
    * Hỗ trợ kết nối giữa các VPC nằm ở các Region khác nhau hoặc các Tài khoản AWS (AWS Accounts) khác nhau.
    * KHÔNG hỗ trợ Transitive Routing (Định tuyến bắc cầu): Nghĩa là nếu VPC A kết nối VPC B, và VPC B kết nối VPC C, thì A không thể đi trực tiếp qua C được. A phải tạo một Peering riêng rẽ nối thẳng sang C.
    * Không thể thiết lập VPC Peering nếu không gian địa chỉ mạng (CIDR Block) của 2 VPC bị trùng lặp (Overlap).
* **Cấu hình thực tế:** Việc thiết lập Peering chưa đủ để hệ thống kết nối. Bạn bắt buộc phải cấu hình lại Bảng định tuyến (Route Table) trên cả hai đầu Subnet của 2 VPC để chỉ đường cho các gói tin. (Có thể cấu hình Destination trỏ thẳng đến 1 Subnet hoặc đích danh 1 IP của máy chủ).
* **Hạn chế:** Nếu doanh nghiệp có hàng chục hay hàng ngàn VPC, việc dùng VPC Peering sẽ tạo ra một mạng lưới kết nối "mạng nhện" cực kỳ phức tạp (Ví dụ: 30 VPC cần tới 435 kết nối Peering).

**b) Transit Gateway:**

* Transit Gateway được dùng để kết nối các VPC và mạng on-premises thông qua một hub trung tâm. Điều này đơn giản hoá mạng và kết thúc các mối quan hệ định tuyến phức tạp.
* Transit Gateway Attachment là một công cụ để gắn các subnet của từng VPC cần kết nối với nhau vào một TGW đã được khởi tạo. Transit Gateway Attachment hoạt động ở quy mô Availability Zone (AZ-level).
* Trong VPC, khi một subnet ở một AZ có Transit Gateway Attachment với một TGW, các subnet khác trong cùng AZ đều có thể kết nối tới TGW đó.
* **Cách hoạt động:**
    * Thay vì các VPC nối trực tiếp chéo nhau, tất cả VPC chỉ cần kết nối vào một Hub Transit Gateway trung tâm duy nhất.
    * Sử dụng tính năng Transit Gateway Attachment: Để VPC kết nối với Transit Gateway, bạn tạo ra các "Attachment" gán vào Subnet.
* **Lưu ý về quy mô:** Attachment hoạt động ở cấp độ AZ (Availability Zone). Mỗi một AZ chỉ cần gán 1 Transit Gateway Attachment là đủ (dù trong AZ có nhiều Subnet). Nếu VPC trải trên 3 AZ, bạn sẽ cần 3 Attachment.

![Hình ảnh cách hoạt động của Transit Gateway](/images/1-Worklog/1.2-Week2/05.png)

* **Cấu hình định tuyến:** Tương tự VPC Peering, chúng ta cần phải cấu hình Route Table trong VPC trỏ gói tin cần thiết về Transit Gateway, và bản thân Transit Gateway cũng có một Route Table riêng để phân phối gói tin tới VPC đích phù hợp.

**3. VPN & Dircet Connect**

* **Tổng quát:** Nó là giải pháp kết nối từ môi trường AWS về các trung tâm dữ liệu cục bộ (On-premises/Local) một cách an toàn và tin cậy.

**a) VPN to Site to Site:** dùng trong mô hình hybrid để thiết lập kết nối liên tục giữa môi trường trung tâm dữ liệu truyền thống tới môi trường VPC của AWS. Việc thiết lập kết nối sẽ cần 2 đầu endpoint ở phía AWS và phía khách hàng:

* **Virtual Private Gateway:** Được quản lý hoàn toàn bởi AWS (chia 2 endpoints ở 2 đầu AZ).
* **Customer Gateway:** Đầu endpoint phía khách hàng, có thể là thiết bị phần cứng hoặc software appliance.
* <https://docs.aws.amazon.com/vpn/latest/s2svpn/your-cgw.html> đây là đường link cung cấp danh sách các thiết bị/software appliance được AWS hỗ trợ và hướng dẫn kết nối VPN Site to Site từ môi trường của khách hàng tới AWS.

**b) VPN Client to Site:** Cho phép một Host truy cập tới tài nguyên trong VPC bằng IP nội bộ không cần kết nối bằng Internet

* **Khuyến khích:**
    * Sử dụng VPN Client to Site trong AWS Market Place ( Bên thứ 3).
    * AWS có cung cấp dịch vụ VPN Client to Site nhưng chi phí khá cao và tính tiền theo giờ, chưa thực sự hợp lý ở thời điểm hiện tại.

**c) AWS Direct Connect:** Là dịch vụ cho phép tạo kết nối riêng từ trung tâm dữ liệu truyền thống tới AWS.

* Là một kết nối dedicated (dành riêng) ở mức thấp (Layer thấp) cho khách hàng.
* Độ trễ ở Việt Nam của Direct Connect là khoảng 20 ms – 30 ms (nếu đấu nối từ Hồ Chí Minh, từ Hà Nội có thể cao hơn một chút).
* AWS Direct Connect ở Việt Nam hiện tại sẽ thông qua AWS Direct Connect partners (ví dụ: Viettel, FPT, CMC) và hoạt động dưới dạng Hosted Connections (băng thông ở Việt Nam hiện tại hỗ trợ tới khoảng 2 Gbps). Nếu kết nối trực tiếp tới AWS thì là Dedicated Connections (băng thông cho phép cao hơn nhưng hiện chưa có ở Việt Nam).
* Băng thông Direct Connect có thể thay đổi lên / xuống tùy nhu cầu. Khi migration (dịch chuyển dữ liệu lớn ban đầu), có thể nâng băng thông lên cao. Sau khi replicate xong, có thể hạ băng thông xuống để tiết kiệm.
* Trong thực tế, Cloud Engineer rất ít khi tự cấu hình Direct Connect mà hầu hết qua đội ngũ partner để làm và cấu hình, chúng ta chỉ sử dụng.
* **Lưu ý quan trọng:** Direct Connect không thực hiện mã hóa dữ liệu. Do đó, sau khi kết nối Direct Connect, vẫn cần phải cấu hình một đường VPN Site to Site trên Direct Connect để tiến hành mã hóa dữ liệu.

#### **Thứ 4**

**4. Elastic Load Balancing**

* **Tổng quát:** là dịch vụ phân phối lưu lượng truy cập (Cân bằng tải) đến nhiều máy chủ đích, đảm bảo khả năng chịu lỗi, hiệu năng và mở rộng.
* **Khái niệm:** Elastic Load Balancing (ELB) là một dịch vụ cân bằng tải được quản lý bởi AWS, có chức năng phân phối lưu lượng cho nhiều EC2 Instance hoặc Container.
* **Đặc điểm:**
    * Sử dụng các giao thức HTTP, HTTPS, TCP và SSL (TCP bảo mật).
    * Có thể nằm ở Public hoặc Private subnet: Thực tế (Best Practice) thì Load Balancer đặt ở Public Subnet để nhận request của người dùng, sau đó Load Balancer sẽ kết nối tới các máy chủ ảo EC2 nằm ở Private Subnet.
    * Mỗi ELB sẽ được cấp tên DNS và chỉ kết nối thông qua DNS. Ngoại trừ Network Load Balancer (NLB) là hỗ trợ gán IP tĩnh.
    * **Health Check:** ELB có tính năng health check để kiểm tra xem các Instance phía sau có còn "sống" (trạng thái healthy) hay không. Không gửi lưu lượng đến các Instance không đạt health check.
* **Tổng cộng có 4 loại:**
    * **Application Load Balancer:** Là một dịch vụ cân bằng tải được quản lý bởi AWS, hoạt động ở Layer 7 (Lớp ứng dụng theo mô hình OSI).
        * Sử dụng giao thức chính: HTTP, HTTPS.
        * Hỗ trợ tính năng Path-based routing: Có thể chuyển hướng request dựa trên đường dẫn. Ví dụ: URL /mobile sẽ được route tới target group chứa máy chủ cho điện thoại, URL /desktop route tới target group cho máy tính.
        * Cho phép route traffic tới cả những target nằm ngoài VPC (dùng IP address), EC2, các serverless function như Lambda, và Container (ECS, EKS).
    * **Network Load Balancer:** Là một dịch vụ cân bằng tải được quản lý bởi AWS, hoạt động ở Layer 4. Tự động auto-scale khi traffic tăng cao.
        * Sử dụng giao thức: TCP, TLS.
        * Hỗ trợ tính năng set IP tĩnh.
        * Hỗ trợ hiệu năng cao nhất trong các loại Load Balancer, có khả năng xử lý lên đến hàng triệu request trên giây (Extreme performance).
        * Cho phép route traffic tới cả target nằm ngoài VPC (IP address), EC2, Container (ECS, EKS). (Lưu ý: Không hỗ trợ Lambda và không hỗ trợ Path-based routing như ALB).
    * **Classic Load Balancer:** Là dịch vụ cân bằng tải cổ điển, hoạt động ở cả Layer 4 và Layer 7.
        * Sử dụng giao thức HTTP, HTTPS, TCP, TLS.
        * Chi phí cao hơn so với ALB và NLB, hiện tại rất ít được sử dụng và dần bị loại bỏ.
        * Chỉ cho phép route traffic tới các máy chủ EC2.
    * **Gateway Load Balancer:** Là hoạt động ở Layer 3, thường được dùng trong các mô hình liên quan tới bảo mật. GWLB lắng nghe toàn bộ IP packets và forward tới target group được chỉ định.
        * Sử dụng GENEVE protocol trên port 6081.
        * Cho phép route traffic tới các Virtual appliance được AWS hỗ trợ (như các Next Generation Firewall từ các nhà cung cấp dịch vụ bảo mật bên thứ 3 (Third-party) để đọc nội dung gói tin xem có an toàn hay không).
        * Đây là đường link danh sách Vendor được AWS hỗ trợ: <https://aws.amazon.com/vi/elasticloadbalancing/partners/>

* Đây là mô hình chúng ta sẽ thường được thấy khi sử dụng Gateway Load Balancer.

![Hình ảnh mô hình Gateway Load Balancer](/images/1-Worklog/1.2-Week2/06.jpeg)

**a) Sticky session (session affinity):**

* Là tính năng cho phép các kết nối được gán vào một target nhất định. Việc này đảm bảo các requests từ một user trong một session sẽ được gửi tới cùng một target. Sticky session là cần thiết trong trường hợp các máy chủ ứng dụng lưu trữ thông tin trạng thái người dùng tại chính server đó. Nếu request bị chuyển sang server khác, người dùng sẽ bị mất thông tin trạng thái (ví dụ: đang đăng nhập bị log out ra ngoài).
    * Hoạt động trên: Network Load Balancer, Application Load Balancer, Classic Load Balancer.
* ELB cung cấp tính năng lưu trữ logs truy cập (access logs) chúng ta có thể sử dụng access logs để phân tích truy cập, trouble shoot. Log truy cập sẽ được lưu trữ vào một dịch vụ lưu trữ đối tượng là Amazon S3 (Simple Storage Service).
* **Tính năng lưu trữ logs truy cập (Access Logs):**
    * ELB cung cấp tính năng lưu trữ logs truy cập.
    * Sử dụng để phân tích truy cập và xử lý sự cố (troubleshoot).
    * Log truy cập sẽ được lưu trữ vào một dịch vụ lưu trữ dạng object là Amazon S3 (Simple Storage Service).

#### **Thứ 5 và Thứ 6**

**Lab03 _ Module 02-Lab03:** ( Amazon VPC and AWS Site-to-Site VPN Workshop :: Start with Amazon VPC and AWS VPN Site-to-Site. )

![Hình ảnh đã tạo VPC thành công](/images/1-Worklog/1.2-Week2/07.png)

![Hình ảnh tạo Subnet thành công](/images/1-Worklog/1.2-Week2/08.png)

![Hình ảnh tạo thành công Internet Gateway](/images/1-Worklog/1.2-Week2/09.jpeg)

![Hình ảnh tạo thành công Route table](/images/1-Worklog/1.2-Week2/10.png)

![Hình ảnh tạo thành công Security Group ( Public )](/images/1-Worklog/1.2-Week2/11.jpeg)

![Hình ảnh tạo thành công Security Group ( Private )](/images/1-Worklog/1.2-Week2/12.jpeg)

![Hình ảnh tạo thành công EC2](/images/1-Worklog/1.2-Week2/13.png)

![Hình ảnh tạo thành công Elastic IP](/images/1-Worklog/1.2-Week2/14.png)

![Hình ảnh tạo thành công NAT Gateway](/images/1-Worklog/1.2-Week2/15.jpeg)

![Hình ảnh tạo thành công Security Group cho EIC Endpoint](/images/1-Worklog/1.2-Week2/16.jpeg)

![Hình ảnh tạo thành công EC2 Endpoint](/images/1-Worklog/1.2-Week2/17.jpeg)

**Lab03 _ Module 02-Lab20** ( Set up AWS Transit Gateway :: SET UP AWS TRANSIT GATEWAY )

![Hình ảnh tạo Key Pairs thành công](/images/1-Worklog/1.2-Week2/18.png)

![Hình ảnh tạo Clould Formation thành công](/images/1-Worklog/1.2-Week2/19.png)

![Hình ảnh tạo thành công Transit Gateway](/images/1-Worklog/1.2-Week2/20.jpeg)

![Hình ảnh tạo Transit Gateway Attachments thành công](/images/1-Worklog/1.2-Week2/21.jpeg)

![Hình ảnh kết nối ec2 thành công](/images/1-Worklog/1.2-Week2/22.png)

![Hình ảnh tạo thành công Transit Gateway Route Tables](/images/1-Worklog/1.2-Week2/23.png)

![Hình ảnh liên kết thành công](/images/1-Worklog/1.2-Week2/24.jpeg)

![Hình ảnh liên kết thành công](/images/1-Worklog/1.2-Week2/25.jpeg)
