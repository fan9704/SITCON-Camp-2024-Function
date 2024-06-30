# 匿名用法
print((lambda r: r * r * 3.14)(3))
# 不匿名用法
calc_circle_area = lambda r: r * r * 3.14
print(calc_circle_area(3))