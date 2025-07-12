# sol1
# class Solution:
#     def isPalindrome(self, x):
#         s=str(x)
#         return s==s[::-1]
        

# sol2
class Solution:
    def isPalindrome(self, x):
        if x<0:
            return False
        if x==0:
            return True
        if x%10==0:
            return False

        a=x
        num=0
        while x>0:
            lastNum=x%10
            num=num*10+lastNum
            x=x//10
        
        return num==a
