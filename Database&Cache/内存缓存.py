from collections import defaultdict
import sys

class Memcache:
    def __init__(self):
        self.keys=defaultdict(list)
        # do intialization if necessary

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: An integer
    """
    def get(self, curtTime, key):
        if key in self.keys and self.keys[key][0] >=curtTime :
            return self.keys[key][1]
        else:
            return 2147483647
        # write your code here

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: value: An integer
    @param: ttl: An integer
    @return: nothing
    """
    def set(self, curtTime, key, value, ttl):
        if ttl :
            t = curtTime + ttl - 1
        else :
            t=sys.maxsize
        self.keys[key]=[t,value]
        # write your code here

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: nothing
    """
    def delete(self, curtTime, key):
        del self.keys[key]
        # write your code here

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    def incr(self, curtTime, key, delta):
        if key in self.keys and curtTime<=self.keys[key][0]:
            self.keys[key][1]+=delta
            return self.keys[key][1]
        else:
            return 2147483647
        # write your code here

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    def decr(self, curtTime, key, delta):
        if key in self.keys and curtTime <= self.keys[key][0]:
            self.keys[key][1] -= delta
            return self.keys[key][1]
        else:
            return 2147483647