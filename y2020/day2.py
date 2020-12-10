def countchars(word, char):
    c = 0
    for i in word:
        if i == char:
            c = c+1

    return c

def validpwd(lines, mode = 0):
  passrules = [i.split(" ") for i in lines]
  correctpwds = 0

  for i in passrules:
      t = [int(j) for j in i[0].split("-")]
      
      pwd = i[2]
      num1 = t[0]
      num2 = t[1]
      char = i[1][0]

      if mode == 0:
        cc = countchars(pwd, char)
        if (cc >= num1 and cc <= num2):
          correctpwds += 1
      else:
        
        if ((pwd[num1-1] == char) + (pwd[num2-1] == char)) == 1:
          correctpwds +=1
  
  return correctpwds

with open('input/d2.txt') as my_file:
    lines = my_file.read().splitlines()

print(validpwd(lines, 0))
print(validpwd(lines, 1))