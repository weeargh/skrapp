---
title: Bagaimana Cara Mengintegrasikan Email
canonical_url: https://help-center.qontak.com/hc/id/articles/5556127164569-Bagaimana-Cara-Mengintegrasikan-Email
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- multi-channel-integration
- integrate-email
- conversation-management
query_examples:
- Cara Mengintegrasikan Email
- Bagaimana cara Mengintegrasikan Email?
- Langkah-langkah Mengintegrasikan Email di Qontak Omnichannel
- How do I Mengintegrasikan Email?
- Mau Mengintegrasikan Email, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengintegrasikan email dengan Qontak Omnichannel, Anda memerlukan:

1. **Role Admin** pada akun Qontak Omnichannel (hanya Admin yang dapat melakukan integrasi email)
2. **Akun Qontak Omnichannel** yang aktif
3. **Akun email aktif** dari provider yang didukung (Outlook, Gmail, atau email provider lainnya dengan fitur email forwarder)
4. **Akses ke menu Integrations** di Qontak Omnichannel
5. Jika tidak memiliki role Admin, hubungi tim support di support-qontak@mekari.com untuk bantuan

## Steps  <!-- confidence:high ✓ -->


**Integrations** merupakan sebuah fitur Omnichannel Qontak dimana para customer bisa menghubungkan berbagai platform dengan chat panel seperti email atau Instagram.
**Penting**  
Hanya pengguna dengan**role Admin yang dapat melakukan integrasi**. Apabila Anda tidak memiliki akun dengan _role_ Admin, Anda dapat menghubungi tim support kami di 
Untuk mengintegrasikan **chat panel** dengan **Email** pada Web, Anda perlu mengikuti langkah-langkah berikut:
  1. Masuk ke akun Omnichannel Anda. Kemudian, masukkan **Username** dan **Password** Anda. Klik tombol **“Sign in”** untuk memulai.  
![Screenshot_2023-03-31_at_15.21.09.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780202487065)
  2. Masuk ke menu**Integrations** , kemudian pilih **Email.  
![9.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50771056144409)  
**
  3. Klik **“Add Email”** untuk menambahkan akun email yang akan diintegrasikan.  
![email.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780193787929)
Pada bagian kanan form integrasi email terdapat tata cara mengintegrasikan email dan siapa saja yang bisa menggunakan fitur tersebut.

Yang bisa menggunakan fitur integrasi email adalah:  
- Hanya **Admin** yang dapat mengintegrasikan email.  
- **Admin, Supervisor** dan **Agen** dapat menggunakannya di Inbox  
Pastikan penyedia email memiliki fitur email forwarder yang memungkinkan pesan yang masuk dapat diteruskan ke email lain (akan disediakan oleh Qontak).

Cara mengintegrasikan email adalah sebagai berikut:  
1. Buat integrasi email baru pada Chat Panel.  
2.Ikuti langkah-langkahnya dan isi formulirnya.  
3. Integrasi dibuat, Anda akan mendapatkan penerusan email dengan mengakses detail integrasi  
4. Salin Penerus Email.  
5. Pada penyedia email, temukan pengaturan yang memungkinkan Anda untuk meneruskan secara manual setiap email yang masuk ke Anda.  
6. Isi Penerus Email yang disalin dari Chat Panel ke daftar forward otomatis dan simpan pengaturannya.
  4. Kemudian pilih provider email yang Anda inginkan pada bagian **Select provider**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780202490393)

## Error States  <!-- confidence:medium ~ -->

Jika ada field yang diisi tidak sesuai format atau belum lengkap, sistem akan secara otomatis menampilkan pesan error. Periksa kembali:

- Alamat email harus valid
- Password provider email harus benar
- Semua field pada Email configuration harus terisi sesuai format yang diminta
- Provider email harus memiliki fitur email forwarder

Jika error persisten, hubungi support-qontak@mekari.com dengan screenshot error dan detail akun email yang digunakan.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak di **support-qontak@mekari.com** dalam situasi berikut:

- Anda tidak memiliki role Admin untuk melakukan integrasi email
- Pesan error tetap muncul setelah memeriksa kembali kredensial dan konfigurasi
- Email provider tidak mendukung fitur email forwarder
- Integrasi email gagal setelah setup email forwarding

Sediakan screenshot error, alamat email yang diintegrasikan (tanpa password), dan detail tentang email provider yang digunakan.