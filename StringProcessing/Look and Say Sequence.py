# 111221 is read of as "Three 1s, two 2s, then one 1"
# which is 312211

def next_number(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])
        i += 1 # repeat the process 
    return ''.join(result)


s = "111221"
print(s)
n = 4
for i in range(n-1):
    s = next_number(s)
    print(s)
