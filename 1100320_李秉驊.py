import collections
def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    lst = []
    lst1 = []
    c = collections.Counter(input_list)
    for k, v in c.items():
        lst.append((v, k))
    lst.sort()
    for a in lst:
        lst1.append(a[1])
    return lst1

   

    
        



if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [8,8,8,7,9,9]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板