n, m, q = map(int, input().split())
episodes = [0] * (n * m + 1)
seasons = [0] * (n + 1)

for _ in range(q):
    ei, si = map(int, input().split())
    episodes[ei] = 1
    seasons[si] += 1

missing_episodes = 0
result = []

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if episodes[(i - 1) * m + j] == 0:
            missing_episodes += 1
            result.append((j, i))

print(missing_episodes)
for episode in result:
    print(episode[0], episode[1])