# Mod = 10**9 + 7
# P = 113

Mod = 7
P = 3

Pinv = pow(P, Mod - 2, Mod)
print(Pinv)
print(Pinv*P % Mod)