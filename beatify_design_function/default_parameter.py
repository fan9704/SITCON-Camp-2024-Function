def calculate_circle_area(x:int = 1): 
	# 標示 x 變數是整數之外也給予預設的 x 值為 1
	area = x * x * 3.14
	return area
# 計算半徑為 3 的圓面積
print(calculate_circle_area(3)) 
# 不給予半徑 預設使用 1 為 x 計算半徑為 1 的圓面積
print(calculate_circle_area()) 