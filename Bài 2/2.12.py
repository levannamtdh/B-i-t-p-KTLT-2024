print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

import re
def kiem_tra_mat_khau(password):
    if len(password)<8:
        return "mat khau phai co it nhat 8 ki tu"
    if not re.search(r'[A-Z]',password):
        return "mat khau phai co it nhat mot chu cai viet hoa"
    if not re.search(r'[a-z]',password):
        return "mat khau phai co it nhat mot chu cai viet thuong"
    if not re.search(r'[0-9]',password):
        return "mat khau phai co it nhat mot chu so"
    if not re.search(r'[!@#$%^&*(),.?:{}|<>]',password):
        return "mat khau phai co it nhat mot ki tu dac biet"
    return"mat khau hop le!"
password = input("nhap mat khau: ")
ket_qua = kiem_tra_mat_khau(password)
print(ket_qua)
    
