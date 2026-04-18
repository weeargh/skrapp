---
title: Bagaimana Penerapan Ask Airene pada Mekari Qontak Omnichannel
canonical_url: https://help-center.qontak.com/hc/id/articles/40980025881497-Bagaimana-Penerapan-Ask-Airene-pada-Mekari-Qontak-Omnichannel
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- agent-productivity
- ai-chatbot-automation
query_examples:
- Cara Ask Airene pada Mekari Qontak Omnichannel
- Bagaimana cara Ask Airene pada Mekari Qontak Omnichannel?
- Langkah-langkah Ask Airene pada Mekari Qontak Omnichannel di Qontak Omnichannel
- How do I Ask Airene pada Mekari Qontak Omnichannel?
- Mau Ask Airene pada Mekari Qontak Omnichannel, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Sebelum menerapkan Ask Airene pada Mekari Qontak Omnichannel, pastikan Anda memenuhi persyaratan berikut:

1. Akun Mekari Qontak Omnichannel aktif dan dapat diakses
2. Fitur Ask Airene sudah diaktifkan untuk Organisasi atau CID Anda (fitur ini masih dalam tahap BETA dan hanya tersedia untuk beberapa pengguna)
3. Akses ke menu "AI Resources" dalam dashboard Omnichannel
4. Minimal satu Agent dengan riwayat percakapan minimal 3 bulan terakhir untuk dijadikan sumber pengetahuan AI
5. Koneksi internet stabil untuk menunggu proses pemrosesan pengetahuan AI

## Steps  <!-- confidence:high ✓ -->


**Penting  
** Fitur ini masih dalam tahap **BETA** dan hanya diaktifkan ke beberapa Organisasi atau CID tertentu.**  
**
Kini Mekari Qontak Omnichannel menghadirkan fitur bernama **Ask Airene** yang akan membantu Anda sebagai Agent untuk memberikan respon secara otomatis pada klien. Dengan **Ask Airene** , Anda akan mendapatkan pengalaman langsung menggunakan AI dan beralih dari merespon secara manual menjadi otomatis dengan mendapatkan bantuan secara parsial oleh AI. 
Pada tutorial berikut, Anda akan mempelajari mulai dari cara menambahkan **Conversation history** sebagai **pengetahuan AI** hingga proses interaksi dengan **Ask Airene** dalam **room conversation** di menu **Inbox** Omnichannel. Simak lebih lanjut alur penerapannya di bawah ini.
### A. Menambahkan Conversation History sebagai Sumber Pengetahuan Airene[](https://help-center.qontak.com/hc/id/articles/40980025881497-Bagaimana-Penerapan-Ask-Airene-pada-Mekari-Qontak-Omnichannel#h_01JEQ552QYPM1SEJC4FD54GQ0Z)
Penerapan Ask Airene dapat dimulai dengan menambahkan **Conversation History**. Hal ini bertujuan untuk mendapatkan lebih banyak informasi melalui riwayat percakapan sehingga Airene dapat mempelajarinya lebih lanjut. Berikut langkah-langkahnya.
  1. Masuk ke akun **Omnichannel** Anda, lalu pilih menu **Ai Resources**.
  2. Kemudian, klik **“Add source”**.  
![1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F40980025806873)
  3. Lalu pilih tab **“Conversation history”**.  
![2.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F40980025809945)
  4. Selanjutnya pilih **Agent** yang akan dipilih riwayat percakapannya sebagai sumber pengetahuan untuk AI pelajari.  
![3.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F40980025811353)

- Riwayat percakapan akan dipelajari oleh AI mulai dari **3 bulan terakhir** sejak riwayat percakapan muncul.  
- Semakin akurat percakapan yang dilakukan oleh Agent, maka akan semakin akurat informasi yang dipelajari dan didapat oleh AI.  
- Anda dapat memilih **lebih dari satu** Agent untuk menambah pengetahuan pada AI (tanpa validasi).
  5. Kemudian klik **“Save”**.  
![4.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F40980025814041)
  6. Lalu akan muncul notifikasi berikut yang menyatakan bahwa riwayat percakapan sedang diproses untuk dipelajari oleh AI. Anda diminta untuk menunggu beberapa saat selama status dalam tahap **‘Processing’**.  
![5.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F40980025815961)

- Proses pembuatan pengetahuan untuk AI biasanya memakan banyak waktu karena bergantung pada ruang percakapan yang ditangani Agent sebelumnya. (biasanya dapat mencapai hingga**1 setengah jam**).  
- Anda **hanya dapat** membuat **satu sumber** dari Riwayat Percakapan. Apabila Anda ingin memperbarui pengetahuan (dalam hal ini memilih Agent yang berbeda), untuk saat ini, pengguna harus menghapus pengetahuan riwayat percakapan terlebih dahulu, lalu mengirimkan ulang/menambahkan kembali pengetahuan dengan Agent yang telah diperbarui.![3.2.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F40980025819545)
  7. Selanjutnya setelah status berubah menjadi **‘Active’** maka AI sudah berhasil menyerap informasi yang terdapat pada riwayat percakapan.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F40980025821849)

### B. Interaksi dengan Ask Airene pada Room Conversation di Menu Inbox[](https://help-center.qontak.com/hc/id/articles/40980025881497-Bagaimana-Penerapan-Ask-Airene-pada-Mekari-Qontak-Omnichannel#h_01JEQ552QYMFCSV32AW6ERCD9K)
Setelah menambahkan **Conversation history** sebagai pengetahuan untuk AI, maka Anda secara otomatis dapat merasakan pengalaman berinteraksi dengan Ask Airene pada**Room Conversation** yang terdapat di menu **Inbox** Omnichannel. Simak penjelasan selengkapnya berikut ini.
**Penting  
** Berikut hal-hal yang dapat dilakukan Airene dalam percakapan:  
1. Menampilkan jawaban saran berdasarkan pertanyaan pelanggan.  
2. Menanggapi pertanyaan sesuai dengan pengetahuan yang telah dilatih dengan kondisi sebagai berikut:  
- Hanya pertanyaan terkait dengan percakapan yang dapat dijawab.  
- Airene akan melihat jawaban dari data yang telah dilatih (**PDF** , **URL** , atau **Conversation history**).  
- Jika Airene tidak dapat menjawab pertanyaan, maka akan ditampilkan pesan konten yang menyatakan bahwa Airene tidak dapat menemukan jawabannya (kondisi ini berbeda dengan Chatbot AI).
  1. Masuk ke menu **Inbox** pada Qontak Omnichannel.
  2. Kemudian di sebelah kanan (tepatnya di dekat sisi detail kontak), klik **ikon Ask Airene** untuk membuka panel.  
![7.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F40980010636441)
  3. Selain itu Anda juga dapat mengakses **Ask Airene** melalui tombol yang terletak di bagian bawah obrolan pelanggan. Hal ini akan memicu **Pertanyaan yang disarankan** di mana Airene akan mendeteksi pesan pelanggan untuk membuat pertanyaan. Setelah itu Anda dapat mulai berinteraksi dengan **Ask Airene** hingga ruang tersebut terselesaikan.  
![8.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F40980010638873)
  4. Untuk dapat menggunakan saran pertanyaan yang telah dibuat, klik tombol **panah** pada pertanyaan yang disarankan.  
![9.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F40980025834009)
  5. Saat menjawab pertanyaan, Airene juga dapat membagikan sumber jawabannya.  
![10.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F40980010650905)
  6. Anda juga dapat menggunakan jawaban Airene untuk menjawab pertanyaan pelanggan dengan klik **“Use Response”** sehingga jawaban akan ditampilkan di kotak percakapan.  
![11.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F40980010678681)
  7. Anda juga dapat mengajukan pertanyaan lanjutan secara berkala kepada Airene. Panel di sisi samping Airene hanya akan aktif hingga ruangan tersebut terselesaikan.

Demikian penerapan Ask Airene pada Mekari Qontak Omnichannel.

## Error States  <!-- confidence:medium ~ -->

Kondisi kesalahan yang mungkin terjadi:

1. **Status Processing terlalu lama (>1,5 jam)**: Proses pembuatan pengetahuan AI bergantung pada volume ruang percakapan yang ditangani Agent. Tunggu lebih lama atau hubungi dukungan jika melampaui waktu yang ditentukan.

2. **Tidak dapat menambah sumber baru**: Sistem hanya memungkinkan satu sumber dari Riwayat Percakapan per organisasi. Jika ingin memperbarui, hapus sumber lama terlebih dahulu sebelum membuat yang baru.

3. **Ask Airene tidak aktif**: Fitur ini masih BETA dan hanya diaktifkan untuk beberapa CID tertentu. Hubungi dukungan untuk mengaktifkannya.

## Escalation  <!-- confidence:medium ~ -->

Hubungi dukungan Mekari Qontak jika mengalami:

1. Fitur Ask Airene tidak tersedia di akun Anda meskipun memenuhi persyaratan (sediakan: CID/Organization ID, screenshot dashboard).

2. Proses "Processing" terhenti atau tidak selesai setelah 2 jam (sediakan: screenshot status, waktu dimulai, daftar Agent yang dipilih).

3. Ask Airene tidak menampilkan rekomendasi dalam room conversation setelah selesai processing (sediakan: screenshot, deskripsi pesan customer, nama Agent yang data-nya diproses).

4. Error atau pesan tidak jelas saat menyimpan sumber pengetahuan (sediakan: screenshot error message lengkap).