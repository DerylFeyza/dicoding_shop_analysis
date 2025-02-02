import streamlit as st
import datetime
import pandas as pd

st.text(
    "Text input merupakan widget yang digunakan untuk memperoleh inputan berupa single-line text. Kita bisa menggunakan function text_input() untuk membuat widget in"
)
name = st.text_input(label="Nama lengkap", value="")
st.write("Nama: ", name)

st.text(
    "Text area merupakan widget yang memungkinkan pengguna untuk menginput multi-line text. Untuk membuat widget ini, streamlit telah menyediakan function bernama text_area(). Kode di bawah ini merupakan contoh kode untuk menggunakan function tersebut."
)
text = st.text_area("Feedback")
st.write("Feedback: ", text)

st.text(
    "number input . Ia merupakan widget yang digunakan untuk memperoleh inputan berupa angka dari pengguna."
)
number = st.number_input(label="Umur")
st.write("Umur: ", int(number), " tahun")

st.text(
    "Selain inputan berupa angka dan teks, pada beberapa kasus kita juga membutuhkan input berupa tanggal dari pengguna melalui date input widget. Kita dapat membuat widget tersebut menggunakan function date_input()."
)
date = st.date_input(label="Tanggal lahir", min_value=datetime.date(1900, 1, 1))
st.write("Tanggal lahir:", date)

st.text(
    "file uploader. Widget ini memungkinkan kita meminta pengguna untuk meng-upload sebuah berkas tertentu ke dalam web app."
)
uploaded_file = st.file_uploader("Choose a CSV file")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

st.text(
    "streamlit juga menyediakan camera input widget yang dapat digunakan untuk meminta user mengambil gambar melalui webcam sekaligus mengunggahnya."
)
picture = st.camera_input("Take a picture")
if picture:
    st.image(picture)

st.subheader("Button Widgets ")

if st.button("Say hello"):
    st.write("Hello there")

agree = st.checkbox("I agree")

st.text(
    "Checkbox merupakan widget yang digunakan untuk menampilkan sebuah checklist untuk pengguna. Kita bisa menggunakan function checkbox() untuk membuat dan menampilkan checklist dalam streamlit app"
)
if agree:
    st.write("Welcome to MyApp")

st.text(
    "Selain button dan checkbox, terkadang kita juga membutuhkan radio button untuk menghasilkan web app yang interaktif. Ia merupakan widget yang memungkinkan pengguna untuk memilih satu dari beberapa pilihan yang ada. "
)
genre = st.radio(
    label="What's your favorite movie genre",
    options=("Comedy", "Drama", "Documentary"),
    horizontal=False,
)

st.text(
    "Select box merupakan widget yang memungkinkan pengguna untuk memilih salah satu dari beberapa pilihan yang ada. Ia merupakan opsi alternatif dari radio button."
)
genre = st.selectbox(
    label="What's your favorite movie genre", options=("Comedy", "Drama", "Documentary")
)

st.text(
    "Multiselect. Ia merupakan widget yang digunakan agar user dapat memilih lebih dari satu pilihan dari sekumpulan pilihan yang ada."
)
genre = st.multiselect(
    label="What's your favorite movie genre", options=("Comedy", "Drama", "Documentary")
)

st.text(
    "Slider merupakan widget yang memungkinkan pengguna untuk untuk memilih nilai (atau range nilai) dari sebuah range nilai yang telah ditentukan. "
)
values = st.slider(
    label="Select a range of values", min_value=0, max_value=100, value=(0, 100)
)
st.write("Values:", values)
