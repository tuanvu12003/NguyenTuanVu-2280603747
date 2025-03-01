j =[]
for item in range(2000, 3201):
    if(item % 7 ==0) and (item % 5 ==0):
        j.append(str(item))
print(', '.join(j))