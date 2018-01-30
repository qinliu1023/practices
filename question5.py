class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

# When ll is the first node of a linked list, to find the mth number from the end
# We can first find out the length of the linked list, say how many items there
# Then we can do a loop to find the mth number from the end
# To identiy a circled singly linked list, I use a set to store all tranvsvered nodes
# If one node attemps to be added to the set twice, the loop will be broken and return -1
# which means, the linked listed is circled

def LinkedListLength(FirstNode):
    if FirstNode.next == None:
        return 1
    else:
        item_counts = 1
        curr_node = FirstNode
        next_node = FirstNode.next
        node_tranversed = set()
        while curr_node != next_node:
            if curr_node not in node_tranversed:
                node_tranversed.add(curr_node)
                curr_node = next_node
                if next_node.next != None:
                    next_node = next_node.next
                item_counts += 1
            else:
                item_counts = -1
                break
                
        return item_counts                

def question5(ll, m):
    # make sure inputs are valid
    if type(ll) != Node:
        return "Error: Invalid Linked List"
    if type(m) != int:
    	return "Error: Invalid Integer Parameter "
    # make sure linked list is not a circled one	
    if LinkedListLength(ll) == -1:
        return "Error: Circled singly linked list"

    # get the length of ll and make sure m is valid for ll
    length_starts_ll = LinkedListLength(ll)
    if length_starts_ll < m:
        return "Error: Second Parameter is out of range"
    else:
        curr_node = ll
        for i in range(length_starts_ll - m):
            curr_node = curr_node.next
        
        return curr_node.data

####### Test Cases ######
n1, n2, n3, n4, n5, n6, n7, n8 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(8)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
print question5(n3,4)
print question5(n3,7)
"""
should be:
    5
    Error: Second Parameter is out of range
"""
n11, n12, n13 = Node(11), Node(12), Node(13)
n11.next = n12
n12.next = n13
n13.next = n11
print question5(n11,1)
"""
should be:
    Error: Circled singly linked list
"""