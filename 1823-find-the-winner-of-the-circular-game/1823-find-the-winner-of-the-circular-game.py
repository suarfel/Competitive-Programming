class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = []
        for j in range(n):
            players.append(j+1)
        i = 0
        def tellWinner(players,k,i):
            if len(players) == 1 :
                return players
            else:
                i += k - 1
                i = i % len(players)
                players.pop(i)
                tellWinner(players,k,i)
            
        tellWinner(players,k,i)
        return players[0]

