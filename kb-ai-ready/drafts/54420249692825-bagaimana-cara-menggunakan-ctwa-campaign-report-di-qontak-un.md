---
title: Bagaimana Cara Menggunakan CTWA Campaign Report di Qontak untuk Optimasi Iklan
canonical_url: https://help-center.qontak.com/hc/id/articles/54420249692825-Bagaimana-Cara-Menggunakan-CTWA-Campaign-Report-di-Qontak-untuk-Optimasi-Iklan
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- campaign-report-evaluation
- use-ctwa-campaign-report
- marketing-campaign-manage
query_examples:
- Cara Menggunakan CTWA Campaign Report di Qontak untuk Optimasi Iklan
- Bagaimana cara Menggunakan CTWA Campaign Report di Qontak untuk Optimasi Iklan?
- Langkah-langkah Menggunakan CTWA Campaign Report di Qontak untuk Optimasi Iklan
  di Qontak Omnichannel
- How do I Menggunakan CTWA Campaign Report di Qontak untuk Optimasi Iklan?
- Mau Menggunakan CTWA Campaign Report di Qontak untuk Optimasi Iklan, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Anda ingin mengoptimalkan iklan Click-to-WhatsApp (CTWA) melalui laporan performa di Qontak.

Persyaratan sebelum memulai:
• Akun Qontak Omnichannel aktif dengan akses ke menu Campaign
• Akun bisnis WhatsApp yang terintegrasi dengan Qontak melalui WhatsApp API
• Nomor WhatsApp terhubung ke Facebook Page bisnis (dengan role admin) atau business portfolio
• Akun Meta Ads Manager aktif untuk membuat kampanye Click-to-WhatsApp
• Izin akses untuk melihat laporan kampanye di dashboard Qontak
• Kampanye Click-to-WhatsApp sudah berjalan di Meta Ads Manager

## Steps  <!-- confidence:medium ~ -->


Fitur **CTWA Ad Campaign Report** menyediakan tampilan terpadu atas performa iklan _**Click-to-WhatsApp**_**(CTWA)** beserta kualitas _lead_ yang dihasilkannya, langsung melalui dashboard Qontak. Dengan fitur ini, pengguna dapat memantau kinerja iklan sekaligus menelusuri percakapan yang berasal dari iklan dengan lebih akurat.
**Penting**  
**Persyaratan Sebelum Melakukan Integrasi**  
**![rev 3.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F54446708024345)**
###  **A. Cara Membuat Ads yang Langsung Mengarah ke WhatsApp**[](https://help-center.qontak.com/hc/id/articles/54420249692825-Bagaimana-Cara-Menggunakan-CTWA-Campaign-Report-di-Qontak-untuk-Optimasi-Iklan#h_01KFDHR4FMDP9P4PHAD85X1M66)
Anda dapat membuat iklan di Meta Ads Manager yang ketika diklik, langsung membuka _chat_ WhatsApp dengan bisnis milik Anda. 
Beberapa fitur, metrik, dan jenis kampanye terkait pesan tidak tersedia untuk iklan atau pesan yang berasal dari atau ditujukan ke Eropa, Jepang, dan Korea Selatan.
Selama Anda memiliki nomor WhatsApp yang terhubung ke Facebook Page, atau nomor WhatsApp yang terhubung ke business portfolio, Anda sudah bisa membuat iklan Click to WhatsApp lewat Meta Ads Manager.

Langkah pembuatannya dapat berbeda-beda, tergantung tujuan iklan (_ad objective_) yang Anda pilih.
Sebelum mulai, pastikan:
  1. **Punya akun bisnis WhatsApp**  
Lakukan[ integrasi dengan WhatsApp API](https://help-center.qontak.com/hc/id/articles/12055228468633-Bagaimana-Cara-Mengintegrasikan-Qontak-dengan-WhatsApp-API).
  2. **Hubungkan WhatsApp ke Facebook**  
Sambungkan akun WhatsApp ke Facebook Page bisnis dan pastikan Anda memiliki _role_ sebagai admin Page, atau hubungkan nomor WhatsApp ke business portfolio.
  3. **Opportunity Score (jika tersedia)**  
Apabila akun Anda telah memenuhi syarat, Meta akan menampilkan Opportunity Score berisi rekomendasi yang sudah diuji untuk membantu meningkatkan performa Ads. Anda dapat memeriksanya melalui menu **Account Overview**.  
Perlu diingat:
     * Opportunity Score belum tersedia untuk semua akun Ads.
     * Skor tinggi tidak menjamin hasil iklan akan bagus.
     * Performa Ads tetap bergantung pada banyak faktor lainnya.

### B. Menambahkan Nomor WhatsApp ke Business Portfolio[](https://help-center.qontak.com/hc/id/articles/54420249692825-Bagaimana-Cara-Menggunakan-CTWA-Campaign-Report-di-Qontak-untuk-Optimasi-Iklan#h_01KFDHR4GCZBFHEGQDKYEZ419B)
Anda dapat menambahkan nomor WhatsApp ke _business portfolio_ agar nomor tersebut dapat dihubungkan ke akun ads atau dibagikan kepada _partner_ yang bekerja sama dengan bisnis Anda. Seperti aset bisnis lainnya di Meta, Anda juga dapat mengatur hak akses (permission) untuk setiap nomor WhatsApp berdasarkan tugas tertentu melalui pengaturan Meta Business Suite.
Beberapa metrik, jenis kampanye iklan, dan fitur pesan organik tidak tersedia untuk bisnis atau iklan yang ditujukan ke atau berasal dari Eropa, Jepang, dan Korea Selatan.

**Hal yang perlu Anda ketahui:**
  * Anda dapat menambahkan lebih dari satu nomor WhatsApp ke dalam satu _business portfolio_.
  * Jika nomor WhatsApp sudah terintegrasi dengan WhatsApp Business API, nomor tersebut akan otomatis terhubung ke _business portfolio_.
  * Satu nomor WhatsApp hanya dapat terhubung ke satu _business portfolio_.

**Sebelum mulai, pastikan:**
  * Hanya pengguna dengan akses penuh (full control) yang dapat menambahkan nomor WhatsApp ke _business portfolio_.
  * Nomor WhatsApp yang sama dapat terhubung ke Facebook Page dan business portfolio sekaligus.
  * Anda juga dapat menambahkan Facebook Page yang terhubung ke nomor WhatsApp tersebut ke dalam _business portfolio_.

**Cara menghubungkan beberapa nomor WhatsApp ke business portfolio:**
  1. Buka Meta Business Suite, lalu masuk ke menu Settings.
  2. Klik **“Accounts”**.
  3. Pilih **“WhatsApp accounts”**.
  4. Tambahkan nomor telepon dari aplikasi WhatsApp Business.
  5. Setelah itu, saat membuat iklan **Click to WhatsApp** , Anda dapat memilih salah satu nomor WhatsApp dari menu _dropdown_.

###    
**Fase 2: Cara Melihat Laporan CTWA di Qontak** [](https://help-center.qontak.com/hc/id/articles/54420249692825-Bagaimana-Cara-Menggunakan-CTWA-Campaign-Report-di-Qontak-untuk-Optimasi-Iklan#h_01KFDHR4HRNCDCNP3JKCR24SZ2)
**Langkah melihat dan memperbarui laporan**
  1. Setelah integrasi selesai, kembali ke menu **Report** pada akun Qontak Anda.
  2. Kemudian klik tab **Ad Campaign.**  
**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F54420249675673)**
  3. Di sini Anda akan melihat area filter, namun badan laporan masih kosong.  
**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F54420265855257)**
  4. Berikut merupakan penjelasan sekilas mengenai halaman indeks **Ad campaign** report.  
**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F54420265855641)**  
**Keterangan:**

**No.** | **Nama Fitur** | **Penjelasan**  
---|---|---  
**1** | **Filter tanggal** | Menyaring data Ad berdasarkan rentang waktu tertentu.  
**2** | **Filter Ad Account** | Menampilkan data Ad Account tertentu.  
**3** | **Sync** |  Tombol untuk melakukan sinkronisasi manual **(wajib).**  
Laporan tidak bersifat real-time. Anda perlu klik **“Sync”** setiap kali ingin memperbarui data.  
**4** | **Last sync** | Menunjukkan waktu terakhir sistem melakukan sinkronisasi data dengan sumber data aslinya.  
**5** | **Ad Data Overview** | Menampilkan rangkuman laporan data Ad yang tersedia. Laporan akan terisi dengan **Overview Report** , **daftar Ad Campaign** , serta daftar **Conversation from Ad**.   
**6** | **Ad campaign list** | Menampilkan rincian informasi _list_ Ad campaign.  
**7** | **Conversations from ad campaigns** | Menampilkan informasi data percakapan yang dihasilkan dari Ad Campaign terkait.  
###  **D. Penggunaan & Praktik Terbaik untuk Iklan CTWA**[](https://help-center.qontak.com/hc/id/articles/54420249692825-Bagaimana-Cara-Menggunakan-CTWA-Campaign-Report-di-Qontak-untuk-Optimasi-Iklan#h_01KFDHR4JHJJ162ZRPDKM69Y83)
**Industri / Skenario** | **Cara Penggunaan di Qontak CTWA Report** | **Contoh Praktik Terbaik Iklan Meta (Teks Iklan & Pesan WhatsApp)**  
---|---|---  
**Retail / E-commerce** | Marketer memilih campaign seperti “Flash Sale” lalu melihat total percakapan yang masuk dari iklan tersebut | 
  * Contoh Teks Iklan (Ad Copy):  
“Mau diskon spesial? Chat kami sekarang!”
  * Contoh Pesan Sambutan di WhatsApp:  
“Hi! Terima kasih sudah chat kami soal Flash Sale. Pilih tombol di bawah untuk lihat katalog produk atau minta kode diskon ya!”

**Layanan / Konsultasi** | Supervisor mengecek daftar Conversation from Ad untuk menilai kualitas _lead_ sebelum dibagikan ke Agent | 
  * Contoh Teks Iklan (Ad Copy):  
“Tanya _expert_ kami di WhatsApp. Solusi bisnis dalam 60 detik.”
  * Contoh Pesan Sambutan di WhatsApp:  
“Halo! Kamu terhubung dengan [Brand Concierge]. Ada yang bisa kami bantu? Beri tahu jenis konsultasi yang kamu butuhkan ya”

**Lead Nurturing / Retargeting** | Agent dapat melihat _tag_ “Ad campaign” sehingga mengetahui bahwa _lead_ tersebut sudah tertarik (_lead_ hangat), bukan percakapan acak. | 
  * Contoh Teks Iklan (Ad Copy):  
“Belanjaan kamu masih menunggu! Chat sekarang untuk klaim diskon 10%.”
  * Contoh Pesan Sambutan di WhatsApp:  
“Hi [nama], terima kasih sudah kembali! Kamu sebelumnya melihat [nama produk]. Ada yang bisa kami bantu untuk selesaikan pesanan hari ini?”

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika Anda mengalami:
• Kampanye Click-to-WhatsApp tidak muncul di dashboard meski sudah terhubung ke Meta Ads Manager
• Data laporan tidak menunjukkan pembaruan selama lebih dari 24 jam
• Pesan error spesifik saat mengakses CTWA Ad Campaign Report
• Kesulitan dalam integrasi WhatsApp API atau koneksi Facebook Page

Siapkan informasi berikut saat menghubungi support:
• ID akun Qontak dan ID kampanye yang bermasalah
• Screenshot dashboard atau pesan error
• Waktu terjadinya masalah
• Daftar langkah yang sudah dicoba