---
title: Bagaimana Cara Melakukan Migrasi ke Marketing Message API
canonical_url: https://help-center.qontak.com/hc/id/articles/52407479373081-Bagaimana-Cara-Melakukan-Migrasi-ke-Marketing-Message-API
article_type: task
solvability_type: tool
products:
- Qontak Chat
product_surface: api
language: id
intent_tags:
- multi-channel-integration
- perform-migrasi
- conversation-management
query_examples:
- Cara Melakukan Migrasi ke Marketing Message API
- Bagaimana cara Melakukan Migrasi ke Marketing Message API?
- Langkah-langkah Melakukan Migrasi ke Marketing Message API di Qontak Chat
- How do I Melakukan Migrasi ke Marketing Message API?
- Mau Melakukan Migrasi ke Marketing Message API, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.3
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk melakukan migrasi ke Marketing Message API (MM API), Anda memerlukan:

- Role Admin pada akun Qontak Omnichannel
- Akun Qontak Omnichannel yang aktif
- WhatsApp Business Account (WABA) yang sudah terdaftar dan terintegrasi dengan Qontak
- Akses ke menu Channel Integration di Qontak Omnichannel
- Template pesan marketing yang sudah tersimpan di WABA Anda
- Data riwayat pengiriman pesan (untuk benchmarking performa template)

Catatan: Mulai 20 Agustus 2025, semua WABA baru otomatis menggunakan MM API.

## Steps  <!-- confidence:medium ~ -->


Marketing Message (MM API) merupakan pembaruan dari WhatsApp Marketing Message API yang telah dilengkapi dengan sistem optimasi otomatis. Melalui MM API, bisnis dapat mengirimkan pesan yang lebih relevan dan tertarget berdasarkan data keterbacaan serta tingkat keterlibatan, sehingga pesan tersampaikan kepada pelanggan yang lebih berpotensi membaca dan merespon.
Sebagai bagian dari mekanisme kerja MM API, terdapat beberapa aspek yang membantu sistem dalam mengatur dan memaksimalkan pengiriman pesan:
**1. Optimasi Pengiriman Pesan**  
Marketing Message API dapat meningkatkan efisiensi pengiriman hingga 7% (_Indonesia Case_) dengan menerapkan limit pesan yang lebih dinamis ketika tingkat keterbacaan meningkat.
**2. Benchmarking Template Pesan**  
MM API juga menyediakan mekanisme untuk membandingkan performa setiap template pesan, yang tidak tersedia pada Cloud API. 
Pada penjelasan di bawah ini, Anda akan mempelajari mulai dari cara kerja pengiriman _marketing message_ melalui MM API, perbandingan antara MM API dan Cloud API untuk _marketing message_ , hingga panduan migrasi ke MM API. Simak selengkapnya berikut ini.
###  **A. Cara Kerja Pengiriman Marketing Message melalui MM API**[](https://help-center.qontak.com/hc/id/articles/52407479373081-Bagaimana-Cara-Melakukan-Migrasi-ke-Marketing-Message-API#h_01KB1JZH4JF1839FTF1DYCPD92)
Saat bisnis memilih pelanggan dan nomor tujuan untuk dikirimi pesan marketing, pengiriman akan diteruskan melalui **MM API** dan diproses oleh kontrol kualitas WhatsApp Business Platform. Pada tahap ini, baik MM API maupun Cloud API dapat mengalami penundaan atau kegagalan pengiriman karena faktor berikut:
  * Pengguna memblokir,
  * Pesan terdeteksi sebagai _spam_ ,
  * _Template_ memiliki performa rendah (misalnya tingkat baca rendah atau _feedback_ negatif tinggi),
  * Batas pesan per pengguna dari _platform_.

Setelah melewati proses tersebut, **MM API memastikan jumlah pesan yang terkirim minimal setara dengan Cloud API** , lalu menerapkan **optimasi otomatis**. Sistem dapat mengenali pesan dengan tingkat keterlibatan tinggi dan memberikan **batas pengiriman yang lebih dinamis** , bahkan memungkinkan batas yang lebih tinggi dibanding Cloud API. Selain itu, mekanisme optimasi MM API akan terus dikembangkan untuk meningkatkan hasil pengiriman, termasuk melalui penerapan **optimasi kreatif otomatis** di tahap berikutnya.
Sebaliknya, **Cloud API tidak memiliki proses optimasi** , sehingga pesan marketing dapat gagal terkirim karena batas pengiriman yang kaku dan tidak menyesuaikan performa pesan.
###  **B. Perbandingan MM API vs Cloud API untuk Marketing Message**[](https://help-center.qontak.com/hc/id/articles/52407479373081-Bagaimana-Cara-Melakukan-Migrasi-ke-Marketing-Message-API#h_01KB1K0295HXDND0D5A5NT8QBD)
Berikut perbandingan fitur antara Cloud API dan MM API untuk penggunaan Marketing Message. Periksa perbandingan harga Cloud API dan MM API [di sini](https://help-center.qontak.com/hc/id/articles/48430892733465).
**Fitur** | **Cloud API** | **MM API**  
---|---|---  
Optimasi Pengiriman | Tidak tersedia | Tersedia melalui MM API Engine (otomatis)  
Pengiriman ke High Engagement Users | Standar | Meningkat hingga 7% untuk pelanggan dengan engagement tinggi  
Laporan Kampanye |  Cloud API menyediakan **laporan dasar** yang berisi metrik teknis standar, yaitu **Sent** , **Delivered** , **Read** , **Clicked** , dan **Cost**.

Laporan ini bersifat **transaksional** , artinya hanya menampilkan performa pesan yang dikirim **apa adanya** , tanpa analisis tambahan.   
|  MM API menyediakan **laporan yang lebih lengkap dan analitis**. Selain seluruh metrik dasar dari Cloud API (sent, delivered, read, clicked, cost), MM API juga memberikan insight tambahan berupa _**benchmarking**_**, rekomendasi otomatis** , serta _**dashboard**_**analitik**.

###  **C. Panduan Migrasi ke MM API**[](https://help-center.qontak.com/hc/id/articles/52407479373081-Bagaimana-Cara-Melakukan-Migrasi-ke-Marketing-Message-API#h_01KB1K24P1ZWH5SMXJFFJ9E55Z)
Mulai **tanggal 20 Agustus 2025** , semua pendaftaran **WABA** baru melalui Qontak akan otomatis terintegrasi dengan **Marketing Messages API (MM API)** untuk pengiriman _**campaign marketing**_. [**Pelajari lebih lanjut disini.**](https://help-center.qontak.com/hc/id/articles/12055228468633-Bagaimana-Cara-Mengintegrasikan-Qontak-dengan-WhatsApp-API)
Akun WhatsApp yang terhubung dengan Qontak sebelum periode di atas dapat diintegrasikan ke **MM API** melalui 2 cara, yaitu:
**Cara 1: Invitation pada menu “Request” aplikasi Facebook Business Manager (FBBM)**
  1. Masuk ke Facebook Business Manager (FBBM) Anda.
  2. Kemudian, buka menu **Settings**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52816180307481)
  3. Selanjutnya, klik tab menu “**Requests”** atau Anda dapat langsung klik _link_.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52816159733913)
  4. Temukan undangan dari Qontak.com, lalu klik **“Review”** untuk melanjutkan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52816159737625)
  5. Tinjau _Terms & Service_, kemudian klik **“Continue”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52816180317081)
  6. Lalu klik **“Finish”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52816159747097)
  7. Kemudian klik**“Verify account”**.  
_![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52816180322969)_
  8. Masukkan alamat email yang terhubung dengan akun**Facebook Business Manager** Anda, lalu klik **“Send email”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52816159755161)
  9. Selanjutnya, periksa kotak masuk email Anda untuk mendapatkan kode verifikasi.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52816159757337)
  10. Masukkan kode verifikasi, kemudian klik **“Submit”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52816159760281)
  11. Maka proses migrasi MM API telah selesai.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52816180334873)
  12. Anda dapat memastikan apakah akun Anda telah berhasil di migrasi ke MM API melalui halaman WhatsApp Manager, pilih **Message Templates** , lalu klik salah satu nama Template dengan kategori **Marketing**. Jika MM API aktif, Anda akan melihat opsi: **Cloud API** dan **Marketing Messages API** pada halaman detail Template.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F52816180336921)

## Error States  <!-- confidence:low ? -->

Kemungkinan masalah migrasi dan solusinya:

**Tombol "Migrate to MM API" tidak muncul:** Akun Anda sudah menggunakan MM API atau memerlukan verifikasi tambahan dari Meta. Hubungi support-qontak@mekari.com.

**Migrasi gagal atau terhenti:** Koneksi Internet putus atau WABA Anda belum sepenuhnya terverifikasi di Meta Business Manager. Coba lagi atau hubungi support Qontak.

**Template pesan tidak tersinkronisasi setelah migrasi:** Refresh halaman atau tunggu 5-10 menit untuk sinkronisasi otomatis. Jika masih bermasalah, hubungi support.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support jika:

- Migrasi gagal berulang kali setelah mencoba langkah-langkah di atas
- Tombol "Migrate to MM API" tidak tersedia di Channel Integration
- Template pesan hilang atau tidak tersinkronisasi setelah migrasi
- Pengiriman pesan marketing masih mengalami gangguan 24 jam setelah migrasi

Sediakan informasi berikut saat menghubungi support:
- ID akun Qontak Omnichannel
- Nomor WhatsApp Business Account (WABA)
- Screenshot menu Channel Integration
- Pesan error lengkap (jika ada)