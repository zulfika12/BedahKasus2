# 📊 Bedah Kasus 1: Dashboard Operasional Penjualan

Project ini dikembangkan menggunakan **Python** dan **Streamlit** untuk menganalisis dan memvisualisasikan dataset operasional penjualan sebanyak 1.000 data sintetis berdasarkan struktur variabel pada Bedah Kasus 1.

---

## 📁 Struktur Folder Project

```
bedah_kasus_1/
│
├── dataset_operasional_penjualan.csv  # Data sintesis (1.000 baris)
├── app.py                            # Source code Dashboard Streamlit
├── requirements.txt                  # Library dependensi Python
└── README.md                         # Petunjuk penggunaan
```

---

## 🛠️ Klasifikasi Tipe Data & Visualisasi (Sesuai Gambar)

| Variable | Tipe Data | Visualisasi |
| :--- | :--- | :--- |
| **Produk** | Kategorik (Nominal) | Bar Chart / Pie Chart |
| **Kategori** | Kategorik (Nominal) | Bar Chart / Pie Chart |
| **Harga (Rp)** | Numerik (Kontinu) - Rasio | Histogram / Boxplot |
| **Jumlah Terjual** | Numerik (Diskrit) - Rasio | Bar Chart / Scatter Plot |
| **Tanggal** | Waktu - Interval | Line Chart (Tren Waktu) |

---

## 🚀 Cara Menjalankan Project di VS Code

### 1. Ekstrak File ZIP
Ekstrak `bedah_kasus_1.zip` dan buka folder `bedah_kasus_1` di **VS Code**.

### 2. Buka Terminal di VS Code
Buka terminal terintegrasi (`Ctrl + ~` atau `Cmd + ~` di Mac).

### 3. (Opsional) Buat Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 4. Install Dependensi
```bash
pip install -r requirements.txt
```

### 5. Jalankan Dashboard Streamlit
```bash
streamlit run app.py
```

Dashboard otomatis terbuka di browser Anda pada alamat `http://localhost:8501`.
