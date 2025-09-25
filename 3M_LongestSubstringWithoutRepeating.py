class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = []
        maxlen = 0
        for i in range(len(s)):
            if s[i] in characters:
                ind = characters.index(s[i])
                if ind == len(characters)-1:
                    characters = []
                else:
                    characters = characters[ind+1:]
                characters+=s[i]
                maxlen = max(maxlen, len(characters))
            else:
                characters+=s[i]
                maxlen = max(maxlen, len(characters))
        return maxlen