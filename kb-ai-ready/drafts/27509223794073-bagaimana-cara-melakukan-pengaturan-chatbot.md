---
title: Bagaimana Cara Melakukan Pengaturan Chatbot
canonical_url: https://help-center.qontak.com/hc/id/articles/27509223794073-Bagaimana-Cara-Melakukan-Pengaturan-Chatbot
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- conversational-ai-chatbot
- perform-pengaturan-chatbot
- ai-chatbot-automation
query_examples:
- Cara Melakukan Pengaturan Chatbot
- Bagaimana cara Melakukan Pengaturan Chatbot?
- Langkah-langkah Melakukan Pengaturan Chatbot di Qontak Omnichannel
- How do I Melakukan Pengaturan Chatbot?
- Mau Melakukan Pengaturan Chatbot, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Sebelum melakukan pengaturan chatbot, pastikan Anda memiliki:

1. Akses ke Mekari Qontak Omnichannel atau Qontak Chat dengan izin manajemen chatbot
2. Fitur Chatbot sudah diaktifkan oleh tim support Qontak (hubungi support-qontak@mekari.com jika belum aktif)
3. Akses ke menu Chatbot Settings
4. Setidaknya satu percakapan chatbot sudah dibuat di menu Chatbot

## Steps  <!-- confidence:high ✓ -->


Anda dapat menggunakan fitur Chatbot pada Mekari Qontak Omnichannel. Fitur Chatbot dapat digunakan untuk merespon percakapan sederhana layaknya manusia, sehingga dapat mempermudah komunikasi dengan customer Anda. Fitur ini dapat Anda atur sesuai kebutuhan Anda melalui tab **Settings** pada Menu **Chabot**.
**Penting**  
Untuk mengaktifkan fitur chatbot, Anda dapat menghubungi tim support Qontak di 
Berikut adalah langkah - langkah mengelola pengaturan chatbot.
### A. AI Response[](https://help-center.qontak.com/hc/id/articles/27509223794073-Bagaimana-Cara-Melakukan-Pengaturan-Chatbot#h_01HKXVVB1Z5EG2225CNJR9RZE7)
Di sini, Anda dapat menyesuaikan alur respon untuk melanjutkan percakapan. Anda dapat menyerahkan ke agen atau melanjutkan percakapan ketika Anda mencapai 10 threshold.
  1. Masuk ke menu **Chatbot**.
  2. Lalu klik **Chatbot settings** dan pilih **AI Response.** Maka, Anda akan diarahkan ke halaman pengaturan berikut.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774150060057)  
**No.** | **Nama Pilihan** | **Deskripsi**  
---|---|---  
1 | Any available agent |  Menugaskan percakapan ke agen aktif yang ditentukan secara acak oleh sistem. Anda dapat menambahkan **Handover message** agar percakapan tidak terputus dan customer dapat menunggu agen.  
2 | Specific division |  Menugaskan percakapan ke agen yang berada di divisi tertentu. Jika memilih ini, Anda wajib **menentukan divisi** nya. Lalu, Anda dapat menambahkan **Handover message** agar percakapan tidak terputus dan customer dapat menunggu agen.  
3 | Specific agent |  Menugaskan percakapan ke agen tertentu. Jika memilih ini, Anda wajib **menentukan siapa agen** nya. Lalu, Anda dapat menambahkan **Handover message** agar percakapan tidak terputus dan customer dapat menunggu agen.  
  3. Pilih **“Save”** jika pengaturan sudah sesuai.

### B. Idle Action[](https://help-center.qontak.com/hc/id/articles/27509223794073-Bagaimana-Cara-Melakukan-Pengaturan-Chatbot#h_01HKXVVB1ZKFM7JQT6J6KY6HGP)
Dengan fitur ini, Anda dapat mengatur tindakan ketidakaktifan percakapan dengan customer dan menyesuaikan respons bot tertentu.
  1. Masuk ke menu **Chatbot**.
  2. Lalu klik **Chatbot settings** dan pilih **Idle Action.** Maka, Anda akan diarahkan ke halaman pengaturan berikut.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774173750297)  
**No.** | **Action** | **Deskripsi**  
---|---|---  
1 | None |  Tidak ada _Idle action._  
2 | Resolve conversation |  Selesaikan percakapan apabila sudah tidak ada respon atau aktivitas percakapan pada room chat. Anda dapat menentukan jumlah waktu dalam jam **_(hours)_** dan/atau menit **_(minutes)_** lamanya customer tidak membalas di kolom **Customer idle time.** Kemudian, lengkapi juga pesan penutup percakapan di kolom **Closing message.**  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774173754393)  
3 | Assign conversation |  Tugaskan agen apabila tidak ada respon atau aktivitas percakapan dalam room chat. Anda dapat menentukan jumlah waktu dalam jam **_(hours)_** dan/atau menit **_(minutes)_** lamanya customer tidak membalas di kolom **Customer idle time.** Lalu, tentukan bagaimana sistem menugaskan agen di bagian **Assign to,** dengan aturan seperti berikut:  
**- Auto:** Menugaskan percakapan ke agen aktif yang ditentukan secara acak oleh sistem.  
**- Division:** Menugaskan percakapan ke agen yang berada di divisi tertentu. Anda dapat memilih divisi tersebut.  
**- Agent:** Menugaskan percakapan ke agen tertentu. Anda dapat memilih agen tersebut. Kemudian, lengkapi juga pesan penutup percakapan di kolom **Closing message.**  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774173790873)  
  3. Pilih **“Save”** jika pengaturan sudah sesuai.

### C. API Integration[](https://help-center.qontak.com/hc/id/articles/27509223794073-Bagaimana-Cara-Melakukan-Pengaturan-Chatbot#h_01HKXVVB1Z602HH452K9K40Y11)
Fitur ini memungkinkan Anda menghubungkan sistem dengan chatbot via API sehingga memungkinkan bot dapat mengirimkan / mengambil / menyimpan / menanyakan data dari end user ke sistem klien.
  1. Masuk ke menu **Chatbot**.
  2. Lalu klik **Chatbot settings** dan pilih **API Integration.** Maka, Anda akan diarahkan ke halaman pengaturan berikut. Anda dapat membuat API Integration yang baru dengan klik tombol **“Add API connection”.**  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774173761305)

Anda bisa melihat daftar API Integration yang telah Anda buat di halaman ini. Selain itu, Anda dapat  
mengeditnya dengan klik ikon **“pensil”** atau menghapusnya dengan klik ikon **“tempat sampah”**.
  3. Maka, isi form API Connection pada kolom-kolom yang tersedia.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774173797401)  
**No.** | **Nama Kolom** | **Deskripsi**  
---|---|---  
1 | Connection name |  Anda **wajib** mengisi nama koneksi di sini.  Contoh: Qontak API.  
2 | Description |  Anda wajib mengisi kolom ini dengan deskripsi koneksi Anda.  Contoh: Untuk menghubungkan chatbot dengan sistem Qontak CRM.  
3 | Code |  Anda **wajib** mengisi kolom ini dengan kode koneksi Anda.  Contoh: QONTAK_CRM, JURNAL API.  
4 | Base URL |  Anda **wajib** mengisi kolom ini dengan URL dasar API Anda.  Contoh: https://api.jurnal.id  
5 | Settings | Anda dapat mengisi kolom ini dengan pengaturan autentikasi Anda seperti nama pengguna, kata sandi, dan lain sebagainya.  
Contoh: {"owner_email":"sandbox@qontak.com"}.  
6 | Headers |  Anda dapat mengisi kolom ini dengan payload Anda. Kami menyarankan masukan di header agar lebih lancar. Contoh: {"apikey":"xxxxxxxx"}  
7 | Token | Isi kolom ini dengan token API akun Anda. Kami menyarankan untuk membuatnya bertahan lama/selamanya untuk waktu token.  
Contoh: {"token_type":"bearer","access_token":"","expires_in"  
:,"refresh_token":"","created_at":}  
  4. Jika seluruh kolom terutama kolom-kolom wajib telah terisi dengan benar, klik **“Add”** untuk menambahkan API Connection.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774150069529)

### D. CRM Integration[](https://help-center.qontak.com/hc/id/articles/27509223794073-Bagaimana-Cara-Melakukan-Pengaturan-Chatbot#h_01HKXVVB206BK46Q23Q54QES99)
Untuk menggunakan fitur ini, Anda perlu mengaktifkan Qontak CRM terlebih dahulu dan mengkoneksikannya dengan Qontak Omnichannel Anda. Anda dapat mempelajari panduannya, [di sini.](https://help-center.qontak.com/hc/id/articles/5642795619737)
  1. Jika CRM sudah terkoneksi, maka Anda dapat masuk ke menu **Chatbot**.
  2. Lalu klik **Chatbot settings** dan pilih **CRM Integration.** Maka, Anda akan diarahkan ke halaman pengaturan berikut. Pada halaman ini, Anda dapat mengelola CRM integration yang telah tersambung.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774150081561)
  3. Anda dapat mengubah rincial integration dengan klik **“Action”** , lalu klik **Edit deal settings**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774173796121)

- Anda juga dapat menghapus CRM Integration yang telah tersambung dengan klik **Delete deal settings**.  
- Anda juga dapat mengakses sidebar deal settings Qontak CRM melalui [Bot response Chatbot Conversation.](https://help-center.qontak.com/hc/id/articles/12128813400857)
  4. Maka, muncul sidebar Edit deal settings seperti berikut.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774173802393)  
**No.** | **Nama Kolom/Tombol** | **Deskripsi**  
---|---|---  
1 | Deal setting | Klik untuk mengaktifkan dan klik kembali untuk menonaktifkan integration.  
2 | Pipeline | Klik untuk memilih pipeline (berdasarkan CRM) apa yang ingin diintegrasikan.  
3 | Stage | Klik untuk memilih stage (berdasarkan CRM) apa yang diintegrasikan.  
4 | Deal name | Isikan nama deal ini.  
5 | Owner | Pilih pemilik dari deal ini (berdasarkan CRM).  
6 | Source | Pilih dari mana asal transaksi ini.  
7 | Customer contact association | Centang untuk menyertakan informasi kontak pelanggan ke transaksi yang dibuat.  
  5. Klik **“Save changes”** untuk menyimpan perubahan.

Demikian cara mengatur percakapan chatbot. Temukan add-ons dan produk rekomendasi untukmu, .

## Error States  <!-- confidence:medium ~ -->

Tidak ada error yang didokumentasikan dalam artikel pengaturan chatbot. Jika pengaturan tidak tersimpan:

1. Pastikan semua field yang wajib (required) sudah diisi (misalnya divisi atau agen jika Anda memilih opsi Specific division atau Specific agent)
2. Pastikan koneksi internet stabil sebelum mengklik tombol Save
3. Refresh halaman dan coba kembali

## Escalation  <!-- confidence:high ✓ -->

Hubungi tim support Qontak di support-qontak@mekari.com jika mengalami masalah:

1. Fitur Chatbot tidak aktif di akun Anda
2. Menu Chatbot settings tidak muncul atau tidak dapat diakses
3. Pengaturan AI Response atau Idle Action tidak tersimpan meskipun sudah mengikuti langkah-langkah
4. Chatbot tidak merespons sesuai dengan pengaturan yang telah dikonfigurasi

Sertakan screenshot halaman error dan deskripsi masalah Anda.