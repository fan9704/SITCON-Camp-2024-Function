def calculate_rectangle_area(height, width):
    return height * width


print(calculate_rectangle_area(3, 4))  # 計算長 3 寬 4 的長方形面積
print(calculate_rectangle_area(6, 8))  # 計算長 6 寬 8 的長方形面積

# 綁定名稱
calculate_rectangle_area = lambda height,width:height*width
print(calculate_rectangle_area(3,4)) #12
# 不綁定名稱
print((lambda width,height:width*height)(3,4))