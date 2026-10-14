# 1. Kết quả công việc tuần 1

- Tìm hiểu về đề tài và các dịch vụ sử dụng trong đề tài.
- Sơ đồ kiến trúc và thiết kế CSDL (Khóa chính, GSI) đã được chốt.
- Môi trường lưu trữ Web (S3) và Database (DynamoDB) đã Active trên Region us-east-1 và sẵn sàng kết nối.
- Đảm bảo không phát sinh chi phí lãng phí trong Lab nhờ dùng On-demand và đã End Lab an toàn.  
- Đã hoàn thiện báo cáo tại: `/docs/reports/week1-report.md` và bổ sung hình ảnh tại: `/docs/screenshots/week1/`.

# 2. Phân công công việc

| Thành viên | Nội dung công việc | Số giờ thực tế |
| :--- | :--- | :--- |
| Chung cả nhóm | Tìm hiểu về đề tài và các dịch vụ sử dụng trong đề tài | 4 giờ |
| Phan Nguyễn Quốc Hoàng | Nghiên cứu AWS Student Guide | 1 giờ |
| Phan Nguyễn Quốc Hoàng | Thao tác trên console: Tạo S3, cấu hình Policy, tạo bảng DynamoDB (GSI, On-demand), gắn Tag (Thành viên còn lại theo dõi việc thực hiện thông qua Google Meet). | 3 giờ |
| Phạm Trần Đức Lương | Thiết kế kiến trúc, lập sơ đồ kiến trúc hệ thống và thiết kế sơ bộ CSDL | 2 giờ |
| Phạm Trần Đức Lương | Tổng hợp viết báo cáo tuần 1 | 2 giờ |

# 3. Kế hoạch tuần 2

- **Nghiên cứu:** Tìm hiểu thư viện `boto3` (AWS SDK for Python) để tương tác với DynamoDB.
- **Thực hành AWS:**
  - Tạo 4 hàm AWS Lambda tương ứng với 4 thao tác CRUD (GET, POST, PUT, DELETE).
  - Gắn LabRole cho Lambda để cấp quyền đọc/ghi vào bảng Students.
  - Viết mã nguồn Python xử lý request, query GSI major-index và trả về HTTP response hợp lệ.
- **Kiểm thử:** Test độc lập các hàm Lambda ngay trên AWS Console trước khi gắn vào API Gateway.