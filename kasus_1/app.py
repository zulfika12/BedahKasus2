import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os

# Set Page Config
st.set_page_config(
    page_title="Dashboard Operasional Penjualan - Zulfika Arin Veranika",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling & Identitas Mahasiswa
st.markdown("""
    <style>
    .student-card {
        background-color: #EFF6FF;
        border-left: 6px solid #2563EB;
        padding: 15px 20px;
        border-radius: 8px;
        margin-bottom: 25px;
    }
    .student-name {
        font-size: 20px;
        font-weight: bold;
        color: #1E3A8A;
        margin: 0;
    }
    .student-nim {
        font-size: 16px;
        color: #3B82F6;
        font-weight: 600;
        margin-top: 4px;
    }
    .main-header {
        font-size: 28px;
        font-weight: bold;
        color: #1E3A8A;
        margin-bottom: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Header & Identitas Mahasiswa
st.markdown('<div class="main-header">📊 Dashboard Analisis Operasional Penjualan</div>', unsafe_allow_html=True)
st.caption("Bedah Kasus 1: Visualisasi Data Kategorik, Numerik, dan Waktu")

# Tampilan Identitas Mahasiswa untuk Tugas
st.markdown("""
    <div class="student-card">
        <div class="student-name">👤 Nama : Zulfika Arin Veranika</div>
        <div class="student-nim">🆔 NIM  : 241041004</div>
    </div>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(BASE_DIR, "dataset_operasional_penjualan.csv")
    
    # Otomatis buat 1.000 data sintetis operasional penjualan jika file belum ada
    if not os.path.exists(csv_path):
        np.random.seed(42)
        n_samples = 1000
        categories_products = {
            'Elektronik': [
                ('Laptop', 8500000, 1000000),
                ('Smartphone', 4500000, 500000),
                ('Tablet', 3200000, 300000),
                ('Headset', 350000, 50000),
                ('Smartwatch', 1200000, 150000)
            ],
            'Pendidikan': [
                ('Buku', 75000, 15000),
                ('Alat Tulis Set', 25000, 5000),
                ('Modul Belajar', 120000, 20000),
                ('Kamus Bahasa', 95000, 10000),
                ('Ensiklopedi', 250000, 35000)
            ]
        }
        dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
        
        data = []
        for _ in range(n_samples):
            cat = np.random.choice(['Elektronik', 'Pendidikan'], p=[0.4, 0.6])
            prod_info = categories_products[cat][np.random.randint(0, len(categories_products[cat]))]
            prod_name, base_price, price_var = prod_info[0], prod_info[1], prod_info[2]
            
            price = max(10000, round(int(np.random.normal(base_price, price_var)), -3))
            qty = min(int(np.random.negative_binomial(1, 0.05)) + 1, 50) if cat == 'Elektronik' else min(int(np.random.negative_binomial(1, 0.01)) + 5, 200)
            date = np.random.choice(dates)
            
            data.append({
                'Tanggal': date,
                'Produk': prod_name,
                'Kategori': cat,
                'Harga (Rp)': price,
                'Jumlah Terjual': qty
            })
            
        df_gen = pd.DataFrame(data)
        df_gen['Total Penjualan (Rp)'] = df_gen['Harga (Rp)'] * df_gen['Jumlah Terjual']
        df_gen = df_gen.sort_values('Tanggal').reset_index(drop=True)
        df_gen.to_csv(csv_path, index=False)
        return df_gen
        
    df = pd.read_csv(csv_path)
    df['Tanggal'] = pd.to_datetime(df['Tanggal'])
    if 'Total Penjualan (Rp)' not in df.columns:
        df['Total Penjualan (Rp)'] = df['Harga (Rp)'] * df['Jumlah Terjual']
    return df

df = load_data()

# Sidebar Filters
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)
st.sidebar.title("📌 Filter Data")

# Info Identitas di Sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("**Identitas Penyusun:**")
st.sidebar.text("Nama : Zulfika Arin Veranika")
st.sidebar.text("NIM  : 241041004")
st.sidebar.markdown("---")

kategori_filter = st.sidebar.multiselect(
    "Pilih Kategori:",
    options=df['Kategori'].unique(),
    default=df['Kategori'].unique()
)

min_date = df['Tanggal'].min().date()
max_date = df['Tanggal'].max().date()

date_range = st.sidebar.date_input(
    "Rentang Tanggal:",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if len(date_range) == 2:
    start_date, end_date = date_range
    filtered_df = df[
        (df['Kategori'].isin(kategori_filter)) &
        (df['Tanggal'].dt.date >= start_date) &
        (df['Tanggal'].dt.date <= end_date)
    ]
else:
    filtered_df = df[df['Kategori'].isin(kategori_filter)]

# Top KPI Metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    total_rev = filtered_df['Total Penjualan (Rp)'].sum() if not filtered_df.empty else 0
    st.metric("Total Pendapatan", f"Rp {total_rev:,.0f}")
with col2:
    total_qty = filtered_df['Jumlah Terjual'].sum() if not filtered_df.empty else 0
    st.metric("Total Terjual (Unit)", f"{total_qty:,} unit")
with col3:
    avg_price = filtered_df['Harga (Rp)'].mean() if not filtered_df.empty else 0
    st.metric("Rata-rata Harga Produk", f"Rp {avg_price:,.0f}")
with col4:
    total_trans = len(filtered_df)
    st.metric("Total Transaksi", f"{total_trans:,}")

st.markdown("---")

# Visualisasi Sesuai Bedah Kasus 1
tab1, tab2, tab3, tab4 = st.tabs(["📈 Tren Waktu (Interval)", "📊 Kategorik (Nominal)", "🔢 Numerik (Kontinu & Diskrit)", "📋 Data Mentah"])

with tab1:
    st.subheader("1. Tren Penjualan Sepanjang Waktu (Line Chart)")
    st.write("*Tipe Data: Waktu - Interval | Visualisasi: Line Chart*")
    
    df_trend = filtered_df.groupby(pd.Grouper(key='Tanggal', freq='ME')).agg({
        'Total Penjualan (Rp)': 'sum',
        'Jumlah Terjual': 'sum'
    }).reset_index()
    
    fig_line = px.line(
        df_trend, x='Tanggal', y='Total Penjualan (Rp)',
        title='Tren Total Pendapatan Bulanan (2024)',
        markers=True,
        line_shape='spline',
        color_discrete_sequence=['#2563EB']
    )
    fig_line.update_layout(xaxis_title="Bulan", yaxis_title="Total Pendapatan (Rp)")
    st.plotly_chart(fig_line, use_container_width=True)

with tab2:
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("2a. Distribusi Produk (Bar Chart)")
        st.write("*Tipe Data: Kategorik Nominal | Visualisasi: Bar Chart*")
        
        prod_df = filtered_df.groupby('Produk')['Jumlah Terjual'].sum().reset_index().sort_values('Jumlah Terjual', ascending=True)
        fig_bar = px.bar(
            prod_df, x='Jumlah Terjual', y='Produk', orientation='h',
            title='Total Unit Terjual Per Produk',
            color='Jumlah Terjual',
            color_continuous_scale='Blues'
        )
        st.plotly_chart(fig_bar, use_container_width=True)
        
    with col_b:
        st.subheader("2b. Proporsi Kategori (Pie Chart)")
        st.write("*Tipe Data: Kategorik Nominal | Visualisasi: Pie Chart*")
        
        cat_df = filtered_df.groupby('Kategori')['Total Penjualan (Rp)'].sum().reset_index()
        fig_pie = px.pie(
            cat_df, values='Total Penjualan (Rp)', names='Kategori',
            title='Proporsi Pendapatan Berdasarkan Kategori',
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig_pie, use_container_width=True)

with tab3:
    col_c, col_d = st.columns(2)
    with col_c:
        st.subheader("3a. Distribusi Harga Produk (Histogram)")
        st.write("*Tipe Data: Numerik Kontinu - Rasio | Visualisasi: Histogram*")
        
        fig_hist = px.histogram(
            filtered_df, x='Harga (Rp)', nbins=30,
            title='Distribusi Frekuensi Harga Produk',
            color='Kategori',
            marginal='box',
            color_discrete_sequence=['#3B82F6', '#10B981']
        )
        st.plotly_chart(fig_hist, use_container_width=True)
        
    with col_d:
        st.subheader("3b. Hubungan Harga vs Quantity (Scatter Plot)")
        st.write("*Tipe Data: Numerik Diskrit & Kontinu | Visualisasi: Scatter Plot*")
        
        fig_scatter = px.scatter(
            filtered_df, x='Harga (Rp)', y='Jumlah Terjual',
            color='Kategori', size='Total Penjualan (Rp)',
            title='Sebaran Harga vs Jumlah Terjual',
            hover_data=['Produk'],
            color_discrete_sequence=['#3B82F6', '#10B981']
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

with tab4:
    st.subheader("📋 Explorer Data Mentah")
    st.dataframe(filtered_df, use_container_width=True)
    
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Unduh Data Terfilter (CSV)",
        data=csv,
        file_name='data_operasional_filtered.csv',
        mime='text/csv',
    )