def merge_the_tools(string, k):
    temp = ""
    inString = False
    for i in range(len(string)):
        for letter  in temp:
            if(string[i]==letter): inString = True
        if(not inString):       
            temp += string[i]
        if((i+1)%k == 0):
            print(temp)
            temp = ""
        inString = False
            
            
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true&h_r=next-challenge&h_v=zen