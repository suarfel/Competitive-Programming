class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat)*len(mat[0]) :
            return mat
        new_mat = [[]]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if len(new_mat[-1]) < c:
                    new_mat[-1].append(mat[i][j])
                else:
                    new_mat.append([])
                    new_mat[-1].append(mat[i][j])
        return new_mat
                
                
                
                