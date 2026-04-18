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

**Langkah-langkah menambahkan Conversation History sebagai pengetahuan Ask Airene:**

1. Masuk ke akun Omnichannel Anda, kemudian pilih menu **AI Resources**.
   - Sistem akan menampilkan halaman manajemen sumber pengetahuan AI.

2. Klik tombol **"Add source"**.
   - Sistem akan menampilkan dialog untuk memilih tipe sumber pengetahuan.

3. Pilih tab **"Conversation history"**.
   - Sistem akan menampilkan opsi untuk memilih Agent.

4. Pilih satu atau lebih Agent yang riwayat percakapannya akan dijadikan sumber pengetahuan AI.
   - AI akan mempelajari percakapan dari 3 bulan terakhir.
   - Anda dapat memilih lebih dari satu Agent tanpa validasi.

5. Klik tombol **"Save"**.
   - Sistem akan menampilkan notifikasi status "Processing" dan mulai memproses riwayat percakapan (biasanya 1-1,5 jam).

## Expected Result  <!-- confidence:high ✓ -->

Setelah menyelesaikan langkah-langkah di atas, Anda akan melihat:

1. Notifikasi status **"Processing"** muncul di halaman AI Resources, menunjukkan bahwa riwayat percakapan Agent sedang diproses oleh sistem.

2. Setelah proses selesai, status akan berubah menjadi "Active" atau "Ready".

3. Ask Airene sekarang memiliki pengetahuan dari percakapan Agent yang dipilih dan siap untuk memberikan rekomendasi otomatis ketika Anda merespons klien di menu **Inbox** Omnichannel.

4. Semakin akurat percakapan yang dilakukan oleh Agent, semakin akurat informasi yang dipelajari oleh AI.

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