# Nama : Agung Mubarok 
# NIM  : 0110120196
# Kelas: Sistem Informasi - 05

def sort_desc(arr):
  # Memulai perulangan dari index 1 sampai panjang dari parameter arr
  for i in range (1, len(arr)):
    # Membuat variabel key untuk menyimpan element di index i
    key = arr[i]
    # Inisialisasi variabel perulangan untuk digunakan dalam perulangan while
    j = i - 1
    # Selama j lebih dari sama dengan 0 dan element di index j kurang dari key
    while j >= 0 and arr[j] < key:
      # Maka dilakukan pergeseran dari j ke j+1
      arr[j+1] = arr[j]
      # Variabel loop j dikurangi 1
      j -= 1
    # key ditempatkan di j, dan di + 1 karena sebelumnya sudah di - 1
    arr[j+1] = key
  # Mengembalikan nilai parameter arr
  return arr





# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya.
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  r = sort_desc([2, 3, 1, 0, 4])
  print(f"sort_desc([2, 3, 1, 0, 4]) = {r} \n(solusi: [4, 3, 2, 1, 0]")
  print()
  r = sort_desc([1, 2, 3])
  print(f"sort_desc([1, 2, 3]) = {r} \n(solusi: [3, 2, 1]")
  print()

if __name__ == '__main__':
  test()