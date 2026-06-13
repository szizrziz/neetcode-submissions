class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt=collections.defaultdict(int) #fruittype->countof fruits
        l,curr_total,res=0,0,0
        for r in range(len(fruits)):
            cnt[fruits[r]]+=1
            curr_total+=1
            while len(cnt)>2:
                f=fruits[l]
                cnt[f]-=1
                curr_total-=1
                l+=1
                if not cnt[f]:
                    cnt.pop(f)
            res=max(res,curr_total)
        return res

        