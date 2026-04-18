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


Anda dapat menghubungi tim developer Anda untuk mendapatkan **Package name** dan **Bundle ID**.
  6. Maka widget installation sudah berhasil dilakukan. Selanjutnya, Anda perlu meminta tim developer Anda untuk memasukkan semua detail tersebut (App ID, Client ID, Secret Key) ke sistem Anda.  
![pasted image 0 \(43\).png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781184476825)

### B. Cara Mengubah Tampilan[](https://help-center.qontak.com/hc/id/articles/22614405832473-Bagaimana-Cara-Mengintegrasikan-Mobile-Chat-di-Omnichannel-Qontak#h_01H9HMR8DMSZH6W1ERRPPJJ999)
Setelah widget sudah berhasil terbuat, selanjutnya Anda dapat mengubah tampilan dari mobile chat. Berikut langkah-langkahnya.
  1. Pada daftar App name yang telah Anda buat, klik**“Action”** lalu pilih **Edit**.  
![pasted image 0 \(44\).png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781184478873)
  2. Untuk mengubah tampilan klik **“Widget content & appearance”**.  
![pasted image 0 \(45\).png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781184470169)
  3. Selanjutnya, Anda dapat mengubah tampilan yang ada seperti berikut.  
![pasted image 0 \(46\).png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781184477465)

**No** | **Kolom** | **Penjelasan**  
---|---|---  
1 | Display name | Masukkan nama tampilan yang Anda inginkan.  
2 | Description | Deskripsi yang telah Anda buat muncul di tampilan chat pelanggan Anda pada header chat.  
3 | Greetings | Greetings yang Anda buat akan muncul saat pertama kali pelanggan mengirimkan pesan. Greetings ini tidak terhitung sebagai bot sehingga tidak akan memengaruhi auto responder.  
4 | Appearance | Anda dapat menyesuaikan warna (room chat), warna pesan agen (bubble chat dari agen), warna pesan pelanggan (customer bubble chat).  
  4. Anda dapat melihat preview dari tampilan yang Anda ubah pada bagian kanan. Dan jika semua pengaturan sudah sesuai, klik **“Save changes”**.  
![pasted image 0 \(47\).png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781142879257)

### C. Cara Menambahkan Push Notification[](https://help-center.qontak.com/hc/id/articles/22614405832473-Bagaimana-Cara-Mengintegrasikan-Mobile-Chat-di-Omnichannel-Qontak#h_01H9HMR8DMFYC3R0SBAM783Z23)
Setelah membuat widget, Anda juga dapat menambahkan push notification pada pelanggan. Jadi jika Anda membalas pesan dari pelanggan, maka pelanggan tersebut akan mendapatkan notifikasi. Berikut langkah-langkahnya.
  1. Pada daftar App name yang telah Anda buat, klik**“Action”** lalu pilih **Edit**.  
![pasted image 0 \(48\).png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781184470681)
  2. Untuk menambahkan notifikasi klik **“Push notification”**.  
![pasted image 0 \(49\).png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781142881049)
  3. Tambahkan **FCM survey key** yang dapat Anda dapatkan dari tim developer Anda kemudian klik **“Add key”**.  
![pasted image 0 \(50\).png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781184479513)
  4. Masukkan FCM server key yang Anda peroleh dan klik**“Add”** untuk menambahkannya.  
![pasted image 0 \(51\).png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36781184471833)
  5. Maka push notification sudah berhasil ditambahkan. Anda juga dapat mengubahnya dengan klik **“Edit”**.  
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