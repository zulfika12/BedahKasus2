# 🎓 Bedah Kasus 2: Dashboard Profil Mahasiswa

Project ini dikembangkan menggunakan **Python** dan **Streamlit** untuk menganalisis serta memvisualisasikan dataset profil mahasiswa sebanyak 1.000 data sintetis berdasarkan struktur variabel pada Bedah Kasus 2.

---

## 📁 Struktur Folder Project

```
bedah_kasus_2/
│
├── dataset_profil_mahasiswa.csv      # Data sintesis (1.000 baris)
├── app.py                            # Source code Dashboard Streamlit
├── requirements.txt                  # Library dependensi Python
└── README.md                         # Petunjuk penggunaan
```

---

## 🛠️ Klasifikasi Tipe Data & Visualisasi (Sesuai Gambar)

| Variable | Tipe Data & Skala Pengukuran | Visualisasi yang Tepat |
| :--- | :--- | :--- |
| **Jurusan** | Kategorik (Nominal) | Bar Chart / Pie Chart (Label pembeda) |
| **Semester** | Kategorik (Ordinal) | Bar Chart Berurutan ($1 \rightarrow 2 \rightarrow 3$) |
| **IPK** | Numerik (Kontinu) | Histogram & Box Plot (Sebaran & Outlier) |
| **Usia** | Numerik (Kontinu / Diskrit) | Histogram & Box Plot (Sebaran Usia) |

---

## 🚀 Cara Menjalankan Project di VS Code

### 1. Ekstrak File ZIP
Ekstrak `bedah_kasus_2_dashboard.zip` dan buka folder `bedah_kasus_2` di **VS Code**.

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
