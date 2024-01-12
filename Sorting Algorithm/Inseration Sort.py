"""
Insertion sort adalah algoritma sorting yang menambahkan elemen baru ke 
posisi yang benar dalam sorted list. 
Contoh kode pada Python adalah sebagai berikut.
"""
def insertionsort(S):
    n = len(S)
    for i in range(1, n):
        print(i)
        print(S)
        x = S[i]  
        j = i - 1
        while j >= 0 and S[j] > x:
            S[j + 1] = S[j]
            j -= 1
        S[j + 1] = x

S = [50,30,40,10,20]
print("Sebelum di sortir", S)
insertionsort(S)
print("Setelah di sortir", S)