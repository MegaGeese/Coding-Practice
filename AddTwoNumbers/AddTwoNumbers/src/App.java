//Problem: https://leetcode.com/problems/add-two-numbers/
class App {
    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        head.next = null;
        ListNode out = head;
        
        while(true){
            if (l1 == null && l2 == null){
                return head;
            }
            else if (l1 == null){
                l1 = new ListNode(0);
            }
            else if (l2 == null){
                l2 = new ListNode(0);
            }
            int sum = l1.val + l2.val + out.val;
            if (sum > 9){
                out.next = new ListNode(1);
            }
            out.val = sum % 10;
            
            
            l1 = l1.next;
            l2 = l2.next;
            if (out.next == null){
                out.next = new ListNode(0);
            }
            if (l1 == null && l2 == null && out.next.val == 0){
                out.next = null;
            }
            else{
                out = out.next;
            }
            
        }
        
    }
    
    public static void main(String[] args) {
        ListNode l1 = new ListNode(9);
        l1.next = new ListNode(9);
        l1.next.next = new ListNode(9);
        l1.next.next.next = new ListNode(9);
        l1.next.next.next.next = new ListNode(9);
        l1.next.next.next.next.next = new ListNode(9);
        l1.next.next.next.next.next.next = new ListNode(9);
        
        ListNode l2 = new ListNode(9);
        l2.next = new ListNode(9);
        l2.next.next = new ListNode(9);
        l2.next.next.next = new ListNode(9);
        App.addTwoNumbers(l1, l2);
    }
}