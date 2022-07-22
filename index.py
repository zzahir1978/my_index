import streamlit as st

st.set_page_config('Zahiruddin Page', ':globe_with_meridians:', layout='wide')
st.header(':globe_with_meridians:' + " " + 'My Web Page')
st.subheader('List Of Webpages:-')
st.write('1. [Main Dashboard](https://share.streamlit.io/zzahir1978/my_dashboard/main/app.py?utm_source=streamlit&utm_medium=zzahir1978@gmail.com&utm_campaign=dashboard)')
st.write('2. [Covid Dashboard](https://zzahir1978-covid-dashboard-covid-gpsg1z.streamlitapp.com/)')
st.write('3. [Utilities Dashboard](https://zzahir1978-utility-dashboard-app-pfacnz.streamlitapp.com/?utm_source=streamlit&utm_medium=zzahir1978@gmail.com&utm_campaign=utility+dashboard)')
st.write('4. [Job Sheet Dashboard](https://zzahir1978-user-dashboard-main-vy308e.streamlitapp.com/)')

# --- HIDE STREAMLIT STYLE ---

hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)