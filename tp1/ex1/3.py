val=17
cptdiv=0
for i in range(2,int(val**(1/2))):
 if(val % i==0):
  cptdiv+=1
if(cptdiv==0):
 print(val," est impaire")
else:
 print(val," est paire")