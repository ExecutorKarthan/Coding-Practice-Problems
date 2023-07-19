def HTMLify (string, length):
    result_string_list = []
    for index in range(0, length+1):
        if string[index] == " ":
            result_string_list.append("%20")
        else:
            result_string_list.append(string[index])
    result_text = "".join(result_string_list)
    print(result_text)
    
HTMLify(input("What string do you want to HTMLify?     "), 13)