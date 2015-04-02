listObject = { ('jack', 'jill'): 'NAME', ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine') : 'NUM' }  
class TaggedSentence:
    def __init__(self):
        self.original = ''
        untagged = []
        tagged = []
        classrTagged = []

    def input(self, sentence):
        self.original = sentence
    
    def output(self):
        print 'input:       ', self.original
        sentence = self.original.lower().split()

        untagged = []
        tagged = []
        classrTagged = []
        for word in sentence:
            for key, value in listObject.items():
                if word in key:
                    tagged += [word]
                    classrTagged += [value]
            else:
                untagged += [word]
                classrTagged += [word]
        print 'untagged:    ', ' '.join(untagged)
        print 'tagged:      ', ' '.join(tagged)
        print 'class tagged:', ' '.join(classrTagged)

tagged_sentence = TaggedSentence()
tagged_sentence.input("I'm Jack and I'm three years old")
tagged_sentence.output()
