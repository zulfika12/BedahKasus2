import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os

st.set_page_config(
    page_title="Dashboard Profil Mahasiswa - Zulfika Arin Veranika",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .student-card {
        background-color: #EFF6FF;
        border-left: 6px solid #2563EB;
        padding: 15px 20px;
        border-radius: 8px;
        margin-bottom: 25px;
    }
    .student-name { font-size: 20px; font-weight: bold; color: #1E3A8A; margin: 0; }
    .student-nim { font-size: 16px; color: #3B82F6; font-weight: 600; margin-top: 4px; }
    .main-header { font-size: 28px; font-weight: bold; color: #1E3A8A; margin-bottom: 5px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🎓 Dashboard Analisis Profil Mahasiswa</div>', unsafe_allow_html=True)
st.caption("Bedah Kasus 2: Visualisasi Data Kategorik (Nominal & Ordinal) dan Numerik Kontinu")

st.markdown("""
    <div class="student-card">
        <div class="student-name">👤 Nama : Zulfika Arin Veranika</div>
        <div class="student-nim">🆔 NIM  : 241041004</div>
    </div>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(BASE_DIR, "dataset_profil_mahasiswa.csv")
    
    if not os.path.exists(csv_path):
        np.random.seed(42)
        n_samples = 1000
        jurusans = ['Sistem Informasi', 'Manajemen', 'Informatika', 'Teknik Industri', 'Akuntansi']
        semesters = [1, 2, 3, 4, 5, 6, 7, 8]
        
        data = []
        for i in range(n_samples):
            jur = np.random.choice(jurusans, p=[0.3, 0.25, 0.2, 0.15, 0.1])
            sem = np.random.choice(semesters, p=[0.2, 0.18, 0.15, 0.15, 0.12, 0.1, 0.06, 0.04])
            age = int(18 + int((sem - 1) / 2) + np.random.choice([0, 1, 2], p=[0.7, 0.25, 0.05]))
            ipk = round(float(np.clip(np.random.normal(3.35, 0.35), 2.0, 4.0)), 2)
            data.append({'NIM': f"241041{i+1:03d}", 'Jurusan': jur, 'Semester': sem, 'IPK': ipk, 'Usia': age})
            
        df_gen = pd.DataFrame(data)
        df_gen.to_csv(csv_path, index=False)
        return df_gen
        
    df = pd.read_csv(csv_path)
    return df

df = load_data()

st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)
st.sidebar.title("📌 Filter Data")
st.sidebar.markdown("---")
st.sidebar.markdown("**Identitas Penyusun:**")
st.sidebar.text("Nama : Zulfika Arin Veranika")
st.sidebar.text("NIM  : 241041004")
st.sidebar.markdown("---")

jurusan_filter = st.sidebar.multiselect("Pilih Jurusan:", options=df['Jurusan'].unique(), default=df['Jurusan'].unique())
semester_filter = st.sidebar.multiselect("Pilih Semester:", options=sorted(df['Semester'].unique()), default=sorted(df['Semester'].unique()))

filtered_df = df[(df['Jurusan'].isin(jurusan_filter)) & (df['Semester'].isin(semester_filter))]

col1, col2, col3, col4 = st.columns(4)
with col1: st.metric("Total Mahasiswa", f"{len(filtered_df):,} orang")
with col2: st.metric("Rata-rata IPK", f"{filtered_df['IPK'].mean():.2f}" if not filtered_df.empty else "0")
with col3: st.metric("Rata-rata Usia", f"{filtered_df['Usia'].mean():.1f} tahun" if not filtered_df.empty else "0")
with col4: st.metric("Jumlah Jurusan", f"{filtered_df['Jurusan'].nunique()} Jurusan")

st.markdown("---")
tab1, tab2, tab3, tab4 = st.tabs(["🏷️ Kategorik (Nominal)", "📈 Kategorik (Ordinal)", "🔢 Numerik Kontinu (IPK & Usia)", "📋 Data Mentah"])

with tab1:
    col_a, col_b = st.columns(2)
    with col_a:
        jur_count = filtered_df['Jurusan'].value_counts().reset_index()
        jur_count.columns = ['Jurusan', 'Jumlah Mahasiswa']
        st.plotly_chart(px.bar(jur_count, x='Jumlah Mahasiswa', y='Jurusan', orientation='h', title='Jumlah Mahasiswa Per Jurusan', color='Jumlah Mahasiswa', color_continuous_scale='Blues'), use_container_width=True)
    with col_b:
        st.plotly_chart(px.pie(jur_count, values='Jumlah Mahasiswa', names='Jurusan', title='Persentase Sebaran Jurusan', hole=0.4, color_discrete_sequence=px.colors.qualitative.Set3), use_container_width=True)

with tab2:
    sem_count = filtered_df.groupby('Semester').size().reset_index(name='Jumlah Mahasiswa')
    sem_count['Semester_Label'] = 'Semester ' + sem_count['Semester'].astype(str)
    sem_count = sem_count.sort_values('Semester')
    st.plotly_chart(px.bar(sem_count, x='Semester_Label', y='Jumlah Mahasiswa', title='Sebaran Mahasiswa Berdasarkan Semester', color='Jumlah Mahasiswa', color_continuous_scale='Teal'), use_container_width=True)

with tab3:
    col_c, col_d = st.columns(2)
    with col_c:
        st.plotly_chart(px.histogram(filtered_df, x='IPK', nbins=25, title='Distribusi Frekuensi IPK', color='Jurusan', marginal='box', color_discrete_sequence=px.colors.qualitative.Safe), use_container_width=True)
    with col_d:
        st.plotly_chart(px.box(filtered_df, x='Jurusan', y='Usia', title='Sebaran Usia Per Jurusan', color='Jurusan', color_discrete_sequence=px.colors.qualitative.Safe), use_container_width=True)

with tab4:
    st.dataframe(filtered_df, use_container_width=True)