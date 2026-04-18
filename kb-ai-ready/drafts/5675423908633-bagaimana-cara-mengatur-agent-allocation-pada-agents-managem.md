---
title: Bagaimana Cara Mengatur Agent Allocation pada Agents Management
canonical_url: https://help-center.qontak.com/hc/id/articles/5675423908633-Bagaimana-Cara-Mengatur-Agent-Allocation-pada-Agents-Management
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- inquiry-assignment-escalation-agent-management
- configure-agent-allocation
- customer-support-ticketin
query_examples:
- Cara Mengatur Agent Allocation pada Agents Management
- Bagaimana cara Mengatur Agent Allocation pada Agents Management?
- Langkah-langkah Mengatur Agent Allocation pada Agents Management di Qontak Omnichannel
- How do I Mengatur Agent Allocation pada Agents Management?
- Mau Mengatur Agent Allocation pada Agents Management, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.3
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengatur Agent Allocation pada Agents Management, Anda memerlukan:

• Role Admin (hanya Admin yang dapat menambahkan atau mengubah pengaturan Agent Management)
• Akun Qontak Omnichannel aktif
• Akses ke menu Settings
• Pemahaman tentang tiga mode alokasi: manual assignment oleh Supervisor, pengambilan mandiri oleh Agent melalui tombol "Get New Chat", atau distribusi otomatis

## Steps  <!-- confidence:high ✓ -->

1. Masuk ke akun Qontak Omnichannel Anda. Sistem akan menampilkan dashboard Omnichannel.

2. Klik menu Settings, kemudian pilih "Agent Management". Halaman Agent Management akan terbuka dengan beberapa tab pilihan.

3. Klik tab "Agent Allocation". Anda akan melihat tiga toggle pengaturan alokasi.

4. Aktifkan atau nonaktifkan "Agent can takeover unassigned chat" sesuai kebutuhan. Jika diaktifkan, Agent dapat mengambil chat yang belum ditetapkan melalui tombol "Get New Chat" di Inbox mereka.

5. Aktifkan atau nonaktifkan "Agent can assign room to another agent". Jika diaktifkan, tombol Assign akan tersedia untuk Agent reassign obrolan ke Agent lain.

6. Pilih satu dari dua mode otomatis (tidak bisa keduanya):
   - "Auto agent allocation (AAA)": Chat baru dialokasikan otomatis ke Agent online tanpa intervensi Supervisor
   - "Custom agent allocation (CAA)": Agent menerima permintaan custom dari klien

7. Klik "Save" atau tombol konfirmasi untuk menyimpan perubahan. Sistem akan menampilkan konfirmasi bahwa pengaturan Agent Allocation telah diperbarui.

## Expected Result  <!-- confidence:high ✓ -->

Setelah mengatur Agent Allocation dengan berhasil:

• Pengaturan Agent Allocation tersimpan dan aktif segera
• Jika "Agent can takeover unassigned chat" diaktifkan: Tombol "Get New Chat" muncul di Inbox Agent
• Jika dinonaktifkan: Tombol "Get New Chat" tidak muncul; Agent hanya menerima chat dari Supervisor assign
• Jika "Agent can assign room to another agent" diaktifkan: Tombol Assign tersedia di room
• Jika dinonaktifkan: Tombol Assign disable
• Mode AAA atau CAA yang dipilih menentukan bagaimana chat baru didistribusikan ke Agent online

## Error States  <!-- confidence:low ? -->

No common errors documented.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support jika mengalami:

• Tombol Save tidak merespons setelah mengubah pengaturan Agent Allocation
• Toggle pengaturan tidak menyimpan perubahan meskipun sudah diklik
• Pesan error muncul saat mencoba mengaktifkan kedua mode AAA dan CAA sekaligus
• Agent tidak menerima chat meskipun sudah mengaktifkan "Agent can takeover unassigned chat"

Siapkan informasi berikut untuk Support: screenshot pengaturan Agent Allocation, ID akun Omnichannel Anda, langkah yang telah dicoba, dan pesan error (jika ada).