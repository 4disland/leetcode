/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    Solution(ListNode* head) {
        _head = head;
    }
    
    /** Returns a random node's value. */
    int getRandom() {
        int i=1;
        ListNode *cur = _head;
        int ans = _head->val;
        while(cur->next) {
            cur = cur->next;
            if( rand()%++i == 0 )
                ans = cur->val;
        }

        return ans;
    }
private:
    ListNode *_head;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */

 /*
 given n elements, randomly select k out of n elements, with each elements selected with probability k/n 
 reservoir sampling method is used to solve this problem.

 basic idea:
 choose 1,2,3,...,k in the reservior;
 for k+1, choose it with probability k/(k+1), then randomly replace a number in the reservoir;
 for k+i, choose it with probability k/(k+i), then randomly replace a number in the reservoir;
 until k+i equals n;
 */