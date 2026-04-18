---
title: Bagaimana Cara Melakukan Pengaturan Tambahan pada Bot Response
canonical_url: https://help-center.qontak.com/hc/id/articles/12128813400857-Bagaimana-Cara-Melakukan-Pengaturan-Tambahan-pada-Bot-Response
article_type: task
solvability_type: tool
products:
- Qontak CRM
- Qontak Chat
product_surface: api
language: id
intent_tags:
- conversational-ai-chatbot
- perform-pengaturan-tambahan
- ai-chatbot-automation
query_examples:
- Cara Melakukan Pengaturan Tambahan pada Bot Response
- Bagaimana cara Melakukan Pengaturan Tambahan pada Bot Response?
- Langkah-langkah Melakukan Pengaturan Tambahan pada Bot Response di Qontak CRM
- How do I Melakukan Pengaturan Tambahan pada Bot Response?
- Mau Melakukan Pengaturan Tambahan pada Bot Response, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.3
---

## Prerequisites  <!-- confidence:high ✓ -->

1. Akses ke Qontak Omnichannel atau Qontak Chat dengan izin manajemen chatbot
2. Conversation sudah dibuat di menu Chatbot
3. Welcome Message sudah dikonfigurasi
4. User Input dan Bot Response sudah diatur
5. Minimal satu Bot Response telah dibuat untuk dikonfigurasi Additional Settings

## Steps  <!-- confidence:high ✓ -->


Pada Chatbot Qontak, Anda dapat melakukan pengaturan untuk setiap bot response, yaitu pengaturan bagaimana cara menyelesaikan percakapan, integrasi API, serta CRM, berikut penjelasannya.
### A. Additional Settings[](https://help-center.qontak.com/hc/id/articles/12128813400857-Bagaimana-Cara-Melakukan-Pengaturan-Tambahan-pada-Bot-Response#h_01HKYAFG2P84RFFNJ86TD16SRB)
Pada bot response yang telah Anda buat di Chatbot Qontak, Anda bisa melakukan pengaturan tambahan yaitu Resolve conversation untuk menyelesaikan percakapan secara otomatis dan assign agent untuk menetapkan agent pada percakapan tertentu. Berikut langkah-langkahnya:
  1. Klik salah satu Bot Response yang ingin Anda atur penyelesaian percakapanya (Resolve conversation).  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780203082265)
  2. Kemudian, muncul _sidebar_ Bot response settings yang berada pada tab **General** , yang dapat Anda gunakan untuk mengatur Additional Settings dari dari percakapan chatbot. Terdapat 3 pengaturan tambahan (additional settings) pada Chatbot Qontak, berikut penjelasannya:  
**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780203086873)****  
**
Untuk mempelajari penjelasan mengenai tab **General** secara keseluruhan, Anda dapat akses [di sini.](https://help-center.qontak.com/hc/id/articles/12263090746137)
****Keterangan:  
**** **No.** | **Additional settings** | **Penjelasan**  
---|---|---  
1 | Default |  Pilih ini, apabila Anda ingin mengatur bot response dengan default settings, yang berarti pengaturan bot response akan sesuai dengan pengaturan yang telah Anda atur pada tab **Settings** Menu **Chatbot**. Pelajari tentang cara mengatur Default Bot Response settings [di sini.](https://help-center.qontak.com/hc/id/articles/27509223794073)  
2 | Resolve Conversation |  Pilih ini, apabila Anda ingin mengatur bot response untuk menyelesaikan percakapan secara otomatis. Pengaturan ini berfungsi apabila Anda ingin bot menyelesaikan percakapan yang sudah tidak mendapatkan respon dari penanya.  
- Lengkapi **Closing Message** untuk menutup percakapan.  
**![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780203089177)  
-** Centang ****Set user idle time**** untuk menetapkan waktu idle sebelum bot menutup percakapan (opsional).  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780203083033)  
3 | Assign Conversation |  Pilih ini, apabila Anda ingin mengatur percakapan secara khusus dengan menetapkan dengan siapa agen yang akan terhubung dengan penanya (Assign Conversation). Dengan tindakan ini, apabila Bot sudah merespons user input yang masuk, sistem akan secara otomatis menetapkan agen yang akan melanjutkan percakapan.  
- Terdapat 3 tipe assign agent:  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780194384153)  
**1.** **Auto** : Sistem akan secara otomatis memilih agen yang aktif atau sedang online untuk merespon percakapan, sistemnya round robin atau terpilih secara acak.  
**2. Division** : Sistem akan menugaskan agen berdasarkan divisi yang Anda pilih disini (pilih dari chat panel).  
**3. Agent** : Pilih agen mana yang akan ditugaskan (pilih dari chat panel).  
- Centang **Set user idle time** untuk menetapkan waktu idle sebelum bot menutup percakapan (opsional).  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780203083033)

### B. API Integration[](https://help-center.qontak.com/hc/id/articles/12128813400857-Bagaimana-Cara-Melakukan-Pengaturan-Tambahan-pada-Bot-Response#h_01HKYAFG2QNNCYS2892JTXPGSH)
Fitur ini memungkinkan Anda menghubungkan sistem dengan chatbot via API sehingga memungkinkan bot dapat mengirimkan / mengambil / menyimpan / menanyakan data dari end user ke sistem klien.
  1. Klik salah satu bot response yang ingin Anda atur.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780203082265)
  2. Masuk ke tab **API integration** dan centang **Use API integration**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780194381721)
  3. Pilih **Connection** yang telah Anda buat sebelumnya di bagian [Chatbot Settings.](https://help-center.qontak.com/hc/id/articles/27509223794073)  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780194385817)
  4. Pilih **API method** dan masukkan **API path**.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780203094297)

**Penting****  
**Connection, API method dan API path merupakan kolom-kolom yang wajib Anda isi.
  1. Selanjutnya, Anda dapat mengisi informasi berikut **secara opsional.** Kolom-kolom opsional tersebut adalah **API header (json format)** , **API body (json format)** , **API response body success** , **API response body value** , dan **API fallback bot response**. Kolom-kolom tersebut dapat Anda isikan sesuai dengan API code Anda sendiri.  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780203092633)
  2. Jika semua bagian yang diperlukan sudah terisi, kembali ke Tab **General** dan di **Bot Response Content** masukan {{CONTENT_API.(data yang ingin Anda berdasarkan API)}}  
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780203095833)
  3. Lalu klik**“Save”** untuk menyimpan.

### C. Qontak CRM[](https://help-center.qontak.com/hc/id/articles/12128813400857-Bagaimana-Cara-Melakukan-Pengaturan-Tambahan-pada-Bot-Response#h_01HKYAFG2QXTDJ1GPCR6BB8RGK)
![Screenshot](/mekarirag/proxy/image?url=https%3A%2F%2Fhelp-center.qontak.com%2Fhc%2Farticle_attachments%2F36780194390425)
Untuk menggunakan fitur ini, Anda perlu mengaktifkan Qontak CRM terlebih dahulu dan mengkoneksikannya dengan Qontak Omnichannel Anda, pelajari panduannya, [di sini](https://help-center.qontak.com/hc/id/articles/5642795619737) dan pelajari pengaturan settingan Qontak CRMnya [di sini.](https://help-center.qontak.com/hc/id/articles/27509223794073)

## Error States  <!-- confidence:low ? -->

No common errors documented.

## Escalation  <!-- confidence:medium ~ -->

Jika pengaturan Additional Settings tidak tersimpan atau Bot Response tidak berfungsi sesuai konfigurasi:
1. Verifikasi bahwa conversation status adalah 'Unpublished' atau 'Published'
2. Pastikan minimal satu User Input telah dikonfigurasi sebelum Bot Response
3. Hubungi support Qontak dengan menyertakan: screenshot pengaturan, nama conversation, dan deskripsi masalah yang dihadapi