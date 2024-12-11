print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

file_name=input("nhap ten tep:")
my_list=["i am robot"]
try:
    with open(file_name,'w',encoding='utf-8') as file:
        for item in my_list:
            file.write(item + '\n')
            print(f"noi dung danh sach ghi vao thanh cong")
except Exception as e:
    print(f"Da xay ra loi:{e}")
