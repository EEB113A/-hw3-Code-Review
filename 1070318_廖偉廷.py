def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    nums = [2,0,9,8,9,2,8,2,0,9,7,9,8,2,9]
    nums_sorted = sorted(nums,key=nums.count)#依照重複次數，從小排列到大
    nums_list = set(nums_sorted)#以集合來去除重複項
    return nums_list 


if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板