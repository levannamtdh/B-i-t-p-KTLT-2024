print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

import numpy as np

student_ids = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
heights = np.array([40.0, 42.0, 45.0, 41.0, 38.0, 40.0, 42.0])

sorted_indices = np.lexsort((student_ids, heights)) 

print("Chỉ số mô tả thứ tự sắp xếp (theo chiều cao):")
print(sorted_indices)

print("\nDữ liệu đã sắp xếp theo chiều cao tăng dần:")
sorted_student_ids = student_ids[sorted_indices]
sorted_heights = heights[sorted_indices]
for id, height in zip(sorted_student_ids, sorted_heights):
    print(f"ID: {id}, Chiều cao: {height}")
