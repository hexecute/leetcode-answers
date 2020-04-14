class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        first_shift = True
        for single_shift in shift:
            if first_shift:
                total_shift = single_shift
                first_shift = False
            else:
                if single_shift[0] == total_shift[0]:
                    total_shift[1] += single_shift[1]
                else:
                    total_shift[1] -= single_shift[1]

        # Now, to handle
        if total_shift[1] < 0:
            total_shift[0] = 1 - total_shift[0]
            total_shift[1] = total_shift[-1] * -1
        elif total_shift[1] == 0:
            return s
        
        
        length = len(s)
        total_shift[1] = total_shift[1] % length
        
        if total_shift[0]:
            return s[length - total_shift[1]:] + s[:length - total_shift[1]:]
        else:
            return s[total_shift[1]:] + s[:total_shift[1]]