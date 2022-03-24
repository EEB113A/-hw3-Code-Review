def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    d_num = {}
    for num in nums: #把每個nums裡的數字(key)加入d_num，並加上對應數字出現的次數(value)
        if num not in d_num:
            d_num[num] = 1
        else:
            d_num[num] += 1
    
    sorted_nums = sorted(sorted(nums, reverse=True), key=lambda n: d_num[n]) #把所有數字出現的頻率由小到大放入sorted_nums
    
    new_nums = [] 
    for n in sorted_nums: #把重複的數字去除，return 照出現次數從小到大排序
        if n not in new_nums:
            new_nums.append(n)
    return new_nums      


if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [2,0,9,8,9,2,8,2,0,9,7,9,8,2,9]
    output_list = sort_by_occurrence(input_list)
    print(output_list)

#留言板