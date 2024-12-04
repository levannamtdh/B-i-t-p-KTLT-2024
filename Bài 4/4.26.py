print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

balance=0
while True:
    transaction=input("nhap giao dich(D so tien de gui tien, W so tien de rut tien, hoac nhan enter de ket thuc):")
    if not transaction:
        break
    action, amount=transaction.split()
    amount=int(amount)
    if action== 'D':
        balance+=amount
        print(f"so du tai khoan hien tai:{balance}")
    elif action=='W':
        balance-=amount
        print(f"so du tai khoan hien tai:{balance}")
