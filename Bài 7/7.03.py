print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

file_name=input("nhap ten tep:")
try:
    with open(file_name,'r',encoding='utf-8') as file:
        content=file.read()
        print("noi dung cua tep: ")
        print(content)
except FileNotFoundError:
    print("Tep khong ton tai.Vui long kiem tra lai")
except Exception as e:
    print(f"Da xay ra loi:{e}")
