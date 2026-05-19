class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        result = right
        
        def canShip(cap):
            ship = 1
            currentCap = cap
            
            for w in weights:
                if currentCap - w < 0:
                    ship += 1
                    if ship > days:
                        return False
                    currentCap = cap
                currentCap -= w
            return True


        while left <= right:
            cap = (left + right) // 2

            if canShip(cap):
                result = min(result, cap)
                right = cap - 1
            else:
                left = cap + 1
            
        return result