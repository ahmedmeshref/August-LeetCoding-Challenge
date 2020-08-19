/**
 * Get all non-negative integers of length N such that the absolute
 *  difference between every two consecutive digits is K.
 * @param {number} N
 * @param {number} K
 * @return {number[]}
 */
let numsSameConsecDiff = function (N, K) {
    function dfs(num, ln) {
        // base case
        if (ln === N) {
            // check for not allowed duplicates
            if (!ans || num !== ans[ans.length - 1]) ans.push(num);
            return
        }
        let last_digit = num % 10;
        ln++;
        num *= 10;
        if (last_digit + K < 10) dfs(num + last_digit + K, ln);
        if (last_digit - K >= 0) dfs(num + (last_digit - K), ln);
    }

    let ans = N === 1 ? [0] : [];
    for (let i = 1; i <= 9; i++) {
        dfs(i, 1);
    }
    return ans;
};


console.log(8 * (8 ** 2))
console.log(numsSameConsecDiff(8, 1).length)