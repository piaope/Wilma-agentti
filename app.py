import streamlit as st
import pandas as pd

# RAW-linkki CSV:ään GitHubista
CSV_URL = "https://raw.githubusercontent.com/piaope/Wilma-agentti/main/wilma_viestipohjat.csv"

# Ladataan CSV
try:
    df = pd.read_csv(CSV_URL)
    # Poistetaan sarakkeiden mahdolliset ylimääräiset välilyönnit
    df.columns = df.columns.str.strip()
except Exception as e:
    st.error(f"CSV:n lataus epäonnistui: {e}")
    st.stop()

# Tulostetaan sarakkeet debugiksi
st.write("CSV-sarakkeet:", df.columns.tolist())

# Tarkistetaan, että 'otsikko' ja 'viesti' löytyvät
if "otsikko" not in df.columns or "viesti" not in df.columns:
    st.error("CSV:stä puuttuu 'otsikko' tai 'viesti' -sarake")
    st.stop()

# Lista viestipohjista
template_names = df["otsikko"].tolist()

# Streamlit UI
st.title("Wilma Agentti")
selected_template = st.selectbox("Valitse viestipohja:", template_names)

# Näytetään viesti
if selected_template:
    message = df.loc[df["otsikko"] == selected_template, "viesti"].values[0]
    st.text_area("Viestisi:", message, height=200)
