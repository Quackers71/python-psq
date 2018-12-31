from urllib.request import urlopen

with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words = []
    for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                    story_words.append(word)

print(story_words)

full_str = ""
for i in story_words:
    full_str += str(i) + " "
full_str = full_str[:-1]
print(full_str)

# or try this
story_words = ' '.join(map(str, story_words))
print(story_words)
