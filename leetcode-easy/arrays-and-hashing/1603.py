# LeetCode Question 
    ## 1603. Design Parking System
# LeetCode Link
    ## https://leetcode.com/problems/design-parking-system/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=d5zCHesOrSk&ab_channel=NeetCodeIO


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.park_space = {1: big, 2: medium, 3: small}
        

    def addCar(self, carType: int) -> bool:
        if self.park_space[carType] > 0:
            self.park_space[carType] -= 1
            return True
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
obj = ParkingSystem(1, 1, 0)
print(obj.addCar(1))
print(obj.addCar(2))
print(obj.addCar(3))
print(obj.addCar(1))