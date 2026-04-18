---
title: Sekilas tentang Customer Insights
canonical_url: https://help-center.qontak.com/hc/id/articles/48123397169433-Sekilas-tentang-Customer-Insights
article_type: concept
solvability_type: content
products:
- Qontak CRM
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- customer-insights
- customer-data-platform
query_examples:
- Apa itu Customer Insights?
- Apa fungsi Customer Insights di Qontak CRM?
- Penjelasan Customer Insights
- What is Customer Insights?
- Bagaimana cara kerja Customer Insights?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Definition  <!-- confidence:high ✓ -->


Saat ini, terdapat sebuah fitur bernama Customer Insight pada Mekari Qontak CRM dan Chat yang akan memudahkan Anda untuk memperoleh informasi terkait Customer secara bersamaaan dikarenakan repositori data customer yang sering kali terpisah. Data tersebut terdiri dari kontak, CRM, dan aktivitas Chat pelanggan.

Fitur Customer Insights berfungsi untuk menyimpan aktivitas pelanggan dari CRM dan Chat yang digabungkan ke dalam satu Gudang Data (DWH) dan menghilangkan data kontak yang mengalami duplikasi. Pada langkah-langkah berikut, Anda akan mempelajari terkait cara mengakses fitur Customer Insights serta setiap komponen yang terdapat di dalamnya. Simak selengkapnya berikut ini.
  1. Masuk ke akun **Omnichannel** Anda, lalu pilih menu **Dashboard**.
  2. Kemudian klik tab **“Customer Insights”**.  
![1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50607917565465)
  3. Lalu Anda akan diarahkan ke halaman Customer Insight. Berikut merupakan penjelasan beberapa komponennya.

###  **A. Customer Growth Overview**  
**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F54370788052761)**[](https://help-center.qontak.com/hc/id/articles/48123397169433-Sekilas-tentang-Customer-Insights#h_01JY582JJ89JSJ5B88VSXB7ZP0)
**Keterangan****:**
**No** | **Nama Fitur** | **Penjelasan**  
---|---|---  
1 | Date filter | Pada menu **Date Filter** , terdapat tiga opsi periode waktu: **Past** , **Current** , dan **Next**. Opsi ini membantu Anda memilih rentang tanggal secara cepat berdasarkan posisi waktu terhadap hari ini.

**Next** digunakan untuk menampilkan data pada **periode mendatang** (belum terjadi).  
Berikut periode yang dapat Anda pilih:  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F54370788066841)  
2 | Total customers |  Menunjukkan jumlah pelanggan di CRM dan _Chat panel_ sesuai periode yang dipilih. Perhitungan menggunakan nomor telepon atau email sebagai identitas. **Cara perhitungan:  
** Jumlah pelanggan yang unik per nomor telepon atau email).  
3 | Monthly Avg. New customers |  Menampilkan total jumlah customer baru yang dibuat pada periode yang dipilih. **Cara perhitungan:** Jumlah catatan customer unik yang tanggal pembuatannya berada dalam periode yang dipilih.  
4 | Monthly Avg. Inactive customers |  Rata-rata jumlah pelanggan per bulan yang tidak lagi berinteraksi dalam periode yang dipilih. **Cara perhitungan:** Jumlah catatan customer unik yang belum mengirim atau menerima pesan (tidak ada ruang percakapan yang dibuat) dan tidak ada transaksi yang dibuat dalam periode yang dipilih.  
5 | Customer Trend Chart |  Grafik ini digunakan untuk melacak jumlah **total pelanggan, pelanggan baru, dan pelanggan tidak aktif** dalam suatu periode waktu tertentu. **Cara perhitungan** : Jumlah dihitung berdasarkan kategori berikut: - **Total customers** : semua pelanggan yang ada.  
- **New customers** : pelanggan yang baru ditambahkan.  
- **Inactive customers** : pelanggan yang berhenti berinteraksi. **Contoh:  
** Jika pengguna memilih periode **September–Desember 2025** , sistem akan menampilkan:
  * Jumlah total pelanggan untuk setiap bulan.
  * Jumlah pelanggan baru untuk setiap bulan.
  * Jumlah pelanggan tidak aktif untuk setiap bulan.

###  **  
B. Customer Demographic/Segmentations**[](https://help-center.qontak.com/hc/id/articles/48123397169433-Sekilas-tentang-Customer-Insights#h_01JY58M24JVSPF7769ACEKGA8C)
  1. **Customer by source****  
**Grafik ini menampilkan asal customer dari channel (obrolan) atau sumber (CRM) tertentu.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F54370788069145)  
**Cara Perhitungan:****  
**Kelompokkan pelanggan berdasarkan kolom _source_.

Kontak yang tidak memiliki nilai _source_(_null_) akan otomatis dikategorikan sebagai **“Other”**.
  2. **Customer by company group  
** Grafik ini menghitung jumlah kontak yang dikelompokkan berdasarkan perusahaan yang terhubung di CRM.![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F54370775773977)  
**Cara Perhitungan:****  
**Hitung kontak yang dikelompokkan berdasarkan CRM.

###  **C. Customer Sales Lifecycle / Conversion Insight**[](https://help-center.qontak.com/hc/id/articles/48123397169433-Sekilas-tentang-Customer-Insights#01JY58XH3YYS311G7PQSGSWET2)
  1. **Customers with Associated Deal Trend  
** Tren persentase pelanggan (kontak) yang terhubung dengan minimal satu _deal_ di sistem CRM dalam suatu periode waktu.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F54370788079001)  
**Cara Perhitungan:  
**(Pelanggan dengan Transaksi / Total Pelanggan) × 100  
**Contoh** :  
Total kontak: 1.200  
Kontak CRM yang terkait dengan transaksi: 450  
Perhitungan:  
**Pelanggan dengan Transaksi Terkait (jumlah): 450  
****Persentase** : (450 / 1.200) × 100 = **37,5%**.

2. **Percentage of Customers whose Transactions were Won  
** Mengukur persentase dari transaksi yang dimenangkan untuk setiap customer.**  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F54370775778713)  
Cara Perhitungan:  
**(Total Transaksi yang Dimenangkan oleh Pelanggan / Total Transaksi yang Dimenangkan oleh Pelanggan) × 100  
**Contoh:  
** Jika 200 pelanggan memiliki transaksi dan 80 di antaranya memiliki setidaknya satu deal yang dimenangkan  
**Perhitungan:  
**(80 / 200) × 100 = **40%

**
  3. **Deal Size per Customer (Avg/Total) (Number)  
** Nilai moneter rata-rata dan total dari semua transaksi yang dikaitkan dengan customer.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F54370918851353)  
**Cara Perhitungan:  
** - Total Deal Size = Jumlah semua Deal Size per pelanggan  
- Avg. Deal Size = Total Deal Size / total customer yang memiliki associated deal.  
**Contoh:  
** Total Deal Size = Rp30.000.000  
Rata-rata ukuran transaksi = (Rp5.000.000 + Rp6.666.667) / 2 = Rp5.833.333

###  **E. Churn Reason by Customer**[](https://help-center.qontak.com/hc/id/articles/48123397169433-Sekilas-tentang-Customer-Insights#h_01JY582JJ9PZ3A0S7SB8F5K82D)
Mengidentifikasi alasan mengapa customer berhenti berinteraksi (churn).
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F48123423757721)  
**Cara Perhitungan:****  
**Jika customer memiliki**associated deal** dengan status **Lost** , maka yang dapat dilakukan adalah**isi kolom Lost Reason (** sebagai contoh, “Harga terlalu tinggi”, “Pilih pesaing”).
### F. Top Sales Frequency & Nominal by Product[](https://help-center.qontak.com/hc/id/articles/48123397169433-Sekilas-tentang-Customer-Insights#h_01JY582JJ9SG7JJDAWPP81KZ27)
Menampilkan produk terlaris dan tren pembelian customer![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F48123397165849)  
**Cara Perhitungan:****  
**a. Filter transaksi dengan tahap = Menang atau probabilitas menang = 100%  
b. Ekstrak data produk dari setiap deal yang dimenangkan (setiap deal dapat dikaitkan dengan satu atau beberapa produk).  
c. Jumlah produk agregat:
  * Hitung berapa kali setiap produk terlibat dalam transaksi yang dimenangkan.
  * Jumlah total pendapatan yang dihasilkan per produk secara opsional.

d. Urutkan berdasarkan jumlah atau pendapatan untuk menentukan produk teratas.**  
**

## Key Attributes  <!-- confidence:high ✓ -->

• Konsolidasi data dari CRM dan Chat panel dalam satu dashboard
• Penghapusan otomatis data kontak duplikat berdasarkan nomor telepon atau email
• Filter tanggal dengan opsi Past, Current, dan Next untuk melihat data historis dan proyeksi
• Metrik utama: Total customers, Monthly Avg. New customers, Monthly Avg. Inactive customers
• Customer Trend Chart untuk melacak perubahan jumlah pelanggan sepanjang waktu
• Perhitungan berbasis identitas unik (nomor telepon atau email)

## Related Tasks  <!-- confidence:medium ~ -->

• Cara mengakses Customer Insights di Omnichannel
• Memahami komponen Customer Growth Overview
• Menggunakan Date Filter untuk analisis periode waktu
• Menginterpretasikan metrik pelanggan baru dan tidak aktif
• Membaca dan menganalisis Customer Trend Chart