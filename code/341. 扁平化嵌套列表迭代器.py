# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/23 01:03
# Description:

__author__ = "BeiYu"


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.myList = []
        self.pt = 0

        def _dfs(curList: [NestedInteger]):
            if curList.isInteger():
                self.myList.append(curList.getInteger())
                return

            for i in curList.getList():
                _dfs(i)

        for i in nestedList:
            _dfs(i)

    def next(self) -> int:
        self.pt += 1
        return self.myList[self.pt - 1]

    def hasNext(self) -> bool:
        return self.pt < len(self.myList)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
