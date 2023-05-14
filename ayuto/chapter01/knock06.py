def nGram(A, n):
    if type(A) == str: #Aが文字列で与えられたときは文字n-gramを返す
        A = A.replace(" ", "")
        A=list(A)
        A += [None] * n
        ans = [A[n*i : n*(i+1)] for i in range(len(A)//n)]
        while ans[-1] == [None] * n: #Noneのみのリストを消す
            ans = ans[:-1]
        while ans[-1][-1] == None: #リスト内のNoneを消す
            ans[-1] = ans[-1][:-1]
        A = []
        for i in range(len(ans)):
            A.append("".join(ans[i])) #文字列に戻す
        return A
    else: #Aがリストで渡されたときは単語n-gramを返す
        A += [None] * n
        ans = [A[n*i : n*(i+1)] for i in range(len(A)//n)]
        while ans[-1] == [None] * n:
            ans = ans[:-1]
        while ans[-1][-1] == None:
            ans[-1] = ans[-1][:-1]
        return ans

p1 = "paraparaparadise"
p2 = "paragraph"
X = set(nGram(p1, 2))
Y = set(nGram(p2, 2))
wa = X | Y
seki = X & Y
sa = X - Y

print("X:", X, "\n", "Y:", Y, "\n", "和集合:" ,wa ,"\n", "積集合:", seki, "\n", "差集合:", sa)