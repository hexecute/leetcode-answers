# from math import ceil, log

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        k = 0
        while n != m:
            n >>= 1
            m >>= 1
            k += 1
        return n << k
        """
        if m == n:
            return m
        range_size = n - m + 1
        num_zeroed_right_bits = int(ceil(log(range_size, 2)))
        interval = 2 ** num_zeroed_right_bits
        # print(num_zeroed_right_bits)
        # print((interval, m % interval, n % interval))
        if m % interval < n % interval:
            return int(m / interval) * interval
        else:
            i = 0
            test_val = 1
            while (test_val <= n):
                if (test_val >= m and test_val <= n):
                    return 0
                else:
                    i += 1
                    test_val = 2 * test_val
            i -= 1
            rv = 0
            while (True):
                temp = (n >> i) & 1
                if n >> i == m >> i:
                    rv += (temp * 2 ** i)
                    i -= 1
                else:
                    return rv
                
        """
        """
            rv = m >> num_zeroed_right_bits
            for i in range(m + 1, n + 1):
                rv = rv & (i >> num_zeroed_right_bits)
            return (rv << num_zeroed_right_bits)
        """