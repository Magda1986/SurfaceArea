
foundation=[
        [10, 12],
        [10, 6],
        [13, 4],
        [13, 2],
        [3, 2],
        [3, 4],
        [6, 6],
        [6, 10],
        [8, 10],
        [8, 12],
    ]

square = [
    [1,2],
    [9,2],
    [9,6],
    [1,6],
]

polygon = [
    [4,4],
    [7,4],
    [9,6],
    [3,7],
]


def foundation_area(points):
    x2=points[-1][0] 
    y2=points[-1][1]
    area=0
    for i in points:
        x = i[0]
        y = i[1]
        area+=((x2+x)*(y-y2))
        x2 = x
        y2 = y
    return (abs(area/2))


print(foundation_area(foundation))
print(foundation_area(square))
print(foundation_area(polygon))


