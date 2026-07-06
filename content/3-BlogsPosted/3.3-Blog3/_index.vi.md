---
title: "Blog 3"
date: 2024-01-01
weight: 3
chapter: false
pre: " <b> 3.3. </b> "
---

# [How AWS DevOps Agent uses multi-agent reasoning to find root causes]

### Khái niệm đề tài

- AWS DevOps Agent là một tác nhân tự trị (autonomous agent) được thiết kế để tự động hóa quy trình vận hành và xử lý sự cố trong hệ thống phân tán. Điểm cốt lõi của công nghệ này là kiến trúc Lập luận đa tác nhân (Multi-Agent Reasoning). Thay vì chỉ tìm kiếm telemetry một cách mù quáng hoặc đưa ra giả định dựa trên định kiến (confirmation bias), hệ thống phân rã các hoạt động vận hành thành nhiều tác nhân chuyên biệt. Các tác nhân này hoạt động song song để đồng thời tạo ra nhiều giả thuyết cạnh tranh, chủ động kiểm chứng bằng cả bằng chứng hỗ trợ lẫn bằng chứng phản bác, từ đó hội tụ chính xác về nguyên nhân gốc rễ (root cause) của sự cố.

### Các điểm chính cần nắm

- **Thách thức của phương pháp điều tra truyền thống:** Khi có cảnh báo, kỹ sư on-call thường dễ mắc bẫy "định kiến xác nhận" (confirmation bias) — đưa ra giả thuyết dựa trên kinh nghiệm ban đầu, tìm một bằng chứng ủng hộ rồi dừng lại, bỏ sót nguyên nhân gốc rễ thực sự bị chôn vùi ở dịch vụ khác. Hệ thống hiện đại không thiếu dữ liệu giám sát (telemetry) mà thiếu khả năng lập luận (reasoning) để xử lý dữ liệu đó một cách khách quan ở quy mô lớn.
- **Bản đồ kiến trúc Topology — Nền tảng của mọi hoạt động:** Trước khi điều tra, hệ thống xây dựng một "Learned Topology" (Bản đồ kiến trúc động) thông qua 4 nguồn: Phân tích stack AWS CloudFormation/CDK, khám phá qua tag bằng AWS Resource Explorer, lập biểu đồ hành vi runtime từ CloudWatch Application Signals (hoặc Datadog, Dynatrace), và tích hợp pipeline CI/CD (GitHub Actions, GitLab CI/CD). Bản đồ này giúp tác nhân hiểu rõ các mối quan hệ phụ thuộc, luồng giao tiếp và lịch sử thay đổi code để khoanh vùng bán kính ảnh hưởng (blast radius) thay vì tìm kiếm mù quáng. Mọi hoạt động này được cô lập an toàn trong các Agent Space riêng biệt.
- **Giai đoạn Triage (Sàng lọc) — Tối ưu hóa cho tốc độ:** Khi nhận tín hiệu từ CloudWatch, PagerDuty, ServiceNow hay Grafana, Triage sẽ kích hoạt ngay lập tức. Cơ chế cốt lõi ở đây là tự động gom nhóm và tương quan (correlate) các cảnh báo liên quan đến cùng một sự kiện. Điều này giảm nhiễu (noise) đáng kể cho kỹ sư, tránh việc một sự cố tạo ra hàng loạt bài toán điều tra phân mảnh. Người vận hành vẫn giữ toàn quyền kiểm soát để tách (unlink) các cảnh báo nếu hệ thống gom sai.
- **Bộ máy lập luận Investigation (Điều tra) — Trung tâm xử lý:** Quy trình phân tích sâu của bộ máy diễn ra khép kín qua các bước chặt chẽ:
  - **Thu thập ngữ cảnh & dữ liệu:** Xác định tài nguyên bị ảnh hưởng, quét biểu đồ topology, kéo các chỉ số metric (đối chiếu với baseline chuẩn), log (CloudWatch, Splunk) và distributed traces.
  - **Tạo giả thuyết song song (Hypothesis Generation):** Hệ thống đưa ra nhiều lý do cùng lúc (do lỗi deploy mới, do bất thường metric, do thắt nút cổ chai tài nguyên như connection pool, CPU...).
  - **Đánh giá và loại trừ:** Ví dụ sự cố chậm ứng dụng checkout, hệ thống kiểm tra 3 giả thuyết cùng lúc. Nó loại trừ lỗi config (vì chỉ đổi log level), loại trừ cổng thanh toán bên thứ ba (vì phát hiện cổng này chậm sau khi ứng dụng đã bị chậm), và xác thực chính xác nguyên nhân do bể kết nối database (connection pool đạt 94%) nhờ dữ liệu thời gian trùng khớp hoàn toàn.
- **Kiến trúc luồng dữ liệu khép kín (Enclave 5 bước):** Để đảm bảo an toàn tuyệt đối, luồng xử lý bên trong môi trường tính toán được chia làm 5 phân hệ:
  - **TLS Fetcher:** Thiết lập kết nối mạng bảo mật từ bên trong.
  - **Parser:** Trích xuất và bóc tách dữ liệu sự cố.
  - **Policy Engine:** Đối chiếu xem giao dịch/sự cố có vi phạm các quy tắc đặt sẵn không.
  - **Notarizer:** Ký chứng nhận giao dịch/kết quả hợp lệ.
  - **Signer:** Xử lý và ký số, sau đó xóa sạch dữ liệu tạm thời trong RAM.
- **Mitigation (Giảm thiểu) — An toàn là trên hết:** Kế hoạch giảm thiểu sự cố được sinh ra tự động bao gồm: chiến lược vá lỗi, quy trình từng bước, kiểm tra xác thực hệ thống, tiêu chí thành công và quy trình rollback (hoàn tác). Để đảm bảo an toàn cho môi trường production, AWS DevOps Agent chỉ có quyền ghi (write) để tạo ticket/support case chứ không tự ý thực thi mã vá lỗi; quyền quyết định nhấn nút áp dụng cấu hình hay dòng lệnh sửa đổi hoàn toàn thuộc về con người.
- **Prevention (Phòng ngừa) — Vòng lặp cải tiến liên tục:** Hệ thống gom cụm (cluster) các sự cố lịch sử có chung bản chất cốt lõi (dù triệu chứng bề ngoài khác nhau) để đưa ra khuyến nghị chủ động. Các khuyến nghị này bao gồm: bổ sung vùng mù giám sát, tinh chỉnh cảnh báo, tối ưu hóa hạ tầng (autoscaling, right-sizing), và thiết lập các rào chắn kiểm soát (deployment gates, chaos engineering). Người vận hành có thể chấp nhận hoặc phản hồi bằng ngôn ngữ tự nhiên để huấn luyện tác nhân thông minh hơn theo thời gian.

### Ứng dụng thực tế

- **Embedded Wallets & Khóa hệ thống:** Đảm bảo các tác vụ kiểm tra phân vùng ứng dụng nhạy cảm hoặc hạ tầng khóa mã hóa (như giải pháp Turnkey/Nitro Enclaves) được giám sát, ghi nhận nhật ký (journal) bất biến và không bị lộ cấu hình khi hệ thống gặp lỗi.
- **AI Agent Transactions:** Hỗ trợ giám sát, phê duyệt và lập luận an toàn cho các tác nhân AI thực hiện giao dịch tự động trên chuỗi (on-chain) hoặc hạ tầng cloud. Khi AI Agent gặp sự cố thực thi, DevOps Agent sẽ tự động nhảy vào phân tích để tìm ra điểm nghẽn chính sách hoặc lỗi kết nối.

### Tổng kết

AWS DevOps Agent đang thay đổi cách ta vận hành hệ thống. Bằng cách ủy thác việc rà soát log, vẽ bản đồ kiến trúc và đối chiếu bằng chứng cho AI, các kỹ sư Backend và DevOps có thể thoát khỏi những đêm thức trắng dò lỗi thủ công. Bạn sẽ bước vào quá trình fix bug với một tâm thế tự tin hơn, bởi mọi giả thuyết đều đã được kiểm chứng bằng data thực tế, kèm theo một lối thoát hiểm an toàn.

### Hình ảnh

![How AWS DevOps Agent uses multi-agent reasoning to find root causes](/images/3-BlogsPosted/3.3-Blog3/01.jpeg)

### Link

* Link bài viết gốc: [How AWS DevOps Agent uses multi-agent reasoning to find root causes | AWS DevOps & Developer Productivity Blog](https://aws.amazon.com/blogs/devops/how-aws-devops-agent-uses-multi-agent-reasoning-to-find-root-causes/)
* Link bài viết update trên gr fb: [AWS Study Group VN | **[How AWS DevOps Agent uses multi-agent reasoning to find root causes]** | Facebook](https://www.facebook.com/groups/awsstudygroupfcj)
