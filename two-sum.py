#given an array of integers nums and a target integer find the two numbers that add up to target
#example Input: nums = [3, 2, 4], target = 6
#Output: [1, 2]

def twoSum(nums, target):
    #create a hashmap/dictionary
    nums_dict = {}
    #loop over each element in nums
    for num_i in range(len(nums)):
        #find the necessary to number to add up to target
        diff = target - nums[num_i]
        #check the hashmap for the presence of a number + num = target
        if diff in nums_dict:
            #if present return the two indices
            return (nums_dict[diff], num_i)
        #else add the current num to the dict with the number being the key and the index the value
        else:
            nums_dict[nums[num_i]] = num_i

if __name__ == "__main__":
    print(twoSum([3, 2, 4], 5))