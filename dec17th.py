class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        charFrequency = [0] * 26
        for ch in s:
            charFrequency[ord(ch) - ord('a')] += 1

        result = []
        i = 25
        while i >= 0:
            if charFrequency[i] == 0:
                i -= 1
                continue

            times = min(charFrequency[i], repeatLimit)
            result.extend(alphabet[i] for _ in range(times))
            charFrequency[i] -= times

            if charFrequency[i] > 0:
                j = i - 1
                while j >= 0 and charFrequency[j] == 0:
                    j -= 1
                if j < 0:
                    break
                result.append(alphabet[j])
                charFrequency[j] -= 1

        return ''.join(result)