
def find_anagrams(string1,string2):
    i = 0
    string_1 = string1.lower()
    string_2 = string2.lower()
    cleared_string_1 = ''.join(char for char in string_1 if char.isalnum())
    cleared_string_2 = ''.join(char for char in string_2 if char.isalnum())

    if len(cleared_string_1) == len(cleared_string_2):
        while i < len(cleared_string_1):
            if (cleared_string_1.count(cleared_string_1[i]) == cleared_string_2.count(cleared_string_2[i])):
                i = i+1
            else:print('strings are not anagrams')
        print('strings are anagrams')
    else: print('strings are not anagrams')

find_anagrams(string1='AaBbcc',string2='bacabc')