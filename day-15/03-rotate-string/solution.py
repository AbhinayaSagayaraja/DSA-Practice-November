def rotateString(s, goal):
    if len(s) !=len(goal):
        return False
    n =len(s)
    if n ==0:
        return True
    combined =s + s
    for i in range(n + 1):
        j = 0
        while j < n and combined[i + j] ==goal[j]:
            j +=1
        if j ==n:
            return True
    return False
s ="abcde"
goal ="cdeab"
print(rotateString(s, goal))