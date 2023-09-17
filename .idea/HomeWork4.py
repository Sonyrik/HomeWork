import string
def find_shortest_longest_word(str):
    test_str = str
    print("The original string is : " + test_str)
    for p in string.punctuation:
        if p in test_str:
            test_str = test_str.replace(p, '')
    print("The string after punctuation filter : " + test_str)

    words = test_str.split()

    if test_str=='':
        shortest_word = None
        longest_word = None
    else:
        shortest_word = words[0]
        longest_word = words[0]

        for word in words:
            if len(word) < len(shortest_word):
                shortest_word = word

            if len(word) > len(longest_word):
                longest_word = word
    return (shortest_word, longest_word)

print(find_shortest_longest_word(''))