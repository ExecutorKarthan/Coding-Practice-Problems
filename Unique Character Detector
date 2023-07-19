used_letters = []
word = input("What word do you want to test for unique characters?  ")
non_unique = False
for letter in word:
    if non_unique == False:
        for test_letter in used_letters:
            if test_letter == letter:
                non_unique = True
                print("Non-unique letter found", letter)
                break
        used_letters.append(letter)
    else:
        break
if(non_unique == False):
    print("The word has unique letters!")

