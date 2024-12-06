print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

class ATM:
    def __init__(self, balance=0):
        self.balance = balance  
    def check_balance(self):
        print(f"Số dư tài khoản của bạn là: {self.balance} VNĐ")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Số dư không đủ để rút tiền!")
        else:
            self.balance -= amount
            print(f"Đã rút {amount} VNĐ. Số dư còn lại: {self.balance} VNĐ")
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Đã nạp {amount} VNĐ. Số dư hiện tại: {self.balance} VNĐ")
        else:
            print("Số tiền nạp vào phải lớn hơn 0!")            
def atm_program():
    atm = ATM(100000)  
    while True:
        print("\nChào mừng bạn đến với hệ thống ATM")
        print("1. Kiểm tra số dư")
        print("2. Rút tiền")
        print("3. Nạp tiền")
        print("4. Thoát")
        try:
            choice = int(input("Vui lòng chọn chức năng (1-4): ")) 
            if choice == 1:
                atm.check_balance()  
            elif choice == 2:
                amount = float(input("Nhập số tiền bạn muốn rút: "))
                atm.withdraw(amount)  
            elif choice == 3:
                amount = float(input("Nhập số tiền bạn muốn nạp: "))
                atm.deposit(amount)  
            elif choice == 4:
                print("Cảm ơn bạn đã sử dụng dịch vụ ATM!")
                break  
            else:
                print("Lựa chọn không hợp lệ, vui lòng chọn lại!")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ!")
atm_program()
    
        
