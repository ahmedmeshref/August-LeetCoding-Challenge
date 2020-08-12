/**
 * Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
 * @param {number} rowIndex
 * @return {number[]}
 */
let getRow = function (rowIndex) {
    let result = [1];
    for (let i = 1; i < rowIndex + 1; i++) {
        result.push(Math.floor(result[i - 1] * (rowIndex - i + 1) / i));
    }
    return result;
};
