/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    if(nums.length === 1){
        return 0;
    }
    for(let i = 1;i < nums.length;i++){
        nums[i] += nums[i-1];
    }
    for(let j = 0;j < nums.length;j++){
        if(j === 0){  
            if(nums[nums.length-1] - nums[j] === 0){
                return 0;
            }
        }
        else if(j === nums.length -1){
            if(nums[j-1] === 0){
                return j;
            }
            else{
                return -1;
            }
        }
        else { 
            if(nums[j-1] === nums[nums.length-1]- nums[j]){
                return j;
            }
        }
    }
};