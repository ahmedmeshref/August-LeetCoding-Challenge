/**
 * Produce string representation of numbers from 1 to n.
 * Note: for multiples of three it should output “Fizz” instead of the number and for
 * the multiples of five output “Buzz”. For numbers which are multiples of both three
 * and five output “FizzBuzz”.
 * @param {number} n
 * @return {string[]}
 */
let fizzBuzz = function(n) {
    let out = [];
    for (let i = 1; i <= n; i++) {
        if (i % 5 === 0 && i % 3 === 0) out.push("FizzBuzz")
        else if (i % 5 === 0) out.push("Buzz")
        else if (i % 3 === 0) out.push("Fizz")
        else out.push(i.toString())
    }
    return out;
};