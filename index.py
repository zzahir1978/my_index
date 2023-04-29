import streamlit as st

st.set_page_config('Zahiruddin Page', ':globe_with_meridians:', layout='wide')
col1, col2, col3 = st.columns(3)
col2.header(':globe_with_meridians:' + " " + 'My Web Page')
col2.write("##")
col2.subheader(':page_facing_up: [Main Dashboard](https://share.streamlit.io/zzahir1978/my_dashboard/main/app.py?utm_source=streamlit&utm_medium=zzahir1978@gmail.com&utm_campaign=dashboard)')
col2.subheader(':pill: [KKM Dashboard](https://zzahir1978-covid-dashboard-covid-gpsg1z.streamlitapp.com/)')
col2.subheader(':bulb:[Utility Dashboard](https://zzahir1978-utility-dashboard-app-vjaj6n.streamlitapp.com/)')
col2.subheader(':bust_in_silhouette: [User Dashboard](https://zzahir1978-user-dashboard-main-vy308e.streamlitapp.com/)')
col2.subheader(':mag: [Python WebScraper](https://zzahir1978-webscraper-webscraper2-f6guvb.streamlitapp.com/)')
#col2.subheader(':inbox_tray: [PRU15 Dashboard (Coming Soon!)](https://zzahir1978-pkr-pkr-1ch5ix.streamlitapp.com/)')

# --- HIDE STREAMLIT STYLE ---

hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)
