import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Belajar Analisis Data")
st.subheader("Sidebar")
st.text(
    "Untuk menambahkan sebuah elemen atau widget ke dalam sidebar, kita bisa menggunakan notasi with yang diikuti sebuah object bernama sidebar yang telah disediakan oleh streamlit"
)

with st.sidebar:

    st.text("Ini merupakan sidebar")

    values = st.slider(
        label="Select a range of values", min_value=0, max_value=100, value=(0, 100)
    )
    st.write("Values:", values)


st.subheader("Columns")
st.text(
    "Columns merupakan elemen layout yang memungkinkan kita untuk mengatur tampilan pada konten utama ke dalam beberapa kolom sesuai kebutuhan. Gambar berikut merupakan ilustrasi tampilan dari elemen layout ini. "
)

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Kolom 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("Kolom 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("Kolom 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")

st.text(
    "Sebenarnya, kita bisa dengan bebas mengatur ukuran dari column yang dibuat. Nah, untuk melakukan hal ini, kita harus memasukkan sebuah list yang berisi perbandingan ukuran dari kolom yang akan dibuat. Sebagai contoh, kode di bawah ini akan menampilkan 3 buah kolom  dengan perbandingan 2:1:1."
)
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    st.header("Kolom 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("Kolom 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("Kolom 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")

st.subheader("Tabs")
st.text(
    "Elemen layout berikutnya yang terdapat dalam streamlit ialah tabs. Ia merupakan elemen layout yang memungkinkan kita untuk menambahkan beberapa tabs ke dalam konten utama. Hal ini tentunya akan sangat membantu kita dalam menghasilkan dashboard yang interaktif. "
)
st.text(
    "Sama halnya dengan columns yang sebelumnya kita bahas, untuk membuat tabs, kita harus membuat object dari setiap tab menggunakan function tabs() yang diikuti dengan list dari nama dari setiap tab. Berikut contoh kode untuk membuat tabs dalam streamlit app."
)

tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.header("Tab 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with tab2:
    st.header("Tab 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with tab3:
    st.header("Tab 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")

st.subheader("Container")
st.text(
    "Container merupakan elemen layout dalam streamlit yang memungkinkan kita untuk membuat sebuah wadah untuk menampung suatu atau beberapa elemen dengan ukuran yang tetap. Container ini dapat kita gunakan untuk menghasilkan dashboard yang rapi."
)
st.text(
    "Untuk membuat container, kita bisa menggunakan notasi with dan diikuti function container(). Kode di bawah ini merupakan contoh kode untuk membuat container dalam streamlit app. "
)

with st.container():
    st.write("Inside the container")

    x = np.random.normal(15, 5, 250)

    fig, ax = plt.subplots()
    ax.hist(x=x, bins=15)
    st.pyplot(fig)

st.write("Outside the container")

st.subheader("Expander")
st.text(
    "Elemen layout selanjutnya yang tidak kalah penting ialah expander. Anda dapat menganggap elemen layout ini sebagai sebuah container yang dapat diperluas atau diciutkan secara interaktif. "
)
st.text(
    "Untuk membuat elemen layout ini, kita bisa menggunakan notasi with dan diikuti dengan function expander() "
)
x = np.random.normal(15, 5, 250)
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)

with st.expander("See explanation"):
    st.write(
        """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor 
        in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
        nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
        sunt in culpa qui officia deserunt mollit anim id est laborum.
        """
    )
