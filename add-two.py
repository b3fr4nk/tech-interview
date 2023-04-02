#given two non-empty linked lists representing non-zero numbers
#the digits are stored in reverse order, and each node contains a single digit
#assume no leading zeroes except 0 itself

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.


class ListNode:
    """ Given in the problem """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def make_list_from_ListNode(l1):
    list1 = []
    # loop over every list node and add it to the list above
    while l1: #is not None
        list1.append(l1.val)
        l1 = l1.next
    return list1

def make_ListNode_from_list(a_list):
    head = l3 = ListNode(a_list[0])
    for x in a_list[1:]:
        l3.next = l3 = ListNode(x)
    return head

class Solution:
    def addTwoNumbers(self, l1, l2):
        # create two list to store the numbers
        list1 = make_list_from_ListNode(l1)
        list2 = make_list_from_ListNode(l2)

        len_list1 = len(list1)
        len_list2 = len(list2)

        # add zeroes to make the numbers the same number of digits
        if len_list1 > len_list2:
            pad = len_list1 - len_list2
            list2 = list2 + [0,] * pad
        elif len_list2 > len_list1:
            pad = len_list2 - len_list1
            list1 = list1 + [0,] * pad

        # add up the two numbers
        d = 0
        the_sum = list()
        for x,y in zip(list1, list2):   #zip makes an iterable of two other iterables, with the shortest iterable being the oen that is checked for length
            # d is the floor division of the sum of x, y, and previous d divided by 10, m is the sum of x, y, and d mod 10
            d, m = divmod(x + y + d, 10)    
            the_sum.append(m)
        if d != 0:  #d is the carryover digit so adding zero would make the number wrong or have no effect
            the_sum.append(d)
        return make_ListNode_from_list(the_sum)