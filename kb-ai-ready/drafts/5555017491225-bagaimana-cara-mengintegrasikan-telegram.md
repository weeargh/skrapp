---
title: Bagaimana Cara Mengintegrasikan Telegram
canonical_url: https://help-center.qontak.com/hc/id/articles/5555017491225-Bagaimana-Cara-Mengintegrasikan-Telegram
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- multi-channel-integration
- integrate-telegram
- conversation-management
query_examples:
- Cara Mengintegrasikan Telegram
- Bagaimana cara Mengintegrasikan Telegram?
- Langkah-langkah Mengintegrasikan Telegram di Qontak Omnichannel
- How do I Mengintegrasikan Telegram?
- Mau Mengintegrasikan Telegram, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengintegrasikan Telegram dengan Qontak Omnichannel, Anda memerlukan:

- **Role Admin** pada akun Qontak Omnichannel (hanya Admin yang dapat melakukan integrasi Telegram)
- **Akun Qontak Omnichannel** yang aktif
- **Token Telegram Bot** dari akun Telegram Anda
- Akses ke menu **Integrations** di Qontak Omnichannel

Perhatian: Pesan yang masuk dalam channel Telegram di Omnichannel hanya pesan yang dikirim melalui link, bukan melalui nomor telepon.

## Steps  <!-- confidence:high ✓ -->


**Integrations** merupakan sebuah fitur Omnichannel Qontak di mana para customer bisa menghubungkan berbagai platform dengan _chat panel_ seperti email atau Telegram.
**Penting**  
Hanya pengguna dengan**role Admin yang dapat melakukan integrasi**. Apabila Anda tidak memiliki akun dengan _role_ Admin, Anda dapat menghubungi tim support kami di 
Perlu diketahui bahwa pesan yang masuk dalam telegram _channel_ pada Omnichannel hanya pesan yang masuk melalui _link_ bukan melalui _phone number_. Untuk mengintegrasikan _chat panel_ dengan Telegram pada Web, Anda perlu mengikuti langkah-langkah berikut:
  1. Masuk ke akun Omnichannel Anda.
  2. Berikut merupakan tampilan web yang muncul setelah anda mengklik menu**Integrations**.  
![1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50699258760985)
  3. Klik **“Add Telegram Channel”** untuk menyambungkan akun Telegram yang akan diintegrasikan.  
![telegram.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774916307737)
Pada bagian kanan _form_ integrasi Telegram terdapat tata cara mengintegrasikan Telegram dan siapa saja yang bisa menggunakan fitur tersebut.
Yang bisa menggunakan fitur integrasi Telegram adalah:
    1. Hanya **Admin** yang dapat mengintegrasikan Telegram.
    2. **Admin, Supervisor** dan **Agen** dapat menggunakannya di Inbox.
Sedangkan cara mengintegrasikan Telegram adalah sebagai berikut:
    1. Untuk membuat akses token dan memulai integrasi, Anda perlu membuka Telegram.
    2. Temukan pengguna dengan nama @botfather dan mulailah mengobrol dengannya.
    3. Pilih perintah /**newbot** untuk membuat bot baru untuk mengobrol dengan @botfather dan ikuti instruksi untuk membuat bot baru.
    4. Setelah selesai, Anda akan menerima kunci API HTTP. Salin dan masukkan pada _field_ Token Akses Telegram.
Anda harus memiliki token akses untuk menghubungkan bot Telegram. Sedangkan untuk membuat bot baru Anda bisa lihat pada halaman “
  4. Pada Chat Panel, Masukkan token Telegram Anda, kemudian klik “**Install** ” untuk mengintegrasikan Telegram.  
![telegram2.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774892739225)
  5. Jika token ditemukan maka otomatis _pop up_ akan menampilkan _success_ dan jika tidak maka _pop up_ akan menampilkan _error_ sebagai berikut.  
![telegram3.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774892739865)
  6. Klik “**Settings** ” pada nama Telegram untuk melihat detail informasi Telegram Anda.  
![telegram4.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774916312985)
  7. Anda bisa melihat detail info Telegram, tapi tidak bisa melakukan perubahan karena semua _field_ dalam kondisi **disable**.  
![telegram5.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774916315033)
  8. Anda bisa berhenti terintegrasi dengan Telegram dengan cara klik ikon **“Disconnect”** seperti gambar berikut.  
![telegram6.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774892745369)
  9. Pop up notification “**Are you sure?****Disconnecting this channel will also delete this channel** ” akan secara otomatis muncul jika Anda mengklik button “**Disconnect** ”, kemudian pilih “**Disconnect** ” jika Anda yakin untuk disconnect akun Telegram dan jika tidak maka klik tombol “**Cancel** ”.  
![telegram7.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774892747545)

## Error States  <!-- confidence:medium ~ -->

**Token Telegram tidak valid atau tidak ditemukan:**
- Pop-up notifikasi "error" akan muncul saat Anda mengklik tombol **Install**
- **Cara mengatasi:** Verifikasi bahwa token Telegram yang Anda masukkan benar. Token harus didapatkan dari Telegram BotFather. Periksa kembali token dan coba **Install** ulang.

**Akun Telegram tidak memiliki permission yang cukup:**
- Integrasi gagal dan error message muncul
- **Cara mengatasi:** Pastikan Anda memiliki akses admin di akun Telegram yang akan diintegrasikan.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika:

- Token Telegram sudah benar tetapi integrasi terus menampilkan error setelah beberapa kali percobaan
- Pesan dari Telegram tidak masuk ke chat panel setelah integrasi berhasil
- Anda tidak memiliki role Admin dan memerlukan bantuan untuk mengintegrasikan Telegram

**Kontak support:** support-qontak@mekari.com

**Informasi yang perlu disertakan:** Screenshot error message, token Telegram (jangan tampilkan secara lengkap), ID akun Qontak Omnichannel Anda.