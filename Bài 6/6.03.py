print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################


class Nguoi:
    def getGender(self):
        pass  

class Nam(Nguoi):
    def getGender(self):
        print("Nam")  
class Nu(Nguoi):
    def getGender(self):
        print("Nữ")  

nam = Nam()  
nu = Nu()    
nam.getGender()  
nu.getGender()   

    
