---
title: Bagaimana Cara Self Integration Tokopedia Chat
canonical_url: https://help-center.qontak.com/hc/id/articles/16320068291353-Bagaimana-Cara-Self-Integration-Tokopedia-Chat
article_type: task
solvability_type: tool
products:
- Qontak CRM
- Qontak Omnichannel
product_surface: mobile
language: id
intent_tags:
- multi-channel-integration
- conversation-management
query_examples:
- Cara Self Integration Tokopedia Chat
- Bagaimana cara Self Integration Tokopedia Chat?
- Langkah-langkah Self Integration Tokopedia Chat di Qontak CRM
- How do I Self Integration Tokopedia Chat?
- Mau Self Integration Tokopedia Chat, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk melakukan Self Integration Tokopedia Chat di Qontak Omnichannel, Anda memerlukan:

- Role Admin di akun Qontak Omnichannel
- Akun Seller aktif di Tokopedia
- Akses ke halaman App Management Tokopedia Developer Console
- Developer Console Tokopedia yang sudah terdaftar dan diapprove oleh pihak Tokopedia (proses persetujuan maksimal 3x24 jam)
- API Credential dari Tokopedia Developer Console
- Akses ke menu Integration > submenu Tokopedia di Qontak Omnichannel

## Steps  <!-- confidence:medium ~ -->


Pada Qontak Omnichannel, Anda dapat melakukan **Self Integration** dan **[Request Integration](https://help-center.qontak.com/hc/id/articles/16319836304793) **dengan Tokopedia Chat. Self Integration merupakan proses integrasi mandiri yang memerlukan Anda untuk membuat Developer Console terlebih dahulu pada Tokopedia.
**Penting  
** Sebelum melakukan Self integration, Anda perlu mengakses halaman App Management Tokopedia Developer Anda untuk mendapatkan API Credential. Klik**“Book consultation”** pada **submenu Tokopedia** di**menu Integration** untuk mengaktifkan integrasi chat Tokopedia dan mendapatkan bimbingan langsung dari kami.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Flh6.googleusercontent.com%2Fe58PbIV6HTPCJrNRUt_d_t0MQ5vKRLJ29BZBUUcap51hCMYRevCPLTlW-dQs3bIeTFwKf5s6U1___ybRDVcxyl7YKSBrIujTZ-QiQkqf9PCzx2qa77mb6Q01LteObkB9INo5_4suaLwWlMPmnrMYEWk)
Sebelumnya Anda dapat mempelajari tentang:  
[**[Fitur] Integrasi Tokopedia dan Chatpanel untuk Permudah Kelola Pesan Pelanggan**](https://qontak.com/fitur/integrasi-tokopedia/?utm_source=ecosystem&utm_medium=qontak+%28help+center%29)
Berikut adalah caranya:
### A. Cara membuat Tokopedia Developer Console[](https://help-center.qontak.com/hc/id/articles/16320068291353-Bagaimana-Cara-Self-Integration-Tokopedia-Chat#h_01HEQ2B7EBCH3VQHBV776P83XH)
  1. Masuk ke akun seller Tokopedia Anda   
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Flh6.googleusercontent.com%2FfFJpkoFqGISGZw4qBfmGrD2233IJMxZkSq7LClmXrshV9wjEX_h-p_JWKM6HujtqmRuSfI_qI745lkut0h1mgRMTmSyttXjJ-YKo6IW9FvW3WwsILqVx8cZLtAUquKpXTKP0VPz4c1OPYPPtZcYW1lk)
  2. Maka, Anda akan diarahkan untuk membuat
  3. Anda dapat mengisi kolom-kolom berikut.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Flh3.googleusercontent.com%2FESi5-2skNl9Pj5fu5Z_mXHAssv8X9bAUS74VeylqN_2T0Meb2KxS0UMW8xPPsGx8KgPBVqgWqTDEDpjC3RxM5X6skDCDvy6dM24asfwnc4T5dVRMJY1QDb3vDwchR7LeFNqw8vFmVsLwkBepRW50WTo)  
**Keterangan:**  
**No.** | **Nama kolom** | **Deskripsi**  
---|---|---  
1 | Company name | Isikan nama perusahaan Anda.  
2 | PIC Contacts name | Isikan nama orang yang dapat dihubungi nantinya.  
3 | Contacts number | Isikan nomor telepon orang yang dapat dihubungi nantinya.  
4 | Business Registration Certificate (SIUP) |  Unggah SIUP (Surat Izin Usaha Perdagangan) di sini. File harus dalam bentuk PDF yang berukuran tidak lebih dari 2MB.  
5 | Company profile |  Anda dapat unggah SIUP (Surat Izin Usaha Perdagangan) atau NIB (nomor Induk Berusaha) di sini. File harus dalam bentuk PDF yang berukuran tidak lebih dari 2MB.  
6 | Company website URL | Isikan alamat website perusahaan Anda.  
7 | Type of member | Pilih **Seller.**  
8 | System | Pilih **InHouse.**  
  4. Kemudian, Anda dapat menunggu maksimal 3x24 jam untuk dikirimnya approval dari tim Tokopedia ke email user sesuai email yang terdaftar dan digunakan di Tokopedia Developer Console.
  5. Jika akun Developer Console Anda sudah di _approve_ oleh pihak Tokopedia, maka Anda dapat lanjut ke proses selanjutnya.

### B. Cara Self Integration Tokopedia Chat[](https://help-center.qontak.com/hc/id/articles/16320068291353-Bagaimana-Cara-Self-Integration-Tokopedia-Chat#h_01HEQ2B7EBFYCWCY8MZ39B5F8C)
  1. Masuk ke akun Tokopedia Developer Anda atau **App Management.**  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Flh4.googleusercontent.com%2FZ56tzrEZOaVVQ7xS9Ez1jg4vh1y7yanMtrefHP8VMpNEE8gn8_EikJH-6w9qwlSJRXqYEhW2PuzXslnuAlSLsaopmVI0aO7NaRz26607SD3sUDrILTryEYxO_CH1qHYplcNTNcwzmuyU35H4d3KTUOo)
  2. Pada App Management, Anda akan melihat Live Apps. Klik pada **nama perusahaan Anda** dan pilih**Authentication Management.**  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Flh3.googleusercontent.com%2FkHQxGLl6YPdr4Gujoo8yaSWlGRde6WO3SGNhXu6c3Bglo-W-HHXIR4vz5nRyuPGmvKhSvMgxj7Q2sTLZJbJMswqBObHYpscCpe1h4q7tv08ShqL85t3cRmpWsVvYwhXpqOOxuGezdFvTa4XMH4IprLE)
  3. Pada halaman Authentication Management, simpan atau salin **App ID** dan**Client ID** Anda. Khusus untuk**Client Secret** , klik **“View”** untuk melihatnya, dan simpan atau salin credential tersebut.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Flh3.googleusercontent.com%2FwBveHg2m_RF2jHt1Y6iPh7fNr4UdxHxWrUFIIz1adYqTc8Tm3Mikj2EDy-EzDScWE6uIjRRrtnq9YXiu2JG80jweFVlFdXPOHUcbtHWBjyJPkNtRDFwEegH_mgWx13xCercQNv39YkhzfbJVb6dswlI)
  4. Jika Anda sudah menyimpan atau menyalin API credentials tersebut. Masuk ke akun Qontak Anda pada tab lain.
  5. Pada menu [**Channel integration**](https://help-center.qontak.com/hc/id/articles/5502818875289), pilih **E-commerce.****  
**![1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49067876049945)
  6. Kemudian, klik**“Book consultation”** untuk dihubungi oleh tim support kami secepatnya.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Flh6.googleusercontent.com%2Fe58PbIV6HTPCJrNRUt_d_t0MQ5vKRLJ29BZBUUcap51hCMYRevCPLTlW-dQs3bIeTFwKf5s6U1___ybRDVcxyl7YKSBrIujTZ-QiQkqf9PCzx2qa77mb6Q01LteObkB9INo5_4suaLwWlMPmnrMYEWk)
  7. Jika submenu Tokopedia sudah aktif, maka akan muncul tombol **Add store** , dan Anda dapat klik **“Self integration”****  
**.![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Flh6.googleusercontent.com%2FOLlwpdMD5Mu5qAh4frCJAsZIpusFScPM1JQGcXwoFIP5IAFb1rjlaeavBbKi7iu6YEgwdsZUpmKQIoN4aGN2X9QPB2juKWFXeWOBUfYRfCEb8oomSTtK6H7SZpWd4rCA2b6jRjyBll5T-EWIgSxorLs)
  8. Kemudian, Anda akan diarahkan ke halaman berikut.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Flh5.googleusercontent.com%2FJH0yxFG2jeEYJ1IHzDcPaZnmEwRqSMxCnXR785GrvikB98TjYmOkYzOFBkudqUjnawAqu2ySUvgXnqhnaYUqge0sqJ4Aj9l0oGEm2b5yQmOTTUKzYQlgcbhNX73l_d1d5ltTpKhWNPA9lsC7J-auPj8)  
**Keterangan:**  
**No.** | **Nama Kolom** | **Deskripsi**  
---|---|---  
1 | Store name | Isikan nama toko di Tokopedia Anda.  
2 | Store ID |  Isikan dengan link toko anda seperti contoh (_nama toko Anda_). Domain toko dapat diambil dengan login ke akun Tokopedia Anda > Klik **“Toko saya”** di ujung kanan atas profile Anda > Anda akan diarahkan ke toko Anda dan domain tersebut merupakan link domain toko Anda.   
3 | Store type | Pilih tipe yang sesuai pada toko Anda di Tokopedia.  
4 | Store domain |  Isikan dengan link toko anda seperti contoh (_nama toko Anda_). Domain toko dapat diambil dengan login ke akun Tokopedia Anda > Klik **“Toko saya”** di ujung kanan atas profile Anda > Anda akan diarahkan ke toko Anda dan domain tersebut merupakan link domain toko Anda.   
5 | FS ID | Isikan App ID sesuai pada halaman Authentication management Tokopedia yang telah Anda salin.  
6 | Client ID | Isikan Client ID sesuai pada halaman Authentication management Tokopedia yang telah Anda salin.  
7 | Client Secret | Isikan Client Secret sesuai pada halaman Authentication management Tokopedia yang telah Anda salin.  
  9. Setelah Anda selesai mengisi detail informasi di atas, klik **“Connect”.**
  10. Maka, proses integrasi Tokopedia dengan Qontak Omnichannel Anda telah berhasil terhubung dengan status **Connected.**  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Flh3.googleusercontent.com%2FqISGiR_CC5eM4QExywq-ZJRKnG0_otMD8vRA8mUgR6tJU0T9g6foaikHTmqmJnR43RIBOmlJ79J3yISAzLb7TfJQJtW5jUJLDDwzqMjVY3cjhs__BWPSGp91Tp8KruEUymdYgRblsPopQOgjmgLqHP0)

Setelah proses integrasi selesai, User harus mengaktifkan "Layanan Pihak Ketiga" melalui link berikut 
Demikian adalah cara Self Integration Tokopedia Chat.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support jika Anda mengalami:

- Developer Console Tokopedia tidak mendapat approval setelah 3x24 jam
- API Credential tidak diterima sistem Qontak Omnichannel
- Integrasi Tokopedia Chat gagal setelah mengikuti semua langkah
- Pesan pelanggan tidak masuk ke Chatpanel meskipun integrasi menunjukkan status Connected

Siapkan informasi berikut saat menghubungi support:
- Screenshot menu Integration > Tokopedia di Qontak Omnichannel
- Email terdaftar di Tokopedia Developer Console
- Nama Seller Shop Tokopedia Anda
- Pesan error lengkap (jika ada)