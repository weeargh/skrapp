---
title: Bagaimana Cara Menerapkan Kebijakan SLA
canonical_url: https://help-center.qontak.com/hc/id/articles/37013811213209-Bagaimana-Cara-Menerapkan-Kebijakan-SLA
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: web
language: id
intent_tags:
- sla-management-countdown
- customer-support-ticketin
query_examples:
- Cara Menerapkan Kebijakan SLA
- Bagaimana cara Menerapkan Kebijakan SLA?
- Langkah-langkah Menerapkan Kebijakan SLA di Qontak CRM
- How do I Menerapkan Kebijakan SLA?
- Mau Menerapkan Kebijakan SLA, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.3
---

## Prerequisites  <!-- confidence:high ✓ -->

Anda ingin menerapkan kebijakan SLA pada perusahaan Anda di Mekari Qontak CRM. Sebelum memulai, pastikan:

- Anda memiliki akses ke akun Qontak CRM
- Peran Anda adalah Admin atau Owner
- Paket langganan Anda adalah Ultimate atau Enterprise di service suite Qontak
- Fitur SLA Management hanya berlaku untuk Ticket Module
- Pipeline sudah dibuat sebelumnya pada Ticket Module

## Steps  <!-- confidence:high ✓ -->


Dengan fitur **SLA management** pada Mekari Qontak CRM, Anda sebagai peran **Admin** atau **Owner** , dapat mengatur kebijakan SLA (Service Level Agreement) pada perusahaan untuk memastikan standar yang telah ditetapkan di semua interaksi layanan pelanggan. Dalam hal ini, Anda juga berperan dalam memantau kinerja dan loyalitas para Agent terhadap SLA yang sudah ditentukan melalui menu **Properties**. Perlu Anda ketahui sebelumnya bahwa fitur ini hanya berlaku untuk **Ticket Module**.

Sebagai contoh:  
Apabila SLA Anda berjalan selama **1 hari** , maka harap konversi ke satuan jam yang dalam hal ini adalah **24 Hours (jam)**. Lalu, apabila SLA Anda berjalan selama **2 hari** , maka perhitungan konversinya adalah **2 x 24 jam** atau **48 Hours (jam)**.
  9. Kemudian tentukan **Operational hours**. Anda dapat memilih antara **24/7 Availability** atau **Custom** dimana Anda dapat menyesuaikan hari dan rentang waktu jam operasional.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F42145207226649)

- Berikut adalah tampilan ketika Anda memilih **Custom**. Tentukan **Working days** serta rentang waktu aktifnya SLA yang sedang berjalan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F42145207229849)  
- Dalam hal ini, SLA hanya dihitung selama hari dan jam kerja yang dipilih. Di luar waktu tersebut, hitungan mundur SLA berhenti.
  10. Pastikan keseluruhan data telah benar lalu klik **“Save”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F42145190657049)
  11. Kemudian akan muncul kotak informasi berikut yang menyatakan bahwa kebijakan telah dibuat tersebut berlaku untuk tiket yang baru dibuat dan telah memenuhi semua ketentuan terkait. Klik **“Save”** untuk melanjutkan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F42145190658073)

### B. Cara Mengedit Kebijakan SLA[](https://help-center.qontak.com/hc/id/articles/37013811213209-Bagaimana-Cara-Menerapkan-Kebijakan-SLA#01JH711PP0CA0CT2TR9R26670R)
  1. Pada halaman utama **SLA Management** , klik **“Actions”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F42145190658841)
  2. Lalu pilih **“Edit”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F42145190660505)
  3. Kemudian edit kembali data sesuai dengan keinginan Anda.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F42145190661913)
Peran **Admin** atau **Owner** dapat membuat perubahan pada field yang terdiri dari **Nama Kebijakan, Deskripsi, Kondisi, Waktu Penyelesaian, atau Jam Operasional.**
  4. Setelah melakukan edit, klik **“Save changes”**.  
Berikut kondisi yang akan berubah apabila Anda mengedit kebijakan SLA:  
1. Jika **Admin/Owner** mengedit **nama kebijakan & jam operasional**, maka akan berdampak pada tiket yang sudah ada.  
2. Jika **Admin/Owner** mengedit bagian **Condition** , maka akan berdampak pada tiket baru saja.

### C. Cara Menghapus Kebijakan SLA[](https://help-center.qontak.com/hc/id/articles/37013811213209-Bagaimana-Cara-Menerapkan-Kebijakan-SLA#h_01JH71A27CQA31APJG8ZRPT59Y)
  1. Pada halaman utama **SLA Management** , klik **“Actions”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F42183051025177)
  2. Lalu pilih **“Delete”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F42183051026841)
  3. Kemudian akan muncul kotak informasi berikut yang menyatakan bahwa penghapusan kebijakan berlaku untuk tiket yang terdapat pada **Pipeline** pada kebijakan SLA terpilih. Kebijakan yang dihapus tidak dapat dikembalikan. Klik **“Delete”** untuk melanjutkan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F42183051032729)

### D. Cara Menduplikasi Kebijakan SLA[](https://help-center.qontak.com/hc/id/articles/37013811213209-Bagaimana-Cara-Menerapkan-Kebijakan-SLA#h_01JH581KNC96SCQPG3AK62Z1GG)
  1. Pada halaman utama **SLA Management** , klik **“Actions”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F42145190658841)
  2. Lalu pilih **“Duplicate”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F42145207272985)
  3. Kemudian **Admin** atau **Owner** akan diarahkan ke halaman Kebijakan SLA yang akan diduplikasi. Dalam hal ini, nama kebijakan akan secara otomatis menyertakan “(duplikat)” atau (1) sesuai dengan jumlah yang diduplikasi dan akan tertera di samping **Policy name**. Sebagai contoh, jika diduplikasi, kebijakan SLA akan berubah namanya menjadi **Premium support** **(1)**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F42145190677785)
  4. Jika keseluruhan data telah diisi, klik **“Save changes”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F42145190681241)

### E. Cara Memantau SLA Activity Logs[](https://help-center.qontak.com/hc/id/articles/37013811213209-Bagaimana-Cara-Menerapkan-Kebijakan-SLA#h_01JH581KNCNYN52PA5VZBD8CXT)
  1. Pada halaman utama **SLA Management** , klik **“Actions”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F42145190658841)
  2. Lalu pilih **“See change log”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F42145190683033)
  3. **Admin** atau **Owner** dapat melihat detail seperti jenis perubahan, siapa yang membuatnya, serta tanggal dan modifikasi waktu pada kebijakan SLA.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F42145190689049)

Demikian cara mengelola kebijakan SLA. Pelajari juga terkait cara membuat Ticket baru [di sini](https://help-center.qontak.com/hc/id/articles/22326228316313-Bagaimana-Cara-Membuat-Ticket-Baru).

## Error States  <!-- confidence:low ? -->

No common errors documented.

## Escalation  <!-- confidence:medium ~ -->

Jika Anda mengalami masalah saat menerapkan kebijakan SLA, hubungi tim dukungan Mekari Qontak dengan informasi berikut:

- ID akun CRM Anda
- Screenshot dari halaman SLA Management atau form Create Policy yang menampilkan masalah
- Deskripsi detail tentang langkah mana yang tidak berfungsi
- Paket langganan Anda (Ultimate atau Enterprise)
- Nama Pipeline dan kondisi yang ingin Anda terapkan