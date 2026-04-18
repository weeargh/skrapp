---
title: Bagaimana Cara Membuat Recipient List untuk Email Campaign
canonical_url: https://help-center.qontak.com/hc/id/articles/47426266423065-Bagaimana-Cara-Membuat-Recipient-List-untuk-Email-Campaign
article_type: task
solvability_type: tool
products:
- Qontak CRM
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- email-campaign
- create-recipient-list-untuk-email-cam
- marketing-campaign-manage
query_examples:
- Cara Membuat Recipient List untuk Email Campaign
- Bagaimana cara Membuat Recipient List untuk Email Campaign?
- Langkah-langkah Membuat Recipient List untuk Email Campaign di Qontak CRM
- How do I Membuat Recipient List untuk Email Campaign?
- Mau Membuat Recipient List untuk Email Campaign, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Anda ingin membuat Recipient list untuk Email Campaign. Sebelum memulai, pastikan Anda memiliki:

1. Akun Mekari Qontak aktif dengan langganan paket Broadcast, Service Suite, Sales Suite, atau Qontak 360
2. Akses ke menu Campaign di Qontak Omnichannel dengan peran manajemen campaign
3. File berisi data recipient (format CSV, XLS, atau XLSX) dengan ukuran maksimal 5 MB
4. Data email recipient dan nama lengkap siap untuk diunggah
5. Kuota email campaign harian yang mencukupi untuk jumlah recipient yang akan diimpor

## Steps  <!-- confidence:high ✓ -->


Untuk dapat membuat [Email campaign](https://help-center.qontak.com/hc/id/articles/47425969961625-Bagaimana-Cara-Membuat-Email-Campaign), Anda perlu membuat Recipient list atau daftar penerima Email Campaign yang akan Anda kirimkan. Pelajari langkah-langkahnya berikut ini.
**Penting**  
Email Campaign hanya akan muncul pada pengguna yang berlangganan paket terbaru dari Mekari Qontak, yaitu: **Broadcast, Service Suite, Sales Suite,** atau **Qontak 360**. Lihat rincian paket tersebut [di sini](https://qontak.com/harga/).
  1. Masuk ke akun **Omnichannel** Anda, lalu pilih menu **“Campaign”**.
  2. Klik tab **“Recipient lists”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F47426266416025)
  3. Kemudian klik **“Create recipient list”** dan pilih **“Upload file”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F47426266416153)
- Opsi **“Select contacts”** saat ini hanya tersedia untuk **WhatsApp Campaign.**  
- Anda tidak dapat mengimpor **Recipient lists** baru jika proses impor yang sebelumnya belum selesai.
  4. Isikan nama **Recipient list** pada kolom berikut.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F47426266416537)
Gunakan nama yang unik pada daftar _recipient_ agar Anda lebih mudah menemukannya saat mengirim _campaign_.
  5. Kemudian pilih tipe data template. Dalam hal ini, pilih **"Email template"** dan tentukan format file yang akan diunggah.  
**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F47426281632153)**
  6. Lalu pada _template_ yang telah disediakan, ganti contoh pengisian dengan data _recipient_ yang Anda inginkan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F47426281632409)
**Penting**  
1. Pastikan kolom pertama **(recipient_email_address)** dan kolom kedua **(full_name)** tidak diubah nama _header_ -nya. Sistem akan mendeteksi _template_ sebagai **Recipient lists “Email”** melalui penamaan _header_ tersebut.  
2. Kolom ketiga **(customer_name)** dan kolom keempat **(company)** merupakan contoh _custom field_. Jika Anda tidak membutuhkan kedua informasi tersebut, Anda dapat menghapusnya. Anda dapat menambahkan informasi lain untuk digunakan sebagai data **variabel** ketika mengirimkan _campaign_ dengan mengisi dari **kolom C** dan seterusnya.  
3. Pastikan semua data atas kolom yang Anda tambahkan diisi dengan lengkap. Data _recipient_ akan gagal diimpor jika ada _value_ yang kosong.  
4. Jika daftar Recipient list Anda mengandung **email yang sama** , sistem akan otomatis mengambil data email pertama sebagai data _recipient_ yang _valid_ , dan data yang duplikat tidak akan diimpor.
  7. Kemudian unggah kembali template yang telah terisi tersebut dengan tarik file tersebut ke tampilan berikut, atau klik **“Browse”** , kemudian unggah file secara manual. Lalu klik **"Import"**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51230879965465)
- Unggah file dengan ukuran maksimal **5 MB**.  
- Untuk **WhatsApp campaign** , Anda dapat mengimpor daftar recipient maksimal **50.000 recipients** dalam 1 file upload.  
- Untuk **Email campaign** , Anda dapat mengimpor daftar recipient dengan jumlah maksimal sesuai dengan [**kuota dasar harian email**](https://help-center.qontak.com/hc/id/articles/50305970510745)Anda. Jika pada saat upload data, **kuota dasar** Anda sebanyak **4.000, maka Anda hanya dapat mengimpor maksimal 4.000 recipients dalam 1 file upload.**  
Limitasi baru pada email campaign berlaku sejak **15 September 2025 sesuai dengan mulai berlakunya penerapan limit harian pengiriman email**.
  8. Maka akan muncul notifikasi berikut yang menyatakan bahwa Recipient list sedang dalam proses pengunggahan. Recipient list yang berhasil terunggah akan muncul pada halaman berikut dengan kategori Channel **‘Email’** sesuai dengan data template yang sebelumnya telah dipilih.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F47426266419737)

### Menghapus Recipient List[](https://help-center.qontak.com/hc/id/articles/47426266423065-Bagaimana-Cara-Membuat-Recipient-List-untuk-Email-Campaign#h_01K9MJ83SDE9ZP9ZXNH6J0ENZ2)
Anda dapat **menghapus** data **Recipient lists** jika data yang diunggah tidak sesuai, atau jika data tersebut tidak relevan lagi untuk digunakan. Berikut langkahnya.
  1. Klik **“Actions”** lalu pilih **“Delete list”** pada salah satu **Recipient lists** yang ingin Anda hapus.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52284811708697)
  2. Klik **“Delete”** untuk mengkonfirmasi penghapusan Recipient lists.  
**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52284836572313)**
  3. Anda juga dapat melakukan penghapusan data melalui halaman _detail_ Recipient list. Klik **“Actions”** pada daftar recipient yang ingin dihapus, lalu pilih **“View details”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52284836572569)
  4. Lalu Klik **“Delete list”** pada halaman berikut.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52284836574489)
  5. Klik **“Delete”** untuk mengkonfirmasi penghapusan Recipient lists.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52284811710745)
  6. Maka daftar recipient berhasil dihapus.  
![22.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52284811711001)

## Error States  <!-- confidence:high ✓ -->

1. **Email duplikat dalam file**: Sistem akan mengimpor hanya data email pertama dan menghapus duplikat. Cek file Anda sebelum mengimpor.
2. **Kolom kosong**: Impor gagal jika ada value kosong pada kolom yang Anda gunakan. Pastikan semua data terisi lengkap.
3. **Melebihi kuota harian**: Jika jumlah recipient melebihi kuota email harian Anda, impor akan gagal. Kurangi jumlah recipient atau tunggu pembaruan kuota.
4. **File terlalu besar**: File maksimal 5 MB. Gunakan file yang lebih kecil atau bagi data menjadi beberapa file.
5. **Impor sebelumnya masih berjalan**: Tunggu impor sebelumnya selesai sebelum mengimpor daftar recipient baru.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Mekari Qontak jika Anda mengalami:

1. Pesan error saat mengimpor recipient list yang tidak jelas atau tidak tercantum di atas
2. File berukuran di bawah 5 MB tetapi tetap ditolak sistem
3. Data recipient tidak muncul setelah impor dinyatakan berhasil
4. Kebutuhan khusus terkait format file atau custom field yang tidak standar

Siapkan screenshot error message, file yang Anda coba impor, dan ID akun Qontak Anda saat menghubungi support.