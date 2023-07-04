def isHappy(n, seen):
    new_n = sum(int(n) ** 2 for n in str(n))
    if new_n in seen:
        return False
    seen.append(new_n)
    if int(new_n) == 1:
        return True
    return isHappy(new_n, seen)

print(isHappy(19, []))