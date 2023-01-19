if __name__ == '__main__':
    N = int(input())
    l = []

    for i in range(N):
        command = input()
        command = command.split()     
        if(command[0] == "print"):
            print(l)
        else:
            firstCom = getattr(l, command[0])
            if(len(command) == 1):
                firstCom()
            elif(len(command) == 2):
                firstCom( int(command[1]) )
            else:
                firstCom( int(command[1]), int(command[2]) )

# My first thought for solving this problem was to make a bunch of if statements for each type of command
# I decided to try a cleaner way and here is what I came up with. 
# It can probably be done with one if statment just for print, or even none with some other way

# Link to challenge: https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true