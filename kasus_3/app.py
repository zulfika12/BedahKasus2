import streamlit as st
import pandas as pd
import plotly.express as px

# Set Page Config
st.set_page_config(
    page_title="Dashboard Pengamatan Cuaca - Zulfika Arin Veranika",
    page_icon="🌤️",
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
st.markdown('<div class="main-header">🌤️ Dashboard Analisis Pengamatan Cuaca</div>', unsafe_allow_html=True)
st.caption("Bedah Kasus 3: Visualisasi Data Kategorik Nominal, Numerik Interval, dan Numerik Rasio")

# Tampilan Identitas Mahasiswa untuk Tugas
st.markdown("""
    <div class="student-card">
        <div class="student-name">👤 Nama : Zulfika Arin Veranika</div>
        <div class="student-nim">🆔 NIM  : 241041004</div>
    </div>
""", unsafe_allow_html=True)

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("dataset_pengamatan_cuaca.csv")
    df['Waktu_Pengamatan'] = pd.to_datetime(df['Waktu_Pengamatan'])
    return df

df = load_data()

# Sidebar Filters
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/1163/1163661.png", width=80)
st.sidebar.title("📌 Filter Data")

# Info Identitas di Sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("**Identitas Penyusun:**")
st.sidebar.text("Nama : Zulfika Arin Veranika")
st.sidebar.text("NIM  : 241041004")
st.sidebar.markdown("---")

kota_filter = st.sidebar.multiselect(
    "Pilih Kota:",
    options=df['Kota'].unique(),
    default=df['Kota'].unique()
)

kondisi_filter = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca:",
    options=df['Kondisi'].unique(),
    default=df['Kondisi'].unique()
)

filtered_df = df[
    (df['Kota'].isin(kota_filter)) &
    (df['Kondisi'].isin(kondisi_filter))
]

# Top KPI Metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    avg_temp = filtered_df['Suhu (°C)'].mean() if not filtered_df.empty else 0
    st.metric("Rata-rata Suhu", f"{avg_temp:.1f} °C")
with col2:
    avg_hum = filtered_df['Kelembaban (%)'].mean() if not filtered_df.empty else 0
    st.metric("Rata-rata Kelembaban", f"{avg_hum:.1f} %")
with col3:
    tot_obs = len(filtered_df)
    st.metric("Total Pengamatan", f"{tot_obs:,} data")
with col4:
    most_cond = filtered_df['Kondisi'].mode()[0] if not filtered_df.empty else "-"
    st.metric("Kondisi Dominan", most_cond)

st.markdown("---")

# Visualisasi Sesuai Bedah Kasus 3
tab1, tab2, tab3, tab4 = st.tabs([
    "🏷️ Kategorik (Nominal)", 
    "🌡️ Numerik Interval (Suhu)", 
    "💧 Numerik Rasio (Kelembaban)", 
    "📋 Data Mentah"
])

with tab1:
    st.subheader("1. Distribusi Kota & Kondisi Cuaca")
    st.write("*Tipe Data: Kategorik (Nominal) | Visualisasi: Bar Chart & Pie Chart*")
    
    col_a, col_b = st.columns(2)
    with col_a:
        kota_count = filtered_df['Kota'].value_counts().reset_index()
        kota_count.columns = ['Kota', 'Jumlah Pengamatan']
        fig_bar_kota = px.bar(
            kota_count, x='Kota', y='Jumlah Pengamatan',
            title='Frekuensi Pengamatan Per Kota',
            color='Jumlah Pengamatan',
            color_continuous_scale='Blues'
        )
        st.plotly_chart(fig_bar_kota, use_container_width=True)
        
    with col_b:
        cond_count = filtered_df['Kondisi'].value_counts().reset_index()
        cond_count.columns = ['Kondisi', 'Jumlah']
        fig_pie = px.pie(
            cond_count, values='Jumlah', names='Kondisi',
            title='Proporsi Kondisi Cuaca (Cerah, Hujan, dll)',
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig_pie, use_container_width=True)

with tab2:
    st.subheader("2. Analisis Suhu Per Kota")
    st.write("*Tipe Data: Numerik (Interval) | Visualisasi: Line Chart & Histogram*")
    st.info("💡 **Catatan Skala Interval:** Suhu memliki jarak antar-derajat yang sama, namun $0^\\circ\\text{C}$ bukan berarti tidak ada suhu.")
    
    col_c, col_d = st.columns(2)
    with col_c:
        fig_temp_hist = px.histogram(
            filtered_df, x='Suhu (°C)', color='Kota',
            title='Distribusi Frekuensi Suhu (°C)',
            nbins=30,
            marginal='box',
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        st.plotly_chart(fig_temp_hist, use_container_width=True)
        
    with col_d:
        df_line = filtered_df.sort_values('Waktu_Pengamatan').head(100)
        fig_temp_line = px.line(
            df_line, x='Waktu_Pengamatan', y='Suhu (°C)', color='Kota',
            title='Tren Perubahan Suhu (100 Pengamatan Pertama)',
            markers=True
        )
        st.plotly_chart(fig_temp_line, use_container_width=True)

with tab3:
    st.subheader("3. Analisis Kelembaban & Hubungan Suhu vs Kelembaban")
    st.write("*Tipe Data: Numerik (Rasio) | Visualisasi: Histogram & Scatter Plot*")
    st.info("💡 **Catatan Skala Rasio:** Kelembaban $0\\%$ berarti benar-benar tidak ada kelembaban (memiliki nol absolut).")
    
    col_e, col_f = st.columns(2)
    with col_e:
        fig_hum_hist = px.histogram(
            filtered_df, x='Kelembaban (%)', color='Kondisi',
            title='Distribusi Kelembaban Udara (%)',
            nbins=25,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig_hum_hist, use_container_width=True)
        
    with col_f:
        fig_scatter = px.scatter(
            filtered_df, x='Suhu (°C)', y='Kelembaban (%)', color='Kondisi',
            title='Hubungan Suhu (°C) vs Kelembaban (%)',
            hover_data=['Kota'],
            color_discrete_sequence=px.colors.qualitative.Set1
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

with tab4:
    st.subheader("📋 Explorer Data Mentah Pengamatan Cuaca")
    st.dataframe(filtered_df, use_container_width=True)
    
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Unduh Data Terfilter (CSV)",
        data=csv,
        file_name='data_pengamatan_cuaca_filtered.csv',
        mime='text/csv',
    )