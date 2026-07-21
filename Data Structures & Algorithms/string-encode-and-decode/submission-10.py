class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for string in strs:
            res += str(len(string))+"$" + string
        return res

    def decode(self, s: str) -> List[str]:
        
        result = []
        i = 0

        while i < len(s):

            str_length = ""
            digit_size = 0

            for c in s[i:]:
                if c == "$":
                    break
                else:
                    str_length += c
                    digit_size += 1

            str_length = int(str_length)

            result.append(s[i+digit_size + 1: i+digit_size + 1 + str_length])

            i = i + digit_size + 1 + str_length

        return result 