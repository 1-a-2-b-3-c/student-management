# 1. Kết quả công việc tuần 3

- **Bổ sung kiểm soát truy cập và lưu lượng API:** Tạo API Key `StudentWebKey`, Usage Plan `BasicPlan` (Rate 5 requests/second, Burst 10 requests, Quota 1000 requests/month), sau đó liên kết với stage `dev` của `StudentAPI`.
- **Hoàn thiện và triển khai Frontend:** Cập nhật `frontend/index.html` để gửi API Key trong header `x-api-key`, tải giao diện lên S3 Static Website Hosting và kiểm thử trực tiếp trên website.
- **Kiểm thử tích hợp E2E:** Thực hiện các thao tác tạo, cập nhật và xóa sinh viên từ giao diện; xác nhận dữ liệu đi qua API Gateway, Lambda và DynamoDB.
- **Thiết lập giám sát:** Cấu hình quyền ghi log cho API Gateway bằng `LabRole`, tạo CloudWatch Log Group, bật Access Logging cho stage `dev`, theo dõi request count và latency, đồng thời xuất dữ liệu Usage Plan.
- **Lưu mã nguồn và minh chứng:** Bổ sung định dạng access log tại `/infrastructure/api-gateway/access-log-format.json`, báo cáo tại `/docs/reports/week3-report.md` và ảnh minh chứng tại `/docs/screenshots/week3/`.

# 2. Phân công công việc


| Thành viên | Nội dung công việc | Số giờ ước tính |
| :--- | :--- | :--- |
| Phan Nguyễn Quốc Hoàng | Tạo API Key, cấu hình Usage Plan và giới hạn Rate/Burst/Quota; liên kết Usage Plan với stage `dev` và API Key. | 3.0 giờ |
| Phan Nguyễn Quốc Hoàng | Cấu hình quyền ghi log cho API Gateway bằng `LabRole`, tạo CloudWatch Log Group, bật Access Logging và kiểm tra log/metrics. Tổng hợp hình ảnh và định dạng báo cáo. | 4.0 giờ |
| Phan Nguyễn Quốc Hoàng | Tải Frontend lên S3, kiểm thử E2E trên website và xuất dữ liệu Usage Plan. | 1.5 giờ |
| Phạm Trần Đức Lương | Cập nhật giao diện `frontend/index.html`, tích hợp API URL và API Key lấy từ AWS Console; gửi API Key trong header `x-api-key` khi gọi API. Tổng hợp hình ảnh và định dạng báo cáo. | 4.5 giờ |
| Phạm Trần Đức Lương | Kiểm thử các chức năng trên website S3, xác nhận thao tác tạo, cập nhật và xóa sinh viên hoạt động bình thường. | 2.0 giờ |
| Phạm Trần Đức Lương | Soạn định dạng JSON cho Access Log của API Gateway, xác định các thông tin request cần ghi nhận. | 1.5 giờ |

# 3. Kế hoạch tuần 4

- **Kiểm thử tổng thể:**
  - Rà soát các API CRUD, API Key và Usage Plan.
  - Kiểm thử giao diện S3 và luồng dữ liệu của hệ thống.
  - Kiểm tra các trường hợp thành công, lỗi và giới hạn truy cập.
- **Hoàn thiện tài liệu và bàn giao:**
  - Rà soát báo cáo và sơ đồ kiến trúc thực tế.
  - Hoàn thiện tài liệu OpenAPI và bộ test Postman.
  - Chuẩn bị nội dung demo/video theo yêu cầu môn học.
- **Tối ưu và kết thúc sử dụng AWS:**
  - Kiểm tra CloudWatch logs/metrics và mức sử dụng tài nguyên.
  - Tổng hợp chi phí sử dụng.
  - Chụp và lưu đầy đủ minh chứng cần thiết.
  - Dừng hoặc xóa tài nguyên không còn cần thiết sau buổi làm việc.
