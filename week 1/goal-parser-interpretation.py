class Solution:
    def interpret(self, command: str) -> str:
        temp=""
        k=len(command)
        for i in range(k):
            if command[i] == "G" :
                temp = temp + "G"
            elif (i < len(command) - 1) and command[i]=="("and command[i+1]==")":
                temp = temp + "o"          
            elif (i < len(command) - 1) and command[i]=="("and command[i+1]=="a":

                temp=temp + "al"
        return temp

             
        