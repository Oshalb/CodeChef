# find two equal values of a triangle

"""
x1,y1


x2,y2       x3,y3
"""


def check_right_angle(x1, y1, x2, y2, x3, y3):
    a = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
    b = ((x3 - x1) ** 2) + ((y3 - y1) ** 2)
    c = ((x3 - x2) ** 2) + ((y3 - y2) ** 2)
    if a + b == c:
        return True
    elif b + c == a:
        return True
    elif a + c == b:
        return True
    else:
        return False


if __name__ == "__main__":
    number_of_triangles = int(input())
    result = 0
    for _ in range(number_of_triangles):
        coordinates = list(map(int, input().rstrip().split()))
        if check_right_angle(*coordinates):
            result += 1
    print(result)
