players = set(["test", "totos","mango"])
players.add("Rooney")
print(players)


players.update(["Pacome","kibu"])
print(players)

players.remove("test")
print(players)

# players.clear()
# print(players)

players.pop()
print(players)


players.discard("Rooney")
print(players)


for player in players:
    print(player)


print(players.copy())

print(len(players))
