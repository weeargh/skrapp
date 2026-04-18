---
title: Bagaimana Cara Mengelola Idle Rule Settings Qontak Omnichannel
canonical_url: https://help-center.qontak.com/hc/id/articles/27247787602969-Bagaimana-Cara-Mengelola-Idle-Rule-Settings-Qontak-Omnichannel
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- settings
- manage-idle-rule-settings-qontak-omni
- general-platform
query_examples:
- Cara Mengelola Idle Rule Settings Qontak Omnichannel
- Bagaimana cara Mengelola Idle Rule Settings Qontak Omnichannel?
- Langkah-langkah Mengelola Idle Rule Settings Qontak Omnichannel di Qontak Omnichannel
- How do I Mengelola Idle Rule Settings Qontak Omnichannel?
- Mau Mengelola Idle Rule Settings Qontak Omnichannel, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengelola Idle Rule Settings di Qontak Omnichannel, Anda memerlukan:

• Akun Mekari Qontak Omnichannel aktif
• Akses dengan role Admin atau izin untuk mengelola pengaturan akun
• Minimal satu Agent terdaftar dalam sistem
• Akses ke menu Settings pada dashboard Qontak Omnichannel

Idle Rule Settings digunakan untuk mengatur mekanisme reassign chat ketika Agent tidak merespons dalam periode waktu tertentu.

## Steps  <!-- confidence:high ✓ -->

1. Masuk ke dashboard Qontak Omnichannel dan klik menu **Settings**. Sistem akan menampilkan halaman pengaturan akun.

2. Pilih **Agent Management** dari menu Settings. Halaman Agent Management akan terbuka dengan beberapa tab pilihan.

3. Klik tab **Idle rule**. Anda akan melihat opsi untuk mengaktifkan fitur Idle Rule.

4. Centang checkbox **Enable idle rule** untuk mengaktifkan fitur. Checkbox akan menunjukkan status tercentang (✓).

5. Isi kolom **Idle period** dengan nilai dalam hitungan menit (contoh: 5 menit, 10 menit). Input field akan menampilkan nilai yang Anda masukkan.

6. Klik tombol **Save changes** untuk menyimpan pengaturan. Sistem akan memproses dan menyimpan konfigurasi Idle Rule Anda.

## Expected Result  <!-- confidence:high ✓ -->

Setelah berhasil menyimpan Idle Rule Settings:

• Idle Rule aktif dan diterapkan ke seluruh akun Omnichannel
• Chat yang tidak direspons Agent dalam periode waktu yang ditentukan akan secara otomatis di-reassign ke Agent lain
• Sistem akan melakukan pencarian Agent pengganti hingga 3 kali (setiap kali menunggu durasi Idle period yang telah ditetapkan)
• Jika semua Agent penuh atau tidak tersedia setelah 3 kali pencarian, chat akan ter-hold sampai direspons Agent manapun
• Pesan konfirmasi atau perubahan status toggle menandakan penyimpanan berhasil

## Error States  <!-- confidence:medium ~ -->

• **Chat tetap di-hold setelah pencarian 3 kali**: Terjadi ketika kapasitas beban kerja semua Agent sudah penuh. Solusi: Tambahkan Agent baru atau kurangi beban kerja Agent yang ada melalui menu Agent Management.

• **Idle Rule tidak aktif meski sudah disimpan**: Pastikan checkbox **Enable idle rule** benar-benar tercentang sebelum klik tombol Save changes.

• **Idle period tidak tersimpan**: Pastikan nilai yang diisi adalah angka valid (dalam menit). Hindari karakter atau nilai negatif.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Mekari Qontak Support jika:

• Chat tidak ter-reassign meskipun Idle Rule sudah diaktifkan dan waktu Idle period terlampaui
• Sistem menampilkan pesan error saat menyimpan pengaturan Idle period
• Fitur Idle Rule tidak muncul di tab Agent Management
• Chat terus ter-hold tanpa respons Agent setelah pencarian 3 kali

Sediakan informasi: screenshot pengaturan Idle Rule yang telah disimpan, ID akun Qontak, durasi Idle period yang diatur, dan jumlah Agent aktif dalam sistem.