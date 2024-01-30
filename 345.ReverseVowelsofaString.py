class Solution(object):
    def reverseVowels(self, s):
        vowels = set("aeiouAEIOU")
        str_list = list(s)
        i, j = 0, len(s) - 1

        while i < j:
            if str_list[i] in vowels and str_list[j] in vowels:
                str_list[i], str_list[j] = str_list[j], str_list[i]
                i += 1
                j -= 1
            elif str_list[i] not in vowels:
                i += 1
            elif str_list[j] not in vowels:
                j -= 1
            else:
                i += 1
                j -= 1

        return ''.join(str_list)
