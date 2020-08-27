
import collections
from collections import deque

def earliest_ancestor(ancestors, starting_node):

    parent_child = {}

    for parent, child in ancestors:
        if child in parent_child:
            parent_child[child].append(parent)
        else:
            parent_child[child] = [parent]

    # if the starting node has no parents
    if starting_node not in parent_child:
        return -1

    node_queue = collections.deque() # deque with contructor

    last_node = [starting_node] # save the last node dequeued

    node_queue.append(last_node)

    while len(node_queue) > 0:
        last_node = node_queue.popleft()
        oldest_node = last_node[-1]

        if oldest_node in parent_child:
            parent_child[oldest_node].sort(reverse=True) #  lowest id goes in queue last
            for parent in parent_child[oldest_node]:
                new_node = last_node.copy()
                new_node.append(parent)

                node_queue.append(new_node)

    return last_node[-1]
