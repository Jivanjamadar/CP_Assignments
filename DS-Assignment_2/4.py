#Submission ID : 1277592817

class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.d = defaultdict(set)
        

    def insert(self, val: int) -> bool:
        if val in self.d and len(self.d[val]) > 0:
            res = False
        else:
            res = True
        self.nums.append(val)
        # store element positions
        self.d[val].add(len(self.nums)-1)
        return res
        

    def remove(self, val: int) -> bool:
        if val in self.d and len(self.d[val]) > 0:
            pos = self.d[val].pop() # element to remove position            
            lpos = len(self.nums)-1 # last position
            lval = self.nums[lpos] # last val
            
            # add lval pos first .. then remove .. so when last == val .. it will take care auto
            self.d[lval].add(pos)            
            self.d[lval].remove(lpos)
            
            # swap with last
            self.nums[pos], self.nums[lpos] = self.nums[lpos], self.nums[pos]                        
            
            # remove element
            self.nums.pop()
            return True
        return False
        

    def getRandom(self) -> int:
        size = len(self.nums)
        i = int(random.random()*size)
        return self.nums[i]