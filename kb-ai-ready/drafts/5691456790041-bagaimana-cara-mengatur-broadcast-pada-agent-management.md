---
title: Bagaimana Cara Mengatur Broadcast pada Agent Management
canonical_url: https://help-center.qontak.com/hc/id/articles/5691456790041-Bagaimana-Cara-Mengatur-Broadcast-pada-Agent-Management
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- inquiry-assignment-escalation-agent-management
- configure-broadcast
- customer-support-ticketin
query_examples:
- Cara Mengatur Broadcast pada Agent Management
- Bagaimana cara Mengatur Broadcast pada Agent Management?
- Langkah-langkah Mengatur Broadcast pada Agent Management di Qontak Omnichannel
- How do I Mengatur Broadcast pada Agent Management?
- Mau Mengatur Broadcast pada Agent Management, caranya gimana?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.3
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengatur fitur Broadcast pada Agent Management, Anda membutuhkan:

• Role Admin (hanya Admin yang dapat mengubah pengaturan Agent Management)
• Akses ke akun Omnichannel Qontak yang aktif
• Menu Settings > Agent Management tersedia di dashboard
• Agen sudah terdaftar dalam sistem Qontak Anda

Perhatikan bahwa mengaktifkan fitur Agent can broadcast akan secara otomatis mengaktifkan Multi-Factor Authentication (MFA) untuk semua user dengan peran Agent. Pastikan Anda siap menerapkan persyaratan OTP login untuk semua agen.

## Steps  <!-- confidence:high ✓ -->

1. Masuk ke akun Omnichannel Qontak Anda.
   Sistem akan menampilkan dashboard utama.

2. Klik menu Settings di navigasi utama.
   Halaman pengaturan akan terbuka.

3. Pilih Agent Management dari submenu.
   Daftar fitur Agent Management akan ditampilkan.

4. Klik tab Broadcast.
   Halaman pengaturan Broadcast akan muncul.

5. Klik toggle ON/OFF pada opsi Agent can broadcast untuk mengaktifkan atau menonaktifkan fitur.
   Status toggle akan berubah.

6. Klik tombol Save untuk menyimpan perubahan.
   Sistem akan menampilkan konfirmasi penyimpanan.

## Expected Result  <!-- confidence:high ✓ -->

Setelah mengaktifkan fitur Broadcast dengan status ON:

• Menu Broadcast akan muncul pada halaman Agent untuk semua pengguna dengan peran Agent.
• Agen dapat melakukan broadcast layaknya Supervisor dan Admin.
• Multi-Factor Authentication (MFA) akan secara otomatis aktif untuk semua pengguna dengan peran Agent.
• Setiap kali agen login, mereka akan diminta memasukkan OTP yang dikirim ke email terdaftar.

Jika status Broadcast dalam kondisi OFF:

• Menu Broadcast tidak akan muncul pada halaman Agent.
• Agen tidak dapat melakukan broadcast.

## Error States  <!-- confidence:low ? -->

No common errors documented.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika mengalami:

• Toggle ON/OFF pada opsi Agent can broadcast tidak merespons saat diklik.
• Tombol Save tidak berfungsi setelah mengubah pengaturan Broadcast.
• MFA tidak aktif secara otomatis setelah mengaktifkan Agent can broadcast.
• Menu Broadcast tidak muncul pada halaman Agent meskipun sudah diaktifkan dan perubahan tersimpan.

Sediakan informasi: ID akun Omnichannel, screenshot halaman Agent Management, dan deskripsi masalah yang dialami.