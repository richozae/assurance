# import streamlit as st
# import pickle
# import pandas as pd
# import numpy as np
# from sklearn.preprocessing import LabelEncoder

# # Load the KNN model from the pickle file
# with open('knn_model.pkl', 'rb') as file:
#     knn_model = pickle.load(file)

# # Title of the Streamlit app
# st.title('Prediksi Biaya Asuransi')

# # User inputs
# usia = st.number_input('Usia', min_value=0, max_value=120, value=25)
# jenis_kelamin = st.selectbox('Jenis Kelamin', ['male', 'female'])
# kadar_lemak = st.number_input('Kadar Lemak', min_value=0.0, max_value=100.0, value=20.0)
# jml_anak = st.number_input('Jumlah Anak', min_value=0, max_value=10, value=0)
# status_perokok = st.selectbox('Status Perokok', ['yes', 'no'])
# asal = st.selectbox('Asal', ['southwest', 'southeast', 'northwest', 'northeast'])

# # Encode categorical variables
# le_jeniskelamin = LabelEncoder()
# le_statperokok = LabelEncoder()
# le_asal = LabelEncoder()

# # Fit the LabelEncoder with the possible values
# le_jeniskelamin.fit(['male', 'female'])
# le_statperokok.fit(['yes', 'no'])
# le_asal.fit(['southwest', 'southeast', 'northwest', 'northeast'])

# jenis_kelamin_encoded = le_jeniskelamin.transform([jenis_kelamin])[0]
# status_perokok_encoded = le_statperokok.transform([status_perokok])[0]
# asal_encoded = le_asal.transform([asal])[0]

# # Prepare the input data for prediction
# input_data = pd.DataFrame({
#     'Usia': [usia],
#     'JenisKelamin': [jenis_kelamin_encoded],
#     'KadarLemak': [kadar_lemak],
#     'JmlAnak': [jml_anak],
#     'StatusPerokok': [status_perokok_encoded],
#     'Asal': [asal_encoded]
# })

# # Prediction button
# if st.button('Simpan dan Proses'):
#     # Make prediction
#     prediction = knn_model.predict(input_data)
#     st.write(f'Prediksi Biaya Asuransi: {prediction[0]:.2f}')










import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Load the KNN model from the pickle file
with open('knn_model.pkl', 'rb') as file:
    knn_model = pickle.load(file)

# Title and description
st.title('🎯 Prediksi Biaya Asuransi')
st.markdown("""
<style>
body {
    background-color: #f7f7f7;
}
h1 {
    color: #ff6347;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)
st.write("Masukkan detail informasi di bawah ini untuk memprediksi biaya asuransi Anda:")

# Sidebar for user inputs
st.sidebar.header('Input Parameter')
usia = st.sidebar.number_input('Usia', min_value=0, max_value=120, value=25, help="Masukkan usia Anda")
jenis_kelamin = st.sidebar.selectbox('Jenis Kelamin', ['male', 'female'], help="Pilih jenis kelamin Anda")
kadar_lemak = st.sidebar.number_input('Kadar Lemak', min_value=0.0, max_value=100.0, value=20.0, help="Masukkan kadar lemak tubuh Anda (%)")
jml_anak = st.sidebar.number_input('Jumlah Anak', min_value=0, max_value=10, value=0, help="Masukkan jumlah anak Anda")
status_perokok = st.sidebar.selectbox('Status Perokok', ['yes', 'no'], help="Apakah Anda perokok?")
asal = st.sidebar.selectbox('Asal', ['southwest', 'southeast', 'northwest', 'northeast'], help="Pilih asal daerah Anda")

# Encode categorical variables
le_jeniskelamin = LabelEncoder()
le_statperokok = LabelEncoder()
le_asal = LabelEncoder()

# Fit the LabelEncoder with the possible values
le_jeniskelamin.fit(['male', 'female'])
le_statperokok.fit(['yes', 'no'])
le_asal.fit(['southwest', 'southeast', 'northwest', 'northeast'])

jenis_kelamin_encoded = le_jeniskelamin.transform([jenis_kelamin])[0]
status_perokok_encoded = le_statperokok.transform([status_perokok])[0]
asal_encoded = le_asal.transform([asal])[0]

# Prepare the input data for prediction
input_data = pd.DataFrame({
    'Usia': [usia],
    'JenisKelamin': [jenis_kelamin_encoded],
    'KadarLemak': [kadar_lemak],
    'JmlAnak': [jml_anak],
    'StatusPerokok': [status_perokok_encoded],
    'Asal': [asal_encoded]
})

# Display input summary
st.write("### Ringkasan Input")
st.write(f"**Usia**: {usia} tahun")
st.write(f"**Jenis Kelamin**: {jenis_kelamin}")
st.write(f"**Kadar Lemak**: {kadar_lemak}%")
st.write(f"**Jumlah Anak**: {jml_anak}")
st.write(f"**Status Perokok**: {status_perokok}")
st.write(f"**Asal**: {asal}")

# Prediction button
if st.button('🔮 Prediksi Biaya'):
    # Make prediction
    prediction = knn_model.predict(input_data)
    st.success(f'### Prediksi Biaya Asuransi: ${prediction[0]:,.2f}')
    
    # Plotting the results
    st.write("### Visualisasi Prediksi")
    st.bar_chart(pd.DataFrame({
        'Parameter': ['Usia', 'Jenis Kelamin', 'Kadar Lemak', 'Jumlah Anak', 'Status Perokok', 'Asal'],
        'Nilai': [usia, jenis_kelamin_encoded, kadar_lemak, jml_anak, status_perokok_encoded, asal_encoded]
    }).set_index('Parameter'))

    # Additional insights
    st.write("### Insights Prediction")
    st.info("Biaya asuransi dapat dipengaruhi oleh berbagai faktor seperti usia, status perokok, dan lain-lain. Pastikan untuk selalu menjaga kesehatan Anda.")

# Footer
st.markdown("""
<hr>
<p style='text-align: center;'>Developed My Application ❤️ by [Richo]</p>
""", unsafe_allow_html=True)









