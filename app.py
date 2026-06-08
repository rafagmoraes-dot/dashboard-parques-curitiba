import streamlit as st
import geopandas as gpd

st.set_page_config(
    page_title="Parques e Bosques de Curitiba",
    layout="wide"
)

gdf = gpd.read_file("parques_bosques_curitiba.geojson")

gdf["AREA_HA"] = gdf.geometry.area / 10000

st.title("🌳 Parques e Bosques de Curitiba")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total de áreas verdes",
        len(gdf)
    )

with col2:
    st.metric(
        "Área total (ha)",
        round(gdf["AREA_HA"].sum(), 2)
    )

st.subheader("Tipos de áreas verdes")

st.write(gdf["TIPO"].value_counts())
