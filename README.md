# Komputasi-Numerik
# Tugas-Program-Komnum
### Anggota Kelompok A07

|    NRP     |      Name      |
| :--------: | :------------: |
| 5025241111 | Hanif Aqil Janardana |
| 5025241113 | Rafa Huga Nirando |
| 5025241115 | Royan Habibi Alfatih |
| 5025241117 | Hazza Danta Hermandanu |
| 5025241123 | Cornelius Andika |

<br>

### Soal

Diketahui f(x) = x ^ 3 + 6x ^ 2 - 19x - 84. Diketahui:
<br>
Batas bawah (XL) = - 4 
<br>
Batas atas (Xu) = 3 
<br>
Nilai X sebenarnya = -3 
<br>
Cari akar x dengan menggunakan metoda bagi dua 
<br>
[Lakukan iterasi sampai 0 <= Et < 1 Print semua iterasinya

<br>

#### Full Code
```python
from decimal import Decimal, ROUND_HALF_UP

def pembulatan(x):
    return Decimal(str(x)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def f(x):
    return x**3 + 6*x**2 - 19*x - 84

def bagi_dua(xl, xu, xt):
    iterasi = 1
    print("Iterasi\t\tXL\t\tXU\t\tXR\t\tf(XR)\t\tEt(%)")
    
    while True:
        xr = (xl + xu) / 2

        xr_pembulatan = pembulatan(xr)
        fxr_pembulatan = pembulatan(f(xr_pembulatan))

        et = abs((xt - xr_pembulatan) / xt) * 100

        et_pembulatan = pembulatan(et)

        print(f"{iterasi}\t\t{xl:.2f}\t\t{xu:.2f}\t\t{xr_pembulatan}\t\t{fxr_pembulatan}\t\t{et_pembulatan}")

        if et < 1 and et >= 0:
            break

        if f(xl) * f(xr_pembulatan) < 0:
            xu = xr_pembulatan
        else:
            xl = xr_pembulatan

        iterasi += 1

    print("\nAkar X =", f"{xr_pembulatan}")

xl = -4
xu = 3
xt = -3

bagi_dua(xl, xu, xt)

```

<br>

#### Penjelasan
```python
from decimal import Decimal, ROUND_HALF_UP
```
Untuk mengimpor Decimal yang digunakan untuk representasi bilangan desimal dan `ROUND_HALF_UP` yang digunakan untuk pembulatan

<br>

```python
def pembulatan(x):
    return Decimal(str(x)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
```
Membuat fungsi pembulatan :
- `Decimal(str(x))` mengonversi input menjadi string lalu dimasukkan ke `Decimal()`
- Menyesuaikan jumlah angka di belakang `,` dengan `.quantize(Decimal('0.01')` agar pembulatannya 2 angka dibelakang `,`
- `rounding=ROUND_HALF_UP` digunakan untuk menentukan aturan pembulatan dimana jika digit ke-tiga >= 5 akan dibulatkan ke-atas, sedangkan jika digit ke-tiga < 5 akan dibulatkan ke bawah

<br>

```python
def f(x):
    return x**3 + 6*x**2 - 19*x - 84
```
Fungsi dari soal

<br>

```python
def bagi_dua(xl, xu, xt):
    iterasi = 1
    print("Iterasi\t\tXL\t\tXU\t\tXR\t\tf(XR)\t\tEt(%)")
    
    while True:
        xr = (xl + xu) / 2

        xr_pembulatan = pembulatan(xr)
        fxr_pembulatan = pembulatan(f(xr_pembulatan))

        et = abs((xt - xr_pembulatan) / xt) * 100

        et_pembulatan = pembulatan(et)

        print(f"{iterasi}\t\t{xl:.2f}\t\t{xu:.2f}\t\t{xr_pembulatan}\t\t{fxr_pembulatan}\t\t{et_pembulatan}")

        if et < 1 and et >= 0:
            break

        if f(xl) * f(xr_pembulatan) < 0:
            xu = xr_pembulatan
        else:
            xl = xr_pembulatan

        iterasi += 1

    print("\nAkar X =", f"{xr_pembulatan}")
```
Fungsi untuk perhitungan metode bagi dua
- `iterasi = 1`, iterasi dimuali dari 1
- ``` python
  while True:
        xr = (xl + xu) / 2

        xr_pembulatan = pembulatan(xr)
        fxr_pembulatan = pembulatan(f(xr_pembulatan))
  ```
  - Menjalankan perulangan while
  - Menghitung nilai xr dengan rumus `xr = (xl + xu) / 2`
  - Melakukan pembulatan xr dan f(xr) 2 angka di belakang `,` dengan memanggil fungsi pembulatan
- ``` python
      et = abs((xt - xr_pembulatan) / xt) * 100
      et_pembulatan = pembulatan(et)
  ```
  - Menghitung nilai Et dengan `abs` agar nilainya selalu positif, lalu kali dengan 100
  - Melakukan pembulatan Et 2 angka di belakang `,` dengan memanggil fungsi pembulatan
- ``` python
  print(f"{iterasi}\t\t{xl:.2f}\t\t{xu:.2f}\t\t{xr_pembulatan}\t\t{fxr_pembulatan}\t\t{et_pembulatan}")
  ```
  Print xl, xu, xr, f(xr), dan Et dari iterasi ke i
- ``` python
  if et < 1 and et >= 0:
            break
  ```
  Saat 0 >= Et > 1, maka keluar dari perulangan dengan `break`
- ``` python
  if f(xl) * f(xr_pembulatan) < 0:
            xu = xr_pembulatan
        else:
            xl = xr_pembulatan

        iterasi += 1
  ```
  - Jika f(xl) * f(xr) < 0, maka xu = xr
  - Jika kondisi tidak terpenuhi maka xl = xr
  - Berallih ke iterasai selanjutnya dengan menambah jumlah iterasi sebanyak 1
- ``` python
  print("\nAkar X =", f"{xr_pembulatan}")
  ```
  Print akar dari x yaitu xr

<br>

``` python
xl = -4
xu = 3
xt = -3
```
Diketahui dari soal

<br>

```python
bagi_dua(xl, xu, xt)
```
Memanggil fungsi `bagi_dua` untuk memulai perhitungan

<br>

#### Output
![image](https://github.com/user-attachments/assets/fc9a9ef4-4034-4dd4-92e3-d6064166f15b)



