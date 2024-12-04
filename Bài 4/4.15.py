print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

input_string=input("nhap cac tu tieng anh(tach nhau boi dau cach): ")
words=input_string.split()
sorted_words=sorted(words)
print("cac tu theo thu tu tu dien:")
for word in sorted_words:
    print(word)
