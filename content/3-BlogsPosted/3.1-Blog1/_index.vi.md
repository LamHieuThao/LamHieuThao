---
title: "Blog 1"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---
# [SECURITY] BẢO MẬT CHUỖI CUNG ỨNG PHẦN MỀM THEO CHUẨN AWS WELL-ARCHITECTED

### Khái niệm đề tài

- Bảo mật chuỗi cung ứng phần mềm (Software Supply Chain Security) trong khung chuẩn AWS Well-Architected là tập hợp các nguyên tắc thiết kế và thực hành kỹ thuật nhằm bảo vệ toàn bộ vòng đời của phần mềm — từ việc quản lý các gói phụ thuộc bên thứ ba, bảo vệ định danh của nhà phát triển, đến việc xác thực tính toàn vẹn của mã nguồn trước khi triển khai (deployment). Mô hình này giúp các tổ chức xây dựng một hệ thống phòng thủ theo chiều sâu (defense in depth), đảm bảo rằng ngay cả khi một mắt xích hoặc một thông tin xác thực bị thỏa hiệp, các cơ chế kiểm soát đa lớp sẽ ngăn chặn sự cố lan rộng ra toàn bộ hệ thống.

### Các điểm chính cần nắm

- **Thách thức của các cuộc tấn công chuỗi cung ứng hiện đại:** Các vụ tấn công nhắm vào các kho lưu trữ công khai như npm Registry (ví dụ: các mã độc Shai-Hulud, Chalk/Debug, hay việc lạm dụng token) ngày càng tinh vi và diễn ra trên quy mô lớn. Nhà phát triển cần các cơ chế ngăn chặn việc chiếm đoạt tài khoản khi thông tin xác thực bị đánh cắp; trong khi đó, người tiêu thụ phần mềm (package consumers) cần các lớp phòng thủ để phát hiện, chặn đứng việc triển khai gói độc hại và giảm thiểu thiệt hại.
- **Giảm thiểu rủi ro lộ thông tin xác thực (Credentials):** Để hạn chế rủi ro, hệ thống bắt buộc phải sử dụng thông tin xác thực tạm thời (temporary credentials) bằng cách liên kết người dùng từ một nhà cung cấp định danh trung tâm (IdP) vào AWS và áp dụng IAM roles. Đồng thời, cần thực hiện nghiêm ngặt nguyên tắc quyền hạn tối thiểu (least privilege) và tiến hành kiểm toán, xoay vòng khóa định kỳ. Nếu tương tác với dịch vụ bên thứ ba không hỗ trợ credential tạm thời, thông tin phải được lưu trữ tập trung tại AWS Secrets Manager kèm theo cơ chế tự động xoay vòng và log kiểm toán chuyên biệt.
- **Chiến lược phòng thủ theo chiều sâu (Defense in Depth):** Kể cả khi áp dụng quyền hạn tối thiểu, một tài khoản bị chiếm đoạt vẫn có thể phát tán các gói mã nguồn độc hại. Do đó, hệ thống cần thiết lập các rào chắn chiến lược như: kích hoạt xác thực đa yếu tố (MFA), phân tách các IAM roles khác nhau cho từng khối công việc nhạy cảm, và áp dụng quy trình phê duyệt (approval workflows) một cách có chọn lọc để cân bằng giữa tốc độ triển khai và tính bảo mật.
- **Ký xác thực Artifact và Quản lý SBOM:** Mọi thành phẩm phần mềm (artifacts) cần được ký số để chứng minh nguồn gốc xuất xứ. Việc này kết hợp với lưu trữ tập trung và lập Danh mục nguyên vật liệu phần mềm (Software Bills of Materials - SBOM) sẽ tạo ra lớp bảo vệ chống giả mạo. Tại thời điểm triển khai, các bộ điều khiển nhập khóa (admission controllers) như Kyverno trên Amazon EKS hoặc các lifecycle hooks trên Amazon ECS sẽ thực hiện đối chiếu và xác thực chữ ký số trước khi cho phép bất kỳ mã nguồn nào chạy trong cụm container.
- **Tập trung hóa quản lý phụ thuộc (Centralized Dependency Management):** Bằng cách tập trung hóa việc quản lý các package và thư viện phụ thuộc, tổ chức có thể chủ động xác thực và phê duyệt các thư viện bên thứ ba trước khi chúng được nhúng vào ứng dụng. Cơ chế này cho phép các đội ngũ an ninh thông tin nhanh chóng kiểm toán và quét toàn bộ hệ thống để tìm ra những package bị thỏa hiệp khi có sự cố xảy ra. Đối với các gói mã nguồn mở (như npm), việc kiểm tra chứng thực nguồn gốc (provenance attestations) trước khi sử dụng là một tín hiệu chi phí thấp giúp đảm bảo tính toàn vẹn.
- **Giám sát liên tục và Phân tích nhật ký tập trung:** Hệ thống yêu cầu bật tính năng ghi nhật ký (logging) cho cả ứng dụng lẫn dịch vụ, sau đó tổng hợp về một trung tâm phân tích để phát hiện các hành vi ký số bất thường (như ký từ IP lạ, khung giờ bất thường). AWS cung cấp bộ công cụ phối hợp mạnh mẽ: Amazon GuardDuty liên tục giám sát các hành vi độc hại và cuộc gọi API bất thường; các phát hiện được tập trung tại AWS Security Hub; và AWS Config chịu trách nhiệm thực thi cũng như giám sát các cấu hình bảo mật tiêu chuẩn.

### Ứng dụng thực tế

- **Hạ tầng CI/CD an toàn:** Nhà phát triển có thể kích hoạt tính năng xác thực provenance bằng cách chạy lệnh `npm publish --provenance` ngay từ môi trường CI/CD được hỗ trợ như GitHub Actions hoặc AWS CodePipeline để chứng minh tính minh bạch của mã nguồn.
- **Xác thực tự động container trong Kubernetes:** Triển khai các chính sách Kyverno trên Amazon EKS nhằm tự động từ chối (block) các container image chưa qua kiểm quét bảo mật hoặc thiếu chữ ký hợp lệ từ hệ thống Build trung tâm, ngăn chặn mã độc lọt vào môi trường chạy thực tế.

### TỔNG KẾT

Bảo mật chuỗi cung ứng phần mềm trên Cloud không chỉ dừng lại ở việc viết code an toàn, mà nó là một chiến lược toàn diện: xây dựng kiến trúc nhiều lớp (defense in depth), triệt tiêu đặc quyền dài hạn và duy trì sự kiểm soát, giám sát tuyệt đối đối với mọi artifact trước khi đưa vào hệ thống vận hành.

### Hình ảnh

![Bảo mật chuỗi cung ứng phần mềm theo chuẩn AWS Well-Architected](/images/3-BlogsPosted/3.1-Blog1/01.jpeg)

![Defense in depth cho software supply chain](/images/3-BlogsPosted/3.1-Blog1/02.jpeg)

![Giám sát và kiểm soát artifact](/images/3-BlogsPosted/3.1-Blog1/03.jpeg)

### Link

* Link bài viết gốc: [Well-architected best practices for software supply chain security | AWS Security Blog](https://aws.amazon.com/blogs/security/well-architected-best-practices-for-software-supply-chain-security/)
* Link bài viết đã update lên gr fb: [AWS Study Group VN | # **[SECURITY] BẢO MẬT CHUỖI CUNG ỨNG PHẦN MỀM THEO CHUẨN AWS WELL-ARCHITECTED** | Facebook](https://www.facebook.com/groups/awsstudygroupfcj)
