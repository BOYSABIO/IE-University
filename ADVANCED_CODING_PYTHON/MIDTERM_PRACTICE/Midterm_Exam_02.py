# Program that gets the number of rows and creates a triangle

rows = int(input("Please enter the number of rows: "))
middle = rows/2
spaces = 0
for i in range(rows):
    print(' '*spaces + '_'*round(middle)+'*'+'_'*round(middle))
    middle -= 1
    spaces +=1 

#for i in range(rows):
    #print('_'*round(middle)+'*'+'_'*round(middle))

starcount = 0

for i in range(rows):
    print(starcount * '*')
    starcount+=1

print()
print()
print()

# This is the one that eventually worked
spacecount = rows
star = 1
for i in range(rows):
    print((spacecount * " ") + (star * '*'))
    spacecount -=1
    star += 2

