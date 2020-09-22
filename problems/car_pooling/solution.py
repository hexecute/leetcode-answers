class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        if not trips:
            return True
        
        deltas = []
        for trip in trips:
            deltas.append([trip[1], trip[0]])
            deltas.append([trip[2], -trip[0]])
            
        deltas = sorted(deltas, key=lambda delta: delta[0])
        for i in range(len(deltas)):
            capacity -= deltas[i][1]
            # "De-duping" events
            if capacity < 0 and (i != len(deltas) - 1) and deltas[i][0] != deltas[i + 1][0]:
                return False
        return True