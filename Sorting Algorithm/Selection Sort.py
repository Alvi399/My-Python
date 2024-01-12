"""
sebah algoritma sortng dimana sebuah elemen kecil ak disimpan didalam himpunan sort
"""

def selection_sort(num):
    n = len(num)
    for i in range(n - 1):
        print(num)
        smllest = i
        for j in range(i + 1,n):
            if num[j] < num[smllest]:
                smllest = j    
        num[i],num[smllest] = num[smllest],num[i]
    print(num)

myList = [50,30,40,10,20]
selection_sort(myList)