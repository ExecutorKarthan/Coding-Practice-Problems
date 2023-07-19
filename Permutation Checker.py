def permutation_checker(string1, string2):
    if(len(string1) == len(string2)):
        for letter in string1:
            letter_value = string2.find(letter)
            if letter_value > -1:
                string2 = string2.replace(letter, "", 1)
            else:
                return False, print("These are not permutations")
        return True, print("These are permutations")
    else:
        return False, print("These are not permutations")
    
string1 = input("What is the value of string1?   ")
string2 = input("What is the value of string2?   ")

permutation_checker(string1, string2)