def repeatedSubstringPattern(s):
    n =len(s)
    for length in range(1, n // 2 + 1):
        if n % length ==0:
            count =n // length
            pattern =s[:length]
            repeated = True
            for i in range(count):
                start =i * length
                end = start +length
                if s[start:end] !=pattern:
                    repeated =False
                    break
            if repeated:
                return True
    return False
s ="abab"
print(repeatedSubstringPattern(s))