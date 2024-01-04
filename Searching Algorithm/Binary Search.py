"""
Binary search merupakan searching algorithm yang melakukan pencarian terhadap suatu list yang tersusun 
atau bukan list yang acak. 
Hal ini yang membedakan binary search dengan sequential search yaitu dari tipe list input masing-masing.
"""
S = [1,23,45,89,109,210,223,445]
x = 223

def bin_search1(nums,x):
    low, high = 0, len(nums) - 1 # menginisialisasikan titik low dan high 
    while low <= high:
        mid = (low + high) // 2 # mendeklarasikan titik mid
        if nums[mid] == x:
            return mid
        elif nums[mid] > x:
            high = mid -1
        else:
            low = mid + 1
    return -1 # apabila resul
pos = bin_search1(S,x)
print(f"posisi bilangan {x} didalam list S adalah di posisi nomer {pos}")







