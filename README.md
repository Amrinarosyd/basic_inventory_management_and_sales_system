# Sweet Savory🍰
## Basic Inventory Management & Sales System with Python
### Capstone Project Module 1 Job Connector Data Science & Machine Learning di Purwadhika Digital Technology School
#### By Amrina Rosyada for Purwadhika JCDS Module 1 Capstone Project
<hr>


Setelah belajar mengenai data collection, conditional statement, looping, regular function, dan beberapa fungsi tambahan lain. menggunakan bahasa Python pada Modul 1 kurikulum program, setiap siswa ditugaskan untuk membuat suatu mini aplikasi yang terdiri dari empat fungsi utama: CRUD (Create, Read, Update, dan Delete). Program akhir ini harus dibuat menggunakan bahasa Python dan bersifat sederhana.

Pada project ini saya membahas mengenai program penjualan/transaksi dalam scope Bakery atau Toko Roti. Bakery tersebut saya beri nama Sweet Savory, berikut penjelasannya:

1. *Login Interface* memiliki 3 pilihan menu yaitu login sebagai employee, login sebagai customer, dan exit program.
> <img width="182" alt="Screenshot 2023-04-30 at 13 07 33" src="https://user-images.githubusercontent.com/115875398/235338526-217ac7ee-d582-4d0e-ba27-f0966c871235.png">

2. Jika user memilih menu 1 untuk masuk sebagai employee,  maka program akan meminta user untuk memasukkan username dan user id yang sudah di-definisikan.
> <img width="181" alt="Screenshot 2023-04-30 at 13 15 13" src="https://user-images.githubusercontent.com/115875398/235338771-505da2a6-23fc-4da1-b1b3-3dc48a386467.png">

3. Jika nama atau user id tidak sesuai atau salah, maka akan ada pemberitahuan bahwa login tidak berhasil dan program akan kembali ke menu awal.
> <img width="182" alt="Screenshot 2023-04-30 at 13 18 31" src="https://user-images.githubusercontent.com/115875398/235338871-9c84aeee-ecb0-462d-b5e3-887caa2ce9a3.png">

4. Jika user id benar, maka program akan berlanjut ke interface menu untuk employee, yang terdiri dari Show stock items (Read), Add Stock (Create), Update Stock (Update), Delete stock (Delete), dan pilihan ke-5 Log Out untuk back to Main Menu.
> <img width="179" alt="Screenshot 2023-04-30 at 13 21 46" src="https://user-images.githubusercontent.com/115875398/235338960-a36a4389-814a-4376-8890-99aa606c7a4f.png">

5. Ketika user memilih menu untuk tampilkan stok, maka akan muncul 3 buah opsi tampilan, yaitu tampilkan semua stok, per Jenis produk, dan tampilkan sesuai keyword yang diinput user.
> <img width="145" alt="Screenshot 2023-04-30 at 13 34 45" src="https://user-images.githubusercontent.com/115875398/235339353-e9b69fb1-270f-4936-8b5f-409551837b86.png">

6. Ketika user memilih opsi untuk menampilkan stok per kategori, maka akan muncul 4 buah kategori stok, yaitu bahan Cake, Bread, Pastry dan Beverage. Pada program ini, dimungkinkan untuk menambahkan kategori stok baru selain 4 kategori yang sudah ada namun belum dapat ditampilkan secara terpisah (hanya akan muncul ketika dimasukkan nama barang dimasukkan sebagai keyword atau ditampilkan semua).
> <img width="159" alt="Screenshot 2023-04-30 at 13 36 24" src="https://user-images.githubusercontent.com/115875398/235339403-762115f8-89f1-41c3-bd3b-8cc342ab7355.png">

7. Sebagai contoh, berikut tampilan ketika user memilih menampilkan stok yang masuk kategori "Cake". Setelah "Cake" ditampilkan, program akan langsung menampilkan kembali menu tampilan stok.
> <img width="341" alt="Screenshot 2023-04-30 at 13 35 29" src="https://user-images.githubusercontent.com/115875398/235339374-255b542c-e879-4c84-a201-3f28f3dee39a.png">

8. Berikut tampilan ketika user ingin menampilkan semua stok.
> <img width="346" alt="Screenshot 2023-04-30 at 13 37 41" src="https://user-images.githubusercontent.com/115875398/235339453-8670e86a-9766-4949-882f-000f75ce0d18.png">

9. Ketika user memilih untuk menampilkan stok sesuai keyword, maka user akan diminta untuk memasukkan input keyword no. barang yang ingin ditampilkan.
> <img width="306" alt="Screenshot 2023-04-30 at 13 39 42" src="https://user-images.githubusercontent.com/115875398/235339505-3b1ec2ac-633a-4d89-9f2e-869085cc738f.png">

10. Ketika user memasukkan keyword dengan contoh "brownies", maka semua stok yang memuat kata "brownies" dalam nama barangnya akan ditampilkan (tidak terkecuali jika diketik dengan lowercase/uppercase/capitalize).
> <img width="325" alt="Screenshot 2023-04-30 at 13 42 41" src="https://user-images.githubusercontent.com/115875398/235339582-bfe2395e-427b-40b2-b49d-f2a14f24d48e.png">

11. Ketika user memilih menu untuk menambahkan stok baru, maka user akan diminta untuk memasukkan nama barang (maks 25 karakter) dan program akan menolak input nama barang baru jika nama sama dengan nama stok yang sudah ada didalam sistem. Jika semua informasi stok baru sudah dimasukkan sesuai ketentuan, maka akan muncul sebuah validasi apakah user yakin untuk menambahkan item. Jika memasukkan value "Y", maka item baru beserta seluruh informasinya akan dimasukkan kedalam list stok.
> <img width="691" alt="Screenshot 2023-04-30 at 13 45 09" src="https://user-images.githubusercontent.com/115875398/235339662-ed3ab3d7-ea5f-40b1-8428-ff17d5fe4001.png">

12. Untuk menu update stok, jenis update terdiri dari update detail stok (hanya untuk barang yang sudah ada di dalam stok). Update yang dapat dilakukan meliputi semua detail barang (nama, jenis, jumlah stok, expired date, dan harga per unit).  
> <img width="401" alt="Screenshot 2023-04-30 at 13 46 22" src="https://user-images.githubusercontent.com/115875398/235339702-6c171cc3-dd53-4159-a485-9eb48b2ec5f5.png">

13. Menu delete stok, untuk menghapus produk yang sudah ada di dalam stok.
> <img width="399" alt="Screenshot 2023-04-30 at 13 47 36" src="https://user-images.githubusercontent.com/115875398/235339770-59eef391-76b4-4e45-baa8-7d69843c02d3.png">

14. Beralih ke Log in as customer, tidak ada pilihan untuk memasukkan username dan employee id, namun ada input nama customer untuk memunculkan namanya saja saat berada di customer interface, dan pilihan menu hanya ada 2, yaitu Show stock items dan buy product. 
> <img width="185" alt="Screenshot 2023-04-30 at 13 50 18" src="https://user-images.githubusercontent.com/115875398/235339862-a4de622f-3bde-4707-95fd-7b737d9fc7b1.png">

15. Dalam menu buy product, user akan ditampilkan stok produk yang dapat dibeli. Ketika user memasukkan No. barang yang salah atau jumlah barang yang melebihi stok, maka program gagal mendeteksi maka pembelian tidak dapat dilakukan. Ketika user selesai membeli produk, maka program akan otomatis menampilkan keranjang belanja beserta total harga yang perlu dibayar oleh customer.
> <img width="322" alt="Screenshot 2023-04-30 at 13 52 33" src="https://user-images.githubusercontent.com/115875398/235339958-a3fe977a-897f-40df-84eb-5f9e92ead874.png">

16. Jika customer memasukkan uang yang lebih sedikit dari total pembelian, maka program akan menolak pembayaran sampai customer input uang yang sesuai nominal pembelian atau melebihi total pembelian. Program juga akan otomatis menghitung kembalian jika uang yang diserahkan customer lebih dari total pembelian, sekaligus mengurangi jumlah stok dari daftar stok toko.
> <img width="363" alt="Screenshot 2023-04-30 at 13 53 57" src="https://user-images.githubusercontent.com/115875398/235340002-93444830-1b75-42cd-ab6d-bd92d50fbc5f.png">
