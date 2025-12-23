class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        digits = set(str(num) for num in range(0, 10))
        state = "number" if abbr[0] in digits else "letter"
        curr_num = 0
        word_ptr = 0
        for i, char in enumerate(abbr):
            if word_ptr >= len(word): return False

            if state == "letter":
                if word[word_ptr] != char:
                    return False

                if i < len(abbr) - 1 and abbr[i + 1] in digits:
                    state = "number"

                word_ptr += 1

            elif state == "number":
                curr_num = curr_num * 10 + int(abbr[i])
                if curr_num == 0:
                    return False

                if i == len(abbr) - 1 or abbr[i + 1] not in digits:
                    if word_ptr + curr_num > len(word):
                        return False

                    word_ptr += curr_num
                    curr_num = 0
                    state = "letter"

        return word_ptr == len(word)
