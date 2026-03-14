class Solution(object):
    def addDigits(self, num):
        if num==0:
            return 0
        return 1+(num-1)%9


# 1      ->      1
# 2      ->      2
# 3      ->      3                     As you can see that after every 9 numbers the sum of digits repeat
# 4      ->      4                         so we are taking mod with 9 
# 5      ->      5                       we are taking 1+(num-1)%9 because if we take 9 the mod with 9 becomes zero but the o/p should be 9
# 6      ->      6                             so we take num-1 = 9-1  => 8 mod 9 = 8 +1  =  9
# 7      ->      7
# 8      ->      8
# 9      ->      9
# 10      ->     1
# 11     ->      2
# 12     ->      3
# 13     ->      4
# 14     ->      5
# 15     ->      6
# 16     ->      7
# 17     ->      8
# 18     ->      9
# 19     ->      1
