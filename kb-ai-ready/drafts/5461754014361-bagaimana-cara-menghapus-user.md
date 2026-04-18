---
title: Bagaimana Cara Menghapus User
canonical_url: https://help-center.qontak.com/hc/id/articles/5461754014361-Bagaimana-Cara-Menghapus-User
article_type: task
solvability_type: tool
products:
- Qontak CRM
product_surface: web
language: id
intent_tags:
- user-permissions
- delete-user
- general-platform
query_examples:
- Cara Menghapus User
- Bagaimana cara Menghapus User?
- Langkah-langkah Menghapus User di Qontak CRM
- How do I Menghapus User?
- Mau Menghapus User, caranya gimana?
compliance_sensitive: false
plan_scope: null
chunk_groups: []
related_chunks: []
last_verified: null
verified_by: AI:claude-haiku-4-5-20251001
faithfulness_threshold: 0.6
---

## Prerequisites  <!-- confidence:high ✓ -->

• Anda harus memiliki akses level Admin di Qontak CRM perusahaan Anda
• Akses ke dashboard CRM Qontak
• User yang akan dihapus harus sudah terdaftar dalam sistem
• Anda harus memiliki akun pengguna lain yang aktif untuk menampung database dari user yang dihapus

## Steps  <!-- confidence:high ✓ -->

1. Klik tanda panah di sebelah kanan username Anda (kanan atas dashboard CRM). Dropdown menu akan muncul.
2. Pilih "Profile Settings" dari menu dropdown. Halaman Profile Settings akan terbuka.
3. Klik tab "Users". Daftar semua user yang terdaftar pada CRM perusahaan Anda akan ditampilkan.
4. Tentukan akun user yang ingin Anda hapus dari daftar tersebut.
5. Klik ikon "Trash bin" (tempat sampah) di sebelah kanan akun user yang dipilih. Pop-up window akan muncul.
6. Pada pop-up, pilih akun pengguna lain yang akan menampung database dari user yang dihapus. Sesuaikan dengan kebutuhan Anda.
7. Klik tombol "Save". Sistem akan memproses pemindahan database dan penghapusan akun.

## Expected Result  <!-- confidence:high ✓ -->

Akun user berhasil dihapus dari sistem CRM. Database yang terkait dengan user tersebut dipindahkan ke akun pengguna yang Anda pilih. User tidak lagi muncul dalam daftar Users di tab "Users" pada Profile Settings. Proses penghapusan dapat memerlukan beberapa saat tergantung volume data yang diproses.

## Error States  <!-- confidence:high ✓ -->

**Penghapusan gagal karena database besar:** Jika user memiliki data yang sangat banyak, sistem mungkin gagal menghapus akun karena ada field wajib yang belum diisi oleh user tersebut. **Error lainnya:** Proses pemindahan database atau penghapusan mungkin mengalami error teknis. Dalam kedua kasus ini, hubungi tim support Qontak dengan menyertakan nama user yang ingin dihapus dan ID perusahaan Anda.

## Escalation  <!-- confidence:medium ~ -->

Jika fitur Hapus User mengalami kegagalan atau Anda menerima pesan error saat mencoba menghapus akun, hubungi konsultan atau tim support Qontak. Siapkan informasi berikut: nama lengkap user yang akan dihapus, email user, ID perusahaan CRM Anda, dan deskripsi error atau pesan yang muncul. Tim support akan membantu memproses penghapusan dan pemindahan database.