def main():
    print("Chào mừng đến với phần mềm giáo dục cho học sinh lớp 8!")
    subjects = ["Toán", "Văn", "Lịch Sử", "Địa Lý", "Vật Lý", "Hóa Học", "Tiếng Anh", "Sinh Học"]
    print("Vui lòng chọn môn học để bắt đầu ôn tập:")
    for index, subject in enumerate(subjects, start=1):
        print(f"{index}. {subject}")
    choice = int(input("Nhập số tương ứng với môn học: ")) - 1
    if 0 <= choice < len(subjects):
        print(f"Bạn đã chọn môn: {subjects[choice]}")
        # Gọi hàm tương ứng cho môn học này
    else:
        print("Lựa chọn không hợp lệ!")

if __name__ == '__main__':
    main()