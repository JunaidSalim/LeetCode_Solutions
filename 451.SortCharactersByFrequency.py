class Solution(object):
    def frequencySort(self, s):
        character_counter = Counter(s)
        sorted_characters = character_counter.most_common()
        sorted_string = ''
        for c, f in sorted_characters:
            sorted_string += c * f
        return sorted_string