def points_counter(team, goals1, goals2):
    if team not in d:
        d[team] = [0] * 5
    d[team][0] += 1
    d[team][1] += int(goals1 > goals2)
    d[team][2] += int(goals1 == goals2)
    d[team][3] += int(goals1 < goals2)
    d[team][4] += int(goals1 > goals2) * 3 + int(goals1 == goals2)

n, d = int(input()), {}
for _ in range(n):
    k = input().split(';')
    points_counter(k[0], int(k[1]), int(k[3]))
    points_counter(k[2], int(k[3]), int(k[1]))
for k, v in d.items():
    print(k + ":" + str(v[0]), v[1], v[2], v[3], v[4])
