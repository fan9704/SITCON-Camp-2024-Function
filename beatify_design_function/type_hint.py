def calculate_circle_area(r: int):
	# 標註 r 變數是整數 int 型別  避免給予 function 錯誤的型別
	area = r * r * 3.14
	return area
print(calculate_circle_area(3)) # 計算為半徑為 3 的圓面積