print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

import numpy as np
dtype = [('Tên', 'S15'), ('Chiều cao', 'f4'), ('Lớp', 'U10')]
data = [
    ('James', 48.5, '5'),
    ('Nail', 52.5, '6'),
    ('Paul', 42.10, '5'),
    ('Pit', 40.11, '5'),
]

students = np.array(data, dtype=dtype)
print("Danh sách sinh viên ban đầu:")
print(students)
sorted_students = np.sort(students, order='Chiều cao')
print("\nDanh sách sinh viên sau khi sắp xếp theo chiều cao:")
print(sorted_students)

