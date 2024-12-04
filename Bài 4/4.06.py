print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

full_name=input("nhap ho va ten(ho ten rieng chi co mot am): ")
name_parts=full_name.split()
if len(name_parts)==2:
    ho=name_parts[0]
    ten_rieng=name_parts[1]
    print("Ho:",ho)
    print("Ten rieng:",ten_rieng)
else:
    print("vui long nhap ho va ten rieng voi chi hai tu.")
