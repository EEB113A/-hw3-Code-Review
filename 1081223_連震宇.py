from collections import Counter


def sort_by_occurrence(nums):
    """按照 list 物件 nums 裡的各元素出現次數，進行遞增排序"""
    # 把你的程式碼放在這裡

    # Counter().most_common() 是返回 n 個最常出現元素的列表，以及從最常出現到最少出現的計數。如果省略 n 或給予 None，則most_common()返回計數器中的所有元素
    nums_counter = Counter(nums).most_common()
    # 因為只需要保留數字(不用數字出現的次數)，這邊將 nums_counter 排好的元素再全部存入 nums_sorted 裡
    nums_sorted = [i[0] for i in nums_counter]
    nums_sorted.reverse()  # 因為要求從小到大排序各元素的出現次數，使用 reverse() 將降序改為升序
    return nums_sorted  # 回傳nums_sorted


if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。

    input_list = [1, 1, 1, 2, 2, 3]  # 可以給予3種範例的input
    output_list = sort_by_occurrence(input_list)  # 呼叫 sort_by_occurrence 函式
    print(output_list)  # 印出結果


#留言板