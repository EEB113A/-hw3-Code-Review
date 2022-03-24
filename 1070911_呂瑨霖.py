from calendar import c
from pickle import NONE
from re import I, X
from typing import List
from collections import Counter

def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    numsset=set(nums) #將nums存為集合
    dicnums = {item: nums.count(item)for item in numsset} #計算set中各元素出現次數value保存到字典中
    sorted_x = sorted(dicnums.items(),key=lambda x:x[1],reverse=False)#根據vlaue進行降冪排序
    print(list(sorted_x)) #(A,b) A為元素b為次數


if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [2,0,9,8,9,2,8,2,0,9,7,9,8,2,9]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板