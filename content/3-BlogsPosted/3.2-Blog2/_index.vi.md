---
title: "Blog 2"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 3.2. </b> "
---

# [SECURITY/Web3] Building secure, verifiable blockchain key management on AWS Nitro Enclaves at Turnkey

### Khái niệm đề tài

- AWS Nitro Enclaves là công nghệ ảo hóa dựa trên phần cứng của AWS, cho phép tạo ra các phân vùng tính toán bị cô lập hoàn toàn (Enclaves) nhằm bảo vệ và xử lý các dữ liệu cực kỳ nhạy cảm. Khi ứng dụng vào Web3, kiến trúc Enclave-Native Key Management của Turnkey chuyển toàn bộ các tác vụ cốt lõi như khởi tạo khóa, ký số và thực thi chính sách vào bên trong môi trường cô lập này. Giải pháp này giúp biến hệ thống quản lý khóa từ một "hộp đen" (đòi hỏi niềm tin mù quáng) thành một mô hình minh bạch, có thể xác minh bằng mã hóa và bảo vệ tuyệt đối trước các cuộc tấn công trích xuất bộ nhớ.

### Các điểm chính cần nắm

- **Thách thức trong kiến trúc truyền thống:** Quá trình ký giao dịch thông thường luôn phải đánh đổi giữa bảo mật và hiệu suất vận hành. Tự xây hạ tầng thì tốn chi phí và rủi ro tuân thủ cao; ủy thác cho bên thứ ba (Custodians) lại làm giảm quyền kiểm soát trực tiếp. Trong khi đó, hạ tầng phần mềm thông thường có nguy cơ lộ khóa thô (raw keys) qua kết xuất bộ nhớ (memory dumps) hoặc tệp tin log khi hệ thống bị xâm nhập.
- **Cơ chế cô lập phần cứng tuyệt đối:** Môi trường enclave hoàn toàn không có lưu trữ vĩnh viễn, không hỗ trợ truy cập tương tác (no SSH) và không kết nối Internet. Dữ liệu giao tiếp bắt buộc phải đi qua kênh ảo nội bộ VSOCK. Khóa cấu hình chỉ được giải mã trong RAM tại thời điểm ký và bị xóa ngay lập tức, khiến cả quản trị viên Turnkey lẫn AWS đều không thể tiếp cận.
- **Quy trình khởi tạo và lưu trữ chuẩn HD Wallet:** Hệ thống quản lý khóa phái sinh theo mô hình ví cây phân cấp. Chuỗi dữ liệu gốc (Seed) được sinh ra từ bộ số ngẫu nhiên an toàn của phần cứng Nitro Security Module (NSM), sau đó mã hóa đối xứng qua khóa Quorum Key trước khi lưu vào database. Khi ký giao dịch, bản mã được nạp vào enclave, giải mã tạm thời trong RAM để ký rồi lập tức xóa bỏ, hoàn toàn không bao giờ ghi xuống đĩa (disk).
- **Kiến trúc phân tách trạng thái và luồng dữ liệu:** Hệ thống được chia làm hai phân vùng rõ rệt nhằm tối ưu hóa an toàn:
  - **Bên ngoài (Hạ tầng AWS Cloud - Không an toàn tuyệt đối):** API Gateway tiếp nhận yêu cầu, máy chủ EC2 (Coordinator) xử lý điều phối. Dữ liệu trạng thái và bản khóa gốc đã mã hóa nằm ở Aurora Database. Các thành phần phụ trợ (Async Queue, Redis, Updater, Heartbeat, Notifier/Webhook Targets) chỉ làm nhiệm vụ đồng bộ và thông báo, hoàn toàn không biết khóa thô là gì.
  - **Bên trong (AWS Nitro Enclave - An toàn tuyệt đối):** Các lệnh nhạy cảm được chuyển xuống Enclave qua gRPC/VSOCK và xử lý khép kín qua 5 bước: (1) TLS Fetcher thiết lập kết nối mạng bảo mật; (2) Parser bóc tách dữ liệu; (3) Policy Engine kiểm tra luật (hạn mức, danh sách chặn); (4) Notarizer ký chứng nhận hợp lệ; (5) Signer giải mã khóa trong RAM, ký số giao dịch và xóa sạch dấu vết.
- **Cơ chế xác thực từ xa bằng toán học (Verifiable Model):** Thay vì tin tưởng tuyệt đối, hệ thống cho phép kiểm chứng thông qua Remote Attestation (AWS ký chứng thực tài liệu mật mã bằng phần cứng để đảm bảo mã thực thi không bị thay đổi) và Reproducible Builds (vận hành trên QuorumOS tối giản, cho phép các bên độc lập tự biên dịch lại mã nguồn từ đầu để đối chiếu tính toàn vẹn).

### Ứng dụng thực tế

- **Embedded Wallets:** Cho phép tích hợp trực tiếp các loại ví không lưu ký (non-custodial) vào ứng dụng phi tập trung với tiêu chuẩn an toàn cấp doanh nghiệp.
- **AI Agent Transactions:** Hỗ trợ các tác nhân trí tuệ nhân tạo (AI Agents) thực thi giao dịch tự động trên chuỗi (on-chain) một cách an toàn theo các chính sách thiết lập sẵn mà không làm lộ khóa cấu hình.

### Tổng kết

Giải pháp của Turnkey tận dụng AWS Nitro Enclaves để thiết lập một quy trình xử lý khóa khép kín trong RAM và tự động giải phóng bộ nhớ sau khi sử dụng. Sự tách biệt hoàn toàn giữa lưu trữ trạng thái (State) và môi trường thực thi phần cứng cô lập (Execution) giúp bảo vệ tài sản số ngay cả khi hạ tầng máy chủ máy ảo bị xâm nhập. Đồng thời, nhờ cơ chế chứng thực từ xa và khả năng tái lập mã nguồn, hệ thống cho phép người dùng kiểm chứng tính toàn vẹn và minh bạch của toàn bộ quy trình mật mã.

### Hình ảnh

![Building secure blockchain key management on AWS Nitro Enclaves at Turnkey](/images/3-BlogsPosted/3.2-Blog2/01.jpeg)

### Link

* Link bài viết gốc: [Building secure, verifiable blockchain key management on AWS Nitro Enclaves at Turnkey | AWS Web3 Blog](https://aws.amazon.com/blogs/web3/building-secure-verifiable-blockchain-key-management-on-aws-nitro-enclaves-at-turnkey/)
* Link bài viết đã update lên gr fb: [AWS Study Group VN | **[SECURITY/Web3] Building secure, verifiable blockchain key management on AWS Nitro Enclaves at Turnkey** | Facebook](https://www.facebook.com/groups/awsstudygroupfcj)
