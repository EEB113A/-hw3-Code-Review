def sort_by_occurrence(nums):
    dis={}
    lst=[]
    for i in nums:
        if i not in nums:
            dis[i]=1
        else:
            dis[i]+=1
    for a,b in dis.items():
        lst.append([b,a])
        print(lst)
    lst.sort()   
    for a in lst:
        ans=a[1]
        lst.append(ans)
    return lst




if __name__ == '__main__':
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板