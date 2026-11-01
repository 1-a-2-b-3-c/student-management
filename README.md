# Hệ thống Quản lý Sinh viên (Student Management System)

Ứng dụng **REST API Quản lý Sinh viên** xây dựng theo kiến trúc không máy chủ (Serverless) trên nền tảng **Amazon Web Services (AWS)** cho đồ án môn học **Điện toán đám mây (Cloud Computing)**.

---

## Thông tin đồ án

- **Môn học:** Điện toán đám mây (Cloud Computing)
- **Giảng viên hướng dẫn:** ThS. Huỳnh Xuân Phụng
- **Nhóm thực hiện:**
  - **Phan Nguyễn Quốc Hoàng** — MSSV: `24110219`
  - **Phạm Trần Đức Lương** — MSSV: `24110281`
- **Môi trường triển khai:** AWS Academy Learner Lab
- **AWS Region:** `us-east-1` (N. Virginia)

---

## Kiến trúc hệ thống tổng quan

Hệ thống hoạt động theo mô hình Serverless hoàn toàn, tối ưu chi phí và tự động co giãn:

<div align="center">
  <figure>
    <img src="docs\architecture\project_architecture.png" alt="project_architecture" style="width: 85%; max-width: 850px;">
  </figure>
</div>

---

## Cấu trúc thư mục dự án

```text
.
├── backend/
│   ├── create_student.py
│   ├── delete_student.py
│   ├── get_students.py
│   └── update_student.py
├── docs/
│   ├── architecture/
│   │   └── project_architecture.png
│   ├── demo_videos/
│   │   └── demo_project_video.mp4
│   ├── reports/
│   │   ├── project-report.pdf
│   │   ├── week1-report.md
│   │   ├── week2-report.md
│   │   ├── week3-report.md
│   │   └── week4-report.md
│   └── screenshots/
│       ├── week1/
│       ├── week2/
│       ├── week3/
│       └── week4/
├── frontend/
│   ├── index.html
│   └── index_test.html
├── infrastructure/
│   ├── api-gateway/
│   │   ├── access-log-format.json
│   │   └── openapi.yaml
│   ├── cloudwatch/
│   ├── dynamodb/
│   │   ├── example_values.json
│   │   └── table.json
│   ├── iam/
│   └── s3/
│       └── bucket_policy.json
└── worklogs/
    ├── week1-worklog.md
    ├── week2-worklog.md
    ├── week3-worklog.md
    └── week4-worklog.md
```

---

## Báo cáo tiến độ & Nhật ký công việc

| Tuần | Nội dung công việc chính | Báo cáo chi tiết | Nhật ký công việc (Worklog) |
| :---: | :--- | :---: | :---: |
| **Tuần 1** | Tìm hiểu dịch vụ AWS, thiết kế kiến trúc, khởi tạo S3 Bucket & bảng DynamoDB | [week1-report.md](docs/reports/week1-report.md) | [week1-worklog.md](worklogs/week1-worklog.md) |
| **Tuần 2** | Triển khai AWS Lambda với API Gateway, thử nghiệm trên file index_test.html độc lập | [week2-report.md](docs/reports/week2-report.md) | [week2-worklog.md](worklogs/week2-worklog.md) |
| **Tuần 3** | Nâng cao bảo mật cho API Gateway bằng cách bắt buộc sử dụng API Key, tạo và liên kết Usage Plan với API Key, triển khai ứng dụng Web lên Amazon S3 dưới dạng Static Website và thực hiện kiểm thử End-to-End trực tiếp trên môi trường Cloud | [week3-report.md](docs/reports/week3-report.md) | [week3-worklog.md](worklogs/week3-worklog.md) |
| **Tuần 4** | Quay video demo, viết báo cáo, dọn dẹp tài nguyên hệ thống | [week4-report.md](docs/reports/week4-report.md) | [week4-worklog.md](worklogs/week4-worklog.md) |

## Kết quả thu được  
* **Báo cáo dự án**: [project-report.pdf](docs/reports/project-report.pdf)
* **Video demo**: [demo_project_video.mp4](docs/demo_videos/demo_project_video.mp4)