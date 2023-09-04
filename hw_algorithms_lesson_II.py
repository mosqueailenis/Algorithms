 #level1
 #Task 1.
def reverse_integer(n: int):
    # Convert the integer to a string
    n_str = str(n)
    if n < 0:
        reversed_str = '-' + n_str[:0:-1]
    else:
        reversed_str = n_str[::-1]
    reversed_int = int(reversed_str)
    return reversed_int


original_number = -907
reversed_number = reverse_integer(original_number)
print(reversed_number)

#Task2


def are_anagrams(s1: str, s2: str):
    s1 = s1.lower()
    s2 = s2.lower()
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)
    if sorted_s1 == sorted_s2:
        return True
    else:
        return False


word1 = "mice"
word2 = "rice"
print(are_anagrams(word1, word2))

word1 = "hEArt"
word2 = "earth"
print(are_anagrams(word1, word2))

word1 = "rattle"
word2 = "battle"
print(are_anagrams(word1, word2))


#Level 2
#task 3
def reverse_words(sentence: str):
    words = sentence.split()
    reversed_words = []
    for word in words:
        reversed_word = word[::-1]
        reversed_words.append(reversed_word)
        reversed_sentence = " ".join(reversed_words)
        return reversed_sentence


sentence1 = "Hello World"
result1 = reverse_words(sentence1)
print(result1)

sentence2 = "mistertwister"
result2 = reverse_words(sentence2)
print(result2)


#task4

def repeat_digits(s: str):
    result = ""

    for char in s:
        current_num = int(char)
        repeated_char = char * current_num
        result += repeated_char
    return result


input_str1 = "641"
output_str1 = repeat_digits(input_str1)
print(output_str1)

input_str2 = "802"
output_str2 = repeat_digits(input_str2)
print(output_str2)

#task5


def shortcut(s: str):
    result = ""

    for char in s:
        if char not in "aeiou":
            result += char

    return result


input1 = "babygirl"
output1 = shortcut(input1)
print(output1)

input2 = "welcome"
output2 = shortcut(input2)
print(output2)
