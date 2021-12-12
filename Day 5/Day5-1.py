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

    lines = []
    for segment in segments:
        x1, y1 = segment[0][0], segment[0][1]
        x2, y2 = segment[1][0], segment[1][1]

        # Only horizontal lines
        points = []
        if x1 == x2:
            step = 1
            if (y2 - y1) < 0: step = -1
            for y in range(y1, y2 + step, step):
                points.append([x1, y])
            lines.append(points)
        elif y1 == y2:
            step = 1
            if (x2 - x1) < 0: step = -1
            for x in range(x1, x2 + step, step):
                points.append([x, y1])
            lines.append(points)

    return lines

def write_points(lines):
    with open("points.txt", "w") as file:
        for line in lines:
            for point in line:
                file.write("{},{};".format(point[0], point[1]))
            file.write("\n")

lines = read_input("day 5.txt")
#write_points(lines)

# cnt = 0
# for line in lines:
#     for point in line:
#         cnt += 1
# print(cnt)
# print(cnt**2)

overlap_count = 0
for l in range(len(lines)):
    line = lines[l]
    for p in range(len(line)):
        point = line[p]
        point_count = 1
        
        for i in range(len(lines)):
            if i != l:
                other_line = lines[i]
                if point in other_line:
                    point_count += 1

        if point_count >= 2:
            overlap_count += 1

print(overlap_count)
