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
    let result = new ListNode()
    let cur = result
    let carry = 0

    while(l1 || l2 || carry){
        let v1 = v2 = 0

        if(l1){
            v1 = l1.val
            l1 = l1.next
        }
        if(l2){
            v2 = l2.val
            l2 = l2.next
        }

        val = v1 + v2 + carry
        carry = Math.floor(val / 10)
        val %= 10
        cur.next = new ListNode(val)

        cur = cur.next
    }

    return result.next
};