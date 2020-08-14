/**
 * Given a string which consists of lowercase or uppercase letters, find the length of
 *  the longest palindromes that can be built with those letters.
 * @param {string} s
 * @return {number}
 */
let longestPalindrome = function (s) {
    let occ = {}, ln_longest_pal = 0, odd_exist = false;
    for (const char of s) {
        if (char in occ) occ[char]++;
        else occ[char] = 1;
    }

    for (const val of Object.values(occ)) {
        ln_longest_pal += Math.floor(val / 2) * 2;
        if (val % 2) odd_exist = true;
    }

    return odd_exist ? ln_longest_pal + 1 : ln_longest_pal
};