def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    
    lst = []   #建立一個空的list
    dic = {}   #建立一個空的字典
    
    for i in nums:     #利用迴圈算出list中各元素重複的次數
        dic[i] = nums.count(i)
        dic = dict(sorted(dic.items(), key=lambda x:x[1]))
    
    count = 0   #初始化count
    
    for j, k in dic.items(): #利用迴圈把元素按照出現的次數排列
        for i in range(k):   #出現最少的排前面，反之排後面   
            lst.append(j)
    
    lst2 = []   #建立一個空的list
    
    for number in lst:          #把lst中的元素append進lst2中
        if number not in lst2:  #重複的元素不會擺進來第二次
            lst2.append(number)
    return lst2   #回傳lst2
    

if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1,1,1,2,2,3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板