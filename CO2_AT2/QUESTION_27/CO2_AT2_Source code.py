import math

stations = [(2, 8), (5, 6), (9, 4), (4, 7), (8, 3)]

min_dist = float('inf')
closest_pair = ()

for i in range(len(stations)):
    for j in range(i + 1, len(stations)):
        x1, y1 = stations[i]
        x2, y2 = stations[j]

        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        if dist < min_dist:
            min_dist = dist
            closest_pair = (stations[i], stations[j])

print("Closest Stations:", closest_pair)
print("Minimum Distance:", round(min_dist, 2))
print("Time Complexity = Θ(n²)")