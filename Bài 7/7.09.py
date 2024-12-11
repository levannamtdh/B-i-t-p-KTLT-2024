print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

source_file=input("nhap ten tep nguon")
destination_file=input("nhap ten tep dich")
try:
    with open(source_file, 'r',encoding='utf-8') as src,open(destination_file,'w',encoding='utf-8') as dest:
        content=src.read()
        dest.write(content)
        print(f"noi dung sao chep thanh cong")
except FileNotFoundError:
    print("Tep khong ton tai.Vui long kiem tra lai")
except Exception as e:
    print(f"Da xay ra loi:{e}")
