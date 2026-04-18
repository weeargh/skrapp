---
title: Bagaimana Cara Menambahkan Bulk Contact Versi  Web  pada Mekari Qontak CRM
canonical_url: https://help-center.qontak.com/hc/id/articles/5522331530265-Bagaimana-Cara-Menambahkan-Bulk-Contact-Versi-Web-pada-Mekari-Qontak-CRM
article_type: task
solvability_type: tool
products:
- Qontak CRM
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- contact-crm
- add-bulk-contact
- customer-data-platform
query_examples:
- Cara Menambahkan Bulk Contact Versi  Web  pada Mekari Qontak CRM
- Bagaimana cara Menambahkan Bulk Contact Versi  Web  pada Mekari Qontak CRM?
- Langkah-langkah Menambahkan Bulk Contact Versi  Web  pada Mekari Qontak CRM di Qontak
  CRM
- How do I Menambahkan Bulk Contact Versi  Web  pada Mekari Qontak CRM?
- Mau Menambahkan Bulk Contact Versi  Web  pada Mekari Qontak CRM, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

- Akun Qontak CRM aktif dengan akses ke menu Contacts
- Akses ke versi web Qontak CRM
- Role pengguna dengan izin untuk membuat kontak
- File template Excel yang tersedia di dashboard CRM
- Data kontak dalam format Excel atau CSV
- File berukuran maksimum 25 MB dengan jumlah baris maksimum 7.000
- Catatan: Jika menggunakan Qontak One, lihat dokumentasi Customer Data Platform yang telah diperbarui

## Steps  <!-- confidence:high ✓ -->


Menu **“Kontak”** pada situs sosial CRM digunakan untuk menginput database representatif perusahaan atau Person In Charge (PIC) dari pelanggan perusahaan Anda. Untuk melakukan penambahan data pada menu **Kontak** CRM dapat dilakukan secara satu per satu _(single upload)_ ataupun massal _(bulk upload)._ Pada tutorial kali ini kami akan menginfokan cara melakukan penambahan data **Kontak** secara massal _(bulk upload)_ melalui _website_ pada situs sosial CRM Qontak. Silahkan mengikuti langkah – langkah berikut ini.
Sudah menggunakan [Qontak One](https://help-center.qontak.com/hc/id/articles/53169095720729-Sekilas-tentang-Qontak-One)? Jelajahi pengalaman[ Customer yang baru](https://help-center.qontak.com/hc/id/articles/53183780046105-Sekilas-tentang-Customer-Data-Platform) di Qontak One untuk langkah-langkah dan panduan antarmuka yang telah diperbarui.
**Penting!**  
- Apabila pada **Q2 2024** Anda **sudah berlangganan** **Qontak CRM** , namun **belum berlangganan Qontak Omnichannel** , maka apabila nantinya Anda berlangganan **Qontak Omnichannel** , Anda **tidak perlu** membuat kontak lagi pada **Qontak Omnichannel** tersebut.  
- Apabila pada **Q2 2024** Anda **sudah berlangganan Qontak Omnichannel** dan **Qontak CRM** , maka kontak yang telah dibuat pada **CRM** akan secara otomatis terbuat di **Omnichannel**.
  1. Pastikan Anda sudah login ke dalam akun CRM Anda.
  2. Masuk ke menu **Kontak/Contacts,** kemudian klik **"Add Contact****”** dan pilih **Bulk add contacts**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49586336116121)

3. Unduh template Excel yang sudah tersedia dalam dashboard CRM.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49586336117785)
  4. Perlu diperhatikan bahwa _unique field _yang menjadi pembeda antara data “**Kontak”** satu dengan yang lainnya adalah pada bagian email dan phone number.
  5. Pada saat pengisian data mengguankan _form_ excel ini, pastikan bahwa data yang diinput tidak ter-double. Kemudian, isilah kolom – kolom yang tersedia pada Excel sesuai _database_ yang Anda miliki.
  6. Apabila terdapat kolom yang bertanda **(*),** artinya kolom tersebut wajib diisi. Sedangkan pada kolom yang terkustomisasi seperti; Status, Job Title, dll. pengisian data pada file excel harus sesuai dengan opsi yang terdapat pada database CRM. Mulai dari ejaan, besar kecil huruf, sampai penempatan spasi perlu diperhatikan harus sama persis, karena jika terdapat _typo_ atau tidak sesuai akan menyebabkan _error_ pada data yang diunggah.  
![Contact_Bulk__3.jpg](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781183618073)
  7. Pada kolom “**Owner”** Anda dapat sesuaikan dengan username ataupun email dari pemilik data kontak tersebut.  
![Contact_Bulk_4.jpg](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781141856665)
  8. Jika data “**Kontak”** pada _file_ excel sudah terisi semua, Anda dapat merubah format pada _file_ excel menjadi **“Text”**.  
![Contact_Bulk_5.jpg](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781141855513)
  9. Klik **“Browse a file”** untuk mengunggah kembali file Excel “**Kontak”** yang sudah terisi.  
![09.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F26552575400089)

Apabila sudah menerima email notifikasi tersebut Anda dapat melihat detail penjelasan data - data apa saja yang gagal terunggah, Silahkan periksa kembali _file_ Anda dan perbaiki data yang salah.

## Error States  <!-- confidence:medium ~ -->

- **Data gagal terunggah**: Jika ada baris data yang tidak sesuai format atau ada typo pada kolom terkustomisasi (Status, Job Title), sistem akan menolak baris tersebut. Perbaiki data dan pastikan ejaan, huruf, dan spasi sama persis dengan opsi di CRM.
- **Duplikasi data**: Jika email atau nomor telepon sudah ada, sistem akan mendeteksi duplikasi. Hapus data duplikat sebelum mengunggah.
- **Format kolom salah**: Jika format file bukan Excel atau Text, sistem mungkin tidak dapat membaca file. Konversi ke format yang didukung.
- **File terlalu besar**: Jika file lebih dari 25 MB atau lebih dari 7.000 baris, bagi menjadi beberapa file dan unggah terpisah.

## Escalation  <!-- confidence:medium ~ -->

Hubungi dukungan Qontak jika:
- File berhasil diunggah tetapi data tidak muncul di menu Contacts setelah 1 jam
- Sistem menampilkan pesan error yang tidak jelas pada saat pengunggahan
- Sebagian besar baris data gagal terunggah tanpa penjelasan yang jelas

Sediakan informasi berikut:
- ID akun Qontak CRM Anda
- Screenshot atau deskripsi error yang muncul
- Jumlah data yang diunggah dan jumlah yang gagal
- File Excel (jika memungkinkan) untuk analisis lebih lanjut