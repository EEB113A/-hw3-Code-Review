def sort_by_occurrence(nums):
    ct_of_nums = {}
    for num in nums:
        if num not in ct_of_nums:
            ct_of_nums[num] = 1
        elif num in ct_of_nums:
            ct_of_nums[num] +=1
    #print(sorted(ct_of_nums.items(), key=lambda x:x[1]))
    s = sorted(ct_of_nums.items(), key=lambda x:x[1])
    ls = []
    lsn = []
    for i in s:
        ls.append(list(i))
    for k in ls:
        lsn.append(k[0])
    print(lsn)
input_list = [7,7,8,8,8,9]
sort_by_occurrence(input_list)
#if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    #input_list = [1, 1, 1, 2, 2, 3]
    #output_list = sort_by_occurrence(input_list)
    #print(output_list)


#留言板