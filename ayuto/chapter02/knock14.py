with open("popular-names.txt", "r") as f:
    popular_names_list = f.readlines()
N = int(input())
ans=""
for i in range(N):
    ans += popular_names_list[i]
print(ans)