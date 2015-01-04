def reverse_sentence(sentence):
    return ' '.join(map(lambda x : x[::-1], sentence.split()))
print reverse_sentence("the boy ran")
