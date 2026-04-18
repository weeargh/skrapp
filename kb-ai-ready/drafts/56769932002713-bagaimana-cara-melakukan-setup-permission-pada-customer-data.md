---
title: Bagaimana Cara Melakukan Setup Permission pada Customer Data Platform
canonical_url: https://help-center.qontak.com/hc/id/articles/56769932002713-Bagaimana-Cara-Melakukan-Setup-Permission-pada-Customer-Data-Platform
article_type: task
solvability_type: tool
products:
- Qontak Chat
product_surface: web
language: id
intent_tags:
- customer-data-platform
- perform-setup-permission
query_examples:
- Cara Melakukan Setup Permission pada Customer Data Platform
- Bagaimana cara Melakukan Setup Permission pada Customer Data Platform?
- Langkah-langkah Melakukan Setup Permission pada Customer Data Platform di Qontak
  Chat
- How do I Melakukan Setup Permission pada Customer Data Platform?
- Mau Melakukan Setup Permission pada Customer Data Platform, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.3
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk melakukan setup permission pada Field Masking di Customer Data Platform, Anda memerlukan:

• Role Admin — hanya pengguna dengan akses Admin yang dapat mengatur permission pada field
• Akun Mekari Qontak aktif dengan fitur Customer Data Platform sudah diaktifkan
• Akses ke menu Settings → Customizations → Customers
• Daftar pengguna atau role yang akan diberikan permission untuk melihat field yang di-mask
• Field atau custom property sudah dibuat sebelumnya di Customer Data Platform, atau Anda siap membuat field baru

## Steps  <!-- confidence:high ✓ -->


**Field Masking** pada halaman **Customer Data Platform** berfungsi untuk menyamarkan (_mask_) informasi penting pada kolom _field_)_masking_ dapat disesuaikan berdasarkan **level** _**role**_ , sehingga hanya pengguna yang memiliki izin yang dapat melihat data sensitif secara lengkap, seperti nomor telepon, nomor identitas, atau informasi keuangan.
Fitur ini membantu meningkatkan keamanan data serta mendukung kebutuhan industri yang memiliki standar perlindungan data yang tinggi, seperti **perbankan, layanan keuangan, dan sektor publik**.
Pada penjelasan di bawah ini, Anda akan mempelajari cara melakukan **setup permission pada Field Masking** , melihat **tampilan Field Masking pada halaman Customer Data Platform** , serta memahami **aturan (**_**rule**_**) yang berlaku saat menerapkan permission tersebut**.
Ikuti langkah-langkah berikut untuk menggunakan fitur **Field Masking**.
### A. Cara Melakukan Setup Permission pada Field Masking[](https://help-center.qontak.com/hc/id/articles/56769932002713-Bagaimana-Cara-Melakukan-Setup-Permission-pada-Customer-Data-Platform#h_01KNNX8H6QK9B8SBBXJCVXRZQK)
  1. Masuk ke akun Mekari Qontak Anda. Kemudian pilih menu **“Settings”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769920649881)
  2. Selanjutnya, klik tab **“Customizations”** dan pilih **Customers**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769931936537)
  3. Kemudian klik **“Create field”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769931937305)
  4. Selanjutnya, tentukan **field** yang ingin Anda buat. Pada contoh pada gambar di bawah ini, tipe field yang dipilih adalah **Multi-line text**. Lalu klik **“Continue”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769920652953)  
Pelajari lebih lanjut mengenai cara mengelola _field_[di sini](https://help-center.qontak.com/hc/id/articles/53210896837145-Bagaimana-Cara-Mengelola-Custom-Properties-Customer-Data-Platform).
  5. Maka Anda akan diarahkan ke tahapan **Field details**. Pada halaman ini Anda akan melihat tampilan _field_ jenis **Multi-line text** yang nantinya akan muncul pada saat Anda menambahkan data **customer** pada halaman **Customer Data Platform**. Selanjutnya klik **“Continue”** kembali.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769931938969)
  6. Selanjutnya, pada halaman **Field Setup** , tentukan **field permission** untuk pengguna tertentu berdasarkan _**role** _yang mereka miliki. Klik **“Add user”** untuk melanjutkan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769931940761)

**Penting**  
**Keterangan:**  
- Akses **View only** : Pengguna dalam _role_ ini hanya dapat melihat _field_(kolom) dan informasi pada kolom tanpa dapat melakukan perubahan apa pun.  
- Akses **View and masked** : Pengguna dalam _role_ ini dapat melihat _field_ , namun informasi yang ditampilkan sudah disamarkan (_masked_) dan tidak dapat diedit. 
  5. Kemudian klik **“Save”** dan lanjutkan proses penambahan _field_. Pelajari [di sini ](https://help-center.qontak.com/hc/id/articles/53210896837145-Bagaimana-Cara-Mengelola-Custom-Properties-Customer-Data-Platform)lebih lanjut.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769931955097)

### B. Melihat Hasil Field Masking pada Halaman Customer Data Platform[](https://help-center.qontak.com/hc/id/articles/56769932002713-Bagaimana-Cara-Melakukan-Setup-Permission-pada-Customer-Data-Platform#h_01KNNX8H8WHF5VP7GY34ZK0ASG)
Pada _section_ ini, dijelaskan cara melihat hasil _masking_ pada _field_ dari sisi pengguna dengan _role_ tertentu yang telah diatur _permission_ -nya. Terdapat 2 kondisi _masking_ ,**View only** dan **View and masked**. Kondisi ini berlaku baik pada tampilan Qontak Web maupun Qontak Mobile. Berikut tahapannya.
### B.1 Melihat Tampilan Field Masking **View Only** [](https://help-center.qontak.com/hc/id/articles/56769932002713-Bagaimana-Cara-Melakukan-Setup-Permission-pada-Customer-Data-Platform#h_01KNNX8H932A6VA17GZV834SD4)
Field Masking **View Only** yang telah diatur pada halaman Qontak Web akan secara otomatis diterapkan pada halaman Qontak Mobile. Maka dari itu, terapkan terlebih dahulu fitur Field Masking pada halaman Qontak Web. Berikut penjelasannya. 
**1. Qontak Web**  
Untuk dapat melihat tampilan _field_ yang telah di-_masking_(disamarkan) pada halaman Qontak Web, Anda dapat mengikuti langkah-langkah berikut:
  1. Setelah masuk ke akun Qontak Anda, pilih menu **Customers**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769931956505)
  2. Lalu klik tab **“All customers”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769920674713)
  3. Kemudian, klik salah satu nama pada kolom **Customer Name**.  
![33.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769920676505)
  4. Maka pada halaman berikut, saat pengguna klik ikon**‘pensil’** untuk mengedit _field_.  
![34.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769931961753)
  5. Beberapa kolom akan ditampilkan dalam kondisi disamarkan (_masked_), namun informasi yang terdapat di dalamnya masih dapat terlihat.  
![35.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769920679065)
  6. Kondisi ini juga akan terlihat pada halaman **Inbox** di bagian **Customer Profile** sebelah kiri. Ketika pengguna klik **“See all”**.  
![36.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769931963033)
  7. Maka akan muncul ikon **‘edit’**.  
![37.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769920682905)
  8. Kemudian ketika ikon **‘edit’** telah diklik, maka akan muncul kolom dengan kondisi disamarkan (_masked_) seperti yang sebelumnya terlihat pada halaman **Customer detail**.  
![38.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769931967513)

**2. Qontak Mobile**
Field Masking yang telah diterapkan pada Qontak Web juga akan otomatis diterapkan pada Qontak Mobile.
Pada Qontak Mobile, tampilan Field Masking berbeda pada masing-masing jenis _platform_ , yaitu: 
  * Untuk Qontak Mobile Chat, Field Masking akan ditampilkan pada halaman **Conversation info** di bagian **Contact Profile**. 
  * Untuk Qontak CRM Chat, Field Masking akan ditampilkan pada halaman **Customer details** di bagian **Profile Information**. Berikut tampilan _masking_ pada halaman **Qontak Mobile Chat** dan **Qontak Mobile CRM** :

**Qontak Chat Mobile** | **Qontak CRM Mobile**  
---|---  
![21.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769920685849)**Edit customer profile via inbox - CHAT Mobile** |  ![21.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769920685849)**Edit page - CRM Mobile**  
![eq.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769920686233)**Customer profile via inbox - CHAT Mobile** |  ![24.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769920687129)**Details page - CRM Mobile**  
|  ![25.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769920687641)**Index page - CRM Mobile**  
###    
B.2 Melihat Tampilan Field Masking **View and Masked** [](https://help-center.qontak.com/hc/id/articles/56769932002713-Bagaimana-Cara-Melakukan-Setup-Permission-pada-Customer-Data-Platform#h_01KNNX8HA3DM119MHRP0K6PEH0)
Field Masking **View and Masked** yang telah diatur pada halaman Qontak Web akan secara otomatis diterapkan pada halaman Qontak Mobile. Maka dari itu, terapkan terlebih dahulu fitur Field Masking pada halaman Qontak Web. Berikut penjelasannya.
**1. Qontak Web**
  1. Setelah masuk ke akun Qontak Anda, pilih menu **Customers**.  
![32.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769931972889)
  2. Lalu klik tab **“All customers”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769920674713)
  3. Kemudian, pada kolom **Customer Name**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769920694297)
  4. Maka pada halaman berikut, saat pengguna klik ikon**‘pensil’** untuk mengedit _field._   
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769920695065)
  5. Beberapa kolom akan ditampilkan dalam kondisi kolom dan informasi yang terdapat di dalamnya disamarkan (_masked_).  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769931974681)
  6. Kondisi ini juga akan terlihat pada halaman **Inbox** di bagian **Customer Profile** sebelah kiri. Klik **"See all"** untuk melanjutkan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769920696089)
  7. Maka akan muncul ikon **‘edit’**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769931978649)
  8. Kemudian ketika ikon **‘edit’** telah diklik, maka akan muncul kolom dengan kondisi disamarkan (_masked_) seperti yang sebelumnya terlihat pada halaman **Customer detail**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769920698393)

**2. Qontak Mobile**
Field Masking **View and Masked** yang telah diterapkan pada Qontak Web juga akan otomatis diterapkan pada Qontak Mobile.
Pada Qontak Mobile, tampilan Field Masking berbeda pada masing-masing jenis _platform_ , yaitu: 
  * Untuk Qontak Mobile Chat, Field Masking akan ditampilkan pada halaman **Conversation info** di bagian **Contact Profile**. 
  * Untuk Qontak CRM Chat, Field Masking akan ditampilkan pada halaman **Customer details** di bagian **Profile Information**. Berikut tampilan _masking_ pada halaman **Qontak Mobile Chat** dan **Qontak Mobile CRM** :

**Qontak Chat Mobile** | **Qontak CRM Mobile**  
---|---  
![27.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769920700313)**Customer profile via inbox - CHAT Mobile** |  ![26.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769931983513)**Index page - CRM Mobile**  
![30.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769931984153) |  ![28.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769931986457)**Details page - CRM Mobile**  
|  ![29.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F56769920709017)**Edit page - CRM Mobile**  
### C. Ketentuan Field Masking[](https://help-center.qontak.com/hc/id/articles/56769932002713-Bagaimana-Cara-Melakukan-Setup-Permission-pada-Customer-Data-Platform#h_01KNNX8HAJ749SDSNQDJH0T049)
Setelah **Field Masking Permission** dikonfigurasi, Anda perlu memahami bagian field yang akan ditampilkan dalam bentuk **masking**. Terdapat dua tipe field yang dapat diatur, yaitu **Default Field** dan **Custom Field**. Tabel berikut menjelaskan ketentuan masking pada masing-masing tipe field, termasuk bagian data yang akan ditampilkan dalam bentuk **asterisks (*)**.
###  C1. Default Field[](https://help-center.qontak.com/hc/id/articles/56769932002713-Bagaimana-Cara-Melakukan-Setup-Permission-pada-Customer-Data-Platform#h_01KNNX8HAMA3FN85AC2MHCPGWZ)
**Field** | **Contoh Data Asli** | **Aturan Masking** | **Tampilan Setelah Masking**  
---|---|---|---  
Full Name | Andi Pratama | Tidak dapat di-_masking_ | Tidak dapat di-_masking_  
Owner | Sarah Wijaya | Ditampilkan 5 asterisks | *****  
Assignee | Tania Larissa | Ditampilkan 5 asterisks | *****  
Sex | Male | Ditampilkan 5 asterisks | ****  
Domicile | Jakarta | Ditampilkan 5 asterisks | ******  
Phone Number | 
  * 6281234567899
  * 50012345690

Date of Birth | 12-05-1998 | Semua di-_masking_ , hanya tahun yang ditampilkan | **-**-1998  
Email | andi.pratama@gmail.com | Bagian nama di-_masking_ , domain tetap ditampilkan. | ****.*******@gmail.com  
###  C2. Custom Field Template by Qontak[](https://help-center.qontak.com/hc/id/articles/56769932002713-Bagaimana-Cara-Melakukan-Setup-Permission-pada-Customer-Data-Platform#h_01KNNX8HBASCDDVA8JGJNA0FQA)
**Field** | **Contoh Data Asli** | **Aturan Masking** | **Tampilan Setelah Masking**  
---|---|---|---  
Source | Instagram | Ditampilkan 5 asterisks | *****  
Status | Qualified | Ditampilkan 5 asterisks | *****  
###  C3. Custom Field[](https://help-center.qontak.com/hc/id/articles/56769932002713-Bagaimana-Cara-Melakukan-Setup-Permission-pada-Customer-Data-Platform#h_01KNNX8HBHW32D27J7904AXF0J)
**Field** | **Contoh Data Asli** | **Aturan Masking** | **Tampilan Setelah Masking**  
---|---|---|---  
Single-line Text | Jakarta | 1–3 karakter: semua karakter di-_masking_ (*******).

Lebih dari 3 karakter: semua karakter di-_masking_ kecuali karakter pertama dan terakhir. | J*****a  
Multi-line Text | Customer   
Jakarta | 1–3 karakter: semua karakter di-_masking_ (*******).

Lebih dari 3 karakter: semua karakter di-_masking_ kecuali karakter pertama dan terakhir. | C******* *******a  
GPS | -6.2088,106.8456 | 1–3 karakter: semua karakter di-_masking_ (*******).

Lebih dari 3 karakter: semua karakter di-_masking_ kecuali karakter pertama dan terakhir. | -**************6  
Number - Numeric | 12345 | 1–3 digit: semua digit dimasking (*******).

Lebih dari 3 digit: semua digit di-_masking_ kecuali digit terakhir. | ****5  
Number - Currency | IDR 150000 | 1–3 digit: semua digit di-_masking_ (*******).

Lebih dari 3 digit: semua digit dimasking kecuali digit terakhir | IDR *****0  
Number - Percentage | 90,17% | Semua digit di-_masking_ kecuali digit terakhir, sementara simbol persen (%) tetap ditampilkan. | **,*7%  
Dropdown Select | Instagram Ads | Informasi field ditampilkan sebagai lima asterisk (*****). | *****  
Multiple Select | Email,   
WhatsApp,   
Website | Informasi field ditampilkan sebagai lima asterisk (*****) serta menampilkan jumlah opsi yang dipilih. | ***** (3 selected)  
Date Format | 12-08-1998 | Nilai tanggal dan bulan di-_masking_ , sementara tahun tetap ditampilkan. |  ****** -****** -1998  
File Upload | contract_  
customer.pdf | Nama file di-_masking_ , sementara ekstensi file tetap ditampilkan. | ********_******.pdf  
URL | https://tokopedia.  
com | Semua karakter di-_masking_ kecuali domain. | *********.com  
Signature | (gambar tanda tangan) | Gambar tanda tangan ditampilkan dalam kondisi blur. | Gambar tanda tangan ditampilkan dalam kondisi blur.  
Demikian penjelasan terkait cara melakukan _setup permission_ pada Customer Data Platform. Pelajari terkait cara membuat Custom Field untuk Customer Data Platform [di sini](https://help-center.qontak.com/hc/id/articles/53210896837145).

## Error States  <!-- confidence:low ? -->

No common errors documented.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim dukungan Mekari Qontak jika mengalami:

• Pengguna yang dipilih tidak muncul di halaman Field Setup setelah klik Apply
• Tombol Save tidak aktif atau tidak merespons saat mengklik
• Permission tidak tersimpan meskipun sudah melakukan konfigurasi
• Akses menu Settings atau Customizations tidak tersedia padahal role Admin sudah ditetapkan

Sertakan informasi: ID akun, nama pengguna yang bermasalah, role yang diberikan, dan screenshot tahap mana error terjadi.