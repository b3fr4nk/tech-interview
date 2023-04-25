# 21. Merge Two Sorted Lists
# Easy
# 18K
# 1.7K
# Companies

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:

# Input: list1 = [], list2 = []
# Output: []

# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]

 

# Constraints:

#     The number of nodes in both lists is in the range [0, 50].
#     -100 <= Node.val <= 100
#     Both list1 and list2 are sorted in non-decreasing order.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    if list1 is None and list2 is None:
        return None
    elif list1 is None:
        return list2
    elif list2 is None:
        return list1
    
    if list1.val <= list2.val:
        return ListNode(list1.val, mergeTwoLists(list1.next, list2))

    elif list2.val <= list1.val:
        return ListNode(list2.val, mergeTwoLists(list1, list2.next))

list1 = ListNode()
node2 = ListNode()
node3 = ListNode()
list1.val = 1
list1.next = node2
node2.val = 2
node2.next = node3
node3.val = 4

list2 = ListNode()
node5 = ListNode()
node6 = ListNode()
list2.val = 1
list2.next = node5
node5.val = 3
node5.next = node6
node6.val = 4

merged_list = mergeTwoLists(list1, list2)
print(merged_list.val)
out = ''
while merged_list is not None:
    out += f'{merged_list.val}, '
    merged_list = merged_list.next

print(out)