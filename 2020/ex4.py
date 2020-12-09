from re import findall
eye_colors = ['amb','blu','brn','gry','grn','hzl','oth']



def check_hgt(x):
    centimeters = findall("([0-9]*)cm$",x)
    inches = findall("([0-9]*)in$",x)
    if len(centimeters) > 0:

        return int(centimeters[0]) >= 150 and int(centimeters[0]) <= 193
    if len(inches) > 0:

        return int(inches[0]) >= 59 and int(inches[0]) <= 76
    return False
     

policy = {"byr":lambda x : int(x) >= 1920 and int(x) <= 2002,'iyr':lambda x: int(x) >= 2010 and int(x) <= 2020, "eyr":lambda x: int(x)>=2020 and int(x) <= 2030, "hgt": check_hgt,"hcl":lambda x: len(findall("^#[0-9a-f]{6}",x)) > 0, 'ecl': lambda x: x in eye_colors ,'pid': lambda x: len(x) == 9 and len(findall("([0-9]{9})",x)) > 0 } 

def is_valid(raw):
    credentials = {}
    for credential in raw:
        k = credential.split(":")[0]
        v = credential.split(":")[1]
        credentials[k] = v
    for k,v in policy.items():
        if not k in credentials:
            return False
        if not v(credentials[k]):
            return False
    return True
    

with open("ex4.txt","r") as file:
    raw = ""
    valids = 0
    for line in file:
        if len(line) == 1:
            if is_valid(raw.strip().split(" ")):
                valids = valids + 1
            raw = ""
        else:
            raw =  raw +" " + line.strip()
    if is_valid(raw.strip().split(" ")):
                valids = valids + 1
    print(valids)
    file.close()


        