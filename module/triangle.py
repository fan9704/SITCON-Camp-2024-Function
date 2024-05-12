def print_triangle(height: int = 3):
    for h in range(height+1):
        row = ""
        for w in range(h):
            row += "*"
        print(row)