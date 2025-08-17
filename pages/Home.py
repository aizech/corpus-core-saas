import streamlit as st
from config import config
from st_paywall import add_auth

# Set page config
icon_image = f"{config.LOGO_ICON_PATH}{st.session_state.theme}.png"
st.set_page_config(
    page_title="GodsinWhite Home", 
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


if st.user.is_logged_in:
    one_cola = st.columns([1])[0]
    with one_cola:
        col1a, col2a = st.columns([2, 6])

        with col1a:
            #team_image = config.LOGO_TEAM_PATH
            st.image(f"assets/godsinwhite_team_{st.session_state.theme}.png", width=400)
            #st.image(team_image, width=400)
        with col2a:
            st.markdown(f"""
            ## {_lang["Welcome to GodsinWhite"]}  
            {_lang["Gods in White is your personal gateway to advanced medical diagnostics—powered by AI and backed by real medical expertise. Designed for patients, healthcare professionals, and curious minds alike, this app transforms how medical images are analyzed and understood."]}
            """, unsafe_allow_html=True)

        st.markdown(f"{_lang['Nice to see you']}, {st.user.name}")
        #st.image(st.user.picture)
        #st.markdown(" ")
        #st.markdown("You are logged in")
        
else:
    #st.markdown("Please login first")
    st.markdown(" ")
