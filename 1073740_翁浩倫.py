from typing import Counter


def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    from collections import defaultdict
    times = defaultdict(list)   #先定義次數

    for i in input_list:
        if i not in times:
            times[i].append(input_list.count(i))
            times[i].append(input_list.index(i))
    #因為這邊是正向排列,不用加上負號或是Reverse=True
    dic = sorted(times.items(), key=lambda item:(item[1][0], item[1][1]))

    res = []       #建立一個空的list
    for (k,v) in dic:       #將剛剛弄好的dic一個一個放入
        res += [k]*v[0]
    res2 = []       #建立一個空的list2
    for i in res:       #將重複的數字移除，只留下一個
        if not i in res2:
            res2.append(i) 
    return res2

if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板