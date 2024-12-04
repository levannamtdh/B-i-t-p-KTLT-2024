print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

import numpy as np
dtype = [('Tên', 'U50'), ('Chiều cao', 'f4'), ('Lớp', 'U10')]
data = [
    ('Alice', 165.5, 'A1'),
    ('Bob', 175.3, 'B2'),
    ('Charlie', 160.0, 'A1'),
    ('David', 180.2, 'B2'),
    ('Eve', 158.4, 'A2'),
    ('Frank', 172.0, 'A1'),
]
students = np.array(data, dtype=dtype)
print("Danh sách sinh viên ban đầu:")
print(students)
sorted_students = np.sort(students, order=['Lớp', 'Chiều cao'])
print("\nDanh sách sinh viên sau khi sắp xếp:")
print(sorted_students)
