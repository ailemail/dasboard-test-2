import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("📊 Realisasi Anggaran 2015–2024")

# Load the file
uploaded_file = "Rekap Realisasi 2015-2024.xlsx"
sheet_names = pd.ExcelFile(uploaded_file).sheet_names
selected_sheet = st.selectbox("Pilih Tahun", sheet_names)

df = pd.read_excel(uploaded_file, sheet_name=selected_sheet)
df.columns = df.columns.str.strip()

if all(col in df.columns for col in ["Program", "Pagu", "Realisasi"]):
    df["Persentase"] = (df["Realisasi"] / df["Pagu"]) * 100

    fig = go.Figure()
    fig.add_trace(go.Bar(x=df["Program"], y=df["Pagu"], name="Pagu", marker_color='lightskyblue'))
    fig.add_trace(go.Bar(x=df["Program"], y=df["Realisasi"], name="Realisasi", marker_color='mediumseagreen'))
    fig.add_trace(go.Scatter(x=df["Program"], y=df["Persentase"], name="Persentase Realisasi",
                             mode='lines+markers', yaxis='y2', line=dict(color='firebrick', width=3)))

    fig.update_layout(
        title=f"📈 Pagu vs Realisasi + Persentase ({selected_sheet})",
        xaxis_title="Program",
        yaxis=dict(title="Jumlah (Rp)", side='left'),
        yaxis2=dict(title="Persentase (%)", overlaying='y', side='right', range=[0, 120]),
        barmode='group',
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Kolom 'Program', 'Pagu', atau 'Realisasi' tidak ditemukan.")
