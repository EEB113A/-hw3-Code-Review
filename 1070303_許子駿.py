from calendar import c
from pickle import NONE
from re import I, X

def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    #print("input:",nums)
    numsset=set(nums) #利用set將nums裡重複的資料移除並命名numsset
    numslist=list(numsset)#將numsset轉回list型態並命名numslist
    #print("numslist",numslist)
    numscount=[0]*len(numslist)#設置一個每項為0的計數器叫做numscount
    #print("計數器:",numscount)
    for i in range(len(numslist)):#由小到大計算nums裡每個數字出現的次數
        numscount[i] =nums.count(numslist[i])
    #print("numscount:",numscount)
    #print(len(numscount))
    outputlist=[]#先設置一個空的list叫做outputlist
    for i in range(max(numscount)+1):#設計兩個迴圈，依據numscount裡的次數大小由小到大把次數所對應到的數字append到outputlist
        for j in range(len(numscount)):
            if(numscount[j]== i):
                outputlist.append(numslist[j])
    return outputlist

if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [2,0,9,8,9,2,8,2,0,9,7,9,8,2,9]
    output_list = sort_by_occurrence(input_list)
    print(output_list)

#留言板