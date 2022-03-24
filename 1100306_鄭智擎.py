def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    Dict={}
    List=[]
    List_set = set(input_list) #List_set是另外一個列表，裡面的內容是List裡面的無重複項
    #print(List_set)
    for item in List_set:
        #print ("the %d has found %d" %(item,input_list.count(item)))
        Dict[item] = input_list.count(item)
    Dict = sorted(Dict.items(),key=lambda item:item[1])
    for key, close in Dict:
        #print (key)
        List.append(key)
    return List
    


if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1, 1, 2, 2, 2,3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板