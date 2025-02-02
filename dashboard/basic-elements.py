import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.write(
    pd.DataFrame(
        {
            "c1": [1, 2, 3, 4],
            "c2": [10, 20, 30, 40],
        }
    )
)

st.title("Belajar Analisis Data")
st.header("Pengembangan Dashboard")
st.subheader("Pengembangan Dashboard")
st.text("Halo, calon praktisi data masa depan.")
st.caption("Copyright (c) 2023")
code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language="python")

st.markdown(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)
st.latex(
    r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
"""
)

df = pd.DataFrame(
    {
        "c1": [1, 2, 3, 4],
        "c2": [10, 20, 30, 40],
    }
)
st.text(
    "dataframe(). Ia merupakan function yang digunakan untuk menampilkan DataFrame sebagai sebuah tabel interaktif. Pada function ini, kita bisa mengatur ukuran dari table yang ingin ditampilkan menggunakan parameter width dan height. Berikut merupakan contoh kode untuk menampilkan data menggunakan function dataframe()."
)
st.dataframe(data=df, width=500, height=150)

st.text(
    "Selain dataframe(), kita juga bisa menggunakan function table()untuk menampilkan data ke dalam streamlit app. Ia dapat digunakan untuk menampilkan data dalam bentuk static table. Berikut merupakan contoh penggunaannya."
)
df = pd.DataFrame(
    {
        "c1": [1, 2, 3, 4],
        "c2": [10, 20, 30, 40],
    }
)
st.table(data=df)

st.text(
    "Ketika membuat dashboard, terkadang kita perlu menampilkan sebuah metrik tertentu. Untuk melakukan hal ini, kita bisa memanfaatkan function metric(). Function ini dapat membantu kita untuk menampilkan sebuah metrik tertentu beserta detailnya seperti label, value serta besar perubahan nilainya. Berikut merupakan contoh kode untuk menggunakannya."
)
st.metric(label="Temperature", value="28 °C", delta="1.2 °C")

st.text(
    "Selain bentuk DataFrame atau tabel, terkadang kita juga perlu menampilkan data dalam format JSON. Streamlit telah menyediakan function json() untuk menampilkan data dalam format JSON. Berikut merupakan contoh penggunaannya."
)
st.json(
    {
        "c1": [1, 2, 3, 4],
        "c2": [10, 20, 30, 40],
    }
)

x = np.random.normal(15, 5, 250)

st.text(
    "Basic element terakhir yang perlu kita ketahui ialah chart. "
    "Sesuai namanya, elemen ini dapat digunakan untuk menampilkan grafik visualisasi data ke dalam streamlit app. Elemen inilah yang akan sering kita gunakan untuk membuat dashboard nantinya. Sebenarnya streamlit telah menyediakan banyak sekali function untuk mendukung berbagai library visualisasi data (dokumentasi: chart). Namun, pada materi ini, kita hanya akan fokus pada function pyplot()."
    "Function pyplot() dapat digunakan untuk menampilkan grafik visualisasi data yang dibuat menggunakan matplotlib. Berikut merupakan contoh kode untuk menggunakannya."
)
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)
