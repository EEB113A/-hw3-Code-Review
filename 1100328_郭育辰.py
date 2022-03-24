def sort_by_occurrence(nums):
    numbers=[]
    numbers.append(nums[0])
    for i in range(1,len(nums)):
        flag=False
        for j in range(len(numbers)):
            if nums[i]==numbers[j]:
                flag=True
                break
        if flag==False:#flag作if的判斷條件
            numbers.append(nums[i])
    List=[]
    #declare List as a 2-D list
    for i in range(len(numbers)):
        List.append([])
        List[i].append(numbers[i])
        List[i].append(nums.count(numbers[i]))
    #bubble sort
    n=len(numbers)    
    for i in range(n-1):
        for j in range(n-i-1):
            if List[j][1]>List[j+1][1]:
                List[j], List[j+1] = List[j+1], List[j]
    out=[]
    for i in range(n):
        out.append(List[i][0])
    return out
if __name__=='__main__':
    input_list=[1,1,1,2,2,3,5,0,0,2,1,2,1,0,0,5,3,3,3,3,3,3,3,5,5,2]
    output_list=sort_by_occurrence(input_list)
    print(output_list)



#留言板