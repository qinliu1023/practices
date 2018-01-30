def question4(T,r,n1,n2):
    # Check if any one of our 4 input arguments is None or Empty or in wrong type
    if T == []:
        return "Warning: T is Empty"
    if type(r) != int or r < 0: 
        return "Error: Invalid input r"
    if type(n1) != int or n1 < 0: 
        return "Error: Invalid input n1"
    if type(n2) != int or n2 < 0: 
        return "Error: Invalid input n2"

    
    def node_closest_ancestor(node):
    # For a given node, its ancestors must be in the column node, to find its ancestors
    # We check every row in that column to see if any number is 1, if exist, then return
    # the row number, and that is the cloest parent of the given node
        rows = range(len(T))
        for row in rows:
            if T[row][node] == 1:
                return row

        
    # using function node_closest_ancestor to find the ancestors set of n1
    n1_ancestor_set = set()
    if type(node_closest_ancestor(n1)) == int:
        closest_ancestor = node_closest_ancestor(n1)
        n1_ancestor_set.add(closest_ancestor)
        while closest_ancestor != r:
            new_ancestor = node_closest_ancestor(closest_ancestor)
            closest_ancestor = new_ancestor
            n1_ancestor_set.add(closest_ancestor)

    # Check n2 ancestors from the bottom to top, until the root, n2 itself is also considered
    # and stops when the first n2 ancestor is in ancestors set of n1
    if type(node_closest_ancestor(n2)) == int:
        n2_ancestor = node_closest_ancestor(n2)
        while n2_ancestor != r:
            if n2_ancestor in n1_ancestor_set:
                return n2_ancestor
                break
            else:
                new_ancestor = node_closest_ancestor(n2_ancestor)
                n2_ancestor = new_ancestor
        return n2_ancestor


###################### Test Cases #########################       
question4([],3,1,4)
# should be: Warning: T is Empty

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
# should be: 3

question4([[0, 1, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0]],
          0,
          4,2)
# should be: 2 