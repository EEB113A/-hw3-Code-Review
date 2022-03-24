from collections import Counter
def sort_by_occurrence(nums):

     c1= Counter(input_list)
     sorted_x = sorted(c1.items(), key=lambda x: x[1])
     res_x=[]
     for item in sorted_x[0:]:
         res_x.append(item[0])
     return res_x
     
if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [2, 2, 4, 3, 3, 8, 4, 9, 8, 4, 8, 3, 8, 4, 8]
    Output_list = sort_by_occurrence(input_list)
    print(Output_list)


#留言板