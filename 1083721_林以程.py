def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    from collections import defaultdict #帶入套件
    from collections import Counter #帶入套件

    method = defaultdict(lambda: 0) #定義默認字典
    for i in nums: #for迴圈
        method[i] = method[i]+1 #計算數量

    a = Counter(method).most_common() #排序字典的值
    b = []
    for j in a:
        b.append(j[0])

    print(b)
   
        


            
if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [6,7,7,8,8,8]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板