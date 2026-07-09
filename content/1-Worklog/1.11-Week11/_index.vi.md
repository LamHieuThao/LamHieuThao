---
title: "Worklog Tuần 11"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 1.11. </b> "
---


### Mục tiêu tuần 11:

- Vẽ Diagram dự án trên draw.io
- Mô tả dự án

### Bảng tóm tắt nhiệm vụ thực hiện trong tuần:

| Thứ | Nhiệm vụ | Ngày bắt đầu | Ngày kết thúc | Nguồn |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ----------------------------------------- |
| 2, 3, 4 & 5 | - Thực hiện vẽ Diagram của dự án trên draw.io | 29/06/2026 | 07/02/2026 | |
| 6 | - Thực hiện chỉnh sửa sau khi được các anh/chị Admin fixback <br> - Mô tả dự án | 03/07/2026 | 03/02/2026 | |

### Thứ 2 -> Thứ 6:

- Thực hiện vẽ "Sơ đồ kiến trúc điện toán đám mây trên nền tảng AWS" trên Draw.io

![Sơ đồ kiến trúc AWS](/images/1-Worklog/1.11-Week11/01-aws-architecture.png)

### Mô tả dự án:

- Tên dự án: GEN AI
- Mô tả: là một dự án có thể khiến người dùng chưa biết gì về mạng máy tính hay tấn công, phòng thủ mà có thể hiểu rõ được chỉ cần nhập 1 prompt.

#### Giai đoạn 1: Khởi tạo kiến trúc mạng (Provisioning & AI Generation)

Quá trình bắt đầu khi luồng truy cập của người dùng được định tuyến và phân giải DNS tới giao diện ứng dụng web (Frontend). Tại đây, người dùng cung cấp một câu lệnh (prompt) đầu vào yêu cầu thiết lập một sơ đồ mạng cơ bản. Yêu cầu này được đóng gói thành các lời gọi hàm (API calls), đi qua các lớp tường lửa và bộ định tuyến xác thực danh tính trước khi được chuyển tiếp đến môi trường tính toán không máy chủ (serverless compute). Cấu phần xử lý logic trung tâm sẽ giao tiếp với mô hình Ngôn ngữ lớn (LLM) để phân tích ngữ nghĩa, từ đó kiến tạo ra một kiến trúc mạng tiêu chuẩn dưới định dạng JSON và phản hồi ngược lại để hiển thị (render) trực quan trên giao diện Drag-Drop của người dùng.

#### Giai đoạn 2: Tinh chỉnh và Kiểm định cấu hình (Modification & Validation)

Dựa trên khung kiến trúc do AI đề xuất, người dùng có toàn quyền tinh chỉnh thông qua việc thêm, sửa, xóa các thiết bị mạng (nodes - như IPS, IDS, Firewall) hoặc thiết lập lại các luồng kết nối (edges) từ bảng công cụ. Ngay khi thao tác lưu (save) được thực thi, trạng thái mới nhất của sơ đồ mạng (network topology) sẽ được đẩy về hệ thống backend. Tại đây, AI đóng vai trò như một bộ kiểm định cấu hình (configuration validator), tự động rà soát toàn bộ sơ đồ nhằm phát hiện các điểm bất hợp lý (misconfigurations) hoặc các vi phạm nguyên tắc thiết kế mạng an toàn. Nếu phát hiện rủi ro, hệ thống sẽ trả về các cảnh báo chi tiết kèm theo khuyến nghị khắc phục trực tiếp trên giao diện để người dùng nắm bắt.

#### Giai đoạn 3: Giả lập tấn công bất đồng bộ và Tối ưu hóa phòng thủ (Async Attack Simulation & Defensive Remediation)

Đây là phân hệ xử lý các công việc mang tải nặng (heavy-workload) được thiết kế theo kiến trúc bất đồng bộ (asynchronous). Khi tính năng "Scan Attack" được kích hoạt, AI sẽ rà soát sơ đồ để kết xuất một danh sách các véc-tơ tấn công khả thi. Người dùng chọn một kịch bản, và lệnh này lập tức được đẩy vào hàng đợi thông điệp để điều phối thực thi ngầm, cô lập hoàn toàn với luồng thao tác trên Frontend. Hệ thống sẽ tự động giả lập từng bước của cuộc tấn công, tính toán độ sát thương và trả về báo cáo kết quả. Dựa trên nhật ký sự kiện (event logs) của cuộc tấn công đó, AI tiếp tục đề xuất các chiến lược giảm thiểu rủi ro (mitigation strategies). Người dùng có thể cập nhật các thiết bị phòng thủ này vào sơ đồ và tái thực thi (re-test) kịch bản tấn công ban đầu, cho phép kiểm chứng trực quan tính hiệu quả của các biện pháp bảo mật vừa áp dụng.

#### Giai đoạn 4: Giám sát, Lưu vết và Cảnh báo (Observability & Notification)

Xuyên suốt vòng đời hoạt động của hệ thống, mọi phiên bản của sơ đồ mạng và các tệp báo cáo phân tích rủi ro đều được duy trì trạng thái (persistence) tại các cơ sở dữ liệu và kho lưu trữ đối tượng an toàn. Khi các chuỗi kịch bản giả lập ngầm hoàn tất hoặc khi hệ thống phát hiện các lỗ hổng mang tính chí mạng (critical vulnerabilities), cơ chế phát tán sự kiện (event-driven) sẽ tự động kích hoạt dịch vụ nhắn tin để đẩy các cảnh báo thời gian thực (real-time alerts) đến thiết bị người dùng. Đồng thời, toàn bộ hành vi giao tiếp giữa các dịch vụ vi mô (microservices) trong hệ thống đều bị ràng buộc bởi nguyên tắc đặc quyền tối thiểu và được đo lường, lưu vết tập trung để phục vụ quá trình giám sát hiệu năng.

### Chức năng các dịch vụ:

- **Amazon Route 53**: Đóng vai trò là dịch vụ Hệ thống phân giải tên miền (DNS), chịu trách nhiệm định tuyến (routing) lưu lượng truy cập từ trình duyệt của người dùng đến các điểm cuối (endpoints) phân phối nội dung web.
- **Amazon CloudFront**: Hoạt động như một Mạng lưới phân phối nội dung (CDN), giúp lưu trữ bộ nhớ đệm (caching) các tài nguyên của giao diện tại các điểm biên (edge locations) nhằm tối ưu hóa độ trễ (latency) truyền tải nội dung tĩnh.
- **AWS WAF (Web Application Firewall)**: Đóng vai trò là tường lửa bảo vệ ở Lớp 7 (Application Layer), thực thi các bộ quy tắc (security rules) để nhận diện và ngăn chặn các dạng tấn công web phổ biến như DDoS, SQL Injection hay XSS.
- **Amazon S3 (Frontend Bucket)**: Dịch vụ lưu trữ đối tượng (Object Storage) được cấu hình dưới dạng Static Website Hosting, dùng để lưu trữ toàn bộ mã nguồn Frontend (HTML, CSS, JS) của công cụ kéo thả sơ đồ mạng.
- **Amazon API Gateway**: Cửa ngõ (Entry point) trung tâm cho mọi giao tiếp API (RESTful API), làm nhiệm vụ tiếp nhận, định tuyến và giới hạn tốc độ (rate limiting) các luồng yêu cầu từ client đến máy chủ.
- **Amazon Cognito**: Đảm nhiệm vai trò Quản lý định danh và truy cập (IAM) ở cấp độ người dùng cuối, chịu trách nhiệm xác thực danh tính (Authentication) và cấp phát các mã thông báo bảo mật JSON Web Token (JWT).
- **AWS Lambda (API Handlers)**: Môi trường tính toán không máy chủ (Serverless Compute), đóng vai trò thực thi toàn bộ logic nghiệp vụ (business logic) của hệ thống, từ việc gọi API ngoại vi, xử lý luồng dữ liệu đến giao tiếp với cơ sở dữ liệu.
- **Google Gemini API**: Nền tảng Trí tuệ nhân tạo (LLM), hoạt động như "bộ não" cốt lõi để phân tích prompt văn bản, kiến tạo sơ đồ cấu trúc (topology), kiểm định tính hợp lệ của mạng và tạo kịch bản mô phỏng tấn công/phòng thủ.
- **Amazon SQS (Simple Queue Service)**: Dịch vụ hàng đợi thông điệp (Message Queuing), hoạt động như một bộ đệm (buffer) giúp tách rời (decouple) các tác vụ. Dịch vụ này cực kỳ quan trọng để giữ lại các lệnh "Scan Attack", tránh tình trạng quá tải (bottleneck) cho hệ thống khi mô phỏng diễn ra lâu.
- **AWS Step Functions**: Dịch vụ điều phối luồng công việc (Workflow Orchestration), chịu trách nhiệm quản lý máy trạng thái (state machine) để phối hợp và điều khiển thứ tự chạy của các hàm Lambda ngầm trong chuỗi giả lập tấn công (attack kill chain).
- **Amazon DynamoDB**: Cơ sở dữ liệu NoSQL với độ trễ mili-giây, chuyên dùng để lưu trữ, đọc/ghi liên tục trạng thái hiện tại của các bản ghi sơ đồ cấu trúc mạng (Topology JSON) trong lúc người dùng chỉnh sửa (edit).
- **Amazon S3 (Results Bucket)**: Kho lưu trữ đối tượng an toàn chuyên dụng, dùng để cất giữ vĩnh viễn các tệp báo cáo kết quả rà quét lỗ hổng và dữ liệu cấu trúc kích thước lớn dưới định dạng PDF hoặc JSON.
- **Amazon SNS (Simple Notification Service)**: Dịch vụ nhắn tin theo mô hình Xuất bản/Đăng ký (Pub/Sub), đảm nhiệm việc phân phối thông báo hoàn tất quá trình giả lập ngầm hoặc các cảnh báo khẩn cấp qua Email/SMS tới quản trị viên.
- **AWS IAM (Identity and Access Management)**: Dịch vụ thiết lập chính sách kiểm soát truy cập cốt lõi, áp dụng nguyên tắc Đặc quyền tối thiểu (Least Privilege Principle) để đảm bảo các dịch vụ đám mây chỉ được tương tác với nhau theo đúng chức năng được phép.
- **Amazon CloudWatch**: Dịch vụ đo lường (Observability), đảm nhiệm việc giám sát tài nguyên, thu thập chỉ số hiệu năng (metrics) và lưu trữ tập trung nhật ký hoạt động (logs) nhằm phục vụ công tác gỡ lỗi (debugging) và truy vết hệ thống.


