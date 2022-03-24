def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡
    def sort_by_occurrence(nums):
        a = list(nums)
        b = set(a)
        c = []
        d = []
        for i in b:
            count = 0
            c = []
            for j in a:
                if i == j:
                    count += 1
            c.append(i)
            c.append(count)
            d.append(c)
            d = sorted(d, key=lambda x: x[1])
        return d



if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    # nums = input("input :")
    # k = sort_by_occurrence(nums)
    # print(k)
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板