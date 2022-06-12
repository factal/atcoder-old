import math
import numpy as np

def rotation(vector, theta):
    rotate_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    return np.dot(rotate_matrix, vector)

n = int(input())
x_0, y_0 = map(int, input().split())
x_n2, y_n2 = map(int, input().split())

u_0 = np.array([x_0, y_0])
u_n2 = np.array([x_n2, y_n2])

edge = np.linalg.norm(u_n2 - u_0) * math.sin(math.pi / n)

phi = np.arccos(np.clip(np.inner(u_n2 - u_0, [1, 0]) / np.linalg.norm(u_n2 - u_0), -1, 1))

rotate = (math.pi - 2 * math.pi / n) / 2

ans = rotation(u_n2 - u_0, -1 * rotate) / np.linalg.norm(u_n2 - u_0)* edge
print(ans[0] + x_0, ans[1] + y_0)