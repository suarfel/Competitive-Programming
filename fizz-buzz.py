class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        collecter=[]*n
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                collecter.append("FizzBuzz")
            elif i%3==0:
                collecter.append("Fizz")
            elif i%5==0:
                collecter.append("Buzz")
            else:
                collecter.append(str(i))
        return collecter