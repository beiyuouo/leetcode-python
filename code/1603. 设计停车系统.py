# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/22 13:26
# Description:

__author__ = "BeiYu"


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.remaining = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.remaining[carType] > 0:
            self.remaining[carType] -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

if __name__ == '__main__':
    obj = ParkingSystem(1, 1, 0)
    print(obj.addCar(1))
    print(obj.addCar(2))
    print(obj.addCar(3))
    print(obj.addCar(1))
