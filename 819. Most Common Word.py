class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.split('\W+',paragraph)
        print(words)
        words_dict={}
        max_len = 0
        for each in words:
            if each.lower() not in banned:
                words_dict[each.lower()] = words_dict.get(each.lower(),0)+1
                max_len = max(max_len,words_dict[each.lower()])
                
        for each in words:
            if words_dict.get(each.low
