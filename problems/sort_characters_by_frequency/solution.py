class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        frequencies = {}
        reverse_frequencies = {}
        rv = ""
        for c in s:
            frequencies[c] = frequencies.get(c, 0) + 1
        
        
        for k, v in frequencies.items():
            if not reverse_frequencies.get(v):
                reverse_frequencies[v] = [k]
            else:
                reverse_frequencies[v].append(k)
                
        for k in sorted(reverse_frequencies.keys(), reverse=True):
            for c in reverse_frequencies[k]:
                for _ in range(k):
                    rv += c
                
        return rv