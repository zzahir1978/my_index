import streamlit as st

st.set_page_config('Zahiruddin Page', ':globe_with_meridians:', layout='wide')
st.header(':globe_with_meridians:' + " " + 'My Web Page')
st.subheader('List Of Webpages:-')
st.write('1. [Main Dashboard](https://share.streamlit.io/zzahir1978/my_dashboard/main/app.py?utm_source=streamlit&utm_medium=zzahir1978@gmail.com&utm_campaign=dashboard)')
st.write('2. [Utilities Dashboard](https://zzahir1978-utility-dashboard-app-pfacnz.streamlitapp.com/?utm_source=streamlit&utm_medium=zzahir1978@gmail.com&utm_campaign=utility+dashboard)')
st.write('3. [Covid Dashboard](https://zzahir1978-covid-dashboard-covid-gpsg1z.streamlitapp.com/)')
st.write('4. [User Dashboard](https://zzahir1978-user-dashboard-main-vy308e.streamlitapp.com/)')
#st.markdown("[![Foo](http://www.google.com.au/images/nav_logo7.png)](http://google.com.au/)")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.subheader("Get In Touch With Me!")
    st.write("##")

# Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/bf85918df6af8e2139d0a995ae42c37a" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()

# --- HIDE STREAMLIT STYLE ---

hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)