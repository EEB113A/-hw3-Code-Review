def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    from collections import Counter
    count=Counter(nums)               #算出每個數字有幾個 Counter({    })
    sorted_nums= sorted(count.items(),reverse=False)        # 轉成list 
    order_nums=sorted(sorted_nums, key=lambda num: num[1])   #將每個括號中第一個位子的數由小到大排列 
    change_dict=dict(order_nums)      # 轉成dict的型態  
    keys=change_dict.keys()           # 將每個key取出 
    
    return  list(keys)       # 回傳轉成list的型態 

if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1,1,1,2,2,3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板