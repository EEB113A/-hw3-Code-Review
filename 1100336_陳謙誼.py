def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡

    List_dict={}     #建一個空的dict(字典)
    for n in nums:   #用for迴圈一個一個把num中的數字取出
        if n in List_dict:    #如果取出的num中有在List_dict內的話，個數加1
            List_dict[n]+=1
        else:
            List_dict[n]=1   #沒有的話就在List_dict內新建一個，且個數等於1
    List_dict =[ (v,k) for (k,v) in List_dict.items()] #把dict轉list
    List_dict.sort()                          #用.sort()排序List_dict的v(value)
    List_dict = [x for (y,x) in List_dict]    
    return List_dict             #回傳最終結果



if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板