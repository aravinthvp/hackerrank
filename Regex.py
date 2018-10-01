

#Solution


import re

para = (str(input()))

ages = re.findall(r'\d{1,3}', para)
names = re.findall(r'[A-Z][a-z]*', para)


ageDic = {}


x = 0

for eachname in names:
    ageDic[eachname] = ages[x]
    x+=1
    
    
print(ageDic)