from math import pi

# from <模組> import <子模組,函式,常數,物件>
print(pi)  # 印出 pi

from math import *

# from <模組> import *
# * 代表模組內的全部的內容也就是所有的 子模組,函式,常數,物件
print('n =', floor(pi))  # 來自 math 中的取出數值最大整數值
print('m =', gcd(28, 35))  # 來自 math 中的最大公因數函式
