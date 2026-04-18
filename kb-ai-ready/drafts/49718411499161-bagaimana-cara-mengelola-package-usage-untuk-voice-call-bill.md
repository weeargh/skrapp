---
title: Bagaimana Cara Mengelola Package Usage untuk Voice Call Billing
canonical_url: https://help-center.qontak.com/hc/id/articles/49718411499161-Bagaimana-Cara-Mengelola-Package-Usage-untuk-Voice-Call-Billing
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
- Bizphone
product_surface: web
language: id
intent_tags:
- platform
- manage-package-usage-untuk-voice-call
- general-platform
query_examples:
- Cara Mengelola Package Usage untuk Voice Call Billing
- Bagaimana cara Mengelola Package Usage untuk Voice Call Billing?
- Langkah-langkah Mengelola Package Usage untuk Voice Call Billing di Qontak Omnichannel
- How do I Mengelola Package Usage untuk Voice Call Billing?
- Mau Mengelola Package Usage untuk Voice Call Billing, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengelola Package Usage Voice Call Billing di Qontak Omnichannel, Anda membutuhkan:

- Akun Qontak Omnichannel aktif dengan akses Admin atau Supervisor
- Fitur WhatsApp Call telah diaktifkan (hubungi tim support kami di support-qontak@mekari.com untuk aktivasi)
- Paket berlangganan aktif dengan kuota Voice Balance
- Akses ke menu Package Usage di dashboard web Qontak Omnichannel
- Koneksi internet stabil

Catatan: Fitur WhatsApp Call masih dalam tahap Beta dan hanya akan muncul untuk pengguna yang telah mengaktifkannya.

## Steps  <!-- confidence:high ✓ -->


Saat ini, pada Package Usage terdapat pengelolaan Voice Call Billing dimana akan digunakan untuk percakapan yang bersifat **Voice** seperti **WhatsApp Call**. Pada penggunaannya, Anda perlu memperhatikan kuota saldo panggilan suara yang telah dilakukan. Berdasarkan hal tersebut, fitur WhatsApp Call akan mengurangi **Voice Balance** karena WhatsApp Call akan menjadi bagian dari **Panggilan Suara**.Berikut langkah-langkah dalam mengelola Package Usage tersebut.
**Penting****  
**- Fitur**WhatsApp Call** masih dalam **Tahap Beta**. Kemunculan saldo WhatsApp Call ini **tidak akan** mempengaruhi semua pengguna.  
- Fitur ini hanya akan mempengaruhi pengguna yang mengaktifkan fitur **WhatsApp Call**. Apabila Anda ingin mengaktifkan fitur tersebut, harap 
  1. Login ke akun Qontak Omnichannel Anda.
  2. Pilih menu **Package Usage** dan klik **Conversation**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49718550832537)
  3. Lalu Anda akan diarahkan ke halaman berikut. Apabila Anda mengaktifkan fitur **WhatsApp Call** , maka akan muncul kuota **Voice Balance** pada kolom **Package usage**. Klik **“ikon tanda tanya”** berikut untuk melihat _detail_ saldo.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49718550834969)
  4. Pada detail saldo dari **Voice balance** , Anda akan melihat **Initial balance** atau saldo awal, **Additional balance** atau saldo tambahan**,** dan **Total balance** atau akumulasi dari jumlah **Initial balance** dan **Additional balance**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F49718529960217)
  5. Berikut catatan **Harga & Potongan **dari penggunaan **WhatsApp Call** :
Potongan akan dihitung berdasarkan **Menit  
****Contoh kasus** : Panggilan **2 detik** → **Voice balance** Anda akan dipotong **1 menit**.  
Saat ini, kami hanya akan menjual berdasarkan harga menit. Terdapat 2 jenis panggilan:  
- Panggilan **Masuk** → Panggilan yang dimulai oleh Pelanggan.  
- Panggilan **Keluar** → Panggilan yang dimulai oleh Anda.  
**Harga:  
** - Panggilan **Masuk** dengan Nomor Indonesia: **Rp 0/menit  
** - Panggilan **Keluar** dengan Nomor Indonesia: **Rp 345.39/menit/menit**
  6. Untuk melakukan panggilan keluar, akan ada batas saldo. Jika Anda memiliki jumlah **Voice balance** di bawah batas saldo, maka panggilan tidak dapat dilakukan.
Klien dapat melakukan panggilan masuk tanpa saldo.

## Error States  <!-- confidence:high ✓ -->

Berikut kondisi-kondisi yang perlu diperhatikan:

1. **Fitur WhatsApp Call tidak muncul di Package Usage**: Fitur ini hanya muncul untuk pengguna yang telah mengaktifkannya. Hubungi tim support kami di support-qontak@mekari.com untuk mengaktifkan fitur tersebut.

2. **Panggilan keluar tidak dapat dilakukan**: Jika Voice Balance Anda berada di bawah batas saldo minimum, panggilan keluar tidak dapat dilakukan. Lakukan top up Voice Balance terlebih dahulu melalui menu Package Usage.

3. **Panggilan terpotong lebih dari durasi sebenarnya**: Sistem menghitung potongan berdasarkan menit penuh. Panggilan 2 detik akan dipotong 1 menit penuh.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika Anda mengalami:

- Fitur WhatsApp Call tidak muncul meskipun sudah diminta untuk diaktifkan
- Ketidaksesuaian antara durasi panggilan dan potongan Voice Balance
- Voice Balance tiba-tiba berkurang tanpa ada panggilan yang dilakukan
- Tidak dapat melakukan panggilan masuk meskipun sudah ada saldo
- Pertanyaan mengenai harga dan billing Voice Call

Saat menghubungi support, sertakan:
- Screenshot halaman Package Usage dan detail Voice Balance
- Nomor/tanggal panggilan yang bermasalah
- Informasi akun Qontak Anda

Email: support-qontak@mekari.com