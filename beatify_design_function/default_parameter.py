def calculate_circle_area(r :int = 1):
	# 標示 r 變數是整數之外也給予預設的 r 值為 1
	area = r* r * 3.14
	return area
# 計算半徑為 3 的圓面積
print(calculate_circle_area(3)) 
# 不給予半徑 預設使用 1 為 r 計算半徑為 1 的圓面積
print(calculate_circle_area()) 