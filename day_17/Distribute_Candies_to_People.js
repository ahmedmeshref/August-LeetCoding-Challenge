/**
 * @param {number} candies
 * @param {number} num_people
 * @return {number[]}
 */
var distributeCandies = function(candies, num_people) {
    let rnd = 0,
        res = new Array(num_people).fill(0),
        required_candies;
    while(candies) {
        for (let i = 0; i < num_people; i++){
            if (!candies) break;
            required_candies = (rnd * num_people) + i + 1;
            if (required_candies <= candies){
                res[i] += required_candies; candies -= required_candies;
            } else {
                res[i] += candies; candies = 0;
            }
        }
        rnd++;
    }
    return res;
};