---
title: Bagaimana Cara Melakukan Pengaturan User Management
canonical_url: https://help-center.qontak.com/hc/id/articles/6153656699545-Bagaimana-Cara-Melakukan-Pengaturan-User-Management
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- platform
- perform-pengaturan-user-management
- general-platform
query_examples:
- Cara Melakukan Pengaturan User Management
- Bagaimana cara Melakukan Pengaturan User Management?
- Langkah-langkah Melakukan Pengaturan User Management di Qontak Omnichannel
- How do I Melakukan Pengaturan User Management?
- Mau Melakukan Pengaturan User Management, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.3
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk melakukan pengaturan User Management di Qontak Omnichannel, Anda membutuhkan:

- Akun Qontak Omnichannel aktif dengan akses role Admin
- Akses ke menu Settings di dashboard Qontak Omnichannel
- Koneksi internet stabil untuk membuka web Qontak Omnichannel
- Informasi user yang akan ditambahkan: nama depan, nama belakang, nomor telepon, email, dan organization
- Penentuan role yang akan di-assign (Agent, Supervisor, atau Admin)

## Steps  <!-- confidence:high ✓ -->


Pada**User Management,** terdapat pengaturan users yang berguna untuk **menambahkan, mengedit atau bahkan menghapus user.** Pada fitur ini juga, Anda dapat membatasi akses pesan masuk berdasarkan semua divisi atau divisi tertentu. Namun perlu diketahui jika hanya **Admin** yang bisa mengakses fitur ini.
  1. Untuk mengaksesnya, Anda dapat masuk ke menu **Settings**.
  2. Lalu pilih tab **User Management**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36776188693785)

### A. Sekilas Tampilan User Management[](https://help-center.qontak.com/hc/id/articles/6153656699545-Bagaimana-Cara-Melakukan-Pengaturan-User-Management#h_01HR4BCZYRCPB2H1BHAJ4TPDR9)
  1. Berikut tampilan dari **User management**.  
**![1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49491303027225)Keterangan:******  
**** **No** | **Kolom** | **Penjelasan**  
---|---|---  
1 | All role | Filter yang dapat Anda gunakan untuk memilih tampilan user berdasarkan Role Supervisor atau Agent.  
2 | Search users | Apabila ingin mencari user secara spesifik, Anda dapat melakukan pencarian melalui kolom Search User.  
3 | Add new user | Klik untuk menambahkan user baru.  
4 | Tabel user | Di sini, Anda dapat melihat user yang sudah terdaftar di Omnichannel Qontak.  
5 | Actions | Tombol untuk mengakses 'Edit' dan 'Delete' user.

2. Kemudian, isi kolom yang dibutuhkan seperti berikut.  
![3.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F38895397536409)  
Keterangan:  
**No** | **Kolom** | **Penjelasan**  
---|---|---  
1 | First name | Masukkan nama depan user.  
2 | Last name | Masukkan nama belakang user  
3 | Phone number | Masukkan nomor telepon user.  
4 | Email | Masukkan email user.  
5 | Organization | Pilih organization user tersebut.  
6 | Role |  Pilih role yang ingin di assign pada user tersebut. ![4.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F38895437613465)  
- Saat ini terdapat pengaktifan **Multi-Factor Authentication (MFA)** dapat membantu Anda dalam menjaga keamanan data yang Anda miliki di Qontak. Jika Anda dengan role tertentu telah mengaktifkan MFA, maka setiap melakukan login, Anda akan diminta untuk memasukkan OTP yang dikirim ke email.   
- Daftar Role yang terdampak:   
a. Agent, dengan Broadcast permission;  
b. Supervisor;  
c. Admin.  
- Trigger yang dapat mengaktifkan MFA pada User Anda:   
1. Mengubah dari Trial Subscription ke Main Subscription, akan membuat Anda yang memiliki role Agent, Supervisor, dan Admin menjadi aktif MFA.   
2. Anda, yang merupakan user baru dengan role Agent, Supervisor, dan Admin akan menjadi aktif MFA.   
3. Perubahan Anda sebagai user lama menjadi role Agent, Supervisor, dan Admin akan membuat Anda menjadi aktif MFA.   
4. Pengaktifan fitur Broadcast untuk semua Agent akan membuat Anda dengan role Agent akan menjadi aktif MFA.  
7 | Chat access |  Ini bagian khusus jika Anda memilih role **Supervisor**. Pilihan ini akan membantu supervisor dalam mengidentifikasi pesan masuk yang ditujukan hanya untuk divisinya.
     * All division: Semua divisi bisa melihat pesan masuk.
     * Assigned division only: Hanya bisa melihat berdasarkan divisi tertentu.  
8 | Division | Masukkan divisi dari user tersebut.

## Error States  <!-- confidence:low ? -->

No common errors documented.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika mengalami:

- Tidak dapat mengakses menu User Management meskipun sudah login dengan role Admin
- User baru tidak muncul di daftar tabel user setelah diklik tombol Simpan
- Multi-Factor Authentication (MFA) tidak teraktifkan secara otomatis pada user dengan role yang seharusnya aktif MFA
- Gagal mengirim notifikasi atau email ke user baru

Siapkan informasi: screenshot error, nama akun Admin Anda, dan email user yang bermasalah.