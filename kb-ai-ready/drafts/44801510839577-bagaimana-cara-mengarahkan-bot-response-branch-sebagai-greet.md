---
title: Bagaimana Cara Mengarahkan Bot Response Branch sebagai Greetings
canonical_url: https://help-center.qontak.com/hc/id/articles/44801510839577-Bagaimana-Cara-Mengarahkan-Bot-Response-Branch-sebagai-Greetings
article_type: task
solvability_type: tool
products:
- Qontak Omnichannel
- Qontak Chat
product_surface: api
language: id
intent_tags:
- conversational-ai-chatbot
- ai-chatbot-automation
query_examples:
- Cara Mengarahkan Bot Response Branch sebagai Greetings
- Bagaimana cara Mengarahkan Bot Response Branch sebagai Greetings?
- Langkah-langkah Mengarahkan Bot Response Branch sebagai Greetings di Qontak Omnichannel
- How do I Mengarahkan Bot Response Branch sebagai Greetings?
- Mau Mengarahkan Bot Response Branch sebagai Greetings, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

Untuk mengarahkan Bot Response Branch sebagai Greetings dengan API response, Anda memerlukan:

1. Akses ke Qontak Omnichannel atau Qontak Chat dengan izin pembuatan chatbot
2. Conversation yang sudah dibuat di menu Chatbot
3. Minimal satu User Input dan Bot Response sudah dikonfigurasi
4. Koneksi API sudah dibuat di menu **API Connection** (wajib, karena Branch hanya cocok dengan API response)
5. Informasi API Integration yang diperlukan: method, path, header, dan body

## Steps  <!-- confidence:high ✓ -->

1. Buka akun Qontak Omnichannel, pilih menu **Chatbot**.
2. Pilih tab **Conversation**.
3. Klik salah satu Conversation yang sudah dibuat. Diagram Pohon akan terbuka.
4. Klik tombol (+) di bawah titik awal dan pilih **Branch**. Form pembuatan Branch baru akan ditampilkan.
5. Isikan **Branch name** (nama Bot response).
6. Pada bagian **API Integration**, pilih **Connection** dari dropdown yang menampilkan semua koneksi dari menu **API Connection**.
7. Tentukan **API method**, **API path**, **API header**, dan **API body**. Centang **API entity** untuk menyimpan respons ke variabel.
8. Atur **Conditions** dengan klik **Add condition**. Isikan **response key** dan **response value**. Anda dapat menambahkan hingga 10 kondisi dengan **Add criteria**.
9. Tentukan **Response type** sesuai kebutuhan.
10. Atur kondisi **Else** untuk fallback jika kondisi tidak terpenuhi.
11. Klik **Save** untuk menyimpan konfigurasi Branch.

## Expected Result  <!-- confidence:high ✓ -->

Setelah semua langkah selesai, Bot Response Branch berhasil dibuat dengan API response. Sistem akan menampilkan Branch baru pada Diagram Pohon dengan koneksi ke API yang dikonfigurasi. Kondisi yang Anda atur akan dicocokkan dengan respons API yang diterima, dan Bot akan memberikan response sesuai kondisi yang terpenuhi atau fallback condition (Else) jika tidak ada kondisi yang cocok.

## Error States  <!-- confidence:medium ~ -->

• **Dropdown Connection kosong**: Koneksi API belum dibuat di menu **API Connection**. Solusi: Buat koneksi API terlebih dahulu di menu **API Connection** sebelum membuat Branch.

• **Kondisi tidak terpenuhi saat runtime**: Response key atau response value tidak sesuai dengan respons API yang diterima. Solusi: Periksa struktur respons API menggunakan API testing tool, lalu sesuaikan response key dan value.

• **Branch tidak dieksekusi**: Pastikan connection sudah dipilih dan minimal satu condition sudah dikonfigurasi.

## Escalation  <!-- confidence:medium ~ -->

Hubungi Qontak Support jika mengalami:

• Koneksi API tidak dapat disimpan atau tidak muncul di dropdown **Connection**
• Bot Response Branch tidak merespons meskipun kondisi sudah sesuai
• Respons API tidak tertangkap dengan benar di **API entity**

Sediakan informasi berikut:
- Screenshot dari Diagram Pohon dan konfigurasi Branch
- API endpoint dan struktur respons yang digunakan
- ID conversation dan conversation flow
- Error message atau logs jika ada