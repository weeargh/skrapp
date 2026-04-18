---
title: Bagaimana Cara Assign Campaign ke Division atau Agent
canonical_url: https://help-center.qontak.com/hc/id/articles/5699768083609-Bagaimana-Cara-Assign-Campaign-ke-Division-atau-Agent
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- campaign-management
- marketing-campaign-manage
query_examples:
- Cara Assign Campaign ke Division atau Agent
- Bagaimana cara Assign Campaign ke Division atau Agent?
- Langkah-langkah Assign Campaign ke Division atau Agent di Qontak Omnichannel
- How do I Assign Campaign ke Division atau Agent?
- Mau Assign Campaign ke Division atau Agent, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk assign campaign ke Division atau Agent, Anda memerlukan:

• Akun Qontak Omnichannel atau Qontak Chat aktif dengan role Admin
• Akses ke menu Campaign pada halaman WhatsApp
• Division sudah dibuat sebelumnya di Settings → Agent Management → Division (jika belum ada, buat Division terlebih dahulu)
• Supervisor dan Agent sudah ditambahkan ke Division yang akan menerima assignment
• Template campaign sudah tersedia untuk dipilih

## Steps  <!-- confidence:high ✓ -->

1. Login ke akun Qontak Omnichannel atau Qontak Chat Anda.
2. Buka menu Campaign pada halaman WhatsApp.
3. Klik tombol **Create campaign**. Sistem akan menampilkan formulir pembuatan campaign.
4. Isi kolom Campaign name, Sender, Recipient list, dan Template sesuai kebutuhan.
5. Pada bagian Campaign assignment, pilih opsi **Division** dari dropdown menu.
6. Pilih Division tujuan dari daftar yang tersedia. Hanya Agent di Division terpilih yang dapat mengelola campaign ini.
7. Verifikasi semua informasi sudah benar.
8. Klik tombol **Send campaign**. Sistem akan mengirimkan campaign ke Division yang ditunjuk.## Expected Result  <!-- confidence:medium ~ -->

Setelah Anda mengklik tombol Send campaign, sistem akan memproses pengiriman campaign ke Division yang telah dipilih. Campaign akan muncul di dashboard campaign dengan status pengiriman. Hanya Agent dan Supervisor dalam Division terpilih yang dapat melihat, mengelola, dan memantau hasil dari campaign tersebut. Anda akan menerima konfirmasi bahwa campaign telah berhasil di-assign ke Division.

![2.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F43824013886617)
![3.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F43824013888025)
![4.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F43824013888665)
![5.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F43824013889177)
![6a.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36774533912089)

## Error States  <!-- confidence:medium ~ -->

• Division belum dibuat: Jika dropdown Division kosong atau tidak ada pilihan, buat Division terlebih dahulu di Settings → Agent Management → Division dengan mengklik tombol **Create Division**, masukkan Nama division, pilih Supervisor, dan pilih Agent, kemudian klik **Create**.
• Agent tidak terlihat di Division: Pastikan Agent sudah ditambahkan ke Division saat pembuatan atau editing Division. Division General (default) mencakup semua user/supervisor/agent.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support jika:

• Campaign tidak berhasil terkirim setelah mengklik tombol Send campaign
• Division tidak muncul di dropdown Campaign assignment meskipun sudah dibuat
• Error message muncul saat proses assignment

Sediakan informasi: screenshot formulir campaign, nama Division yang digunakan, daftar Agent dalam Division, dan waktu percobaan assignment.