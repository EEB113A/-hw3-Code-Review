def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    element_count={}
    final_sort=[]
    for i in nums: #建立一個字典(Key為元素，Value為出現次數)
        if i not in element_count:
            element_count[i]=1
        else:
            element_count[i]+=1
    key_value=sorted(element_count.items(), key=lambda element_count:element_count[1])#將字典從小到大排序並以List of tuple回傳
    for j in range(len(key_value)):#將排序後的key值放入一個新的list作為funtion最後的return
        final_sort.append(key_value[j][0])
    return final_sort
        
    



if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [5,5,6,6,6,6,0,1,1,1]
    output_list = sort_by_occurrence(input_list)
    print(output_list)
    

#留言板