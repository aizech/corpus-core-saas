import streamlit as st
import os
from config import config

# Set page config
icon_image = f"{config.LOGO_ICON_PATH}{st.session_state.theme}.png"
st.set_page_config(
    page_title="GodsinWhite Pricing", 
    page_icon=icon_image,
    #layout="wide",
    #initial_sidebar_state="collapsed"
)

# Language selection
# get browser language
#st.write(f"Locale: {st.context.locale}")
browser_language = st.session_state.get('browser_language', 'en')
if 'lang' not in st.session_state:
    st.session_state.lang = browser_language
    lang = browser_language
else:
    lang = st.session_state.lang

if lang == 'en':
    from locales.en import translations
elif lang == 'de':
    from locales.de import translations

_lang = translations[lang]



# Page title
one_cola = st.columns([1])[0]
with one_cola:
    col1a, col2a = st.columns([2, 6])

    with col1a:
        #team_image = config.LOGO_TEAM_PATH
        st.image(f"assets/godsinwhite_team_{st.session_state.theme}.png", width=400)
        #st.image(team_image, width=400)
    with col2a:
        st.markdown(f"""
        ## {_lang['Help']}  
        *[{_lang['A Corpus Analytica Innovation']}](https://www.corpusanalytica.com)*
        """, unsafe_allow_html=True)
    
def read_locale_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

file_path = os.path.join('locales', 'help.' + lang + '.md')
locale_text = read_locale_file(file_path)

st.markdown(locale_text, unsafe_allow_html=True)