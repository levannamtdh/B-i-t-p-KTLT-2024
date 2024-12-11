print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

file_name=input("nhap ten tep:")
try:
    with open(file_name,'r',encoding='utf-8') as file:
        content=file.read()
        words=content.split()
        max_length=max(len(word) for word in words)
        longest_word=[word for word in words if len(word)==max_length]
        unique_longest_words=list(set(longest_word))
        print("nhung tu dai nhat trong tep la: ")
        print(unique_longest_words)
        print(f"do dai cua tu dai nhat:{max_length}")
except FileNotFoundError:
    print("Tep khong ton tai.Vui long kiem tra lai")
except Exception as e:
    print(f"Da xay ra loi:{e}")
