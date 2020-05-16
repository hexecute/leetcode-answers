class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        rv = ""
        for i in range(len(num)):
            if i < k:
                continue
            elif i == k:
                for j in range(i + 1):
                    if j == 0:
                        leftmost = 0
                    else:
                        if int(num[j]) < int(num[leftmost]):
                            leftmost = j
                rv += str(num[leftmost])
                k_prime = k - (j + 1)
                possibles = [c for c in num[leftmost + 1:k + 1]]
            else:
                possibles.append(num[i])
                for j in range(len(possibles)):
                    if j == 0:
                        leftmost = 0
                    else:
                        if int(possibles[j]) < int(possibles[leftmost]):
                            leftmost = j
                rv += str(possibles[leftmost])
                possibles = possibles[leftmost + 1:]
        rv = rv.lstrip("0")
        if not rv:
            rv = "0"
        return rv
            