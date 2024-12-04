print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

input_string=input("nhap chuoi: ")
words=input_string.split()
max_length=max(len(word) for word in words)
longest_words=[word for word in words if len(word)==max_length]
print("tu dai nhat:", ','.join(longest_words))
print("do dai cua tu:",max_length)
