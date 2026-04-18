---
title: Bagaimana Cara Mengintegrasikan Email
canonical_url: https://help-center.qontak.com/hc/id/articles/5556127164569-Bagaimana-Cara-Mengintegrasikan-Email
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: web
language: id
intent_tags:
- multi-channel-integration
- integrate-email
- conversation-management
query_examples:
- Cara Mengintegrasikan Email
- Bagaimana cara Mengintegrasikan Email?
- Langkah-langkah Mengintegrasikan Email di Qontak Omnichannel
- How do I Mengintegrasikan Email?
- Mau Mengintegrasikan Email, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengintegrasikan email dengan Qontak Omnichannel, Anda memerlukan:

1. **Role Admin** pada akun Qontak Omnichannel (hanya Admin yang dapat melakukan integrasi email)
2. **Akun Qontak Omnichannel** yang aktif
3. **Akun email aktif** dari provider yang didukung (Outlook, Gmail, atau email provider lainnya dengan fitur email forwarder)
4. **Akses ke menu Integrations** di Qontak Omnichannel
5. Jika tidak memiliki role Admin, hubungi tim support di support-qontak@mekari.com untuk bantuan

## Steps  <!-- confidence:high ✓ -->

1. Masuk ke akun Qontak Omnichannel dengan Username dan Password, lalu klik tombol "Sign in".
2. Buka menu **Integrations** dan pilih **Email**.
3. Klik tombol "Add Email" untuk menambahkan akun email baru. Sistem menampilkan form integrasi email.
4. Pada bagian **Select provider**, pilih provider email yang ingin diintegrasikan (Outlook, Gmail, atau lainnya).
5. Pada bagian **Email authentication**, masukkan alamat email dan password provider email Anda.
6. Isi semua field pada bagian **Email configuration** sesuai dengan provider email yang dipilih.
7. Klik tombol "Submit" untuk menyelesaikan integrasi email.## Expected Result  <!-- confidence:high ✓ -->

Setelah klik tombol "Submit", email berhasil diintegrasikan dengan Qontak Omnichannel. Sistem akan menampilkan detail integrasi email termasuk **Penerus Email** (email forwarder). Salin Penerus Email ini, kemudian masuk ke pengaturan email provider Anda dan atur email forwarding otomatis ke alamat Penerus Email yang disediakan. Setelah setup selesai, Admin, Supervisor, dan Agen dapat mengakses email di **Inbox** dalam chat panel Qontak.

![Screenshot_2023-03-31_at_15.21.09.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780202487065)
![9.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F50771056144409)
![email.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780193787929)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780202490393)

## Error States  <!-- confidence:medium ~ -->

Jika ada field yang diisi tidak sesuai format atau belum lengkap, sistem akan secara otomatis menampilkan pesan error. Periksa kembali:

- Alamat email harus valid
- Password provider email harus benar
- Semua field pada Email configuration harus terisi sesuai format yang diminta
- Provider email harus memiliki fitur email forwarder

Jika error persisten, hubungi support-qontak@mekari.com dengan screenshot error dan detail akun email yang digunakan.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak di **support-qontak@mekari.com** dalam situasi berikut:

- Anda tidak memiliki role Admin untuk melakukan integrasi email
- Pesan error tetap muncul setelah memeriksa kembali kredensial dan konfigurasi
- Email provider tidak mendukung fitur email forwarder
- Integrasi email gagal setelah setup email forwarding

Sediakan screenshot error, alamat email yang diintegrasikan (tanpa password), dan detail tentang email provider yang digunakan.