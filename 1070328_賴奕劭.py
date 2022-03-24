def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    output_nums = []
    for i in nums:
        if i not in output_nums:                                # 如果output_nums沒有i這個元素
            output_nums.append(i)                               # 則將其加入output_nums中
            for j in output_nums:                               # 如果元素已在output_nums中
                if nums.count(i) < nums.count(j):               # 計算元素出現的次數
                    output_nums.remove(i)                       # 若小於則移除元素i
                    output_nums.insert(output_nums.index(j), i) # 並在output_nums(j)之前插入元素i
                    break
    return output_nums

if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)
    print(type(output_list))                                    # 顯示output_list之資料型態


#留言板