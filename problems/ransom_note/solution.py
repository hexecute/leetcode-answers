class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        storage = {}
        for letter in magazine:
            storage[letter] = storage.get(letter, 0) + 1
        for letter in ransomNote:
            remaining = storage.get(letter, 0) - 1
            if remaining < 0:
                return False
            storage[letter] = remaining
        return True
            