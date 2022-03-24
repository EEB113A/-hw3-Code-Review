def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    count=dict()
    l=list()
    nums=sorted(nums)
    for i in range(len(nums)):
        try:
            count[nums[i]]+=1
        except:
            l+=[nums[i]]
            count[nums[i]]=1
    l=sorted(l,key=lambda x:count[x])
    return l

    






if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [2,0,9,8,9,2,8,2,0,9,7,9,8,2,9]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板