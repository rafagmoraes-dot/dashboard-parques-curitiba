import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Parques e Bosques de Curitiba",
    layout="wide"
)

# Leitura dos dados
gdf = gpd.read_file("parques_bosques_curitiba.geojson")

# Centralizar o mapa em Curitiba
m = folium.Map(
    location=[-25.43, -49.27],
    zoom_start=11
)

# Adicionar os polígonos
folium.GeoJson(
    gdf,
    tooltip=folium.GeoJsonTooltip(
        fields=["NOME", "TIPO"],
        aliases=["Nome:", "Tipo:"]
    )
).add_to(m)

st.title("🌳 Parques e Bosques de Curitiba")

st.write(
    "Mapa interativo dos parques e bosques de Curitiba."
)

st_folium(
    m,
    width=1200,
    height=700
)
