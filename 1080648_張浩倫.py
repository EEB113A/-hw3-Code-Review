from contextlib import nullcontext
from pickle import FALSE

def sort_by_occurrence(nums):    
    number=set(nums)#去除重複數字
    count={item: nums.count(item) for item in number}#計算nums裡面的各個數字的數量
    sort=sorted(count.items(), key=lambda x:x[1], reverse=False)#根據上列計算的數量由少到多排列
    array=[]#設定空陣列
    for i in range(len(sort)):#設定迴圈次數為已排序陣列的長度
        array.insert(i,sort[i][0])#將數字照順序插入陣列內
    return array#將陣列答案回傳

if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [1,1,1,2,2,3]#輸入陣列
    output_list = sort_by_occurrence(input_list)#將輸入陣列進行函式運算過後回傳
    print(output_list)#印出輸出的陣列

#留言板