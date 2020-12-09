


def is_valid_lvl1(item):
    policy = line.split(":")[0]
    password = line.split(":")[1].strip()
    letter = policy.split(" ")[1]
    occ_range = policy.split(" ")[0]
    start_range = int(occ_range.split("-")[0])
    end_range = int(occ_range.split("-")[1])

    count = 0
    
    for c in password:
        if c == letter:
            count = count + 1
    return  start_range <= count and end_range >= count

def is_valid_lvl2(item):
    policy = line.split(":")[0]
    password = line.split(":")[1].strip()
    letter = policy.split(" ")[1]
    occ_range = policy.split(" ")[0]
    first_pos = int(occ_range.split("-")[0]) - 1
    second_pos = int(occ_range.split("-")[1]) - 1
    return (password[first_pos] == letter and password[second_pos] != letter) or (password[second_pos] == letter and password[first_pos]!=letter) 



valids = 0

with open("ex2.txt","r") as file:
    for line in file:
        if is_valid_lvl2(line.strip()):
            valids = valids + 1
print(valids)



