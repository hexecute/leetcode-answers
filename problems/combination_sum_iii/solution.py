class Solution(object):
    def __init__(self):
        self.helper = []
        
    def combinationSum3(self, k, n):
        self.foo(k, n, [])
        uniq = set()
        for each in self.helper:
            string_version = ','.join([str(x) for x in sorted(each)])
            if string_version in uniq:
                continue
            uniq.add(string_version)
        return [x.split(',') for x in uniq]
        
    def foo(self, k, n, inclusion):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        rv = []
        if k == 0 and n == 0:
            self.helper.append(inclusion)
        elif k == 0 or n <= 0:
            return
        for i in range(1, 10):
            if i in inclusion:
                continue
            self.foo(k - 1, n - i, list(inclusion) + [i])
        return
        
