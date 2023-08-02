class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boatNum = 0
        i = 0
        j = len(people) - 1
        people.sort()
        people.reverse()
        while i < len(people):
            if (people[i] + people[j]) <= limit :
                boatNum += 1
                i += 1
                j -= 1
            else : 
                boatNum += 1
                i += 1
            if j < i :
                return boatNum
        return boatNum




                

             