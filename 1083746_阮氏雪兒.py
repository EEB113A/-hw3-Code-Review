"""Function to sort the apprearance of elements of the given list"""
def sort_by_occurrence(nums):
    #Create an empty dictionary 
    dictionary = {}
    
    #Check whether each element appears in the dictionary or not
    #Then count how many times they appear (values of keys)
    for i in nums:
        if i in dictionary:
            dictionary[i] += 1           
        else:
            dictionary[i] = 1
    
    #Creatae empty list to store the result
    result = []
    
    #Sort by values of keys, will return a list with elements are tuples: (key, value)
    sort_orders = sorted(dictionary.items(), key=lambda x: x[1], reverse=False)
    
    #Add item to the result list, the first item of tuple
    for i in sort_orders:
        result.append(i[0])
      
    return result

"""Print the output value with the given data set"""
if __name__ == '__main__':
    input_list = [1, 1, 1, 2, 2, 3]
    output_list = sort_by_occurrence(input_list)
    print(output_list)


    
    

#留言板