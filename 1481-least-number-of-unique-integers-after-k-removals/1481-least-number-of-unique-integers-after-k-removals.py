class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count_dict = {}
        val_list = []
        for i in arr:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
        sorted_dict = sorted(count_dict.items(),key = lambda x:x[1])
        converted_dict = dict(sorted_dict)
        for i in converted_dict:
            val_list.append(i)
        for i in range(k):
            converted_dict[val_list[0]] -= 1
            if converted_dict[val_list[0]] == 0:
                del converted_dict[val_list[0]]
                val_list.pop(0)
        return len(converted_dict)

        