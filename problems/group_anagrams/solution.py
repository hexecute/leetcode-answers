class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        rv = []
        helper_dict = {}
        for word in strs:
            counts = {}
            for letter in word:
                if counts.get(letter):
                    counts[letter] += 1
                else:
                    counts[letter] = 1
            key = ''
            for k in sorted(counts.keys()):
                key += k
                key += str(counts[k])
            if helper_dict.get(key):
                helper_dict[key].append(word)
            else:
                helper_dict[key] = [ word ]
        for v in helper_dict.values():
            rv.append(v)
        return rv