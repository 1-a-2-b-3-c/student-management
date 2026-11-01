# 1. Kết quả công việc tuần 4

- **Cải tiến logic xử lý ngoại lệ Backend:** Rà soát và cập nhật mã nguồn Python cho 4 hàm Lambda (`GetStudents`, `CreateStudent`, `UpdateStudent`, `DeleteStudent`) trực tiếp trên AWS Lambda Console, đảm bảo xử lý triệt để các lỗi nghiệp vụ và trả về thông báo lỗi rõ ràng.
- **Tối ưu hóa bộ lọc giao diện Frontend:** Cập nhật tệp `index.html` bổ sung chức năng tìm kiếm, lọc danh sách sinh viên theo Mã số (`student_id`) hoặc Chuyên ngành (`major`) sử dụng Global Secondary Index (GSI).
- **Trích xuất tài liệu chuẩn hóa OpenAPI:** Sinh và xuất tài liệu đặc tả API chuẩn OpenAPI 3 (định dạng JSON) từ AWS API Gateway, lưu trữ phục vụ tài liệu hóa hệ thống.
- **Xây dựng bộ kiểm thử Postman toàn diện:** Khởi tạo Postman Collection và kiểm thử các kịch bản thành công (200 OK) và ngoại lệ (400 Bad Request, 404 Not Found, thiếu trường dữ liệu, sai định dạng).
- **Nghiệm thu toàn hệ thống trên môi trường Cloud:** Chạy kiểm thử End-to-End toàn bộ luồng dữ liệu thao tác trực tiếp trên giao diện tĩnh Amazon S3 tĩnh và xác thực với các thông báo Toast Notification. 
- **Theo dõi giám sát & Đánh giá chi phí:** Kiểm tra quá trình giám sát lưu lượng tại CloudWatch đã cài đặt ở tuần trước; phân tích chi phí tiêu thụ cuối kỳ qua Billing Dashboard và Cost Explorer đảm bảo chi phí luôn dưới mức tối thiểu.
- **Tổng kết dự án:** Xóa tài nguyên, viết báo cáo đồ án và quay video demo.

---

# 2. Phân công công việc

| Thành viên | Nội dung công việc | Số giờ thực tế |
| :--- | :--- | :--- |
| Phạm Trần Đức Lương | Rà soát và viết lại logic xử lý lỗi cho 4 hàm Lambda (`Create`, `Get`, `Update`, `Delete`) trực tiếp trên console nhằm tối ưu mã nguồn và bẫy lỗi nghiệp vụ chặt chẽ. | 1 giờ |
| Phạm Trần Đức Lương | Cập nhật file Frontend `index.html` bổ sung UI/UX cho tính năng tìm kiếm, lọc danh sách sinh viên qua API; xử lý logic hiển thị các bảng thông báo xác nhận và thông báo lỗi. | 0.5 giờ |
| Phạm Trần Đức Lương | Tìm hiểu và xây dựng bộ test Postman Collection toàn diện. | 1 giờ |
| Phạm Trần Đức Lương | Quay video demo phần test Postman và viết báo cáo phần Introduction, Testing and Monitoring, Problems Encountered and Lessons Learned, Team Contribution and AI Usage Declaration | 6 giờ |
| Phan Nguyễn Quốc Hoàng | Kiểm thử giao diện E2E trên Web S3: Test các thao tác thêm, sửa, xóa, lọc kèm hiển thị lỗi thông báo khi trùng ID, sai định dạng email, sai GPA. | 1.0 giờ |
| Phan Nguyễn Quốc Hoàng | Tìm hiểu và xuất file đặc tả OpenAPI 3 từ API Gateway. | 0.5 giờ |
| Phan Nguyễn Quốc Hoàng | Đọc, phân tích và trích xuất báo cáo Cost & Billing, CloudWatch Metrics. Viết báo cáo tuần 4. | 1.5 giờ |
| Phan Nguyễn Quốc Hoàng | Quay video phần cài đặt dự án và test E2E; viết báo cáo phần System Architecture, System Implementation, Security Configuration, Cost Analysis | 6.0 giờ |