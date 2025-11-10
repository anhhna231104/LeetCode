/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let n = x, res = 0

    while(n){
        let tmp = n % 10
        res = res*10 + tmp
        n = parseInt(n / 10)
    }

    if (res > 2**31 - 1 || res < (-2)**31){
        return 0
    }
    return res
};