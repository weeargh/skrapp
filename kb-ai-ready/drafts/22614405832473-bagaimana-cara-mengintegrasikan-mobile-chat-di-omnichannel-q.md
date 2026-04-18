---
title: Bagaimana Cara Mengintegrasikan Mobile Chat di Omnichannel Qontak
canonical_url: https://help-center.qontak.com/hc/id/articles/22614405832473-Bagaimana-Cara-Mengintegrasikan-Mobile-Chat-di-Omnichannel-Qontak
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
product_surface: mobile
language: id
intent_tags:
- multi-channel-integration
- conversation-management
query_examples:
- Cara Mengintegrasikan Mobile Chat di Omnichannel Qontak
- Bagaimana cara Mengintegrasikan Mobile Chat di Omnichannel Qontak?
- Langkah-langkah Mengintegrasikan Mobile Chat di Omnichannel Qontak di Qontak Omnichannel
- How do I Mengintegrasikan Mobile Chat di Omnichannel Qontak?
- Mau Mengintegrasikan Mobile Chat di Omnichannel Qontak, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.3
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengintegrasikan Mobile Chat di Omnichannel Qontak, Anda membutuhkan:

- Role Admin di akun Qontak Omnichannel
- Akses ke menu Integrations
- Aplikasi mobile yang sedang dikembangkan (Android dan/atau iOS)
- Package name untuk aplikasi Android
- Bundle ID untuk aplikasi iOS
- Tim developer yang siap memasukkan App ID, Client ID, dan Secret Key ke sistem aplikasi Anda

## Steps  <!-- confidence:high ✓ -->

**Instalasi Widget:**

1. Buka menu **Integrations** di Qontak Omnichannel.
2. Pilih tab **Mobile chat**, lalu klik tombol **Create chat widget**. Sistem akan menampilkan formulir pembuatan widget.
3. Masukkan **App name** sesuai nama aplikasi Anda. Sistem akan menerima input nama tersebut.
4. Pilih sistem operasi (Android dan/atau iOS). Anda dapat menambah OS lain dengan klik **Add operating system**.
5. Masukkan **Package name** (Android) dan **Bundle ID** (iOS), lalu klik **Create**. Sistem akan menyimpan widget dan menampilkan detail teknis: App ID, Client ID, Secret Key.
6. Bagikan ketiga detail tersebut kepada tim developer untuk diintegrasikan ke aplikasi Anda.

**Mengubah Tampilan Widget:**

1. Pada daftar app yang telah dibuat, klik **Action** → **Edit**.
2. Klik **Widget content & appearance**. Sistem akan menampilkan form pengaturan tampilan.
3. Ubah **Display name**, **Description**, **Greetings**, dan **Appearance** (warna). Klik simpan untuk menerapkan perubahan.## Expected Result  <!-- confidence:high ✓ -->

Setelah langkah instalasi selesai:

- Widget berhasil dibuat dengan status aktif di daftar Mobile chat
- Detail teknis (App ID, Client ID, Secret Key) tersedia untuk diberikan kepada tim developer
- Setelah tim developer mengintegrasikan detail tersebut ke kode aplikasi, fitur Mobile Chat akan tersedia di aplikasi mobile Anda
- Pelanggan dapat membuka chat dari aplikasi tanpa membuka WhatsApp terpisah
- Tampilan chat akan sesuai dengan konfigurasi Display name, warna, dan greeting yang telah Anda atur

![pasted image 0 \(43\).png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781184476825)
![pasted image 0 \(44\).png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781184478873)
![pasted image 0 \(45\).png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781184470169)
![pasted image 0 \(46\).png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781184477465)
![pasted image 0 \(47\).png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781142879257)
![pasted image 0 \(48\).png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781184470681)
![pasted image 0 \(49\).png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781142881049)
![pasted image 0 \(50\).png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781184479513)
![pasted image 0 \(51\).png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781184471833)
![pasted image 0 \(52\).png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781184474649)

## Error States  <!-- confidence:low ? -->

No common errors documented.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim Qontak Support (support-qontak@mekari.com) jika:

- Anda tidak dapat menemukan tab **Mobile chat** di menu Integrations
- Widget gagal disimpan setelah klik **Create**
- Tim developer mengalami kesulitan saat mengintegrasikan App ID, Client ID, atau Secret Key
- Mobile Chat tidak muncul di aplikasi setelah integrasi teknis selesai
- Terdapat error teknis yang tidak dijelaskan dalam dokumentasi

Sertakan screenshot, App ID, dan deskripsi masalah saat menghubungi support.