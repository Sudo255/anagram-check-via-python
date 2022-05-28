# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # convert both the strings into lowercase
    string1 = word.lower()
    string2 = anagram.lower()
    
    # check if they have equal length
    if(len(string1) == len(string2)):
        # sort the strings
        sorted_string1 = sorted(string1)
        sorted_string2 = sorted(string2)

        # if sorted char arrays are same
        if(sorted_string1 == sorted_string2):
            return True
        else:
            return False

    else:
        return False

