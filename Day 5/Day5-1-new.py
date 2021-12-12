def read_input(path):
    segments = []
    with open(path, "r") as file:
        line = file.readline()
        while line:
            segment = []
            for p in line.strip("\n").split(" -> "):
                point = []
                for t in p.split(","):
                    point.append(int(t))
                segment.append(point)

            segments.append(segment)
            line = file.readline()

    points = []
    for segment in segments:
        x1, y1 = segment[0][0], segment[0][1]
        x2, y2 = segment[1][0], segment[1][1]

        # Only horizontal lines
        if x1 == x2:
            step = 1
            if (y2 - y1) < 0: step = -1
            for y in range(y1, y2 + step, step):
                points.append([x1, y])
        elif y1 == y2:
            step = 1
            if (x2 - x1) < 0: step = -1
            for x in range(x1, x2 + step, step):
                points.append([x, y1])

    return points

points = read_input("day 5.txt")

overlap_count = 0
for p in points:
    count = points.count(p)
    if count >= 2:
        overlap_count += 1

print(overlap_count)