class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize > 0: return False
        count_map = {}
        for c in hand:
            count_map[c] = count_map.get(c, 0) +1
        sorted_counter_map = dict(sorted(count_map.items()))
        while sorted_counter_map:
            first_key, first_value = next(iter(sorted_counter_map.items()))
            for i in range(groupSize):
                if first_key+i not in sorted_counter_map or  sorted_counter_map[first_key+i] == 0: return False
                sorted_counter_map[first_key+i] -= 1
                if sorted_counter_map[first_key+i] == 0:
                    del sorted_counter_map[first_key+i]
        return True


            






        