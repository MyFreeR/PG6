def circlecross():
    x1, y1, r1 = map(int, input().split())
    x2, y2, r2 = map(int, input().split())
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 > (r2 + r1) ** 2:
        print("NO")
    else:
        print("YES")


def linecross(x11, x12, x21, x22):
    return x21 <= x11 <= x22 or x11 <= x21 <= x12


left1, top1, width1, height1 = map(int, input().split())
left2, top2, width2, height2 = map(int, input().split())
# если проекции обеих сторон обоих прямоугольников пересекаются
# то и прямоугольники пересекаются

if linecross(left1, left1 + width1, left2, left2 + width2) and linecross(top1, top1 + height1, top2, top2 + height2):
    print("YES")
else:
    print("NO")
