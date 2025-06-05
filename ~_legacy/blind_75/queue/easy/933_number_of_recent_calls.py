from collections import deque # double ended queue
# APPENDING AND EXTENDING
# .append()
# .appendleft()
# .extend([itr]) like append but appends an iterable [1,2,3]
# .extendleft([itr]) like extend but on the left, note it appends in REVESE order

# POPPING AND REMOVING
# .pop() - remove and returns element from the right end
# .popleft() - removes and returns element from the left end
# .remove(value) removes 1st occurence of value

# ROTATING
# dq = deque([1,2,3,4])
# dq.rotate(1) -> deque([4,1,2,3])
# dq.rotate(-2) -> deque([2,3,4,1])

# MISC
# .clear() remove all
# .count() count

# INDEXING AND ACCESSING
# .index(value, start=0, stop=None) returns first occurence of `value` within the range, raises ValueError if not found - O(n)
# .insert(index, value) - returns IndexError if out of bounds - O(n)
# all left/right operations are O(1) - even insert at index =  0, unlike an array/list
class RecentCounter:

    def __init__(self):
        self.queue = deque()


    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()

        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)