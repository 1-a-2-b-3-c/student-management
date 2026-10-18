# 1. Kết quả công việc tuần 2

- **Hoàn thiện tầng xử lý nghiệp vụ (Backend):** Cấu hình thành công 4 hàm AWS Lambda chạy trên môi trường `Python 3.12` (`CreateStudent`, `GetStudents`, `UpdateStudent`, `DeleteStudent`) để thực thi các chức năng CRUD tương ứng lên bảng `Students` của DynamoDB (Đặt trong thư mục `/backend`).
- **Kiểm thử và tối ưu hóa thao tác:** Tạo các tập JSON Test Event để giả lập request từ API Gateway và thực hiện Unit Test trực tiếp 4 hàm trên AWS Console.
- **Tích hợp API Gateway (RESTful API):** 
  - Khởi tạo thành công REST API (`StudentAPI`), cấu hình Resource `/students` và ánh xạ 4 HTTP Methods thông qua **Lambda Proxy Integration**.
  - Thiết lập thành công chính sách bảo mật CORS, cho phép các HTTP request từ nguồn bên ngoài truy cập vào hệ thống.
  - Đã triển khai API lên môi trường `dev` và trích xuất thành công Invoke URL.
- **Kiểm thử hệ thống End-to-End:** 
  - Xây dựng file `index_test.html` tích hợp JavaScript Fetch API để giao tiếp với Invoke URL.
  - Chạy kiểm thử luồng dữ liệu 2 chiều thành công: Giao diện web lấy và hiển thị dữ liệu chính xác từ DynamoDB; các thao tác thêm, sửa, xóa sinh viên từ giao diện hoạt động đúng chức năng đã cài đặt.
- **Hoàn thiện báo cáo:** Đã hoàn thiện báo cáo tiến độ chi tiết tại `/docs/reports/week2-report.md` và đính kèm ảnh `screenshots` minh chứng theo đúng định dạng tại `/docs/screenshots/week2/`.

---

# 2. Phân công công việc

| Thành viên | Nội dung công việc | Số giờ thực tế |
| :--- | :--- | :--- |
| Phạm Trần Đức Lương | Nghiên cứu `boto3`, khởi tạo và viết mã Python cho hàm `CreateStudent` và `GetStudents` (Bao gồm logic quét toàn bảng và truy vấn qua GSI `major-index`). | 3.5 giờ |
| Phạm Trần Đức Lương | Viết mã Python cho `UpdateStudent` và `DeleteStudent`. | 2.0 giờ |
| Phạm Trần Đức Lương | Thiết lập các Test Event (định dạng JSON) để kiểm thử độc lập 4 hàm trực tiếp trên AWS Lambda. Thực hiện Unit Test trực tiếp 4 hàm trên AWS Console. Điều chỉnh `UpdateStudent` và `DeleteStudent` để áp dụng `ConditionExpression` để xử lý ngoại lệ `ConditionalCheckFailedException` và các lỗi nghiệp vụ khác gặp phải. Tổng hợp hình ảnh và định dạng báo cáo. | 4.0 giờ |
| Phan Nguyễn Quốc Hoàng | Thiết lập quyền thực thi `LabRole`. Cấu hình API Gateway (Resource `/students`, ánh xạ 4 HTTP Methods qua Lambda Proxy Integration). | 3.0 giờ |
| Phan Nguyễn Quốc Hoàng | Cấu hình bảo mật CORS, thực hiện Deploy API lên môi trường `dev` và trích xuất Invoke URL. | 2.0 giờ |
| Phan Nguyễn Quốc Hoàng | Viết mã JavaScript tích hợp Fetch API vào `index_test.html`. Trực tiếp kiểm thử End-to-End luồng dữ liệu. Tổng hợp hình ảnh và định dạng báo cáo. | 4.5 giờ |

---

# 3. Kế hoạch tuần 3

- **Triển khai Static Website Hosting:**
  - Chuẩn bị mã nguồn Frontend (`index.html` hoàn chỉnh).
  - Tải file lên Amazon S3 Bucket đã khởi tạo từ Tuần 1.
  - Kích hoạt tính năng Static Website Hosting cho Bucket.
- **Cấu hình quyền truy cập (Public Access):**
  - Vô hiệu hóa Block Public Access trên S3 Bucket.
  - Thiết lập và rà soát S3 Bucket Policy để cấp quyền đọc công khai cho mọi người dùng truy cập vào trang web, đảm bảo tuân thủ nguyên tắc bảo mật của AWS Learner Lab.
- **Kiểm thử nghiệm thu E2E (Final Testing):**
  - Chạy thử toàn bộ các kịch bản CRUD thông qua Endpoint URL do Amazon S3 cung cấp (không chạy local file).
  - Đánh giá độ trễ và khả năng xử lý phản hồi của giao diện.
- **Tổng kết và đóng gói dự án:**
  - Cập nhật và hoàn thiện báo cáo tổng kết toàn khóa.
  - Cập nhật sơ đồ kiến trúc hệ thống thực tế (nếu có tinh chỉnh so với thiết kế Tuần 1).
  - Thực hiện các bước End Lab an toàn để bảo vệ tài khoản và tránh phát sinh chi phí ngoài luồng.