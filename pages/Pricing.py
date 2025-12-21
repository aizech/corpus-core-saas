import streamlit as st
from st_paywall import add_auth
from config import config

# Set page config
icon_image = f"{config.LOGO_ICON_PATH}{st.session_state.theme}.png"
st.set_page_config(
    page_title=f"{config.APP_NAME} - Pricing", 
    page_icon=icon_image,
    #layout="wide",
    initial_sidebar_state="expanded"
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
            ## {_lang["Pricing"]}  
            """, unsafe_allow_html=True)

height = 50
st.markdown(f'<div style="height: {height}px;"></div>', unsafe_allow_html=True)


# Pricing Page
plans = {
    "Free": {
        "price": 0.00,
        #"features": [_lang["Free use for 14 days"], _lang["Premium"], "&nbsp;", "&nbsp;"],
        "features": [_lang["Trial Content"], "&nbsp;", "&nbsp;", "&nbsp;"],
    },
    "Premium": {
        "price": 15.00,
        "features": [_lang["Unlimited use"], _lang["Premium"], _lang["AI doctor consultation"], _lang["... many more features"]],
    },
}

plan_names = list(plans.keys())
col1, col2 = st.columns(2, gap="small", border=True, vertical_alignment="top")
with col1:
    st.markdown("## " + plan_names[0])
    st.markdown("### " + f"{plans[plan_names[0]]['price']} EUR")
    features = "<br>".join([f"{feature}" for feature in plans[plan_names[0]]["features"]])
    st.markdown(features, unsafe_allow_html=True)
    #add_auth(
    #    required=False,  # Don't stop the app for non-subscribers
    #    show_redirect_button=True,
    #    subscription_button_text=_lang["Upgrade"],
    #    button_color="#cb785c",  # Green button
    #    use_sidebar=False  # Show button in main section
    #)

with col2:
    #st.markdown(":blue-badge[most popular]")
    st.markdown("## " + plan_names[1])
    st.markdown("### " + f"{plans[plan_names[1]]['price']} EUR / month")
    features = "<br>".join([f"{feature}" for feature in plans[plan_names[1]]["features"]])
    st.markdown(features, unsafe_allow_html=True)
    add_auth(
        required=False,  # Don't stop the app for non-subscribers
        show_redirect_button=True,
        subscription_button_text=_lang["Upgrade"],
        button_color="#cb785c",  # Green button
        use_sidebar=False  # Show button in main section
    )


