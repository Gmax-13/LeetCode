class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Stores seen numbers and their corresponding indices
        num_to_index = {}
        
        for current_index, num in enumerate(nums):
            complement = target - num
            
            # Check if the complement already exists in the map
            if complement in num_to_index:
                return [num_to_index[complement], current_index]
            
            # Store the index of the current number
            num_to_index[num] = current_index
            
        return []
