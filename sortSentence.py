class Solution:
    def sortSentence(self, s: str) -> str:
        sentence=[]
        pair= {}
        collecter=s.split()
        for i in collecter:
            pair[int(i[-1])] = i[:-1]
        for i in range(1,len(collecter)+1):
            sentence.append(pair[i])
        sentence=' '.join(sentence)
        return sentence