class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        trans_matrix = []
        for i in range(len(matrix[0])):
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            trans_matrix.append(temp)
        return trans_matrix
    
        