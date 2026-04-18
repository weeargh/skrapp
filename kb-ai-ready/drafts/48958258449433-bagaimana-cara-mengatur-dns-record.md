---
title: Bagaimana Cara Mengatur DNS Record
canonical_url: https://help-center.qontak.com/hc/id/articles/48958258449433-Bagaimana-Cara-Mengatur-DNS-Record
article_type: task
solvability_type: tool
products:
- Qontak CRM
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- email-campaign
- configure-dns-record
- marketing-campaign-manage
query_examples:
- Cara Mengatur DNS Record
- Bagaimana cara Mengatur DNS Record?
- Langkah-langkah Mengatur DNS Record di Qontak CRM
- How do I Mengatur DNS Record?
- Mau Mengatur DNS Record, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengatur DNS Record guna mendukung fitur Email Campaign, Anda memerlukan:

1. Langganan aktif ke paket Broadcast, Service Suite, Sales Suite, atau Qontak 360
2. Akses ke akun Qontak Omnichannel dengan peran Campaign management
3. Subdomain yang belum digunakan pada layanan email lain
4. Akses ke Domain Manager penyedia domain Anda
5. Email untuk menerima informasi DNS Records dari tim Qontak

Subdomain harus eksklusif untuk pengiriman campaign melalui Qontak dan tidak boleh digunakan untuk kebutuhan lain.

## Steps  <!-- confidence:high ✓ -->


Prosedur pengajuan pendaftaran subdomain dan pembuatan email pengirim **di bawah ini** dapat Anda ikuti hingga fitur **self-integration** tersedia. Qontak akan merilis fitur **self-integration** secara bertahap dari **awal November 2025**.
Untuk menggunakan fitur [Email Campaign](https://help-center.qontak.com/hc/id/articles/47425969961625-Bagaimana-Cara-Membuat-Email-Campaign), Anda perlu melakukan langkah berikut:
  1. Pastikan Anda memiliki **subdomain** yang belum digunakan pada _mail service_ lain, dan akses ke **Domain Manager**.
Subdomain yang digunakan pada fitur **Email Campaign** dihimbau untuk tidak digabungkan dengan kebutuhan lain. Oleh karena itu, Anda disarankan menggunakan subdomain yang eksklusif untuk kepentingan pengiriman _campaign_ melalui Qontak saja.
  2. Pada kolom **Company Sub-domain** , isi nama **subdomain** yang ingin digunakan. Lalu pada kolom **Email** , isi **email pengirim** yang ingin dibuat untuk melakukan pengiriman _campaign_.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50344321699481)  
**Contoh:**  
**Company subdomain** : mail.mekari.com  
**Email:** noreply@mail.mekari.com  
*Pastikan informasi yang Anda isi pada kolom ‘**Company Sub-domain** ’ dan **‘Email’** memiliki nama subdomain yang sama. Jika berbeda, kami akan mendaftarkan subdomain sesuai pada kolom '**Company Sub-domain'**.

**Penting**  
- Email pengirim (atau email sender) yang didaftarkan merupakan jenis email yang diperuntukkan untuk outbound messaging, dan tidak dapat menerima balasan email (incoming email).  
- **Tips** : Anda dapat menggunakan **noreply** (contoh: **noreply@mail.mekari.com**) sebagai _username_ email, atau menambahkan informasi pada konten _campaign_ Anda agar customer Anda dapat membalas pesan ke alamat email yang tepat.
  3. Centang _**consent**_ di bawah dan klik **Daftarkan sekarang** untuk mengirimkan _request_. _Consent_ ini bersifat **wajib** untuk melakukan pendaftaran. Dengan mencentang, nama alamat email Anda akan kami simpan, untuk kebutuhan pengiriman informasi DNS records kepada Anda, yang selanjutnya dapat Anda daftarkan ke **Domain Manager** Anda.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50344540069401)
Informasi DNS Records akan diberikan tim Qontak via **email** dalam **1x24 jam (hari kerja)** , setelah Anda mengisi informasi**Company Sub-domain** dan **Email** pada _form_ di atas. Silakan cek email yang Anda pakai untuk login ketika melakukan pendaftaran.

###  **A.****Tentang Subdomain** [](https://help-center.qontak.com/hc/id/articles/48958258449433-Bagaimana-Cara-Mengatur-DNS-Record#h_01K0BP5TAHBDEJAZR0KTBD97BS)
Subdomain merupakan bagian dari domain yang muncul sebelum domain utama dan ekstensi domain. Contohnya mail.mekari.com, **mail** pada alamat “**mail**.mekari.com” adalah subdomain. 
Untuk mendaftarkan **subdomain** , Anda perlu memiliki domain terlebih dahulu. Lalu, pada halaman DNS Editor, Anda dapat mengisi **Host/Name** yang berisi nama subdomain pada kolom **Name** ketika mengisi value DNS Records, baik untuk tipe MX record, TXT, dan lainnya. Value DNS Records ini akan diberikan oleh tim Qontak setelah Anda mengisi _form_ pendaftaran di atas.
###  **B. Mengapa kita perlu mengatur DNS Record?**[](https://help-center.qontak.com/hc/id/articles/48958258449433-Bagaimana-Cara-Mengatur-DNS-Record#h_01K45A9PJ0KY9VNFMTBE897VD1)
Sebelum **mendaftarkan alamat pengirim email (**_**email sender**_**)** , pemilik domain perlu mendaftarkan **DNS Record** yang bertujuan untuk menentukan tujuan pengiriman email, memverifikasi identitas pengirim, dan memastikan pengiriman email yang aman. Tanpa **DNS Record** yang tepat, email mungkin tidak terkirim dengan benar atau dapat ditandai sebagai spam.
###  **C. Cara Menambahkan DNS Record**[](https://help-center.qontak.com/hc/id/articles/48958258449433-Bagaimana-Cara-Mengatur-DNS-Record#h_01K0BP5TAHX5K5RARZ700YP0KY)
Selain menjual domain, beberapa penyedia domain seperti **GoDaddy** , **Hostinger (NiagaHoster)** ,**NameCheap** , dan lainnya memiliki akses **Domain Manager**. Melalui domain manager, Anda dapat:
  * Mendaftarkan **subdomain**.
  * Mengelola **DNS Record** melalui **DNS Editor**.

Jika penyedia **domain** Anda tidak memiliki **Domain Manager** , Anda dapat menggunakan _domain hosting_ lain yang memberikan akses untuk mengelola **DNS Record**. Di bawah ini merupakan beberapa contoh tampilan **DNS Editor** dari beberapa penyedia domain.
**A. cPanel**
  1. Masuk ke akun **cPanel** Anda.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50344540070169)
  2. Pilih menu **Zone Editor**.  
**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50344540075289)**
  3. Pilih nama **domain** Anda, lalu klik **“Manage”**.  
**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50344553181209)**
  4. Klik **“+Add Record”** , lalu isi kolom sesuai dengan _**records**_ yang Qontak berikan.  
Konfigurasi DNS record untuk**subdomain** ditandai dari kolom **‘Name’** dimana Anda dapat langsung mengisi **Host/Name** yang berisi nama subdomain Anda.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50344553182617)
Anda akan menerima **Value** dari **DNS Record** yang dikirimkan oleh tim kami melalui **email**. Dalam hal ini, Anda **wajib** mendaftarkan **5 (lima) value** di bawah ini ke **Domain Manager**. Contoh **Host/Name** di bawah telah mengandung nama **subdomain** yaitu **‘bd’.**  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50344553184281)
  5. Ulangi langkah di atas hingga semua _records_ telah ditambahkan. 
  6. Klik **Save Record** untuk menyimpan _record_ per baris, atau Anda dapat klik **Save All Records** untuk menyimpan semua sekaligus.

###  **D. Verifikasi Subdomain dan Membuat Email Sender**[](https://help-center.qontak.com/hc/id/articles/48958258449433-Bagaimana-Cara-Mengatur-DNS-Record#h_01K0BPSJZTZ6W0C6116ZMWDX34)
Setelah pengaturan **DNS Record** selesai, mohon informasikan kepada tim Mekari Qontak dengan cara membalas email yang sebelumnya telah dikirimkan agar **subdomain Anda dapat diverifikasi oleh tim kami.**
Proses ini dapat memakan waktu hingga maksimal **2x24 jam** , tergantung status dari proses _propagate_**DNS Record** pada masing-masing **domain provide** r.
Setelah proses verifikasi berhasil, **email pengirim (**_**sender email**_**)** yang Anda _submit_ akan dibuat oleh sistem, dan Anda dapat menggunakan email tersebut untuk mengirimkan **email campaign** melalui Mekari Qontak.
Selanjutnya, Anda dapat mempelajari cara membuat [ Email Campaign](https://help-center.qontak.com/hc/id/articles/47425969961625-Bagaimana-Cara-Membuat-Email-Campaign), [Recipient List](http://help-center.qontak.com/hc/id/articles/47426266423065-Bagaimana-Cara-Membuat-Recipient-List-untuk-Email-Campaign), dan [Template untuk Email Campaign](https://help-center.qontak.com/hc/id/articles/47426448666521-Bagaimana-Cara-Membuat-Template-untuk-Email-Campaign) pada Mekari Qontak.

###  **E. Frequently Asked Questions (FAQs)**[](https://help-center.qontak.com/hc/id/articles/48958258449433-Bagaimana-Cara-Mengatur-DNS-Record#h_01K45AFS25QNZS92CB9TVQXDRW)
  1. **Mengapa saya disarankan menggunakan subdomain eksklusif (bukan domain utama) untuk mengirim email campaign di Qontak?**  
Pengaturan DNS untuk **email campaign** membutuhkan **MX Record**. Walaupun **email campaign** hanya digunakan untuk mengirim email (tidak dapat menerima balasan), **MX Record** tetap wajib sesuai ketentuan penyedia layanan email kami.  
Jika domain utama digunakan untuk lebih dari satu layanan email, hal ini dapat mengganggu kelancaran penerimaan email masuk. Karena itu, kami menyarankan penggunaan **subdomain khusus** **yang tidak digabung dengan layanan email lain** , agar proses pengiriman dan penerimaan email tetap stabil.

1. **Apakah saya harus mengikuti aturan TTL (Time to Live) yang diberikan oleh Qontak?**  
Jika domain editor Anda memiliki _default_ nilai TTL, Anda dapat mengikuti konfigurasi yang telah ada. Namun, jika**domain editor** Anda tidak memiliki nilai tersebut, Anda dapat mengikuti nilai yang kami berikan, yaitu **3600**.

1. **Mengapa proses verifikasi gagal meskipun saya telah melakukan penambahan dan/atau perubahan DNS Record sesuai value yang diberikan oleh Qontak?**  
Jika Anda yakin **value** yang di-_setup_ telah sesuai dengan yang **value** yang diberikan, Anda dapat menunggu maksimal**2x24 jam** untuk melakukan verifikasi ulang. Kondisi ini dapat terjadi karena proses _propagate_ **DNS Record** dari _domain provider_ belum selesai.

1. **Mengapa proses verifikasi gagal meskipun saya sudah menambahkan atau mengubah DNS Record sesuai value dari Qontak?**  
Berikut beberapa kemungkinan **penyebab proses verifikasi gagal** :  
- **Value DNS belum sesuai** – pastikan **value** yang Anda masukkan sama persis dengan yang diberikan Qontak (tanpa tambahan spasi, titik, atau karakter lain).  
- **Propagasi DNS belum selesai** – meskipun **value** sudah benar, perubahan DNS biasanya membutuhkan waktu hingga**2x24 jam** untuk sepenuhnya aktif di semua _server_.  
- **Cache domain provider** – beberapa penyedia domain bisa menyimpan _cache_ sehingga perubahan tidak langsung terbaca.  
Jika **value** yang Anda isi sudah benar, silakan tunggu maksimal **2x24 jam** lalu lakukan verifikasi ulang.

1. **Mengapa value Host/Name yang saya isi di DNS Editor bisa duplikat?**  
Beberapa penyedia domain secara otomatis menambahkan nama **domain/subdomain** saat Anda mengisi **Host/Name**. Jika hal ini terjadi, Anda perlu menyesuaikan agar tidak tercatat sebagai duplikat.  
**Contoh:** Pada **Amazon Route 53** atau **cPanel** , nama subdomain akan terisi otomatis. Jadi, jika Qontak memberikan Host/Name seperti **aliyundm.bd** , **dmtrace.bd** , atau **dmarc.bd** , maka Anda hanya perlu mengisi **aliyundm** , **dmtrace** , atau **dmarc** saja, karena _value_**.bd** akan otomatis ditambahkan oleh **domain manager**.

## Error States  <!-- confidence:medium ~ -->

Subdomain dan email pengirim tidak cocok: Pastikan bagian subdomain sebelum domain utama (contoh: "mail" pada "mail.mekari.com") sama persis pada kolom "Company Sub-domain" dan bagian sebelum simbol @ pada kolom "Email". Jika berbeda, tim Qontak akan mendaftarkan sesuai kolom "Company Sub-domain".

Subdomain sudah digunakan: Pilih subdomain baru yang belum terdaftar di layanan email manapun.

Email tidak diterima: Periksa folder spam atau gunakan email alternatif yang Anda gunakan untuk login Qontak.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika:

1. DNS Records tidak diterima dalam 1x24 jam (hari kerja)
2. Mengalami kesulitan memasukkan DNS Records ke Domain Manager
3. Subdomain atau email pengirim tidak muncul di akun Qontak setelah pendaftaran
4. Menerima pesan error saat mengklik tombol "Daftarkan sekarang"

Siapkan informasi berikut saat menghubungi support: subdomain yang didaftarkan, email pengirim, nama penyedia domain, dan screenshot error jika ada.