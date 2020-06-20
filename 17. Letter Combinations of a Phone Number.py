class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        char_map = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
        }
        if not digits:
            return []
        
        def recur(result,cur_list,idx):
            if idx == len(digits):
                result.append("".join(cur_list))
                return
            for char in char_map[digits[idx]]:
                cur_list.append(char)
                recur(result,cur_list,idx+1)
                cur_list.pop()
        recur(result,[],0)
        return result
