import re

required_props = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

def validateprop(prop, val):    
    try:
        intval = int(val)
    except:
        intval = 0
    
    if prop == "byr":
        return len(val) == 4 and intval >= 1920 and intval <= 2002
    if prop == "iyr":
        return len(val) == 4 and intval >= 2010 and intval <= 2020
    if prop == "eyr":       
        return len(val) == 4 and intval >= 2020 and intval <= 2030
    if prop == "hgt":
        if val[-2:] == "cm":
            intval = int(val[0:-2])
            return intval >= 150 and intval <= 193
        if val[-2:] == "in":
            intval = int(val[0:-2])            
            return intval >= 59 and intval <= 76
    if prop == "hcl":
        if val[0] == "#":
            return bool(re.search("^\w+$", val[1:])) and len(val) == 7
        
    if prop == "ecl":
        return val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    
    if prop == "pid":
        return len(val) == 9 and bool(re.search("\d+", val))
    
    if prop == "cid":
        return True
        
    return False

def validatepassp(passdata):    
    valid = True
    
    for p in passdata:
        valid = validateprop(p[0], p[1])
        if not valid:
            break
        
    return valid

with open('input/d4.txt') as file:
    data = list(map(lambda x: x.replace("\n", " "), file.read().split("\n\n")))

data_validation = []
for passp in data:
    passpdata = set(re.findall(r"(\w+):(#?\w+)", passp))
    props = set(map(lambda x: x[0], passpdata))
    
    diffprop = len(required_props - props)
    if (diffprop > 0):
        data_validation.append(False)
    else:
        data_validation.append(validatepassp(passpdata))

        
print(data_validation.count(True))