class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        # i = 0 
        # j = i + 1
        # k = j + 1
        # arr.sort()
        # counter = 0
        # while i < len(arr)-2  :
        #     if (k < len(arr) - 1):
        #         if arr[i] + arr[j] + arr[k] == target :
        #             counter += 1
        #             k += 1
        #         else :
        #             k += 1
        #     elif (k == len(arr)-1) and  j < k-1 :
        #         if  arr[i] + arr[j] + arr[k] == target :
        #             counter += 1
        #             j += 1 
        #             k = j + 1
        #         else:
        #             j += 1 
        #             k = j + 1
        #     elif (k == len(arr)-1) and  j == k-1 :
        #         if  arr[i] + arr[j] + arr[k] == target :
        #             counter += 1
        #             i += 1
        #             j = i + 1 
        #             k = j + 1
        #         else:
        #             i += 1
        #             j = i + 1 
        #             k = j + 1
        # return counter % (pow(10,9) + 7)
        # distnictSet = set()
        # arrDict ={}
        # sumList = []
        # counter = 0
        # for i in arr:
        #     distnictSet.add(i)
        #     if i not in arrDict :
        #         arrDict[i] = 1
        #     else :
        #         arrDict[i] += 1
        # distnictList = list(distnictSet)
        # distnictList.sort()
        # for i in range(len(distnictList)):
        #     for j in range(i+1,len(distnictList)):
        #         for k in range(j+1,len(distnictList)):
        #             if distnictList[i] + distnictList[j] + distnictList[k] == target :
        #                 sumList.append([distnictList[i],distnictList[j],distnictList[k]])
        # print(distnictList)
        # print(arrDict)
        # print(sumList)
        # for i in sumList:
        #     if i[0] != i[1] and i[0] != i[2] and i[1] != i[2] :
        #         temp =  arrDict[i[0]] * arrDict[i[0]] * arrDict[i[0]] 
        #         counter += temp
        #     elif i[0] == i[1] and i[0] != i[2] :
        #         temp = *
        # return counter
        arr.sort()
        ans = 0
        for i in range(2, len(arr)):
            j, k = 0, i - 1
            while j < k:
                sm = arr[i] + arr[j] + arr[k]
                if sm < target:
                    j += 1
                elif sm > target:
                    k -= 1
                else:
                    l = r = 1
                    while j + l < k and arr[j] == arr[j + l]:
                        l += 1
                    while j + l <= k - r and arr[k] == arr[k - r]:
                        r += 1
                    ans += (l + r) * (l + r - 1) // 2 if arr[j] == arr[k] else l * r
                    j += l;
                    k -= r;
        return ans % (10 ** 9 + 7)
