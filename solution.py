class Solution(object):
    def isHappy(self, n):
        l=[]
        sqrt_sum=0
        num=n
        while num>0:
            rem=num%10
            sqrt_sum=sqrt_sum+(rem*rem)
            num=num//10
            if(num==0):
                num=sqrt_sum
                if sqrt_sum==1:
                    return True
                    break
                if sqrt_sum not in l:
                    l.append(sqrt_sum)
                else:
                    return False
                    break

                sqrt_sum=0

