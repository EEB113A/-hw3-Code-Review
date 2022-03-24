def sort_by_occurrence(nums):
    dic={}   #建立一個空dictionary
    lst2=[]  #建立一個空list
    for items in nums:          #items為nums的元件
        if items not in dic:    #把它依序放入字典(dic)中
            dic[items] = 1
        elif items in dic:
            dic[items] += 1
    
    lst1 = sorted(dic.items(),key=lambda x:x[1])  #將key由小排到大
    lst1_len=len(lst1)
    for i in range (0,lst1_len):
        lst2.append(lst1[i][0])    #取前面的數字
    return lst2
    

if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板