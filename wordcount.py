
text_file = open(raw_input("> "))

word_dictionary = {}

for line in text_file:
    word_list = line.split()

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

# for word, frequency in word_dictionary.items():
for word, frequency in word_dictionary.iteritems():
    print "{} {}".format(word, frequency)

text_file.close()
    # .get not quite working, Heather is helping
    # for word in word_list:
    #     # if word in word_dictionary:
    #     #     word_dictionary[word] += 1
    #     # else:
    #     #     word_dictionary[word] = 1
    #     word_frequency = word_dictionary.get(word, 0) + 1
    #     print word_frequency