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


**Agent Management - Broadcast** merupakan sebuah fitur Omnichannel Qontak yang terdiri dari **Division** , **Agent Allocation, Broadcast** dan **Workload** dimana hanya Admin yang bisa menambahkan atau melakukan perubahan pada fitur yang ada pada agents management.
Untuk menampilkan menu broadcast pada halaman Agent, Anda perlu mengikuti langkah-langkah berikut:
  1. Masuk ke akun Omnichannel Anda. 
  2. Pilih menu **Settings** , kemudian klik **Agent Management.  
![1.1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F38953072708249)  
**
  3. Pilih “**Broadcast** ” dan klik _toggle_ “**ON/OFF** ” pada pilihan **Agent can broadcast**. Klik “**Save** ” untuk menyimpan perubahan yang dilakukan.
![1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F38953027384729)
- Apabila Anda mengaktifkan fitur **Agent can broadcast** , maka fitur **MFA** akan secara otomatis aktif kepada semua user dengan peran Agent.  
- Saat ini terdapat pengaktifan **Multi-Factor Authentication (MFA)** dapat membantu Anda dalam menjaga keamanan data yang Anda miliki di Qontak. Jika Anda dengan role tertentu telah mengaktifkan MFA, maka setiap melakukan login, Anda akan diminta untuk memasukkan OTP yang dikirim ke email.  
- Apabila broadcast dalam status “**ON** ” maka menu tersebut akan muncul pada halaman agent sehingga agent bisa melakukan broadcast layaknya Supervisor dan Admin, namun jika broadcast dalam status “**OFF** ” maka agent tersebut tidak bisa melakukan broadcast karena menu broadcast tidak akan muncul pada halaman Agent.

## Error States  <!-- confidence:low ? -->

No common errors documented.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika mengalami:

• Toggle ON/OFF pada opsi Agent can broadcast tidak merespons saat diklik.
• Tombol Save tidak berfungsi setelah mengubah pengaturan Broadcast.
• MFA tidak aktif secara otomatis setelah mengaktifkan Agent can broadcast.
• Menu Broadcast tidak muncul pada halaman Agent meskipun sudah diaktifkan dan perubahan tersimpan.

Sediakan informasi: ID akun Omnichannel, screenshot halaman Agent Management, dan deskripsi masalah yang dialami.