import streamlit as st
import pandas as pd

# Lataa viestipohjat GitHubista
CSV_URL = "https://raw.githubusercontent.com/piaope/Wilma-agentti/refs/heads/main/wilma_viestipohjat.csv"

@st.cache_data
def load_templates():
    return pd.read_csv(CSV_URL, sep=";")

df = load_templates()

st.title("Wilma Agentti")
st.write("Valitse viestipohja ja muokkaa viestiä")

# Valikko
template_names = df["otsikko"].tolist()
selected_template = st.selectbox("Valitse viestipohja", template_names)

# Näytä sisältö
row = df[df["otsikko"] == selected_template].iloc[0]
message = st.text_area("Viestin sisältö", row["sisalto"], height=300)

if st.button("Kopioi viesti"):
    st.code(message, language="markdown")
