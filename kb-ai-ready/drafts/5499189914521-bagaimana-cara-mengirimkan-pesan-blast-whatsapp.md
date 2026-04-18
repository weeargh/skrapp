---
title: Bagaimana Cara Mengirimkan Pesan Blast WhatsApp
canonical_url: https://help-center.qontak.com/hc/id/articles/5499189914521-Bagaimana-Cara-Mengirimkan-Pesan-Blast-WhatsApp
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- campaign
- send-pesan-blast-whatsapp
- marketing-campaign-manage
query_examples:
- Cara Mengirimkan Pesan Blast WhatsApp
- Bagaimana cara Mengirimkan Pesan Blast WhatsApp?
- Langkah-langkah Mengirimkan Pesan Blast WhatsApp di Qontak Omnichannel
- How do I Mengirimkan Pesan Blast WhatsApp?
- Mau Mengirimkan Pesan Blast WhatsApp, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengirimkan pesan Blast WhatsApp, Anda memerlukan:

• Akun Qontak Omnichannel atau Qontak Chat yang aktif
• Akses ke menu Campaigns dengan produk WhatsApp
• Nomor WhatsApp Business yang sudah terhubung ke Qontak
• Daftar kontak penerima (Recipient list)
• Template pesan WhatsApp yang sudah dibuat sebelumnya
• Saldo WhatsApp balance yang mencukupi untuk jumlah kontak yang akan menerima broadcast
• Izin untuk mengakses fitur Campaign pada akun Qontak Anda

## Steps  <!-- confidence:high ✓ -->

1. Login ke akun Qontak Omnichannel Anda. Halaman dashboard akan ditampilkan.

2. Buka menu Campaigns, lalu pilih "WhatsApp". Daftar campaign WhatsApp akan muncul.

3. Klik tombol "New campaign Message". Form pembuatan campaign baru akan terbuka.

4. Isi semua kolom yang tersedia: nama campaign (Campaign name), pengirim (Sender), daftar penerima (Recipient list), dan pilih template pesan. Sistem akan menampilkan sisa saldo WhatsApp balance di sisi kanan.

5. Tambahkan isi pesan (Content message) termasuk media header jika diperlukan, dan lakukan variable mapping untuk personalisasi konten.

6. Centang "Select division" untuk menentukan divisi yang akan mengirim campaign.

7. Pilih jadwal pengiriman: "Send now" untuk langsung atau "Send later" untuk dijadwalkan. Klik tombol "Send campaign". Notifikasi pop-up akan muncul untuk konfirmasi pengiriman.## Expected Result  <!-- confidence:high ✓ -->

Setelah campaign berhasil dikirim, notifikasi pop-up konfirmasi akan muncul menampilkan bahwa campaign telah berhasil diproses. Campaign akan muncul di daftar Campaigns dengan status pengiriman (Send now atau terjadwal di waktu yang ditentukan). Anda dapat memantau status pengiriman melalui Campaign Logs di halaman detail campaign. Pesan akan dikirimkan ke semua kontak dalam Recipient list yang telah ditentukan sesuai Template Pacing WhatsApp yang berlaku sejak 12 Oktober 2023.

![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F43703581240729)
![tes1234.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36776243511577)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F43703628949273)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F43703628955033)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F43703628958489)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F43703581255833)

## Error States  <!-- confidence:high ✓ -->

Notifikasi "field is required" muncul ketika Anda meninggalkan kolom wajib yang belum diisi (Campaign name, Sender, Recipient list, atau Template). Isi semua kolom yang ditandai sebelum mengirim.

Pop-up notifikasi "Top Up" muncul ketika saldo WhatsApp balance Anda kurang dari jumlah kontak yang akan menerima broadcast. Klik tombol "Top Up" untuk menambah saldo sebelum melanjutkan pengiriman.

Gagal terkirim dapat juga terjadi karena Messaging Limit exceeded, kategori template Marketing dengan aturan lebih ketat, atau penerima yang tidak memberikan opt-in consent. Periksa Campaign Logs untuk detail error spesifik.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim Qontak support jika Anda mengalami:

• Campaign gagal terkirim meskipun saldo dan data lengkap (siapkan Campaign Logs screenshot)
• Notifikasi error yang tidak jelas atau tidak sesuai dengan kondisi akun
• Template pesan menunjukkan status "Not Connected" atau "Low Quality" padahal sudah pernah berhasil sebelumnya
• Messaging Limit terus meningkat tanpa alasan yang jelas

Sediakan informasi berikut saat menghubungi support: ID campaign, daftar error messages dari Campaign Logs, jumlah kontak penerima, dan screenshot halaman campaign.