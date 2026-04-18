---
title: Logout Otomatis untuk Keamanan Anda (Qontak Web & Mobile)
canonical_url: https://help-center.qontak.com/hc/id/articles/50356345374489-Logout-Otomatis-untuk-Keamanan-Anda-Qontak-Web-Mobile
article_type: concept
solvability_type: content
products:
- Qontak CRM
- Qontak Omnichannel
product_surface: mobile
language: id
intent_tags:
- account
- general-platform
query_examples:
- Apa itu Logout Otomatis untuk Keamanan Anda (Qontak Web & Mobile)?
- Apa fungsi Logout Otomatis untuk Keamanan Anda (Qontak Web & Mobile) di Qontak CRM?
- Penjelasan Logout Otomatis untuk Keamanan Anda (Qontak Web & Mobile)
- What is Logout Otomatis untuk Keamanan Anda (Qontak Web & Mobile)?
- Bagaimana cara kerja Logout Otomatis untuk Keamanan Anda (Qontak Web & Mobile)?
compliance_sensitive: true
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Definition  <!-- confidence:high ✓ -->

Logout otomatis adalah mekanisme keamanan dalam Mekari Qontak yang secara otomatis mengeluarkan pengguna dari akun mereka setelah periode tidak aktif tertentu. Fitur ini berlaku pada aplikasi web Qontak CRM dan Qontak Omnichannel untuk melindungi data akun dari akses tidak sah, terutama pada perangkat bersama atau perangkat yang hilang atau dicuri. Durasi timeout berbeda tergantung platform: Omnichannel Web App logout setelah 1 jam tidak aktif, sementara CRM Web App logout setelah 6 jam tidak aktif. Aplikasi mobile Qontak Chat tidak menerapkan logout otomatis dan menggunakan fitur auto refresh token untuk mempertahankan sesi.

## Why It Matters  <!-- confidence:high ✓ -->

Logout otomatis melindungi keamanan akun Qontak Anda dengan mengurangi risiko akses tidak sah ketika Anda lupa keluar atau meninggalkan perangkat tanpa sengaja. Fitur ini sangat penting untuk pengguna yang bekerja di lingkungan bersama atau menggunakan perangkat yang dapat diakses oleh orang lain. Dengan menerapkan timeout yang berbeda untuk setiap aplikasi, Qontak menyeimbangkan keamanan dengan produktivitas—memberikan waktu cukup untuk sesi kerja berkelanjutan di CRM sambil menjaga keamanan lebih ketat di Omnichannel.

## Key Attributes  <!-- confidence:high ✓ -->

• **Omnichannel Web App**: Logout otomatis setelah 1 jam tanpa aktivitas; timer direset dengan setiap interaksi pengguna
• **CRM Web App**: Logout otomatis setelah 6 jam tanpa aktivitas; timer direset dengan setiap interaksi pengguna
• **Qontak Chat Mobile App**: Tidak ada logout otomatis; menggunakan auto refresh token untuk mempertahankan sesi di latar belakang
• **Aktivitas terpantau**: Interaksi dengan aplikasi (klik, input, navigasi) mereset penghitung timeout
• **Redirect otomatis**: Setelah logout, sistem mengarahkan pengguna ke halaman login

## Related Tasks  <!-- confidence:medium ~ -->

• Bagaimana Cara Mengubah Info Pribadi pada Qontak Omnichannel
• Bagaimana Cara Mengubah Info Pribadi pada Qontak CRM
• Overview Supervisor Access (untuk memahami konteks keamanan berbasis peran di Qontak)