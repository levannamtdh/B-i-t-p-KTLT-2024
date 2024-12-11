print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

file_name=input("nhap ten tep:")
try:
    with open(file_name,'r',encoding='utf-8') as file:
        line_count=sum(1 for line in file)
        print(f"so dong trong tep la:{line_count}")
except FileNotFoundError:
    print("Tep khong ton tai.Vui long kiem tra lai")
except Exception as e:
    print(f"Da xay ra loi:{e}")
