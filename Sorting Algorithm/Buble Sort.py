"""
sebuh metode penyotiran/pengurutan dari sebuah himpunan 
dimana setiap dua anggota himpunan dibandingan sampai tersortir (urut)
"""
def buble_sort (num:list):
    n = len(num)
    for i in range(n):
        print(num)
        for j in range(n - 1):
            if num[j] > num[j + 1]:
                num[j],num[j + 1] = num[j + 1],num[j]

MyList = [1,2,4,7,4,9,11,44,7,3]
buble_sort(MyList)
