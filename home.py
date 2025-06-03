import streamlit as st

st.set_page_config(
    page_title="Pest-pd",
    page_icon="icon.jpg",
)

st.write("Bienvenido a pest-pd 👋")

st.sidebar.success("Menú principal")

st.markdown(
    """
Desde la Universidad de Burgos en colaboración con el Hospital universitario de Burgos,
 estudiamos los efectos de los pesticidas en el desarrollo de la enfermedad de Parkinson, 
analizando su impacto en la salud y los posibles biomarcadores involucrados. 
"""
)

st.image("cartel.jpeg", width=1920)

