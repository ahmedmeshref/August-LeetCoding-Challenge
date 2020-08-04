/**
 * Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
 * @param {number} num
 * @return {boolean}
 */
let isPowerOfFour = function(num) {
    if (num == 1) return true;
    else if (num < 4) return false;
    return isPowerOfFour(num/4);
};