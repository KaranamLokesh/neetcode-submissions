class Solution:
    def backtrackNQueens(self, k, col, pos_diag, neg_diag, res, currSet):
        n = len(col)
        if k < 0:
            res.append([''.join(r) for r in currSet])
            return
        
        for i in range(n):
            if not col[i] and not pos_diag[k-i+n-1] and not neg_diag[k+i]:
                col[i] = True
                pos_diag[k-i+n-1] = True
                neg_diag[k+i] = True
                currSet[k][i] = 'Q'
                self.backtrackNQueens(k-1, col, pos_diag, neg_diag, res, currSet)
                col[i] = False
                pos_diag[k-i+n-1] = False
                neg_diag[k+i] = False
                currSet[k][i]='.'


    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        currSet = [["."] * n for i in range(n)]
        col = [False]*n
        counter = 2*n-1
        pos_diag = [False]*counter
        neg_diag = [False]*counter
        self.backtrackNQueens(n-1, col, pos_diag, neg_diag, res, currSet)
        return res

        