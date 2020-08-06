/** Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear   once. Find all the elements that appear twice in this array without extra space and in O(n) runtime.
 * @param {number[]} nums
 * @return {number[]}
 */
let findDuplicates = function(nums) {
    let dup = [],
        ind;
    for (let num of nums){
        ind = Math.abs(num) - 1;
        nums[ind] *= -1;
        if (nums[ind] > 0){
            dup.push(ind + 1);
        }
    }
    return dup;
};