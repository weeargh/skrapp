---
title: Bagaimana Cara Mengintegrasikan Line Messenger
canonical_url: https://help-center.qontak.com/hc/id/articles/5642104351513-Bagaimana-Cara-Mengintegrasikan-Line-Messenger
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- multi-channel-integration
- integrate-line-messenger
- conversation-management
query_examples:
- Cara Mengintegrasikan Line Messenger
- Bagaimana cara Mengintegrasikan Line Messenger?
- Langkah-langkah Mengintegrasikan Line Messenger di Qontak Omnichannel
- How do I Mengintegrasikan Line Messenger?
- Mau Mengintegrasikan Line Messenger, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengintegrasikan Line Messenger dengan Qontak Omnichannel, Anda memerlukan:

1. **Role Admin** di akun Qontak Omnichannel — hanya pengguna dengan role Admin yang dapat melakukan integrasi
2. **Akun Qontak Omnichannel** yang aktif
3. **Akun Line Messenger** yang sudah aktif
4. **Line Channel Token** — token yang diperlukan untuk menghubungkan akun Line dengan Qontak
5. Akses ke menu **Integrations** di Qontak Omnichannel

Jika Anda tidak memiliki role Admin, hubungi tim support kami di support-qontak@mekari.com.

## Steps  <!-- confidence:high ✓ -->


**Integrations** merupakan sebuah fitur Omnichannel Qontak dimana para customer bisa menghubungkan berbagai platform dengan chat panel seperti email atau Instagram.
**Penting**  
Hanya pengguna dengan**role Admin yang dapat melakukan integrasi**. Apabila Anda tidak memiliki akun dengan role Admin, Anda dapat menghubungi tim support kami di 
Untuk mengintegrasikan chat panel dengan Line Messenger pada Web, Anda perlu mengikuti langkah-langkah berikut:
  1. Masuk ke akun Omnichannel Anda. 
  2. Masuk ke Menu**Integrations,** lalu pilih **Line Messenger.  
![10.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50771100808473)  
**
  3. Klik “**Add Line Account** ” untuk menyambungkan akun Line yang akan diintegrasikan.  
![line.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36775773552409)
Pada bagian kanan form integrasi Line Messenger terdapat tata cara mengintegrasikan Line dan siapa saja yang bisa menggunakan fitur tersebut.
Yang bisa menggunakan fitur integrasi Line Messenger adalah:
    1. Hanya **Admin** yang dapat mengintegrasikan Line Messenger.
    2. **Admin, Supervisor,** dan**Agen** dapat menggunakannya di Inbox.
Sedangkan, cara mengintegrasikan Line Messenger adalah sebagai berikut:
    1. Pastikan Anda memiliki akun resmi. Anda dapat membuat akun resmi di Line Official Account Manager.
    2. Siapkan akun resmi Anda untuk menggunakan API pesan di Line Official Account Manager ->Settings -> Messaging API -> Use Messaging API. Anda akan diminta untuk menambahkan provider and channel.
    3. Atur mode respons Anda ke Line Official Account Manager -> Settings -> Response Settings -> Response Mode.
    4. Isi **channel secret** Anda. Anda dapat menemukan rahasia saluran Anda di Line Developer Console -> Basic Settings -> Channel secret.
    5. Isi **channel access token** Anda. Anda dapat menemukan token akses Anda di Line Developer Console -> Messaging API -> Channel access token. Klik issue untuk mendapatkan token akses saluran Anda.
    6. Klik **install**.
    7. Setelah saluran Anda berhasil ditambahkan di Chat Panel, pastikan Anda mengaktifkan **Use Webhook** di Line Developer Console -> Messaging API -> Webhook Settings.
  4. Pada Chat Panel, Masukkan token Line Anda, kemudian klik “**Install** ” untuk mengintegrasikan Line.  
![line1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36775773557273)
_Field_ yang kosong akan manampilkan error “**field is required** ” saat Anda mengklik “**Install** ”.
  5. Jika token ditemukan maka otomatis popup akan manampilkan _success_ dan jika tidak maka _popup_ akan menampilkan _error_ sebagai berikut.  
![line2.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36775773559321)
  6. Klik “**Settings** ” pada nama Line untuk melihat _detail_ informasi Line Messenger Anda.  
![line3.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36775763602457)
  7. Anda bisa melihat detail info Line Anda, tapi tidak bisa melakukan perubahan pada channel name dan channel secret karena _field_ dalam kondisi _disable_.  
![line4.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36775763599001)
  8. Anda bisa berhenti terintegrasi dengan Line Messenger dengan cara mengklik ikon “**Disconnect** ” seperti gambar berikut.  
![line5.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36775773562521)
  9. Pop-up notification “**Are you sure?****Disconnecting this channel will also delete this channel** ” akan secara otomatis muncul jika Anda klik “**Disconnect** ”, kemudian pilih “**Disconnect** ” jika Anda yakin untuk _disconnect_ akun Line Messenger dan jika tidak maka klik “**Cancel** ”.  
![line6.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36775763600665)

## Error States  <!-- confidence:medium ~ -->

**Error yang dapat terjadi:**

1. **"Field is required"** — Muncul saat Anda mengklik tombol **Install** tanpa mengisi Line Channel Token. Solusi: Pastikan Line Channel Token sudah dimasukkan dengan benar di Chat Panel sebelum mengklik **Install**.
2. **Error message pada popup** — Token Line yang Anda masukkan tidak valid atau tidak sesuai. Solusi: Verifikasi kembali Line Channel Token Anda dan pastikan Anda menggunakan token yang benar dari akun Line Anda.
3. **Integrasi gagal** — Jika sistem tidak dapat mendeteksi token. Hubungi support-qontak@mekari.com dengan screenshot error dan Channel Token ID Anda.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak di **support-qontak@mekari.com** jika Anda mengalami:

1. Pesan error yang persisten saat mengklik tombol **Install**
2. Token Line diterima tetapi integrasi tetap gagal
3. Tidak dapat mengakses menu **Integrations** (kemungkinan masalah permission/role)
4. Channel Line sudah terintegrasi tetapi pesan tidak masuk ke Inbox

Sertakan dalam laporan:
- Screenshot pesan error lengkap
- Line Channel ID/Account ID
- Email akun Qontak Omnichannel Anda
- Waktu saat error terjadi