def find_indices(lst, target, index=0):
    if index >= len(lst):
        return []
    
    indices = find_indices(lst, target, index + 1)
    if lst[index] == target:
        indices.append(index)
    
    return indices



'''
make sure you understand this
the recursion goes to the base case first and sets indices to [] and then indices gets appended
REALLY IMPORTANT

Certainly! Let's go through the steps to understand how the `indices` list is being populated in the `find_indices` function.

1. Initially, when the function is called, the `index` is set to 0.
2. The function checks if the `index` is greater than or equal to the length of the list (`index >= len(lst)`). If it is, it means we have reached the end of the list, so an empty list `[]` is returned.
3. If the `index` is within the valid range, the function recursively calls itself with an incremented index (`index + 1`). This recursive call continues until the base case is reached (i.e., when `index >= len(lst)`).
4. At each recursive call, a new `indices` list is created and stored in the current call's local scope.
5. As the recursive calls start to unwind and return, the `indices` list from the previous call is accessed and modified.
6. When the function reaches the line `if lst[index] == target:`, it checks if the current element at the `index` matches the target. If it does, it appends the `index` to the `indices` list from the previous call.
7. Finally, the `indices` list, which has been accumulated and modified through the recursive calls, is returned.

Essentially, as the recursive calls unwind, the `indices` list from each call is updated with the current index if the target is found at that index. This allows the function to build up the list of indices where the target occurs in the list.

It's important to note that each recursive call has its own local `indices` list, and modifications to the `indices` list in one call do not affect the `indices` lists in other calls. The recursive calls build up their own lists separately, and the final result is obtained by returning the `indices` list from the initial call.

I hope this explanation clarifies how the `indices` list is being populated in the `find_indices` function.
'''
