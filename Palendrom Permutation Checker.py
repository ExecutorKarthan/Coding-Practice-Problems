from string import ascii_lowercase
import random

def palendrome_permutation_detector(string):
    letter_dict = {}
    for letter in ascii_lowercase:
        letter_dict[letter] = 0
    for letter in string:
        lowercase_letter = letter.lower()
        if(lowercase_letter in letter_dict):
            letter_dict[lowercase_letter] = letter_dict[lowercase_letter]+1
    odd_count = 0
    for key in letter_dict:
        if(letter_dict[key] != 0 and letter_dict[key]%2 == 1):
            odd_count += 1
    if odd_count > 1:
        return False, print("This is not a palendrome permutation")
    else:
        return True, print("This is a palendrome permutation.")

correct_palendrome = "Naomi, Gianna, Eddy, Nall, Robert, Allen, Red, Hon, Evan, Eden, Mel, Lola, Alol, Lemned, Enave, Noh, Der, Nella, Trebor, Llan, De, Anna, Ig & I moan."
list_to_mix = []
for letter in correct_palendrome:
  list_to_mix.append(letter)
  random.shuffle(list_to_mix)
string = "".join(list_to_mix)
palendrome_permutation_detector(string)