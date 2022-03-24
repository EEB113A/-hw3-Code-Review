from tkinter import TRUE
import operator

def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    a = {} 
    for i in input_list:
        if input_list.count(i)>0:
            a[i]= input_list.count(i) #出現次數
    a = sorted(a.items(),key=operator.itemgetter(1)) #排序
    res = []
    for item in a:
        res.append(item[0])
    return res

if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [7,7,7,8,1,1]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板