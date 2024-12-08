class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        space_index = 0
        result = ""
        index = 0
        for i in range(len(s)):
            if space_index < len(spaces):
                if i == spaces[space_index]:
                    result += s[index:i] + " "
                    index = i
                    space_index += 1
        return result + s[index:]
