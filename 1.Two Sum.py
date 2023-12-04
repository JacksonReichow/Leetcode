class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #make hashmap mapping value to index
        prevMap = {} #val : index
        for i, n in enumerate(nums): 
        #provides index i and num at index n
            diff = target - n 
        #calc each num vs target, 
            if diff in prevMap:
                return [prevMap[diff], i]
                #found soluion to problem
            prevMap[n] = i
            #updates array
        return 
