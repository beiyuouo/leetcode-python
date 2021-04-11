# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/12 01:18
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = image[i][::-1]
            for j in range(len(image[i])):
                image[i][j] = image[i][j] ^ 1

        return image
