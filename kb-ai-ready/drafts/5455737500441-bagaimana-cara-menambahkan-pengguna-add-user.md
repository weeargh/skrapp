---
title: Bagaimana Cara Menambahkan Pengguna (Add User)
canonical_url: https://help-center.qontak.com/hc/id/articles/5455737500441-Bagaimana-Cara-Menambahkan-Pengguna-Add-User
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: web
language: id
intent_tags:
- user-permissions
- add-pengguna-add-user
- general-platform
query_examples:
- Cara Menambahkan Pengguna (Add User)
- Bagaimana cara Menambahkan Pengguna (Add User)?
- Langkah-langkah Menambahkan Pengguna (Add User) di Qontak CRM
- How do I Menambahkan Pengguna (Add User)?
- Mau Menambahkan Pengguna (Add User), caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Anda ingin menambahkan pengguna baru ke dalam Qontak CRM. Untuk melakukan ini, Anda harus memenuhi persyaratan berikut:

• Anda harus memiliki akses level Admin di Qontak CRM perusahaan Anda
• Akses ke dasbor Qontak CRM
• Alamat email aktif yang akan digunakan untuk pengguna baru (pengguna akan menerima pesan dari CRM Qontak ke email ini)
• Jika menggunakan struktur tim, tentukan tim utama dan tim sekunder yang sesuai untuk pengguna baru

## Steps  <!-- confidence:high ✓ -->


3. Isi data diri dari pengguna yang akan Anda tambahkan sesuai dengan kolom yang tersedia.  
![a3.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774121087897)  
Keterangan:
**No.** | **Nama Tombol/Kolom** | **Deskripsi**  
---|---|---  
1 | First name | Nama depan dari pengguna (bisa berupa nama lengkap ataupun nama panggilan).  
2 | Last name | Nama belakang dari pengguna (bisa berupa nama lengkap, nama panggilan, ataupun nama divisi/bagian dari pengguna tersebut).  
3 | Mobile Phone | Nomor ponsel dari pengguna, jika dibutuhkan.  
4 | NIK | Nomor Induk Kependudukan dari pengguna, jika dibutuhkan.  
5 | Email address | Alamat e-mail aktif, yang dapat menerima pesan dari CRM Qontak.  
6 | Primary team | Tim utama dari akun tersebut (jika memberlakukan tim di dalam CRM).  
7 | Secondary team | Tim kedua dari akun tersebut (jika tergabung di dalam lebih dari 1 tim).  
8 | Tags | Informasi tambahan lain, untuk penanda sebuah akun pengguna.  
9 | Staff level | Pilih salah satu level karyawan dengan cara klik pada kolomnya.  
10 | Role |  Level akun di dalam CRM, berupa Admin dan Member (Admin: memiliki akses yang lebih luas di dalam CRM, biasa dimiliki oleh Supervisor; Member: akses untuk para staff, di bawah supervisor). - Saat ini terdapat pengaktifan Multi-Factor Authentication (MFA) dapat membantu Anda dalam menjaga keamanan data yang Anda miliki di Qontak. Jika Anda dengan role tertentu telah mengaktifkan MFA, maka setiap melakukan login, Anda akan diminta untuk memasukkan OTP yang dikirim ke email.  
- Daftar Role yang terdampak:  
1. Agent, dengan pengaturan akses pada semua fitur menjadi “Everything”  
2. Member dengan pengaturan akses pada semua fitur menjadi “Everything”  
3. Administrator  
- Trigger yang dapat mengaktifkan MFA pada User Anda:  
1. Mengubah**dari Trial Subscription ke Main Subscription** , akan membuat Anda yang memiliki role Admin, member, dan agent dengan kriteria akses pada semua fitur adalah **“Everything”** menjadi aktif MFA.  
2. Anda**yang merupakan user baru dengan role Administrator** , member dan agent dengan kriteria akses pada semua fitur adalah **“Everything”** akan menjadi aktif **MFA**.  
3. Perubahan**Anda sebagai Admin** , **dan member atau agent** dengan akses **'everything'** pada seluruh permission akan membuat anda menjadi aktif MFA.  
Tanda bintang (*) pada beberapa kolom menandakan kolom tersebut bersifat **wajib/required** , dan kolom lainnya bersifat opsional.
  4. Lalu, Anda dapat mengatur banyak akses seperti, **Contact access, Company access, Deals access,** dan**Task access.**  
**![a4.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774121090841)**
     * **View:** Tentukan akses user tersebut **(everything, team only, atau owned only)** untuk melihat **Contact, Company, Deals, atau Task.**
     * **Edit:** Tentukan akses user tersebut **(everything, team only, atau owned only)** untuk mengedit **Contact, Company, Deals, atau Task.**
     * **Search association:** Tentukan akses user tersebut **(everything, team only, atau owned only)** untuk mencari asosiasi **Contact, Company, Deals, atau Task.**
     * **Timeline view:** Tentukan akses user tersebut **(everything, team only, atau owned only)** untuk melihat timeline **Deals.**
     * **Delete:** Tentukan akses _delete_ untuk user tersebut pada masing - masing bagian.
     * **Upload:** Tentukan akses _upload_ untuk user tersebut pada masing - masing bagian.
     * **Download:** Temtukan akses _download_ untuk user tersebut pada masing - masing bagian.
  5. Selain itu, tentukan akses admin dan akses _report_ seperti berikut.  
![a5.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774147715097)
**No.** | **Nama Tombol/Kolom** | **Deskripsi**  
---|---|---  
1 | Add & edit user | Izinkan user untuk **Add** dan **edit** user dengan klik toggle button ke ON atau tidak ijinkan dengan klik toggle button ke OFF.  
2 | Add & edit teams | Izinkan user untuk **Add** dan **edit** **teams** dengan klik toggle button ke ON atau tidak ijinkan dengan klik toggle button ke OFF.  
3 | Add & edit properties | Izinkan user untuk **Add & edit properties** dengan klik toggle button ke ON atau tidak ijinkan dengan klik toggle button ke OFF.  
4 | Add & edit products | Izinkan user untuk **Add & edit products** dengan klik toggle button ke ON atau tidak ijinkan dengan klik toggle button ke OFF.  
5 | Freeze deal stage | Izinkan user untuk **Freeze deal stage** dengan klik toggle button ke ON atau tidak ijinkan dengan klik toggle button ke OFF.  
6 | View | Izinkan user untuk melihat **report (everything, team only, atau owned only).**  
7 | Download | Izinkan user untuk mengunduh report.  
  6. Klik **"Create User"** setelah pengisian data selesai dilakukan. Sistem akan menyimpan data pembuatan akun baru.

## Error States  <!-- confidence:high ✓ -->

• Email address sudah terdaftar: Sistem akan menampilkan pesan error jika alamat email yang Anda masukkan sudah digunakan oleh pengguna lain. Gunakan alamat email yang berbeda dan unik.
• Kolom yang diperlukan kosong: Jika Anda meninggalkan kolom yang ditandai bintang (*) kosong, tombol "Create User" tidak akan aktif. Pastikan semua kolom wajib telah diisi dengan benar sebelum menyimpan.
• Anda bukan Admin: Hanya pengguna dengan level Admin yang dapat menambahkan pengguna baru. Jika Anda bukan Admin, hubungi administrator CRM perusahaan Anda.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim dukungan Qontak jika Anda mengalami:

• Tidak dapat mengakses menu "Profile Settings" meskipun memiliki akses Admin
• Tombol "Add user" tidak muncul atau tidak responsif
• Pesan error yang tidak jelas saat membuat pengguna baru
• Pengguna baru tidak menerima email aktivasi akun
• Masalah dengan aktivasi Multi-Factor Authentication (MFA) untuk pengguna baru

Siapkan informasi berikut sebelum menghubungi support: ID akun Qontak Anda, nama pengguna Admin Anda, tangkapan layar pesan error (jika ada), dan deskripsi masalah yang detail.