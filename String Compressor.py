
def string_compressor(string):
    result = ""
    index = 0
    temp = string[0]
    count = 0
    if len(string) > 0:
        test = len(string)
        for letter in string:
            if ((letter == temp) and (index == len(string)-1)):
                result = result + temp + str(count+1)
            if((letter == temp) and (index < len(string))):
                count = count + 1
            else:
                if(count == 1):
                    result = result + temp
                else:
                    result = result + temp + str(count)
                count = 1
                temp = letter
            index = index + 1
        return result
    else:
        return "Empty String"
    
string = "aabccccaaa"

print(string_compressor(string))