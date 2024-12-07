# 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        source = sentence.split()
        for i in range(len(source)):
            if source[i].startswith(searchWord):
                return i + 1

        return -1