from collections import Counter #呼叫(module) collections去取Counter裡面的值
def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    a1=Counter(nums).most_common() #Counter會去抓陣列裡面要的出現在結果的值，而且用most_common function去抓最常出現的
    a2 = [i[0] for i in a1 ] #從陣列的第0個位置(i[0])開始讀值
    a2.reverse() #預設是數字多到少的排列，但是目要求要少到多，因此要用reverse function
    return a2 #回傳已排序完的陣列(少到多)

    
if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [2,0,9,8,9,2,8,2,0,9,7,9,8,2,9]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板