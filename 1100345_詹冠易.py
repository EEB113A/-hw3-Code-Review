def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    a = nums
    b = set(a) #將a之中重複的數字去除
    c = []
    d = []


    for eachb in b:
        count = 0   #計算重複的次數
        c = []      #計算另一組[count,eachb]的list 
        for eacha in a:
            if eacha == eachb: 
                count +=1
        c.append(count) 
        c.append(eachb)
        d.append(c) # 將一組[count,eachb]的list放到 list 之中
        d = sorted(d,key=lambda x:x[0]) #依小到依小到大排序
    
    d_len = len(d)
    e=[]
    for i in range(0,d_len):
        e.append(d[i][1]) #把d裡面的eachb提出來放到list之中
        
    return e

if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [2,0,9,8,9,2,8,2,0,9,7,9,8,2,9]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板