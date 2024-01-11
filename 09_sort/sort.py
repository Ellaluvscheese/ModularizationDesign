# 1. Name:
#      Ella Galbraith
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      This program is a sorting algorithm that has to sort a list with only two lists.
#      It find the "sub lists" which are the index variables for the sub sorted in the list.
#      It also has a build in automation test that checks all my test cases to make sure everything is working correctly.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this assignment was designing the algorithm but that was the last two weeks, 
#      so the hardest part this week would be writing the test cases, It just took a little bit of time
# 5. How long did it take for you to complete the assignment?
#      This took me about an hour to complete this assignment, but an hour and a half overall because of the video.
import json

def main(user_list):
    # user_list = input("What list file do you want to sort?: ")
    open_list = read_list(user_list)
    sorted = sort(open_list)
    # print(f"Original List: {open_list}")
    # print(f"Sorted List: {sorted}")
    return sorted

def read_list(file_name):
    with open(file_name, "r") as file:
        list_data = json.load(file)
    the_list = list_data["list"]  
    return the_list

def sort(array):
    size = len(array)
    src = array
    des = [0] * size
    num = 2

    while num > 1:
        num = 0
        begin1 = 0

        while begin1 < size:
            end1 = begin1 + 1
            while end1 < size and src[end1 - 1] <= src[end1]:
                end1 += 1
            
            begin2 = end1
            if begin2 < size:
                end2 = begin2 + 1
            else:
                end2 = begin2
            
            while end2 < size and src[end2 - 1] <= src[end2]:
                end2 += 1
            
            num += 1
            combine(src, des, begin1, begin2, end2)
            begin1 = end2
        src, des = des, src
    return src

def combine(src, destination, begin1, begin2, end2):
    end1 = begin2

    for i in range(begin1, end2):
        if (begin1 < end1) and (begin2 == end2 or src[begin1] < src[begin2]):
            destination[i] = src[begin1]
            begin1 += 1
        else:
            destination[i] = src[begin2]
            begin2 += 1

    return destination

def auto_testing():
    if main('empty.json') == []:
        print(f"Empty: ✓")
    else:
        print('Empty: ❌')
        return
    if main('singular.json') == [23]:
        print(f"Singular: ✓")
    else:
        print('Singular: ❌')
        return
    if main('small_sorted.json') == [1, 2]:
        print(f"Small Sorted: ✓")
    else:
        print('Small Sorted: ❌')
        return
    if main('small_unsorted.json') == [2, 3]:
        print(f"Small Unsorted: ✓")
    else:
        print('Small Unsorted: ❌')
        return
    if main('sorted_even.json') == [3, 12, 26, 38, 49, 59, 64]:
        print(f"Sorted Even: ✓")
    else:
        print('Sorted Even❌')
        return
    if main('reversed_even.json') == [3, 12, 26, 38, 49, 59, 64]:
        print(f"Reversed Even: ✓")
    else:
        print('Reversed Even: ❌')
        return
    if main('sorted_odd.json') == [3, 12, 26, 38, 49, 59, 64, 79]:
        print(f"Sorted Odd: ✓")
    else:
        print('Sorted Odd: ❌')
        return
    if main('reversed_odd.json') == [3, 12, 26, 38, 49, 59, 64, 79]:
        print(f"Reversed Odd: ✓")
    else:
        print('Reversed Odd: ❌')
        return
    if main('duplicates.json') == [31, 31, 49, 49, 55, 99]:
        print(f"Duplicates: ✓")
    else:
        print('Duplicates: ❌')
        return
    
auto_testing()