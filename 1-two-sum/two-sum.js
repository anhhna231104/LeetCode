/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    hash = []

    for(let i = 0; i < nums.length; i++){
        comp = target - nums[i]
        if (comp in hash){
            return [i, hash[comp]];
        }
        else{
            hash[nums[i]] = i
        }
    }
};