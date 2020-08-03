/**
 * @param {string} s
 * @return {boolean}
 */
let isPalindrome = function (s) {
    let re = /[a-zA-Z0-9]+/gi,
        complete_str = [...s.matchAll(re)].join("").toLowerCase(),
        word_len = complete_str.length;
    for (let i = 0; i <= word_len/2; i++){
        if (complete_str[i] !== complete_str[word_len-i-1]) return false;
    }
    return true;
};
