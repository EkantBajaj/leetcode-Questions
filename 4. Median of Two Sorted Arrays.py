class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        
        if (nums1_len > nums2_len):
            return self.findMedianSortedArrays(nums2,nums1)
        
        low = 0
        high = nums1_len
        
        while(low<=high):
            partition_nums1 = (low+high)//2
            partition_nums2 = (nums1_len+nums2_len+1)//2 - partition_nums1
            
            max_left_x = nums1[partition_nums1-1] if partition_nums1 else -float('inf')
            min_right_x = nums1[partition_nums1] if partition_nums1 < nums1_len else float('inf')
            
            max_left_y = nums2[partition_nums2-1] if partition_nums2 else -float('inf')
            min_right_y = nums2[partition_nums2] if partition_nums2 < nums2_len else float('inf')
            
            if (max_left_x<=min_right_y and max_left_y <= min_right_x):
                
                if (nums1_len+nums2_len)%2 == 0:
                    return (max(max_left_x,max_left_y)+min(min_right_x,min_right_y))/2
                else:
                    return max(max_left_x,max_left_y)
            elif(max_left_x>min_right_y):
                high = partition_nums1-1
            else:
                low = partition_nums1+1
