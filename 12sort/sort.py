# 1. Name:
#      Ella Galbraith
# 2. Assignment Name:
#      Lab 13 : Segregation Sort Program
# 3. Assignment Description:
#      This program is supposed to sort a list of numbers through a recursive function
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me was deciding how to implement the recursion, but when I figured it out I was amazed with the result!
# 5. How long did it take for you to complete the assignment?
#      It took me about 2 hours to complete this assignment, including the video.
def main():
    # should_sort = read_list("list1.json")
    autoTest()
    return

# def read_list(file_name):
#     with open(file_name, "r") as file:
#         list_data = json.load(file)
#     the_list = list_data["list"]  
#     return the_list

def sort(array):
    sorted = sort_recur(array, 0, len(array) - 1)
    return sorted

def sort_recur(array, i_begin, i_end):
    if i_end - i_begin < 1 or i_end < 0:
        return
    
    i_pivot = segregate(array, i_begin, i_end)

    sort_recur(array, i_begin, i_pivot - 1)
    sort_recur(array, i_pivot + 1, i_end)

    return array

def segregate(array, i_begin, i_end):
    if i_begin == i_end:
        return i_begin
    
    i_pivot = round((i_begin + i_end) / 2)
    i_up = i_begin
    i_down = i_end

    while i_up < i_down:
        while i_up < i_down and array[i_up] < array[i_pivot]:
            i_up += 1
        while i_up < i_down and array[i_down] >= array[i_pivot]:
            i_down -= 1
        
        if i_up < i_down:
            if i_down == i_pivot:
                i_pivot = i_up
            elif i_up == i_pivot:
                i_pivot = i_down
            array[i_up], array[i_pivot] = array[i_pivot], array[i_up]
    
    array[i_up], array[i_pivot] = array[i_pivot], array[i_up]
    return i_up

def autoTest():
    three = sort([3,1,2])
    if three == [1,2,3]:
        print(f"✓")
    else:
        print("❌")
    multiples = sort([2,3,1,1])
    if multiples == [1,1,2,3]:
        print("✓")
    else:
        print(multiples)
    reversed = sort([4,3,2,1])
    if reversed == [1,2,3,4]:
        print("✓")
    else:
        print("❌")
    long = sort([3,2,7,6,1,4])
    if long == [1,2,3,4,6,7]:
        print("✓")
    else:
        print("❌")


main()