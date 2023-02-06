# Prints a door mat of a certain design with variable input. M must be n*3 for design to work properly

size = input().split(' ')
n = int(size[0])
m = int(size[1])
rows = []

# for i in range(n):
#     for i in range(m):
#         if(i == ((m-3)/2)): print('.', end='')
#         print('-', end ='')
#         if(i == m-1): print()

for i in range(n):
    
    #If in the top half
    if(i == (n-1)/2 ):
        line = ""
        welcLen = int( (m-7)/2 )
        line += '-'*welcLen
        line += "WELCOME"
        line += '-'*welcLen
        print(line)
    #If in the middle, print Welcome row
    if(i < (n-1)/2 ):
        line = ""
        imult = (i*2)+1
        dashlen = int((m-3)/2) - 3*i
        line += '-'*dashlen
        line += ".|."*imult
        line += '-'*dashlen
        rows.append(line) #Store lines in list to access for bottom half
        print(line)
    if(i > (n-1)/2 ): #If in the bottom half
        index = int((n-i)-1)
        print(rows[index]) #Print the stored rows from the top half, in reverse order