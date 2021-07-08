def find_farthest_points(points):
    result = [(0, 0), (0, 0)]
    maxDistance = 0
    for p1 in range(len(points) - 1):
        for p2 in range(p1 + 1, len(points)):
            currentDistance = ((points[p2][0] - points[p1][0]) ** 2 + (points[p2][1] - points[p1][1]) ** 2) ** (1 / 2)
            if currentDistance > maxDistance:
                maxDistance = currentDistance
                result = [points[p1], points[p2]]
    return result


if __name__ == '__main__':
    print(find_farthest_points([(2, 96), (43, 28), (11, 18)]))
