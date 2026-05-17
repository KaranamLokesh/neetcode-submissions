class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = map(str, digits)
        number = int(''.join(digits)) +1
        return list(map(int, str(number)))
        