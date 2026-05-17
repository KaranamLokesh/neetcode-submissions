class Solution:
    def calc_two(self, digitToChar, res, second):
        if res == []:
            return list(digitToChar[second])
        n = len(digitToChar[second])
        temp = []
        for i in res:
            for char in digitToChar[second]:
                temp.append(i+ char) 
        return temp

    def check (self, digits, res, digitToChar):
        n = len(digits)   
        ## recursive case
        for digit in digits:
            res = self.calc_two(digitToChar, res, digit)
        return res

    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        if len(digits) == 0:
            return []
        if len(digits) ==1:
            return list(digitToChar[digits])

        return self.check(digits, res, digitToChar)
        
