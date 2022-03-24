def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    
    ans=[]  #放最後答案的list
    count_dict={}  #用來計算次數的字典
    for i in input_list:
        if i  in count_dict:
            count_dict[i]+=1  #若字典已經有此數字，則計數+1
        else:
            count_dict[i]=1  #若字典沒有此數字，則把此數字放入字典，並讓它計數一次
    lst=[[v,k]for k,v in count_dict.items()]  #將key和value的位置相反過來，較容易進行sort
    lst.sort()   #進行sort
    for j in lst:
        ans.append(j[1])  #將答案append進去ans，也就是放入最後答案的list
    
    return ans  #return 答案



    








if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [7,7,7,8,9,9]
    output_list = sort_by_occurrence(input_list)

    print(output_list)


#留言板