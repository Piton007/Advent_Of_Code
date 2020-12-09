numbers = []

def get_diff(total):
    diff = {}
    for n in numbers:
        diff[n] = total - n
    return diff 

def pairsOfSum(total):
    diff = get_diff(total)
    
    result = -1
    for k in diff:
        if diff[k] in diff:
            result = k * diff[k]
    return result


with open('ex1.txt','r') as file:
    for line in file:
        numbers.append(int(line.strip()))



result = -1
for v in numbers:
    s1 = pairsOfSum(2020-v)
    if s1 > 0:
        result = s1 * v

print(result)
 

