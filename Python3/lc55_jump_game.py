class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr_idx = 0
        max_jump = nums[0]
        while (curr_idx < len(nums)):
            if (len(nums)-1) <= curr_idx + max_jump:
                return True
            else:
                i = curr_idx + 1
                while(i < len(nums) and i <= curr_idx+max_jump and nums[i]+i <= curr_idx + max_jump):
                    i += 1

                if (i < len(nums) and i <= curr_idx+max_jump):
                    max_jump = nums[i]
                    curr_idx = i
                else:
                    return False

        return False