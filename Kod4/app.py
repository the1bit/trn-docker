# Importáljuk a streamlit modult
import streamlit as st
import pandas as pd
import numpy as np
import time

# Session state
st.session_state.szamlalo = st.session_state.get("szamlalo", 0)

# Cím
st.title("Mentor Klub - Docker alapú alkalmazások Cloud-ban")
# Szöveg, amely formázva van
st.write(
    """
         ## (Mentor Klub - 2024.05.09.)
         # """
)

# Számláló
ertek = st.number_input("", 0, 10)
if st.button("Hozzáad"):
    st.session_state.szamlalo += ertek
st.markdown(f"Számláló: {st.session_state.szamlalo}")

# Csúszka
window = st.slider("Mennyire van jó kedved ma?", 1, 10, 7)
# Csúszka aktuális értéke
st.write(f"Jó kedv mértéke: {window}")
st.html("<hr>")

# Lufik
if st.button("Jöjjenek a lufik", type="primary"):
    st.toast("Figyelj! Jönnek a lufik!", icon="🎈")
    time.sleep(1)
    st.toast("3", icon="🎈")
    time.sleep(1)
    st.toast("2", icon="🎈")
    time.sleep(1)
    st.toast("1", icon="🎈")
    time.sleep(1)
    st.toast("Már itt is vannak!", icon="🎈")
    time.sleep(1)
    st.balloons()
# Hóesés
if st.button("Legyen hóesés"):
    st.toast("Máris itt a tél?", icon="❄️")
    time.sleep(1)
    st.snow()
st.html("<hr>")

# Grafikon
st.markdown("### Web szerverek CPU terhelése")
chart_data = pd.DataFrame(
    14 * (4 + np.random.randn(100, 4)),
    columns=["WEB 1 CPU", "WEB 2 CPU", "WEB 3 CPU", "WEB 4 CPU"],
)
st.area_chart(chart_data)
st.html("<hr>")
# Linkek
st.markdown("### Linkek")
st.page_link("https://gerillamentorklub.hu/", label="Mentor Klub", icon="🌟")
st.page_link("https://streamlit.io/", label="Streamlit", icon="⚙️")
st.page_link(
    "https://github.com/cloudsteak/trn-docker", label="Forráskód (GitHub)", icon="🚀"
)
