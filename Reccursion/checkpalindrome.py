s = 'asdfdsaa'

def fun(l , r):
    if l >= r:
        print("Palindrome")
        return 

    if s[l] != s[r]:
        print("Not")
        return
    else:
        fun(l + 1, r - 1)

fun(0, len(s) - 1)