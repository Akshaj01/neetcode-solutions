/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    void reorderList(ListNode* head) {
        
        ListNode* slow = head;
        ListNode* fast = head;

        //get midpoint
        while (fast and fast->next){
            fast = fast->next->next;
            slow = slow->next;
        }
        ListNode* r = slow->next; //save start of second list
        slow->next = nullptr; //seperates lists

        //reverse second half of list
        ListNode* curr = r;
        ListNode* prev = nullptr;
        
        while(curr){ //reverse second list
            ListNode* temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }

        //merge two lists into 1
        ListNode* l1 = head;
        ListNode* l2 = prev;

        while (l2){
            ListNode* t1 = l1->next;
            ListNode* t2 = l2->next;
            l1->next = l2;
            l1 = t1;
            l2->next = l1;
            l2 = t2;
        }

    }
};
