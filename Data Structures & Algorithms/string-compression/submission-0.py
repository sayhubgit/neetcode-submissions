class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0 
        j = 0 
        n = len(chars)

        while i < n:
            current_char = chars[i]
            count = 0 

            while i < n and current_char == chars[i]:
                count += 1
                i += 1

            chars[j] = current_char 
            j += 1

            if count > 1:
                for digit in str(count):
                    chars[j] = digit
                    j += 1
        return j 
