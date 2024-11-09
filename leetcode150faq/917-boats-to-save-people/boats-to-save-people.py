class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat_count = 0
        i,j = 0, len(people) - 1
        while i <= j:
            if people[i]+people[j] <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
            boat_count += 1
        return boat_count

