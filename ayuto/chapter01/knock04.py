S = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
ichimozi = [1, 5, 6, 7, 8, 9, 15, 16, 19]
S = list(S.split())
S = [S[i][:1] if i+1 in ichimozi else S[i][:2] for i in range(len(S))]
D = {S[i]:i+1 for i in range(len(S))}
print(D)