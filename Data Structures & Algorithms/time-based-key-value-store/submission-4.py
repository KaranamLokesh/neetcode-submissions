class TimeMap:

    def __init__(self):
        self.mood_map = {}
    
    def bin_search(self,entries, timestamp):
        low,high = 0, len(entries)-1
        res = ""
        while low <= high:
            
            mid = low + (high-low)//2
            if entries[mid][0] <= timestamp:
                res = entries[mid][1]
                low = mid+1
            else:
                high = mid-1
        return res


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mood_map:
            self.mood_map[key] = []
        
        # Set the value at the given timestamp
        self.mood_map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        entries = self.mood_map.get(key, [])
        return self.bin_search(entries, timestamp) if entries else ""
        
