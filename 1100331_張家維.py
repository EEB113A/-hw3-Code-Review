def sort_by_occurrence(nums):
    dic = {}
    lst2 = []
    for items in nums:
        if  items not in dic:
                dic[items]=1
        elif items in dic:
                dic[items] +=1
    lst1 = sorted(dic.items(),key=lambda x:x [1])
    lst1_len = len(lst1)
    for i in range (0,lst1_len):
        lst2.append(lst1[i][0])
    return lst2
x = [1,1,1,2,2,3]
sort_by_occurrence(x)
print(sort_by_occurrence(x))
y = [5,5,6,6,6,6,0,1,1,1]
print(sort_by_occurrence(y))
z = [2,0,9,8,9,2,8,2,0,9,7,9,8,2,9]
print(sort_by_occurrence(z))


#留言板