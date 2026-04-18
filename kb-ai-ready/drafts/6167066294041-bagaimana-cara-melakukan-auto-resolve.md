---
title: Bagaimana Cara Melakukan Auto Resolve
canonical_url: https://help-center.qontak.com/hc/id/articles/6167066294041-Bagaimana-Cara-Melakukan-Auto-Resolve
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
product_surface: web
language: id
intent_tags:
- platform
- perform-auto-resolve
- general-platform
query_examples:
- Cara Melakukan Auto Resolve
- Bagaimana cara Melakukan Auto Resolve?
- Langkah-langkah Melakukan Auto Resolve di Qontak Omnichannel
- How do I Melakukan Auto Resolve?
- Mau Melakukan Auto Resolve, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengatur Auto Resolve pada chat di Qontak Omnichannel, Anda membutuhkan:

- Akun Qontak Omnichannel aktif dengan akses Admin
- Akses ke menu Setting dan tab Inbox
- Koneksi internet stabil untuk membuka web Qontak Omnichannel
- Setidaknya satu channel aktif (jika ingin mengatur Auto Resolve untuk channel tertentu)
- Pengetahuan tentang periode inaktivitas percakapan yang diinginkan

## Steps  <!-- confidence:high ✓ -->


Anda bisa mengatur **Auto Resolve** pada chat yang masuk dari customer. Fitur ini membuat chat akan secara otomatis ter-resolve dalam jangka waktu tertentu. Berikut cara yang bisa Anda lakukan untuk melakukan **Auto Resolve** pada chat.
  1. Masuk ke menu **Setting** , dan pilih tab **"Inbox".  
**
  2. Setelah itu, pilih tab **"Auto Resolve"**.  
![1.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F26947322330521)
  3. Anda dapat centang **“Enable auto-resolve for messages”** apabila Anda ingin mengaktifkan **auto-resolve** untuk fitur pesan dan **“Enable auto-resolve for comments”** untuk fitur komentar.  
![2.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36777848118169)
  4. Setelah diaktifkan, Anda dapat memilih untuk mengatur **Auto-resolve** ke**semua** **channel** atau **channel tertentu**.   
![NEW.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36777834109209)
  5. Apabila Anda memilih **All channel** , maka Anda perlu mengatur **Inactivity period** atau periode tidak aktif dari percakapan yang dilakukan.  
![NEW.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F26947313528985)

- Apabila Anda menambahkan **tag** pada **Auto-resolve** lalu menghapusnya dari menu **Tag** dan **Auto Resolve** , maka tag tersebut akan terhapus namun tetap berada di **room** yang lama.   
- **Room** yang lama tidak akan terselesaikan sampai Agent mengirimkan pesan setelah admin mengaktifkan **Auto-resolve** (selama pesan terakhir dari pengguna tidak melebihi rentang waktu yang ditentukan).   
- **Room** akan terselesaikan apabila Agent mengirim pesan ke dalam **room** tetapi Agent sudah tidak lagi berada di dalam room tersebut (dengan pesan terakhir masih diatribusikan ke Agen).   
- Apabila Anda menggunakan **“Resolve all expired channel”** , maka **customer** tidak akan menerima survei.  
![G.png](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36777834112153)

## Error States  <!-- confidence:medium ~ -->

- Jika Anda menghapus tag dari menu Tag setelah menerapkannya pada Auto Resolve, tag akan terhapus dari pengaturan namun tetap tersisa di room lama yang sudah ter-resolve.

- Jika room tidak ter-resolve setelah periode inaktivitas berakhir, periksa apakah Agent baru saja mengirim pesan. Room tidak akan ter-resolve sampai Agent tidak lagi mengirim pesan dalam jangka waktu yang ditentukan (asalkan pesan terakhir dari customer masih dalam rentang waktu yang ditentukan).

- Jika Anda ingin mengatur channel spesifik tetapi tidak melihat channel tersebut di daftar, pastikan channel sudah aktif dan terhubung dengan akun Qontak Anda.

## Escalation  <!-- confidence:medium ~ -->

Hubungi tim support Qontak jika Anda mengalami:

- Tombol **Save changes** tidak merespons atau pengaturan tidak tersimpan setelah klik save
- Tab **Auto Resolve** tidak tampil di menu Setting → Inbox
- Fitur Auto Resolve tidak berfungsi meskipun sudah diaktifkan dan periode inaktivitas sudah tercapai
- Error message muncul saat mengatur Inactivity period atau memilih channel

Sediakan informasi: screenshot halaman error, nama channel yang bermasalah, browser yang digunakan, dan account ID Qontak Anda.