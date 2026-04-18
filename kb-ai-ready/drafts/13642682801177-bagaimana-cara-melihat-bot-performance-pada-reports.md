---
title: Bagaimana Cara Melihat Bot Performance pada Reports
canonical_url: https://help-center.qontak.com/hc/id/articles/13642682801177-Bagaimana-Cara-Melihat-Bot-Performance-pada-Reports
article_type: task
solvability_type: tool
products:
- Qontak Chat
product_surface: web
language: id
intent_tags:
- conversational-ai-chatbot
- view-bot-performance
- ai-chatbot-automation
query_examples:
- Cara Melihat Bot Performance pada Reports
- Bagaimana cara Melihat Bot Performance pada Reports?
- Langkah-langkah Melihat Bot Performance pada Reports di Qontak Chat
- How do I Melihat Bot Performance pada Reports?
- Mau Melihat Bot Performance pada Reports, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.3
---

## Prerequisites  <!-- confidence:medium ~ -->

Untuk melihat Bot Performance pada Reports, Anda memerlukan:

1. Akses ke Qontak Chat dengan permission untuk melihat laporan
2. Chatbot yang sudah dipublikasikan dan aktif menangani percakapan pelanggan
3. Minimal satu percakapan yang telah diproses oleh bot
4. Data historis percakapan tersedia di sistem (biasanya tersedia setelah bot aktif menangani percakapan)

## Steps  <!-- confidence:high ✓ -->


Pada Qontak, Anda bisa melihat bot performance melalui menu **Report**. Fitur ini memungkinkan Anda melihat bagaimana kinerja bot dalam menangani pelanggan seperti melihat berapa banyak chat room yang sudah di-_resolve_ oleh chatbot. Berikut langkah-langkahnya.
  1. Masuk ke menu **Report**.
  2. Lalu pilih **Bot Performance**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F48427363329177)
  3. Maka akan ditampilkan laporan bot performance sebagai berikut.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F48427388783129)  
**No.** |  **Nama Laporan/ Tombol** |  **Keterangan**  
---|---|---  
1 |  Date filter |  Untuk memfilter laporan berdasarkan rentang waktu tertentu.  
2 |  Conversation Handled by Bot |  Menunjukkan total chat yang sudah di-_handle_ oleh bot _._  
3 |  Conversation Resolved by bots |  Menunjukkan total chat yang sudah di-_resolved_ oleh bot.  
4 |  Conversation Assigned to Agent |  Menunjukkan total jumlah percakapan yang di-_assign_ ke Agent.  
5 |  Avg. Resolution Time |  Rata-rata waktu yang dibutuhkan bot untuk menyelesaikan percakapan tanpa melibatkan Agent.  
  4. Selain itu, Anda juga dapat melihat grafik Performance trend, yang berisi perbandingan antara percakapan yang di-_resolved_ oleh bot dengan percakapan yang telah di-_assign_ ke Agent oleh bot.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F48427388784409)
  5. Selanjutnya, Anda dapat melihat laporan dari **Top Bot performance** yang menampilkan **bot response** mana yang paling banyak ditampilkan kepada pelanggan. Di sini, Anda dapat melihat nama respon bot dan perhitungan jumlah total respon bot yang ditampilkan.  
![4.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F48495938997657)
  6. Terdapat **Fallback rate details** , di sini akan menampilkan berapa banyak pesan Fallback yang di-_trigger_ dan menunjukkan Confusion Rate dari Bot Response tersebut.  
![8.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F48495935249305)

Keterangan setiap kolom:  
1. Bot Response Name: nama respon bot yang telah dibuat.  
2. Total Fallback: jumlah fallback yang ditampilkan kepada pelanggan per respon bot.  
3. Total Answered: jumlah pelanggan yang dapat dijawab oleh bot.  
4. Confusion Rate: persentase respon fallback dari semua pesan yang dijawab. Hal ini menunjukkan seberapa sering bot gagal memahami pelanggan.
  7. Terakhir terdapat **Customer and Bot Interactions**. Grafik ini akan menampilkan bagaimana setiap interaksi pelanggan berhubungan dengan respons bot tertentu.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F48430152491929)

Keterangan setiap kolom:  
1. Customer name: nama pelanggan yang berinteraksi dengan bot.  
2. First bot response: menunjukkan respons bot pertama yang berinteraksi dengan pelanggan.  
3. Last Bot Response: menunjukkan respons bot terakhir yang berinteraksi dengan pelanggan sebelum di-_resolve_ atau di-_assign_ ke Agent.  
4. Channel: tempat percakapan terjadi.  
5. Created at: saat **room/conversation** dibuat.
  8. Selanjutnya, Anda dapat mengunduh laporan **Bot response performance, Performance****Trend** , **Top Bot Performance** ,**Fallback rate****details** , dan **Customer and Bot Interactions** dengan klik **‘ikon titik tiga’** di pojok kanan dari setiap tabel lalu klik **“Download results”**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F48430152499609)

## Error States  <!-- confidence:low ? -->

No common errors documented.

## Escalation  <!-- confidence:medium ~ -->

Jika Anda mengalami masalah saat mengakses Bot Performance:

1. Pastikan chatbot sudah dipublikasikan dan telah menangani percakapan pelanggan
2. Verifikasi bahwa Anda memiliki permission yang tepat untuk melihat Report
3. Coba refresh halaman atau logout kemudian login kembali
4. Jika data tidak muncul meski chatbot aktif, hubungi Qontak Support dengan menyertakan: nama chatbot, rentang tanggal yang dicek, dan screenshot halaman Report