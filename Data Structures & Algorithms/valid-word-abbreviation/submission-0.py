class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0 
        j = 0 

        while i < len(word) and j < len(abbr):

            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isalpha():
                return False
            elif abbr[j] == '0':
                return False
            else:
                sublength = 0 
                while j < len(abbr) and abbr[j].isdigit():
                    subslength = sublength * 10 + int(abbr[j])
                    j += 1
                i += subslength
        
        return i == len(word) and j == len(abbr)


                            
            
            

