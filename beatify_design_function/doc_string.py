def calculate_circle_area(x: int = 1):
    """這是一個計算給予半徑算出圓面積的函式
    Parameters:
    argument1 (int): 圓的半徑長度
    
    Returns: 
    float: 計算出的面積
    """  # 撰寫 doc string
    area = x * x * 3.14
    return area


print(calculate_circle_area(3))
print(calculate_circle_area.__doc__)  # 顯示 這是一個計算給予半徑算出圓面積的函式
