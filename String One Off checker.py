def diff_size_string (large_string, small_string, num_diff):
    index = 0
    for letter in large_string:
        if index >= len(small_string):
            break
        if letter == small_string[index]:
            print("Letter Match")
        else:
            if letter == small_string[index +1]:
                num_diff = num_diff + 1
                index = index + 1
            else:
                return num_diff
        index = index +1
    return num_diff
        
num_diff = 100
str1, str2 = input("What two strings are you entering to check if they are off by one?    ").split()
if(len(str1) == len(str2)):
    num_diff = 0
    for index in range (0, len(str1)):
        if str1[index] == str2[index]:
            continue
        else:
            num_diff == num_diff + 1
if(len(str1) - len(str2) == 1 or len(str2) - len(str1) == 1):
    num_diff = 0
    if(len(str1) > len(str2)):
        diff_size_string(str1, str2, num_diff)
    else:
        diff_size_string(str2, str1, num_diff)        
if num_diff <= 1:
    print(True)
else:
    print(False)