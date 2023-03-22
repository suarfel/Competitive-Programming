class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        size = 0
        for i  in sentences:
            i = i.split()
            if len(i) > size:
                size = len(i)
        return size
        