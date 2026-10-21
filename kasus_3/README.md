# 🌤️ Bedah Kasus 3: Dashboard Pengamatan Cuaca

Project ini dikembangkan menggunakan **Python** dan **Streamlit** untuk menganalisis serta memvisualisasikan dataset pengamatan cuaca sebanyak 1.000 data sintetis berdasarkan struktur variabel pada Bedah Kasus 3.

---

## 📁 Struktur Folder Project

```
bedah_kasus_3/
│
├── dataset_pengamatan_cuaca.csv      # Data sintesis (1.000 baris)
├── app.py                            # Source code Dashboard Streamlit
├── requirements.txt                  # Library dependensi Python
└── README.md                         # Petunjuk penggunaan
```

---

## 🛠️ Klasifikasi Tipe Data & Visualisasi (Sesuai Gambar)

| Variable | Tipe Data & Skala Pengukuran | Visualisasi yang Tepat |
| :--- | :--- | :--- |
| **Kota** | Kategorik (Nominal) | Bar Chart / Pie Chart (Label teks tanpa urutan) |
| **Kondisi** | Kategorik (Nominal) | Bar Chart / Pie Chart (Label teks tanpa urutan) |
| **Suhu (°C)** | Numerik (Interval) | Histogram / Line Chart (Tanpa nol absolut) |
| **Kelembaban (%)** | Numerik (Rasio) | Histogram / Scatter Plot (Memiliki nol absolut) |

---

## 🚀 Cara Menjalankan Project di VS Code

### 1. Ekstrak File ZIP
Ekstrak `bedah_kasus_3_dashboard.zip` dan buka folder `bedah_kasus_3` di **VS Code**.

### 2. Buka Terminal di VS Code
Buka terminal terintegrasi (`Ctrl + ~` atau `Cmd + ~` di Mac).

### 3. Install Dependensi (Jika belum)
```bash
pip install -r requirements.txt
```

### 4. Jalankan Dashboard Streamlit
```bash
python -m streamlit run app.py
```
atau
```bash
streamlit run app.py
```

Dashboard otomatis terbuka di browser Anda pada alamat `http://localhost:8501`.
