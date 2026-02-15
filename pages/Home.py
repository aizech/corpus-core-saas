import streamlit as st
from config import config
from st_paywall import add_auth

# Set page config
icon_image = f"{config.LOGO_ICON_PATH}{st.session_state.theme}.png"
st.set_page_config(
    page_title=f"{config.APP_NAME} - Home",
    page_icon=icon_image,
    # layout="wide",
    initial_sidebar_state="expanded",
)

# Language selection
# get browser language
# st.write(f"Locale: {st.context.locale}")
browser_language = st.session_state.get("browser_language", "en")
if "lang" not in st.session_state:
    st.session_state.lang = browser_language
    lang = browser_language
else:
    lang = st.session_state.lang

if lang == "en":
    from locales.en import translations
elif lang == "de":
    from locales.de import translations

_lang = translations[lang]


if st.user.is_logged_in:
    one_cola = st.columns([1])[0]
    with one_cola:
        col1a, col2a = st.columns([2, 6])

        with col1a:
            # team_image = config.LOGO_TEAM_PATH
            st.image(f"assets/godsinwhite_team_{st.session_state.theme}.png", width=400)
            # st.image(team_image, width=400)
        with col2a:
            st.markdown(
                f"""
            ## {_lang["Welcome to CorpusCoreSaaS"]}  
            {_lang["Gods in White is your personal gateway to advanced medical diagnostics—powered by AI and backed by real medical expertise. Designed for patients, healthcare professionals, and curious minds alike, this app transforms how medical images are analyzed and understood."]}
            """,
                unsafe_allow_html=True,
            )

        st.markdown(f"{_lang['Nice to see you']}, {st.user.name}")
        # st.image(st.user.picture)
        # st.markdown(" ")
        # st.markdown("You are logged in")

else:
    main_container = st.container(key="form", border=True)

    with main_container:
        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(f"{config.LOGO_TEAM_PATH}{st.session_state.theme}.png", width=250)
        with col2:
            st.markdown(
                f"""
            <p style="font-family: 'Roboto', sans-serif; font-size: 24px; font-weight: 300; line-height: 1.5; color: #333;">
            Welcome to <b>{config.APP_NAME}</b>  
            </p>
            """,
                unsafe_allow_html=True,
            )
            st.markdown(
                _lang["Welcome to the Corpus Analytica Platform"]
                + "<br>  "
                + _lang["Login with your Google or Microsoft account"]
                + "  ",
                unsafe_allow_html=True,
            )

            if st.button(
                _lang["Login or Sign up"],
                key="login_auth0",
                width="stretch",
                type="primary",
            ):
                st.login(provider="auth0")

            st.markdown(
                "<br>  <font size='2'>"
                + _lang[
                    "By clicking, you agree to our Terms of Service and Privacy Policy."
                ]
                + "</font>",
                unsafe_allow_html=True,
            )
