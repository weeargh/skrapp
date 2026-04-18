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


Melalui Mekari Qontak Omnichannel, Anda dapat mengatur _default settings_ untuk keseluruhan akun. Tindakan ini dapat Anda lakukan dengan mengakses menu **Settings**. Salah satunya, adalah**Idle Rule Settings**. Dengan mekanisme ini, _chat room_ yang belum dapat dilayani karena tingginya _traffic_ percakapan dapat dikelola. Apabila Agent tidak merespon _chat room_ pada waktu tertentu (ditentukan pada pengaturan ini), maka _chat room_ tersebut akan di _assign_ ke _Agent_ lainnya.
Berikut adalah langkah-langkahnya.
  1. Masuk ke menu**Settings** , lalu klik **Agent Management.**  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36776163185305)
  2. Pada tab **Idle rule** , Anda dapat mencentang **Enable idle rule** untuk mengaktifkannya. Lalu, isikan**Idle period** Anda dalam hitungan menit.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36776163187865)
  3. Klik **“Save changes”** untuk menetapkan aturan _default_ ini.

**Penting  
** Jika Agent tidak merespon pada waktu yang telah ditentukan, maka sistem percakapan akan dibebankan ke Agent lain (penerapan beban kerja). Jika kapasitas beban kerja semua Agent penuh, maka sistem akan mencoba mencari agen lain sebanyak 3 kali (Idle period yang telah ditentukan akan berlaku untuk setiap proses pencarian agent). Setelah tiga kali sistem tidak menemukan agen, maka _room chat_ tidak akan bergerak (ter-_hold_ sampai chat direspon oleh Agent).
Demikian cara mengatur Idle rule settings Qontak Omnichannel.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Mekari Qontak Support jika:

• Chat tidak ter-reassign meskipun Idle Rule sudah diaktifkan dan waktu Idle period terlampaui
• Sistem menampilkan pesan error saat menyimpan pengaturan Idle period
• Fitur Idle Rule tidak muncul di tab Agent Management
• Chat terus ter-hold tanpa respons Agent setelah pencarian 3 kali

Sediakan informasi: screenshot pengaturan Idle Rule yang telah disimpan, ID akun Qontak, durasi Idle period yang diatur, dan jumlah Agent aktif dalam sistem.