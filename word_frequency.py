def word_frequency(sentence):
    words=sentence.replace(".", "").split(" ")
    my_word_frequency={}

    for word in words:
        if word in my_word_frequency:
            my_word_frequency[word] += 1
        else:
            my_word_frequency[word]=1
        
    return my_word_frequency


sentence = "The curious cat explored the mysterious garden under the shimmering moonlight."
result = word_frequency(sentence)
print(result)