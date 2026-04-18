---
title: Bagaimana Cara Agent Handover Chat Versi Web
canonical_url: https://help-center.qontak.com/hc/id/articles/5894603902745-Bagaimana-Cara-Agent-Handover-Chat-Versi-Web
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- inquiry-assignment-escalation-agent-management
- customer-support-ticketin
query_examples:
- Cara Agent Handover Chat Versi Web
- Bagaimana cara Agent Handover Chat Versi Web?
- Langkah-langkah Agent Handover Chat Versi Web di Qontak Omnichannel
- How do I Agent Handover Chat Versi Web?
- Mau Agent Handover Chat Versi Web, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:medium ~ -->

Anda ingin melakukan Handover Chat kepada agent lain melalui versi web Qontak Omnichannel. Sebelum memulai, pastikan:

• Anda memiliki akun Qontak Omnichannel yang aktif
• Anda memiliki role Agent atau lebih tinggi (minimal dapat mengakses fitur Inbox)
• Fitur Agent Allocation telah diaktifkan oleh Admin (konfigurasi "Agent can assign room to another agent" pada Settings > Agent Management)
• Sudah ada minimal 2 agent dalam sistem untuk melakukan handover
• Chat atau percakapan yang akan di-handover memiliki status tertentu yang memungkinkan reassignment

## Steps  <!-- confidence:high ✓ -->

1. Masuk ke akun Qontak Omnichannel Anda melalui web browser.
2. Navigasikan ke menu Inbox, kemudian klik submenu "All chats".
3. Pilih Room Percakapan yang ingin Anda handover ke agent lain. Sistem akan membuka detail percakapan.
4. Pada pesan atau room percakapan tersebut, klik tombol "Assign".
5. Pilih nama Agent dari daftar yang tersedia untuk menerima handover chat.
6. Klik tombol konfirmasi untuk menyelesaikan proses Handover Chat.
Agent yang ditunjuk akan menerima notifikasi tentang percakapan yang telah di-assign kepada mereka.

## Expected Result  <!-- confidence:medium ~ -->

Setelah berhasil melakukan Handover Chat:

• Room Percakapan akan dialihkan dari Agent sebelumnya ke Agent baru yang ditunjuk
• Status assignment pada percakapan akan menunjukkan nama Agent penerima
• Agent penerima akan melihat percakapan muncul di daftar chat mereka di menu Inbox
• Riwayat handover akan tercatat dalam history percakapan untuk audit trail
• Pelanggan tidak melihat perubahan ini namun percakapan akan dilanjutkan oleh Agent baru

## Error States  <!-- confidence:medium ~ -->

Masalah umum saat Handover Chat:

• **Tombol "Assign" tidak muncul**: Fitur handover mungkin belum diaktifkan di Agent Allocation settings. Minta Admin untuk mengaktifkan opsi "Agent can assign room to another agent" di Settings > Agent Management.
• **Percakapan tidak bisa di-handover**: Pastikan pesan memiliki status yang mendukung reassignment. Pesan dengan status tertentu (misalnya closed atau archived) mungkin tidak dapat di-handover.
• **Agent target tidak muncul di daftar**: Periksa bahwa Agent target aktif dan memiliki akses ke channel/menu yang sama dengan percakapan.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika:

• Tombol "Assign" tidak tersedia meskipun fitur sudah diaktifkan di Agent Allocation
• Handover berhasil dilakukan tetapi Agent target tidak menerima percakapan
• Terjadi error saat mengklik tombol "Assign" dengan pesan error tertentu

Siapkan informasi berikut saat menghubungi support:
• Screenshot dari room percakapan dan tombol "Assign"
• ID percakapan atau Room Percakapan yang bermasalah
• Nama Agent pengirim dan Agent penerima
• Waktu terjadinya masalah dan pesan error lengkap (jika ada)