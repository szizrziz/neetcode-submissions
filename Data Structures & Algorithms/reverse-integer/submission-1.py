
class Solution:
    def reverse(self, x: int) -> int:
        minn=-(2**31)
        maxx=(2**31) -1
        res=0
        while x:
            digit=int(math.fmod(x,10))
            x=int(x/10)
            if res>maxx//10 or (res==maxx//10 and digit>maxx%10):
                return 0
            if res<minn//10 or (res==minn//10 and digit<mainn%10):
                return 0
            res=(res*10)+digit
        return res