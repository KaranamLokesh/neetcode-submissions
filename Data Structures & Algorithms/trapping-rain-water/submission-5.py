class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, 1
        water = 0
        count = 0

        while j < len(height):
            if height[j] >= height[i]:
                # Found a right boundary taller or equal to left boundary
                water += (min(height[i], height[j]) * (j - i - 1)) - count
                i = j
                count = 0
            else:
                # Accumulate heights between boundaries
                count += height[j]
            j += 1

        # Now handle case where no taller bar was found on right side, 
        # by scanning from right to left (this is necessary)
        if i < len(height) - 1:
            
            # Repeat same logic from right side towards the last tallest bar found (i)
            i, j = len(height) - 1, len(height) - 2
            count = 0

            while j >= 0:
                if height[j] > height[i]:
                    water += (min(height[i], height[j]) * (i - j - 1)) - count
                    i = j
                    count = 0
                else:
                    count += height[j]
                j -= 1

        return water
