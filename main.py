subway1 = 10
subway2 = 20
subway3 = 20

subway = [10, 20, 30]

print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway.index("조세호"))  # 출력 1

subway.append("하하")
print(subway)

subway.insert(1, "정형돈")
print(subway)

print(subway.pop())
print(subway)

subway.append("유재석")

print(subway.count("유재석"))
print(subway)

num_list = [5, 3, 2, 1, 2]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

num_list.clear()
print(num_list)

t3 = ["조세호", 20, True]
num_list = [3, 1, 3, 2, 4]

num_list.extend(t3)
print(num_list)
