
def sort_by_occurrence(nums):
    
    d1={}
    e=[]
    ans=[]
    for i in nums:
        if i not in d1:
            d1[i]=1
        else:
            d1[i]+=1
    for k,s in d1.items():
        e.append([s,k])
    e=sorted(e)
    for k in e:
        c=k[1]
        ans.append(c)
    return ans
nums = [3,3,4,4,4,2,1,1,1,1]
output_list = sort_by_occurrence(nums)
print(output_list)


#留言板