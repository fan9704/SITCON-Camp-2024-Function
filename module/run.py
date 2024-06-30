# import <模組>

import triangle

triangle.print_triangle(6)  # 印出高度為 6 的三角形

# from <模組> import <function>

from triangle import print_triangle

print_triangle(5)  # 印出高度為 5 的三角形

# from <模組> import <函式> as <別名>
from triangle import print_triangle as pt

pt(4)  # 印出高度為 4 的三角形
