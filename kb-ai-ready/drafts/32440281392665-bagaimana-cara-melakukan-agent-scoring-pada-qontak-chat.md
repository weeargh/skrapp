---
title: Bagaimana Cara Melakukan Agent Scoring pada Qontak Chat
canonical_url: https://help-center.qontak.com/hc/id/articles/32440281392665-Bagaimana-Cara-Melakukan-Agent-Scoring-pada-Qontak-Chat
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- agent-performance-and-quality-assurance
- perform-agent-scoring
- customer-support-ticketin
query_examples:
- Cara Melakukan Agent Scoring pada Qontak Chat
- Bagaimana cara Melakukan Agent Scoring pada Qontak Chat?
- Langkah-langkah Melakukan Agent Scoring pada Qontak Chat di Qontak Omnichannel
- How do I Melakukan Agent Scoring pada Qontak Chat?
- Mau Melakukan Agent Scoring pada Qontak Chat, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk melakukan Agent Scoring pada Qontak Chat, Anda memerlukan:

• Akun Qontak Omnichannel aktif dengan role supervisor, manager, atau admin
• Akses ke menu Settings dan Scorecard
• Pemahaman tentang parameter penilaian kinerja agen
• Belum ada Scorecard yang dibuat sebelumnya (jika membuat baru)

Proses ini memerlukan dua tahap utama: membuat Scorecard beserta parameter penilaian, kemudian melakukan penilaian terhadap agen pada ruang percakapan.

## Steps  <!-- confidence:high ✓ -->


### B. Pengaturan Scorecard (Set up Scorecard)[](https://help-center.qontak.com/hc/id/articles/32440281392665-Bagaimana-Cara-Melakukan-Agent-Scoring-pada-Qontak-Chat#h_01HXTKASWC46Z2E9ATHF9VXBH8)
Setelah membuat kategori penilaian, langkah selanjutnya adalah membuat pengaturan scorecard. Anda dapat melakukan beberapa konfigurasi untuk menentukan penilaian berupa **Pass**(berhasil) atau **Failed**(gagal) berdasarkan skor tersebut. Berikut langkah-langkahnya. 
  1. Pada halaman **Scorecard** , klik **“Set up scorecard”**.  
![8.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F44411239187993)
  2. Selanjutnya tentukan **Passing grade** untuk menentukan standar penilaian agen. Anda juga dapat mengaktifkan toggle **Auto scoring by Mekari Airene** apabila ingin melakukan penilaian secara otomatis.  
![11.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774535931033)
- Nilai **passing grade** akan menentukan apakah agen tersebut **berhasil** atau **gagal** dalam ruang percakapan. Jumlahnya akan ditentukan oleh **skor parameter**. Jika skor agen **diatas** atau **sesuai** dengan **passing grade** maka statusnya adalah **Pass**. Apabila skor agen **di bawah** **passing grade** berarti **Fail**. Secara default nilai kelulusannya adalah **75%**.  
- Apabila Anda mengaktifkan toggle **Auto scoring by Mekari Airene** , maka otomatisasi akan dilakukan jika ruangan percakapan telah terselesaikan dan jumlah pesan dalam ruangan dapat berjumlah **lebih dari 10 pesan** oleh agen.

### C. Penilaian Agen (Agent Scoring)[](https://help-center.qontak.com/hc/id/articles/32440281392665-Bagaimana-Cara-Melakukan-Agent-Scoring-pada-Qontak-Chat#h_01HXTKHH9KW708H03E6D26EB3W)
Setelah membuat **kategori parameter** dan mengatur **scorecard** , kini Anda dapat melakukan penilaian. 
**Penting**  
Berikut adalah **syarat sebelum melakukan penilaian** :  
1. Ruangan percakapan harus diselesaikan terlebih dahulu.  
2. Jika ruangan diselesaikan dengan **chatbot** , maka scorecard tidak akan ditampilkan.  
3. Untuk saat ini, apabila terdapat dua agen dalam satu ruangan percakapan, maka skor akan muncul pada agen pertama yang menyapa atau muncul di ruang percakapan.  
4. Anda hanya dapat meninjau skor yang telah dilakukan **1 kali**.
  1. Masuk ke menu **Inbox**.
  2. Klik salah satu pesan yang sudah terselesaikan dengan status **‘Resolved’**.  
![94.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50941930030233)
  3. Kemudian klik tombol **“Agent scorecard”**.  
![95.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50941921107737)
  4. Selanjutnya, berikan nilai pada ruang percakapan berdasarkan kategori yang telah dibuat. Setelah mengisi semua parameter dan mengisi kotak **Remarks** sebagai alasan pemberian rating, klik **“Submit”** maka kartu skor akan menunjukkan nilainya.  
![96.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50941930033177)
- Jika Anda mengaktifkan tombol **Auto Scoring** , maka akan ditampilkan **logo AI**.  
- Anda dapat melakukan penilaian hanya dengan klik **"jempol ke atas"** atau **"jempol ke bawah"**.  
- Anda **wajib** mengisi semua parameter pada kategori untuk dapat mengirimkan skor.
  5. Anda dapat melihat Skor dengan status **Pass** atau **Failed** berdasarkan **Passing grade** yang telah ditetapkan, Tanggal Review, dan Reviewer/Scorer. Anda juga dapat mengedit kartu skor sebanyak **satu kali** dengan klik **“Edit scorecard”**.   
![97.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50941930034969)
  6. Selanjutnya, Anda dapat melihat hasil _score_ dengan klik **“Report”**.  
![15.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774529406873)
  7. Lalu pilih tab **General**.  
![16.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774529408537)
  8. Anda akan melihat hasil laporan pada halaman **List of conversation**. Klik ikon **“Scorecard”** untuk melihat hasil penilaian pada salah satu agen.  
![17.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774535948697)
  9. Maka Anda akan melihat ringkasan penilaian agen yang telah dinilai.  
![18.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774535961881)

Demikian cara melakukan penilaian agen pada **Qontak Chat**. Selanjutnya Anda juga dapat mempelajari lebih lanjut terkait [cara generate API Token](https://help-center.qontak.com/hc/id/articles/21045464958617-Bagaimana-Cara-Generate-API-Token-pada-Qontak-Omnichannel) dan [Mekari Airene](https://help-center.qontak.com/hc/id/articles/17681735789977-Bagaimana-Cara-Menggunakan-Mekari-Airene-pada-Qontak).

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support jika mengalami:

• Tombol Create scorecard atau Add parameter tidak berfungsi
• Scorecard tidak tersimpan meskipun semua kolom wajib sudah diisi
• Tidak dapat mengakses menu Settings → Scorecard
• Parameter yang telah dibuat hilang atau tidak muncul di halaman Scorecard

Siapkan informasi berikut saat menghubungi support:
• Screenshot halaman error
• Nama akun Omnichannel
• Daftar langkah yang sudah dicoba
• Browser dan versi yang digunakan