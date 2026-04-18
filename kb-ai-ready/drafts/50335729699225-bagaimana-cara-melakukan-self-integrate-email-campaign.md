---
title: Bagaimana Cara Melakukan Self Integrate Email Campaign
canonical_url: https://help-center.qontak.com/hc/id/articles/50335729699225-Bagaimana-Cara-Melakukan-Self-Integrate-Email-Campaign
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
product_surface: mobile
language: id
intent_tags:
- email-campaign
- perform-self-integrate-email-campaign
- marketing-campaign-manage
query_examples:
- Cara Melakukan Self Integrate Email Campaign
- Bagaimana cara Melakukan Self Integrate Email Campaign?
- Langkah-langkah Melakukan Self Integrate Email Campaign di Qontak Omnichannel
- How do I Melakukan Self Integrate Email Campaign?
- Mau Melakukan Self Integrate Email Campaign, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Anda ingin melakukan self integrate email campaign di Mekari Qontak. Sebelum memulai, pastikan Anda memenuhi persyaratan berikut:

1. Langganan aktif paket Broadcast, Service Suite, Sales Suite, atau Qontak 360
2. Akses ke akun Qontak Omnichannel dengan peran Admin (hanya Admin yang dapat melakukan konfigurasi Email Campaign)
3. Subdomain eksklusif yang tidak digunakan pada layanan email lain
4. Akses ke domain manager (aplikasi eksternal tempat mengelola domain Anda)
5. Belum memiliki subdomain dan email sender yang terintegrasi dengan Qontak

## Steps  <!-- confidence:high ✓ -->


Sebelum menggunakan fitur [Email Campaign](https://help-center.qontak.com/hc/id/articles/47425969961625-Bagaimana-Cara-Membuat-Email-Campaign), Anda perlu mengintegrasikan **subdomain** dan membuat **email sender** terlebih dahulu melalui halaman **Integrations** Mekari Qontak. Kini, Anda dapat melakukannya secara mandiri, tanpa bergantung pada tim Qontak untuk mendapatkan **DNS Records,** melakukan **verifikasi subdomain** , dan membuat**alamat email pengirim.**
Melalui halaman **Integrations** , Anda dapat:
  * **Menambahkan subdomain** yang ingin digunakan.
  * **Mendapatkan value DNS record** yang dibutuhkan untuk konfigurasi pada domain manager (_external app_) Anda.
  * **Melakukan verifikasi subdomain** setelah _record_ dikonfigurasi pada domain manager.
  * **Membuat alamat email pengirim (**_**email**_ _**sender**_**)** secara mandiri setelah subdomain berhasil diverifikasi.

**Penting**  
1. Anda hanya dapat mengintegrasikan 1 subdomain dengan 1 _email sender_ pada 1 akun Qontak.  
2. Anda **wajib** menggunakan **subdomain eksklusif** yang tidak digunakan pada layanan email lain, dikarenakan pengaturan DNS untuk email campaign membutuhkan **MX Record** , agar proses pengiriman dan penerimaan email tidak terganggu. Pelajari lebih lanjut [di sini](https://help-center.qontak.com/hc/id/articles/48958258449433-Bagaimana-Cara-Mengatur-DNS-Record#h_01K45AFS25QNZS92CB9TVQXDRW).  
3. Hanya user dengan _role_**Admin** yang dapat melakukan konfigurasi Email Campaign.
Dengan adanya _self-integration_ , aktivasi fitur dapat dilakukan kapan saja sesuai kebutuhan Anda. 
Pada penjelasan di bawah ini, kami akan memandu Anda mulai dari menambahkan **subdomain** hingga membuat _**email sender**_ baru.
### A. Cara Menambahkan dan Melakukan Verifikasi Subdomain[](https://help-center.qontak.com/hc/id/articles/50335729699225-Bagaimana-Cara-Melakukan-Self-Integrate-Email-Campaign#h_01K8N53HCNE7YN74NR3R1513C5)
  1. Masuk ke akun**Qontak Omnichannel** Anda. Kemudian pilih menu **“Integrations”**.
  2. Lalu klik submenu **“Email”,** lalu pilih**“Campaign”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982346649)
  3. Kemudian, Anda akan diarahkan ke halaman **Integrasi Email Campaign**. Klik tab **“Subdomain”** untuk melanjutkan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982348953)
- Jika Anda terdaftar sebagai _role_**Admin** , dan Anda belum memiliki **subdomain** dan **Email Sender** yang terintegrasi dengan Qontak**,** maka Anda akan melihat tampilan berikut pada halaman **Campaign > Email**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931941037593)  
- Anda dapat klik **“Connect subdomain”** untuk diarahkan ke halaman **Integrations** untuk menambahkan subdomain hingga membuat _email sender_ baru.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982360345)  
- Jika Anda terdaftar sebagai _role_**Supervisor** atau **Agent** , maka Anda akan melihat tampilan berikut dan Anda perlu menginformasikan ke _role_**Admin** yang terdaftar pada akun Qontak untuk melakukan integrasi Email Campaign.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982364313)
  4. Selanjutnya, klik **“Add subdomain”** untuk menambahkan subdomain yang akan digunakan untuk mengirimkan Email Campaign.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982364953)
  5. Lalu, akan muncul _pop up_ berikut. Isikan subdomain pada kolom yang tersedia. Kemudian klik **“Add”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982365849)
**Penting**  
Harap gunakan**subdomain khusus** untuk melakukan pengiriman _campaign_ melalui fitur Email Campaign Qontak. Pastikan subdomain tidak terhubung dengan layanan email lainnya, seperti Google, Outlook, dan mail service lainnya. 
  6. Setelah subdomain berhasil ditambahkan, sistem secara otomatis akan memberikan **5 (lima) value DNS Record** yang perlu Anda salin dan konfigurasikan pada aplikasi **Domain Manager** Anda.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982366873)
Pengaturan DNS Record diperlukan untuk memverifikasi kepemilikan subdomain, memastikan keamanan pengiriman, dan mencegah email ditandai sebagai _spam_. 
  7. Kemudian, buka situs penyedia domain tempat domain Anda terdaftar, dan cantumkan _value_ yang sudah disalin dari Qontak pada pengaturan DNS. Pelajari lebih lanjut terkait cara melakukan konfigurasi **DNS Records** pada **Domain Manager** [di sini](https://help-center.qontak.com/hc/id/articles/48958258449433-Bagaimana-Cara-Mengatur-DNS-Record#h_01K0BP5TAHX5K5RARZ700YP0KY).
- Pastikan data telah terisi dengan benar pada halaman Domain Manager Anda sebelum kembali ke menu Qontak untuk melakukan verifikasi subdomain.  
- Jika proses verifikasi ingin dilakukan nanti, Anda dapat klik **“Verify later”** untuk kembali ke halaman utama subdomain.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982367897)
  8. Setelah DNS records telah selesai dikonfigurasi, klik **“Verify subdomain”** untuk melakukan verifikasi.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931941044633)
**Penting**  
- Jika proses verifikasi gagal, Anda dapat klik **“Verify subdomain”** untuk melakukan verifikasi kembali setelah **5 menit** dari percobaan terakhir**.**  
- Jika hanya **sebagian** _value_ yang berhasil diverifikasi, Anda disarankan untuk memastikan kembali tidak ada _typo_ maupun kesalahan penginputan pada _domain manager_ Anda.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931941046425)  
- Apabila konfigurasi **DNS records** dipastikan sudah dilakukan dengan benar namun hasil verifikasi masih menunjukkan _**Unverified**_ , Anda dapat menunggu maksimal **2x24 jam** untuk melakukan verifikasi ulang. Kondisi ini dapat terjadi karena proses _propagate_ DNS Record dari _domain provider_ belum selesai. 
  9. Jika semua _value_ sudah berhasil diverifikasi, maka status **subdomain** Anda akan menjadi **Connected** , dan Anda dapat melanjutkan pembuatan **Email Sender** baru untuk mengirimkan Email Campaign melalui Qontak.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982371865)

### B. Cara Membatalkan dan Menghapus Integrasi Subdomain[](https://help-center.qontak.com/hc/id/articles/50335729699225-Bagaimana-Cara-Melakukan-Self-Integrate-Email-Campaign#h_01K8N5F0A213NDCHGWWPSBV4EN)
Anda dapat masuk ke halaman detail subdomain untuk membatalkan integrasi dan menghapus subdomain. Hal ini dapat dilakukan jika Anda ingin mengganti subdomain baru, atau ingin berhenti menggunakan fitur Email Campaign.
Jika Anda ingin **membatalkan integrasi** subdomain yang telah ditambahkan, Anda dapat melakukan **Cancel Integration**. Opsi ini tersedia untuk subdomain dengan status **Unverified.** Berikut langkahnya: 
  1. Masuk ke menu **Integrations** , lalu pilih sub menu **Email** dan klik tab **“Campaign”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931941049113)
  2. Kemudian klik nama **Subdomain** yang ingin Anda batalkan integrasinya.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931941049881)
  3. Lalu pada halaman _detail_ subdomain, klik **“Cancel integration”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931941050521)
  4. Kemudian, klik **“Cancel integration”** untuk konfirmasi pembatalan proses integrasi.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982376089)
  5. Maka, proses pembatalan sudah selesai dan sistem akan menghapus subdomain dan DNS records yang terhubung dengan akun Qontak Anda.

### D. Cara Mengubah Sender Name[](https://help-center.qontak.com/hc/id/articles/50335729699225-Bagaimana-Cara-Melakukan-Self-Integrate-Email-Campaign#h_01K8N5JKJ3DZKX1TMNHD0M1C8G)
Anda dapat mengubah **Sender name** jika Anda ingin menggunakan nama baru sebagai pengirim email. Berikut langkahnya:
  1. Masuk ke menu **Integrations** , lalu pilih sub menu **Email** dan klik tab **“Campaign”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982397977)
  2. Kemudian klik tab **“Sender”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982399385)
  3. Lalu, klik **“Actions”** dan pilih **“Edit”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931941080729)
  4. Maka akan muncul _pop up_ berikut. Ubah nama pengirim sesuai dengan keinginan Anda. Lalu klik **“Save changes”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982401689)
  5. Perubahan nama ini hanya berlaku untuk pembuatan _campaign_ berikutnya.

### E. Cara Menghapus Email Sender[](https://help-center.qontak.com/hc/id/articles/50335729699225-Bagaimana-Cara-Melakukan-Self-Integrate-Email-Campaign#h_01K8N5NNBVHEWQ9CGM5W3JNMXN)
Anda dapat menghapus Email Sender jika ingin menggunakan alamat email lain sebagai email pengirim, atau ingin berhenti menggunakan fitur Email Campaign. Berikut langkahnya:
  1. Masuk ke menu **Integrations** , lalu pilih sub menu **Email** dan klik tab **“Campaign”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982403097)
  2. Kemudian klik tab **“Sender”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982406041)
  3. Lalu klik **“Actions”** , dan pilih **“Delete”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931941093529)
  4. Maka akan muncul _pop up_ berikut. Lalu klik **“Delete”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F51931982411417)
Anda tidak dapat menghapus **email sender** jika ada proses pengiriman campaign yang sedang berlangsung.
  5. Jika _email sender_ telah dihapus, Anda masih dapat mengakses riwayat pengiriman _campaign_ pada menu [Email Campaign](https://chat.qontak.com/campaign/email).

## Error States  <!-- confidence:medium ~ -->

**Verifikasi DNS gagal:**
Jika tombol Verify menampilkan status gagal, pastikan:
- Semua DNS Records (MX Record, CNAME, SPF, DKIM) telah dikonfigurasi dengan benar pada domain manager
- Nilai DNS Records yang dimasukkan sama persis dengan yang ditampilkan di Qontak (termasuk titik akhir)
- Propagasi DNS telah selesai (dapat memakan waktu hingga 48 jam)
- Tunggu beberapa saat, lalu coba verifikasi kembali

**Subdomain tidak dapat ditambahkan:**
Pastikan subdomain yang digunakan bersifat eksklusif dan tidak digunakan pada layanan email lain. Satu akun Qontak hanya dapat mengintegrasikan 1 subdomain dengan 1 email sender.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim dukungan Qontak jika:

1. Status verifikasi subdomain tetap gagal setelah 48 jam dan semua DNS Records sudah dikonfigurasi dengan benar
2. Pesan error spesifik muncul saat menambahkan atau memverifikasi subdomain
3. Anda tidak dapat mengakses tab Integrations atau Email Campaign
4. Subdomain yang diverifikasi tidak muncul di halaman Email Campaign

Siapkan informasi berikut saat menghubungi support:
- Screenshot halaman Integrations Email Campaign menunjukkan status subdomain
- Nama subdomain yang ditambahkan
- Nama penyedia domain (domain manager)
- ID akun Qontak Anda