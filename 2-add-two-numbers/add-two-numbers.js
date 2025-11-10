/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let res = new ListNode()
    let cur = res
    let carry = 0;

    while (l1 || l2 || carry) {
        let v1 = 0;
        let v2 = 0;

        if (l1){
            v1 = l1.val
            l1 = l1.next
        }
        if(l2){
            v2 = l2.val
            l2 = l2.next
        }

        value = v1 + v2 + carry
        carry = Math.floor(value / 10)
        value %= 10
        
        cur.next = new ListNode(value)
        cur = cur.next
    }

    return res.next

};