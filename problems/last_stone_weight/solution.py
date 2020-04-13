class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stone_storage = {}
        total_stones = len(stones)
        for stone in stones:
            if stone_storage.get(stone):
                stone_storage[stone] += 1
            else:
                stone_storage[stone] = 1
        
        weight = 1000
        while (weight >= 0):
            # No more stones to process
            if (total_stones == 0):
                return 0
            stone_quantity = stone_storage.get(weight, 0)
            if stone_quantity:
                # print(stone_storage)
                # This stone is the last one to process
                if (total_stones == 1):
                    return weight
                remainder = stone_quantity % 2
                total_stones -= (stone_quantity - remainder)
                # Smash against a smaller stone
                if remainder:
                    smaller_weight = weight - 1
                    while (smaller_weight >= 0):
                        if stone_storage.get(smaller_weight, 0):
                            stone_storage[weight] = 0
                            stone_storage[smaller_weight] -= 1
                            if stone_storage.get(weight - smaller_weight):
                                stone_storage[weight - smaller_weight] += 1
                            else:
                                stone_storage[weight - smaller_weight] = 1
                            total_stones -= 1
                            break
                        else:
                            smaller_weight -= 1
                else:
                    stone_storage[weight] = 0  
            else:
                weight -= 1