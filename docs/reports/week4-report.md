# 1. Mục tiêu tuần 4

Sau khi triển khai hệ thống và cấu hình giám sát trong các tuần trước, tuần 4 tập trung cập nhật logic xử lý dữ liệu, kiểm thử tổng thể và hoàn thiện các tài liệu bàn giao. Các mục tiêu chính gồm:

- Cập nhật các hàm Lambda để kiểm tra dữ liệu đầu vào cho các thao tác CRUD và xử lý rõ các trường hợp dữ liệu không hợp lệ hoặc không tìm thấy sinh viên.
- Xuất tài liệu OpenAPI từ API Gateway và kiểm thử các endpoint bằng Postman.
- Kiểm thử lại luồng hoạt động từ giao diện website trên S3 đến API Gateway, Lambda và DynamoDB.
- Theo dõi metrics, kiểm tra mức sử dụng và chi phí AWS; lưu minh chứng và dọn dẹp tài nguyên không còn cần thiết.

# 2. Nội dung công việc

## 2.1. Cập nhật logic xử lý và kiểm tra dữ liệu

Các hàm Lambda `GetStudents`, `UpdateStudent`, `CreateStudent` và `DeleteStudent` được cập nhật để xử lý nghiệp vụ và kiểm tra dữ liệu trước khi thao tác với DynamoDB. Các trường hợp được xử lý gồm thiếu mã sinh viên hoặc họ tên bắt buộc, mã sinh viên đã tồn tại, email không đúng định dạng và GPA nằm ngoài khoảng từ 0 đến 4. Các thao tác cập nhật và xóa cũng kiểm tra sự tồn tại của hồ sơ để trả về lỗi phù hợp khi không tìm thấy sinh viên.

Đối với chức năng đọc, API tiếp tục hỗ trợ lấy toàn bộ danh sách, tìm theo mã sinh viên và lọc theo chuyên ngành thông qua GSI `major-index`. Giao diện `frontend/index.html` được cập nhật để đồng bộ kiểm tra email, GPA và các thao tác tìm kiếm với backend.

<div align="center">
  <figure>
    <img src="../screenshots/week4/01.update_get_students_logic.png" alt="update_get_students_logic" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 1. Cập nhật hàm Lambda GetStudents.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/02.update_update_student_logic.png" alt="update_update_student_logic" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 2. Cập nhật hàm Lambda UpdateStudent.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/03.update_create_student_logic.png" alt="update_create_student_logic" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 3. Cập nhật hàm Lambda CreateStudent.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/04.update_delete_student_logic.png" alt="update_delete_student_logic" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 4. Cập nhật hàm Lambda DeleteStudent.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/05.update_index_html.png" alt="update_index_html" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 5. Cập nhật giao diện và kiểm tra dữ liệu trên Frontend.
    </figcaption>
  </figure>
</div>

## 2.2. Xuất tài liệu API và kiểm thử bằng Postman

Tài liệu OpenAPI được xuất từ API Gateway để mô tả các endpoint và phương thức API của hệ thống. Postman được sử dụng để kiểm thử độc lập các thao tác tạo, đọc, cập nhật và xóa, bao gồm cả trường hợp dữ liệu không hợp lệ hoặc mã sinh viên không tồn tại.

Kết quả kiểm thử ghi nhận các phản hồi phù hợp: tạo thành công trả về HTTP `201`; dữ liệu không hợp lệ trả về HTTP `400`; mã sinh viên đã tồn tại trả về HTTP `409`; không tìm thấy hồ sơ trả về HTTP `404`; các thao tác đọc, cập nhật và xóa thành công trả về HTTP `200`.

<div align="center">
  <figure>
    <img src="../screenshots/week4/06.export_open_api.png" alt="export_open_api" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 6. Xuất tài liệu OpenAPI từ API Gateway.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/07.postman_add_student_success.png" alt="postman_add_student_success" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 7. Kiểm thử tạo sinh viên thành công bằng Postman.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/08.postman_error_student_exists.png" alt="postman_error_student_exists" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 8. Kiểm thử trường hợp mã sinh viên đã tồn tại.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/09.postman_error_gpa_range.png" alt="postman_error_gpa_range" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 9. Kiểm thử dữ liệu GPA ngoài phạm vi cho phép.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/10.postman_error_empty_student_id.png" alt="postman_error_empty_student_id" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 10. Kiểm thử trường hợp mã sinh viên bị bỏ trống.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/11.postman_error_missing_fullname.png" alt="postman_error_missing_fullname" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 11. Kiểm thử trường hợp thiếu họ tên bắt buộc.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/12.postman_get_by_student_id.png" alt="postman_get_by_student_id" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 12. Kiểm thử truy vấn sinh viên theo mã sinh viên.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/13.postman_get_by_major.png" alt="postman_get_by_major" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 13. Kiểm thử lọc sinh viên theo chuyên ngành.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/14.postman_get_all_students.png" alt="postman_get_all_students" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 14. Kiểm thử lấy toàn bộ danh sách sinh viên.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/15.postman_error_id_not_found.png" alt="postman_error_id_not_found" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 15. Kiểm thử truy vấn mã sinh viên không tồn tại.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/16.postman_put_update_success.png" alt="postman_put_update_success" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 16. Kiểm thử cập nhật hồ sơ thành công bằng Postman.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/17.postman_verify_update_with_get.png" alt="postman_verify_update_with_get" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 17. Xác nhận dữ liệu sau cập nhật bằng yêu cầu GET.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/18.postman_put_error_invalid_gpa.png" alt="postman_put_error_invalid_gpa" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 18. Kiểm thử cập nhật với GPA không hợp lệ.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/19.postman_put_error_invalid_email.png" alt="postman_put_error_invalid_email" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 19. Kiểm thử cập nhật với email không hợp lệ.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/20.postman_delete_error_not_found.png" alt="postman_delete_error_not_found" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 20. Kiểm thử xóa mã sinh viên không tồn tại.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/21.postman_delete_success.png" alt="postman_delete_success" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 21. Kiểm thử xóa sinh viên thành công.
    </figcaption>
  </figure>
</div>

## 2.3. Kiểm thử End-to-End trên giao diện website

Kiểm thử lại giao diện website được lưu trữ trên S3, bao gồm thao tác thêm, sửa, tìm kiếm và xóa sinh viên. Các tình huống dữ liệu trùng, email không hợp lệ và GPA ngoài phạm vi cũng được kiểm tra trực tiếp trên giao diện. Kết quả cho thấy giao diện hiển thị thông báo lỗi phù hợp và cho phép tiếp tục thao tác khi dữ liệu hợp lệ.

<div align="center">
  <figure>
    <img src="../screenshots/week4/22.e2e_add_existing_student_error.png" alt="e2e_add_existing_student_error" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 22. Kiểm thử giao diện với mã sinh viên đã tồn tại.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/23.e2e_invalid_email_error.png" alt="e2e_invalid_email_error" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 23. Kiểm thử giao diện với email không hợp lệ.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/24.e2e_invalid_gpa_error.png" alt="e2e_invalid_gpa_error" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 24. Kiểm thử giao diện với GPA ngoài phạm vi cho phép.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/25.e2e_add_student_success.png" alt="e2e_add_student_success" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 25. Kiểm thử luồng E2E tạo sinh viên thành công.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/26.e2e_edit_invalid_email_error.png" alt="e2e_edit_invalid_email_error" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 26. Kiểm thử cập nhật với email không hợp lệ trên giao diện.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/27.e2e_edit_invalid_gpa_error.png" alt="e2e_edit_invalid_gpa_error" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 27. Kiểm thử cập nhật với GPA không hợp lệ trên giao diện.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/28.e2e_edit_student_success.png" alt="e2e_edit_student_success" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 28. Kiểm thử luồng E2E cập nhật sinh viên thành công.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/29.e2e_search_student_not_found.png" alt="e2e_search_student_not_found" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 29. Kiểm thử tìm kiếm mã sinh viên không có trong hệ thống.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/30.e2e_filter_by_student_id.png" alt="e2e_filter_by_student_id" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 30. Kiểm thử lọc danh sách theo mã sinh viên.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/31.e2e_filter_by_major_gsi.png" alt="e2e_filter_by_major_gsi" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 31. Kiểm thử lọc danh sách theo chuyên ngành qua GSI.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/32.e2e_delete_confirmation_alert.png" alt="e2e_delete_confirmation_alert" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 32. Hộp thoại xác nhận trước khi xóa sinh viên trên giao diện.
    </figcaption>
  </figure>
</div>

## 2.4. Theo dõi tài nguyên, chi phí và dọn dẹp

Biểu đồ metrics trên CloudWatch và thông tin mức sử dụng trong AWS Billing/Cost Management được kiểm tra. Sau khi hoàn tất kiểm thử, tài nguyên DynamoDB không còn cần thiết được dọn dẹp; minh chứng ghi nhận tài nguyên DynamoDB đã được xóa.

<div align="center">
  <figure>
    <img src="../screenshots/week4/33.cloudwatch_metrics_chart.png" alt="cloudwatch_metrics_chart" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 33. Theo dõi biểu đồ metrics của hệ thống trên CloudWatch.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/34.billing_and_cost_management.png" alt="billing_and_cost_management" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 34. Rà soát thông tin trong AWS Billing and Cost Management.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/35.cost_and_usage_detailed_chart.png" alt="cost_and_usage_detailed_chart" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 35. Kiểm tra biểu đồ chi phí và mức sử dụng tài nguyên.
    </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="../screenshots/week4/36.dynamodb_resources_deleted.png" alt="dynamodb_resources_deleted" style="width: 80%; max-width: 750px;">
    <figcaption style="font-style: italic; color: gray;">
      Hình 36. Minh chứng dọn dẹp tài nguyên DynamoDB sau khi kiểm thử.
    </figcaption>
  </figure>
</div>

# 3. Kết quả công việc tuần 4

- Cập nhật các hàm Lambda để kiểm tra dữ liệu cho các thao tác CRUD; xử lý các trường hợp thiếu dữ liệu, dữ liệu sai định dạng, mã sinh viên trùng hoặc không tồn tại.
- Xuất tài liệu OpenAPI và kiểm thử các chức năng API bằng Postman, bao gồm cả trường hợp thành công và lỗi.
- Kiểm thử End-to-End trên giao diện S3 với các thao tác thêm, sửa, tìm kiếm, lọc và xóa sinh viên.
- Kiểm tra metrics trên CloudWatch, rà soát thông tin chi phí và lưu đầy đủ minh chứng Tuần 4.
- Dọn dẹp tài nguyên DynamoDB không còn cần thiết sau khi hoàn tất kiểm thử.
