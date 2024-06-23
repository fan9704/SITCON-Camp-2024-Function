def calculate_rectangle_area(height: int, width: int):
    area = height * width
    return area


hw = [3, 4]
print(calculate_rectangle_area(*hw))  # 12
hw2 = {"height": 3, "weight": 4}
print(calculate_rectangle_area(**hw2))  # 12
