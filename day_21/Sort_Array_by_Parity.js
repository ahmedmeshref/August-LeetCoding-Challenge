/**
 * @param {number[]} A
 * @return {number[]}
 */
var sortArrayByParity = function(A) {
    let even = [],
        odd = [];
    for (const num of A){
        if (num % 2) odd.push(num);
        else even.push(num);
    }
    return even.concat(odd);
};