import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("📊 Tren Realisasi Anggaran 2015–2024")

# Read the Excel sheet
df = pd.read_excel("Rekap Realisasi 2015-2024.xlsx", sheet_name="Summary", dtype=str)

# Clean and convert columns
df.columns = df.columns.str.strip()
df["Tahun"] = df["Tahun"].astype(str)

# Remove dots and convert to numbers
df["Pagu"] = df["Pagu"].str.replace(".", "", regex=False).astype(float)
df["Realisasi"] = df["Realisasi"].str.replace(".", "", regex=False).astype(float)

# Clean percentage column
df["%"] = df["%"].str.replace("%", "").str.replace(",", ".", regex=False).astype(float) * 100


# Create chart
fig = go.Figure()

fig.add_trace(go.Bar(x=df["Tahun"], y=df["Pagu"], name="Pagu", marker_color='lightskyblue'))
fig.add_trace(go.Bar(x=df["Tahun"], y=df["Realisasi"], name="Realisasi", marker_color='mediumseagreen'))
fig.add_trace(go.Scatter(x=df["Tahun"], y=df["%"], name="Persentase Realisasi",
                         mode='lines+markers', yaxis='y2', line=dict(color='firebrick', width=3)))

fig.update_layout(
    title="📈 Pagu vs Realisasi + Persentase (2015–2024)",
    xaxis_title="Tahun",
    yaxis=dict(title="Jumlah (Rp)", side='left'),
    yaxis2=dict(title="Persentase (%)", overlaying='y', side='right', range=[0, 120]),
    barmode='group',
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)
