class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        # Linear space
        helper = {}
        rv = []
        for num in nums:
            helper[num] = helper.get(num, 0) + 1
        for k, v in helper.iteritems():
            if v > (len(nums) / 3):
                rv.append(k)
        return rv
        """
        count_1 = 0
        count_2 = 0
        candidate_1 = None
        candidate_2 = None
        for num in nums:
            if count_1 == 0 and candidate_2 != num:
                candidate_1 = num
            if count_2 == 0 and candidate_1 != num:
                candidate_2 = num
            if num == candidate_1:
                count_1 += 1
            elif num == candidate_2:
                count_2 += 1
            else:
                count_1 -= 1
                count_2 -= 1
        rv = []
        if candidate_1 is not None:
            verification_count = 0
            for num in nums:
                if num == candidate_1:
                    verification_count += 1
            if verification_count > len(nums) / 3:
                rv.append(candidate_1)
        if candidate_2 is not None:
            verification_count = 0
            for num in nums:
                if num == candidate_2:
                    verification_count += 1
            if verification_count > len(nums) / 3:
                rv.append(candidate_2)
        return rv