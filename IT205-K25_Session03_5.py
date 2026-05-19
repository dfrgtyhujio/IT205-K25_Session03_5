print("=========================================")
print("  KIOSK HR: CẬP NHẬT HỒ SƠ & ĐÁNH GIÁ KPI")
print("=========================================\n")

while True:
    print("[Nhập thông tin nhân viên]")
    
    employee_id = input("1. Enter Employee ID: ")
    employee_name = input("2. Enter Full Name: ")
    
    while True:
        current_salary = float(input("3. Enter current Salary in VND (Number > 0): "))
        if current_salary > 0:
            break
        print("[!] LỖI: Lương không thể là số âm hoặc bằng 0. Vui lòng nhập lại!")
        
    while True:
        performance_score = float(input("4. Enter Performance Score (1.0 to 5.0): "))
        if 1.0 <= performance_score <= 5.0:
            break
        print("[!] LỖI: Điểm KPI phải nằm trong khoảng từ 1.0 đến 5.0!")
        
    while True:
        experience_years = int(input("5. Enter Year of Experience (Integer >= 0): "))
        if experience_years >= 0:
            break
        print("[!] LỖI: Số năm kinh nghiệm không hợp lệ!")


    print("=========================================")
    print("            E-PROFILE CẬP NHẬT            ")
    print("=========================================")
    print(f"- ID: {employee_id}")
    print(f"- Name: {employee_name}")
    print(f"- Salary: {current_salary} VND")
    print(f"- KPI Score: {performance_score} / 5.0")
    print(f"- Experience: {experience_years} years")
    print("=========================================")
    print("               IT SYSTEM LOG             ")
    print("=========================================")
    print(f"employee_id       | {type(employee_id)}")
    print(f"employee_name     | {type(employee_name)}")
    print(f"current_salary    | {type(current_salary)}")
    print(f"performance_score | {type(performance_score)}")
    print(f"experience_years  | {type(experience_years)}")
    print("=========================================")
    
    choice = input("Do you want to enter another employee? (y/n): ")
    if choice != 'y':
        break

print("Đang tắt Kiosk... Tạm biệt!")