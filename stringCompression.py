class Solution:
    def compress(self, chars: List[str]) -> int:
        j = 0
        i = 0
        s = []
        while i < len(chars):
            if j != len(chars)-1 and chars[i] == chars[j] :
                j += 1
            elif j == len(chars)-1 and chars[i] == chars[j] :
                if j-i == 0 :
                    s.append(chars[i])
                    i = j + 1
                else :
                    s.append(chars[i])
                    if (j - i + 1) > 9 :
                        temp =  str(j - i + 1)
                        for x in temp:
                            s.append(x)
                    else:
                        s.append(str(j-i + 1))
                    i = j + 1
            else:
                if j-i == 1 :
                    s.append(chars[i])
                    i = j
                else :
                    s.append(chars[i])
                    if (j - i + 1) > 9 :
                        temp =  str(j - i)
                        for x in temp:
                            s.append(x)
                    else:
                        s.append(str(j-i ))
                    i = j
        for i in range(len(s)):
            chars[i] = s[i]
        return len(s)