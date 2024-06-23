area = 12
print(area)


def calculate_circle_area(r: int = 1):
    """這是一個計算給予半徑算出圓面積的函式"""
    global area
    area = r * r * 3.14
    return area


print(calculate_circle_area(4))  # 16 pi
print(area)  # 16 pi
