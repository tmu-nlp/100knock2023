N = int(input())
with open("popular-names.txt", "r") as f:
    popular_names_list = f.readlines()

for i in range(len(popular_names_list)//N):
    try:
        print("".join(popular_names_list[i*N:i*(N+1)]), end="\n")
    except:
        print("".join(popular_names_list[i*N:]), end="\n")
