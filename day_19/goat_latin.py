class Solution:
    def toGoatLatin(self, S: str) -> str:
        """
        convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)
        """
        words = S.split(" ")
        vowels = {"a", "e", "i", "u", "o", "A", "O", "I", "U", "E"}
        added_chars = "ma"
        for i in range(len(words)):
            first_char = words[i][0]
            if first_char in vowels:
                words[i] = words[i] + added_chars + ("a"*(i+1))
            else:
                words[i] = words[i][1:] + first_char + added_chars + ("a"*(i+1))
        return " ".join(words)