from collections import defaultdict

class FriendshipService:

    def __init__(self):
        self.followers=defaultdict(set)
        self.followings=defaultdict(set)

    # do intialization if necessary

    """
    @param: user_id: An integer
    @return: all followers and sort by user_id
    """

    def getFollowers(self, user_id):
        if user_id not in self.followers:
            return []
        res=list(self.followers[user_id])
        res.sort()
        return res

    # write your code here

    """
    @param: user_id: An integer
    @return: all followings and sort by user_id
    """

    def getFollowings(self, user_id):
        if user_id not in self.followings:
            return []
        res=list(self.followings[user_id])
        res.sort()
        return res

    # write your code here

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """

    def follow(self, to_user_id, from_user_id):
        self.followers[to_user_id].add(from_user_id)
        self.followings[from_user_id].add(to_user_id)

    # write your code here

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """

    def unfollow(self, to_user_id, from_user_id):
        if to_user_id in self.followers:
            if from_user_id in self.followers[to_user_id]:
                self.followers[to_user_id].remove(from_user_id)

        if from_user_id in self.followings:
            if to_user_id in self.followings[from_user_id]:
                self.followings[from_user_id].remove(to_user_id)
# write your code here

test=FriendshipService()
test.follow(1, 3)
print(test.getFollowers(1))
print(test.getFollowings(3))