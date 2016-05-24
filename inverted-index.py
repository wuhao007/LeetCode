'''
Definition of Document
class Document:
    def __init__(self, id, cotent):
        self.id = id
        self.content = content
'''
class Solution:
    # @param {Document[]} docs a list of documents
    # @return {dict(string, int[])} an inverted index
    def invertedIndex(self, docs):
        # Write your code here
        rt = {}
        for doc in docs:
            for word in doc.content.split():
                if word in rt:
                    rt[word][-1] != doc.id:
                        rt[word].append(doc.id)
                else:
                    rt[word] = [doc.id]
        return rt
