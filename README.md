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
student-management/
├── backend/                        # Mã nguồn các hàm AWS Lambda & cấu hình API Gateway
├── frontend/                       # Mã nguồn giao diện Web tĩnh lưu trữ trên S3
├── infrastructure/                 # Cấu hình hạ tầng AWS (IaC / JSON Template)
│   ├── dynamodb/
│   │   ├── table.json              # Định nghĩa bảng DynamoDB Students & GSI major-index
│   │   └── example_values.json     # Dữ liệu mẫu kiểm thử
│   └── s3/
│       └── bucket_policy.json      # S3 Bucket Policy cấp quyền đọc public cho website
├── docs/                           # Tài liệu kỹ thuật, báo cáo & minh chứng
│   ├── architecture/
│   │   └── project_architecture.png# Sơ đồ kiến trúc Serverless
│   ├── reports/
│   │   └── week1-report.md         # Báo cáo kết quả Tuần 1
│   └── screenshots/
│       └── week1/                  # Ảnh chụp minh chứng thao tác trên AWS Console
├── worklogs/                       # Nhật ký phân công và tiến độ công việc
│   └── week1-worklog.md            # Nhật ký phân công Tuần 1
└── README.md
```

---

## Báo cáo tiến độ & Nhật ký công việc

| Tuần | Nội dung công việc chính | Báo cáo chi tiết | Nhật ký công việc (Worklog) |
| :---: | :--- | :---: | :---: |
| **Tuần 1** | Tìm hiểu dịch vụ AWS, thiết kế kiến trúc, khởi tạo S3 Bucket & bảng DynamoDB | [week1-report.md](docs/reports/week1-report.md) | [week1-worklog.md](worklogs/week1-worklog.md) |
| **Tuần 2** |  |  |
| **Tuần 3** |  |  |
| **Tuần 4** |  |  |
