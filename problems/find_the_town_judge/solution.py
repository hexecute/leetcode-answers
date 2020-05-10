class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trust_scores = [0] * N
        for relation in trust:
            trust_scores[relation[1] - 1] += 1
            trust_scores[relation[0] - 1] -= 1
        for i in range(len(trust_scores)):
            if trust_scores[i] == N - 1:
                return i + 1
        return -1
            