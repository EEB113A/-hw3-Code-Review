def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    dict={}  #建立一個空的dictionary  
    for a in nums: #計算 nums 裡面各元素出現的次數，把元素當key，次數當value。
        cunt=nums.count(a)
        if a not in dict:
            dict[a]=cunt
            
    lst=[(v,k)for k,v in dict.items()] #將dict的key與對應value包在一個tuple,再放在空的list  
    lst.sort() #進行遞增排序。
    nums=[] #將 nums 指派到空的list。
    
    for c in lst: #從lst抓出排好的元素順序，放在nums裡。
        nums.append(c[1])    
    return nums


if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1,1,1,2,2,3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板