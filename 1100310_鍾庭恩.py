def sort_by_occurrence(nums):
    from collections import Counter
    c = Counter(nums)
    e=[]
    ans=[]
    for k,v in c.items():
        e.append([v,k])
    e = sorted(e)
    for k in e:
        n = k[1]
        ans.append(n)
    return ans

if __name__ == '__main__':
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_list = [2,3,3,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,7,7,7]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


#留言板