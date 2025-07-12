import streamlit as st

st.set_page_config(page_title="Konversi Satuan Kimia", page_icon="🧪")

st.title("🧪 Konversi Satuan Kimia")

# Fungsi konversi
def konversi_satuan(nilai: float, dari: str, ke: str) -> float:
    dari = dari.lower()
    ke = ke.lower()

    match (dari, ke):
        case ("mmol", "mol"):
            return nilai / 1000
        case ("mol", "mmol"):
            return nilai * 1000
        case ("mg", "g"):
            return nilai / 1000
        case ("g", "mg"):
            return nilai * 1000
        case ("ml", "l"):
            return nilai / 1000
        case ("l", "ml"):
            return nilai * 1000
        case ("ppm", "%"):
            return nilai / 10000
        case ("%", "ppm"):
            return nilai * 10000
        case ("g", "kg"):
            return nilai / 1000
        case ("kg", "g"):
            return nilai * 1000
        case ("mmol/l", "mol/l"):
            return nilai / 1000
        case ("mol/l", "mmol/l"):
            return nilai * 1000
        case _:
            return None

# Input pengguna
nilai = st.number_input("Masukkan nilai:", value=1.0)

dari_satuan = st.selectbox("Dari satuan:", [
    "mmol", "mol", "mg", "g", "kg", "ml", "l", "ppm", "%", "mmol/l", "mol/l"
])

ke_satuan = st.selectbox("Ke satuan:", [
    "mmol", "mol", "mg", "g", "kg", "ml", "l", "ppm", "%", "mmol/l", "mol/l"
])

# Tombol konversi
if st.button("Konversi"):
    hasil = konversi_satuan(nilai, dari_satuan, ke_satuan)
    if hasil is not None:
        st.success(f"Hasil: {hasil:.6f} {ke_satuan}")
    else:
        st.error("Konversi tidak dikenali atau tidak valid.")
