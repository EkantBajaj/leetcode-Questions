class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_list = version1.split('.')
        version2_list = version2.split('.')
        
        if len(version1_list)<len(version2_list):
            version1_list.extend([0]*(len(version2_list)-len(version1_list)))
            
        else:
            version2_list.extend([0]*(len(version1_list)-len(version2_list)))
        
        res = 0
        for i in range(len(version1_list)):
            if int(version1_list[i])>int(version2_list[i]):
                res = 1
                break
            elif int(version1_list[i])<int(version2_list[i]):
                res=-1
                break
        return res
