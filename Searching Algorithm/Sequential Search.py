"""
digunakan untuk mencari sebuat item satu persatu secara urut
dan cocokuntuk mencari data acak
"""
def search_squen(nums,x):
    for i in range(len(nums)):
        if x == nums[i]:
            return i
    return -1

Mylist = [1,2,3,5,33,45,9]
x = 5
result = search_squen(Mylist,x)
print(f"Nilai {x} ada di list indexke- {result}")