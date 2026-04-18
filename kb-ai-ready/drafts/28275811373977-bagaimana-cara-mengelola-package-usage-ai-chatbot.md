---
title: Bagaimana Cara Mengelola Package Usage AI Chatbot
canonical_url: https://help-center.qontak.com/hc/id/articles/28275811373977-Bagaimana-Cara-Mengelola-Package-Usage-AI-Chatbot
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- platform
- manage-package-usage-ai-chatbot
- general-platform
query_examples:
- Cara Mengelola Package Usage AI Chatbot
- Bagaimana cara Mengelola Package Usage AI Chatbot?
- Langkah-langkah Mengelola Package Usage AI Chatbot di Qontak Omnichannel
- How do I Mengelola Package Usage AI Chatbot?
- Mau Mengelola Package Usage AI Chatbot, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengelola Package Usage AI Chatbot di Qontak Omnichannel, Anda membutuhkan:

- Akun Qontak Omnichannel aktif dengan akses Admin atau Supervisor
- Paket berlangganan aktif dengan fitur AI Chatbot
- Akses ke menu Package Usage di dashboard Qontak Omnichannel
- Koneksi internet stabil untuk membuka antarmuka web Qontak
- Pengetahuan tentang struktur percakapan (Intent Classification dan Chatbot AI) untuk memahami pemakaian kuota

## Steps  <!-- confidence:high ✓ -->


Package Usage merupakan sebuah halaman yang menampilkan pemakaian paket tertentu pada Qontak Omnichannel. Anda dapat melihat pemakaian dan sisa kuota [Conversation](https://help-center.qontak.com/hc/id/articles/10265853268121) maupun AI Chatbot.
**Penting****  
****Apa sajakah yang dapat mengurangi AI Dialog?  
** AI Dialog digunakan pada 2 fitur berikut:  
1. **Intent Classification  
** a. Setiap input dari pengguna yang diarahkan ke **_bot response_** dengan **_keyword_** yang sudah dilatih akan memotong**1 AI Dialog**.  
b. Pemotongan terjadi ketika **_bot response_** tersebut muncul dalam percakapan.  
2. **Chatbot AI  
** a. Setiap 1 pertanyaan dari **customer (1**** _bubble message_****dari customer)** dan 1 jawaban dari Chatbot AI**(1**** _bubble message_****dari bot)** akan mengurangi**1 AI Dialog.  
** b. Hal ini berarti semua **_bubble messages_** dari**Chatbot AI** , termasuk pesan untuk **_assign_** maupun pesan otomatis saat customer **_idle_** ,**tetap dihitung** dan **mengurangi kuota AI Dialog.**
Pada panduan ini, Anda dapat mempelajari cara membaca dan mengelola package usage AI Chatbot.
  1. Pada Qontak Omnichannel, pilih menu **Package Usage** , lalu klik **Chatbot AI.**  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780962579993)
  2. Maka, Anda akan diarahkan ke halaman rincian keterangan pemakaian paket Chatbot AI.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50764839968921)

**No.** | **Nama Bagian** | **Deskripsi**  
---|---|---  
1 | Initial AI dialogs | Jumlah kuota AI yang didapatkan beserta sisanya.   
2 | Extra AI dialogs |  Jumlah kuota tambahan AI yang didapatkan beserta sisanya. Kuota tersebut termasuk dialog tambahan pascabayar atau prabayar. - Apabila **pascabayar** mencapai limit, maka limit akan direset setiap bulannya.  
- Apabila **prabayar** , maka sisa kuota bulan lalu akan diteruskan ke bulan selanjutnya.  
- Apabila sisa kuota dari bulan lalu minus (negatif) maka, Initial dialog tidak akan direset kecuali di saat sudah lunas.  
  3. Pada bagian selanjutnya, terdapat tabel **Chatbot AI usage.** Pada daftar ini, terdapat informasi lengkap tentang pemakaian kuota setiap dialog, seperti**Room ID, Channel, Account ID, Response Date, Dialog Deduction,** dan **AI Dialog Usage.  
**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780962581401)

- Anda dapat memfilter rentang waktu yang ditampilkan pada tabel dengan klik pada **Periode Filter.**  
- Anda dapat mengunduh tabel ini dalam format spreadsheet CSV dengan rentang periode **maksimal 90 hari** dengan klik **“Download”**.
**Penting**  
1 pengurangan Dialog AI = 1x pertanyaan dari pelanggan ke klien dan respons dari klien ke pelanggan yang menggunakan AI.  
Ini berarti di dalam 1 chat room bisa terdapat beberapa pengurangan Dialog AI.

## Error States  <!-- confidence:high ✓ -->

**Kuota AI Dialog hampir habis**: Anda akan menerima banner notifikasi ketika saldo kuota mendekati batas minimum. Tindakan yang dapat dilakukan adalah melakukan top up kuota tambahan melalui menu Package Usage.

**Saldo negatif**: Apabila sisa kuota dari bulan lalu minus (negatif), Initial AI Dialog tidak akan direset sampai tagihan sudah lunas.

**Perbedaan perhitungan kuota**: Setiap 1 pertanyaan dari customer dan 1 jawaban dari Chatbot AI mengurangi 1 AI Dialog. Semua bubble message dari Chatbot AI, termasuk pesan assign dan pesan otomatis saat customer idle, tetap dihitung dan mengurangi kuota.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support jika mengalami:

- Perbedaan perhitungan kuota AI Dialog yang tidak sesuai dengan penggunaan aktual
- Masalah akses ke menu Package Usage atau tab Chatbot AI
- Kegagalan mengunduh tabel Chatbot AI usage dalam format CSV
- Pertanyaan tentang kebijakan reset kuota pascabayar atau prabayar

Siapkan informasi berikut saat menghubungi support: Account ID, screenshot halaman Package Usage, rentang waktu masalah terjadi, dan deskripsi detail masalah yang dialami.