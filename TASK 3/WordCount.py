paragraph = input("Enter a paragraph: ")

word_count = {}
for word in paragraph.split():
    word = word.strip('.,!?";:()[]{}')
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


print("\nWord Count:")
for word, count in word_count.items():  
    print(f"{word}: {count}")

