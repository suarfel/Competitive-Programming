class Solution:
    def reverse(self, x: int) -> int:
        str_num = ""
        x = str(x)
        for i in x:
            str_num = i + str_num
        if str_num[-1] == '-':
            str_num = "-" + str_num
            str_num = str_num[0:len(str_num)-1]
        if int(str_num) >= pow(2,31)-1 or int(str_num) <= -pow(2,31):
            return 0
        else:
            return int(str_num)
        