---
title: "Event 3"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 4.3. </b> "
---


### Event Objectives

- Hiểu chiến lược phát triển sản phẩm (POC → MVP) và triển khai hạ tầng trên AWS Cloud.
- Nắm được kiến trúc Voice AI (Speech-to-Speech hoặc STT → LLM → TTS) và các thách thức khi triển khai cho tiếng Việt.
- Tìm hiểu AI Agent (DevOps Agent, MCP) để tự động hóa xử lý sự cố và giảm thời gian khôi phục hệ thống (MTTR).
- Khám phá ứng dụng AI (Amazon Q) trong tuyển dụng như: sàng lọc CV, chấm điểm ứng viên và tối ưu quy trình phỏng vấn.
- Hiểu cách thiết lập kết nối bảo mật giữa AI và dữ liệu nội bộ doanh nghiệp thông qua MCP Server và VPC riêng tư.

---

### Agenda Overview

**Thời gian:** 9:00 AM – 12:00 PM, Thứ Bảy, ngày 27 tháng 6 năm 2026  
**Địa điểm:** AWS Vietnam Office

---

## Điểm nổi bật

### 1. Chào mừng & Giới thiệu

- Check-in và networking giữa người tham dự.
- Giới thiệu mục tiêu, nội dung trọng tâm.
- Tổng quan nội dung sự kiện

---

### 2. Tổng quan về các dịch vụ có trong buổi Workshop

Buổi workshop tập trung giới thiệu tập trung vào 5 nhóm chính:

- Vận hành hệ thống và chiến lược startup
- Voice AI trong doanh nghiệp
- Tự động hóa vận hành với DevOps Agent
- AI và quản trị nguồn nhân lực
- Bảo mật và kết nối hệ thống, nhằm mang đến góc nhìn thực tế, đa chiều về việc ứng dụng AWS và AI trong vận hành, sản phẩm, nhân sự và bảo mật doanh nghiệp.

---

## Nội dung chính của Workshop

### 1. AgenticOps For Your Cloud (vận hành hệ thống và chiến lược startup)

**Diễn giả:** Steve Trần  
**Vị trí:** CTO/ Founder Cloud Thinker

#### **Nội dung chính**

- Chia sẻ về quá trình chuyển đổi hạ tầng từ máy chủ truyền thống (on-premise) lên AWS Cloud. Anh Steve Trần nhấn mạnh tư duy thực thi (execution), tầm quan trọng của việc xây dựng sản phẩm theo lộ trình từ POC (Proof of Concept) đến MVP (Minimum Viable Product), cũng như cách kết nối với các khách hàng chiến lược (Champion customers) như F88 hoặc FPT để giải quyết các bài toán kinh doanh thực tế.

#### **Kiến thức tiếp thu**

- Hiểu cách tiếp cận thực tế khi chuyển đổi hạ tầng vận hành lên Cloud trong bối cảnh startup.
- Nắm được lộ trình phát triển sản phẩm từ POC đến MVP.
- Học được kinh nghiệm tìm kiếm và hợp tác với khách hàng chiến lược (Champion customers) để giải quyết bài toán kinh doanh thực tế.

---

### 2. Building Voice Agent at Scale (Voice AI trong doanh nghiệp)

**Diễn giả:** Doanh Hoàng Hiếu Nghị, Kiệt Trần, Trung Vũ  
**Vị trí:** AI Engineer Renova Cloud, AI Engineer AWS Student Builder Group, CEO Revve AI

#### **Nội dung chính**

- Giới thiệu các kiến trúc phổ biến để xây dựng Voice AI, từ mô hình Speech-to-Speech trực tiếp đến mô hình 3 thành phần (Speech-to-Text → LLM → Text-to-Speech). Các diễn giả tập trung phân tích những thách thức khi triển khai tại thị trường Việt Nam: dữ liệu giọng nói khan hiếm (low-resource language), khó khăn trong nhận diện giới tính và giọng vùng miền, cùng kỹ thuật quản lý ngữ cảnh để tránh lỗi ngắt lời người dùng (interruption handling). Anh Hiếu Nghị phụ trách phần điều phối và kiến trúc mô hình; Anh Kiệt chia sẻ góc nhìn sản phẩm thực tế và demo kỹ thuật; Anh Trung Đ đóng góp chuyên sâu về kỹ thuật LLM và Speech-to-Text.

#### **Kiến thức tiếp thu**

- Nắm được các kiến trúc phổ biến (Speech-to-Speech, hoặc STT-LLM-TTS) để xây dựng một Voice Agent.
- Hiểu các rào cản kỹ thuật đặc thù khi ứng dụng Voice AI cho thị trường và ngôn ngữ Việt Nam (dữ liệu khan hiếm, giọng vùng miền, giới tính).
- Biết đến kỹ thuật quản lý ngữ cảnh hội thoại để xử lý tình huống ngắt lời, cải thiện trải nghiệm người dùng.

---

### 3. AWS DevOps Agent Your Always Available Operations Teammate (tự động hóa với DevOps Agent)

**Diễn giả:** Bao Phan, Nguyen Nguyen  
**Vị trí:** Cloud Engineer – Cloud Kinetics.

#### **Nội dung chính**

- Trình bày cách tự động hóa quy trình điều tra sự cố bằng DevOps Agent, bao gồm các bước: phân loại log, điều tra nguồn gốc sự cố, đề xuất phương án xử lý và cải thiện hệ thống. Điểm nhấn của phần chia sẻ là việc ứng dụng Model Context Protocol (MCP) để kết nối AI Agent với hệ thống vận hành, giúp tối ưu hóa đáng kể thời gian hồi phục sự cố (MTTR). Chị Bảo là diễn giả chính về quy trình tự động hóa điều tra sự cố; Anh Nguyên hỗ trợ trình bày sâu về kỹ thuật kết nối hệ thống qua MCP.

#### **Kiến thức tiếp thu**

- Hiểu quy trình tự động hóa điều tra sự cố: phân loại log, điều tra nguồn gốc, đề xuất phương án, cải thiện hệ thống.
- Nắm được khái niệm và vai trò của Model Context Protocol (MCP) trong việc kết nối AI Agent với hệ thống vận hành.
- Nhận thấy lợi ích của việc giảm MTTR đối với độ ổn định và độ tin cậy của hệ thống.

---

### 4. AI – Powered Productivity Workforce Planning For Enterprise (AI và quản trị nguồn nhân lực)

**Diễn giả:** Truong Tran, Anh Dang  
**Vị trí:** AI Solution Sales Noventiq

#### **Nội dung chính**

- Giới thiệu giải pháp ứng dụng Amazon Q để hỗ trợ bộ phận nhân sự (HR): tự động hóa khâu sàng lọc CV, phân tích dữ liệu ứng viên dựa trên JD (Job Description), chấm điểm ứng viên và tối ưu quy trình phỏng vấn. Bài chia sẻ nhấn mạnh vào việc tăng năng suất cho bộ phận nhân sự cũng như tính bảo mật của dữ liệu nội bộ. Anh Trường trình bày về giải pháp Amazon Q và kỹ thuật bảo mật hệ thống; Chị Minh Anh chia sẻ về các bài toán thực tế của bộ phận HR trong kỷ nguyên AI.

#### **Kiến thức tiếp thu**

- Hiểu cách ứng dụng Amazon Q vào các nghiệp vụ nhân sự cụ thể: sàng lọc CV, phân tích và chấm điểm ứng viên theo JD.
- Nhận thấy tiềm năng tăng năng suất và hỗ trợ ra quyết định chính xác hơn trong tuyển dụng nhờ AI.
- Nắm được tầm quan trọng của việc đảm bảo bảo mật dữ liệu nội bộ khi ứng dụng AI vào nghiệp vụ HR.

---

### 5. Building Secure private MCP for Quick (Bảo mật & Kết nối hệ thống)

**Diễn giả:** Toan Nguyen, Truong Tran  
**Vị trí:** AI Solution Sales Noventiq, AWS Security Builder.

#### **Nội dung chính**

- Đi sâu hơn vào kỹ thuật thiết lập MCP server để kết nối Amazon Q với các nguồn dữ liệu bên thứ ba một cách riêng tư, không đi qua Internet công cộng, nhằm đảm bảo an toàn bảo mật trong môi trường VPC (Virtual Private Cloud) của doanh nghiệp.

#### **Kiến thức tiếp thu**

- Hiểu kỹ thuật thiết lập MCP server để kết nối AI với nguồn dữ liệu bên thứ ba một cách an toàn.
- Nắm được cách triển khai kết nối riêng tư (private connectivity) trong môi trường VPC, không đi qua Internet công cộng.
- Nhận thức rõ hơn về tầm quan trọng của bảo mật khi tích hợp AI vào hệ thống dữ liệu nội bộ doanh nghiệp.

---

### Minh chứng đã tham gia event

![Minh chứng đã tham gia event](/images/4-EventParticipated/4.3-Event3/01.png)

![Minh chứng đã tham gia event](/images/4-EventParticipated/4.3-Event3/02.png)

---

> Thông qua 5 phiên chia sẻ, em đã có cái nhìn thực tế và đa chiều hơn về việc ứng dụng AWS và AI trong doanh nghiệp — từ tư duy thực thi khi vận hành hệ thống và phát triển sản phẩm startup, xây dựng Voice AI cho thị trường Việt Nam, tự động hóa DevOps bằng AI Agent, ứng dụng AI trong quản trị nhân sự, đến kỹ thuật đảm bảo bảo mật khi kết nối AI với dữ liệu nội bộ. Đặc biệt, em nhận thấy xu hướng chung là AI đang được tích hợp ngày càng sâu vào các quy trình vận hành và nghiệp vụ thực tế, đòi hỏi người làm công nghệ không chỉ nắm vững kỹ thuật mà còn cần tư duy thực thi, khả năng giải quyết các bài toán đặc thù (rào cản ngôn ngữ, bảo mật dữ liệu) khi triển khai vào thực tế tại Việt Nam.
