import streamlit as st
from st_paywall import add_auth
import stripe
import sys
import os

# Add the parent directory to the path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import config

# Set Stripe API key from secrets
if st.secrets.get("testing_mode", False):
    stripe.api_key = st.secrets.get("stripe_api_key_test", "")
else:
    stripe.api_key = st.secrets.get("stripe_api_key", "")

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

# Theme selection
if "theme" not in st.session_state:
    st.session_state.theme = "light"  # Default theme

# Apply theme-specific styles with proper Streamlit element targeting
if st.session_state.theme == "dark":
    with open("styles_dark.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    with open("styles_light.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Set page config
icon_image = f"{config.LOGO_ICON_PATH}{st.session_state.theme}.png"
st.set_page_config(
    page_title="GodsinWhite Login", 
    page_icon=icon_image,
    layout="centered",
    #initial_sidebar_state="collapsed"
)

# Logo in sidebar
logo_image = f"{config.LOGO_TEXT_PATH}{st.session_state.theme}.png"
#st.write(logo_image)
#breakpoint()
st.logo(logo_image,
    size="large",
    icon_image=icon_image
)

# Remove the menu and footer
with open("styles_common.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Display GodsinWhite team image in sidebar above all pages
#with st.sidebar:
#    st.image(f"./assets/godsinwhite_team_{st.session_state.theme}.png", width=250)

def is_email_subscribed_to_product(email):
    for customer in stripe.Customer.list(email=email):
        for subscription in stripe.Subscription.list(customer=customer['id']):
            #if subscription['plan']['product'] == product:
            return True
    return False


# Add pages
pages = [
    st.Page(
        "pages/Home.py",
        title=_lang["Home"],
        icon=":material/home:"
    ),
]


if not st.user.is_logged_in:
    main_container = st.container(
        key="form",
        border=True
    )

    with main_container:
        
    
        # Center the content using columns
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(f"assets/godsinwhite_team_{st.session_state.theme}.png", width=250)
        with col2:

            st.markdown("""
            <p style="font-family: 'Roboto', sans-serif; font-size: 24px; font-weight: 300; line-height: 1.5; color: #333;">
            We are <b>Gods in White</b>  
            </p>
            """, unsafe_allow_html=True)
            st.markdown(_lang["Welcome to the Medical AI Platform"] + "<br>  " + _lang["Login with your Google or Microsoft account"] + "  ", unsafe_allow_html=True)
    
            # Create the login buttons
            if st.button(_lang["Login or Sign up"], key="login_auth0", use_container_width=True, type="primary"):
                st.login(provider="auth0")
            #if st.button(_lang["Login with Microsoft"], key="microsoft_login", use_container_width=True, type="secondary"):
            #    st.login(provider="auth0")

            st.markdown("<br>  <font size='2'>" + _lang["By clicking, you agree to our Terms of Service and Privacy Policy."] + "</font>", unsafe_allow_html=True)

else:
    with st.sidebar:
        pages.append(
            st.Page(
                "pages/Medical_Image_Analysis.py",
                title=_lang["Medical Image Analysis"],
                icon=":material/diagnosis:"
            ),
        )

        is_subscribed = is_email_subscribed_to_product(st.user.email)
        if not is_subscribed:
            col1p = st.columns([1], vertical_alignment="center", border=True)[0]
            with col1p:
                st.markdown(f"<p align='center' style='font-size: 20px; font-weight: bold;'>{_lang['Upgrade to Premium']}</p>", unsafe_allow_html=True)
                st.markdown(f"<p align='center' style='font-size: 14px;'>{_lang['Get 14 days free and unlock all Premium features.']}</p>", unsafe_allow_html=True)
                col1up = st.columns([1])[0]
            with col1up:
                add_auth(
                    required=False,  # Don't stop the app for non-subscribers
                    show_redirect_button=True,
                    subscription_button_text=_lang["Upgrade"],
                    #button_color="#4CAF50",  # Green button
                    button_color="#cb785c",
                    #use_sidebar=False  # Show button in main section
                )

        account_page = "Account"
        col1s, col2s = st.columns([0.2, 0.8])
        with col1s:
            if st.user.is_logged_in:
                avatar = st.user.picture
                st.markdown(f"<a href='{account_page}' style='text-decoration: none;' target='_self'><div style='font-size: 24px; margin-top: 15px;'><img src='{avatar}' style='width: 34px; height: 34px; border-radius: 50%;'></div></a>", unsafe_allow_html=True)
            else:
                st.markdown(f"<a href='{account_page}' style='text-decoration: none;' target='_self'><div style='font-size: 24px; margin-top: 15px;'>:material/account_circle:</div></a>", unsafe_allow_html=True)
        with col2s:
            #is_subscribed = is_email_subscribed_to_product(st.user.email)
            #color = "red" if not is_subscribed else "green"
            color = "grey"
            if is_subscribed:
                account_type = _lang["Premium (Paid)"]
            else:
                account_type = _lang["Free (Trial)"]
            
            st.markdown(f"<a href='{account_page}' style='text-decoration: none;' target='_self'><div style='margin-top: 15px;'>{st.user.name}</div></a>", unsafe_allow_html=True)
            st.markdown(f"<div style='margin-top: -22px; color:{color}; font-size: 12px'>{account_type}</div>", unsafe_allow_html=True)

        if st.button(f":material/logout: {_lang['Sign out']}", use_container_width=True, type="secondary"):
            st.logout()
            st.rerun()
            

        col1t, col2t = st.columns([0.2, 0.6], vertical_alignment="top")
        with col1t:
            # Initialize session state for theme
            if "theme" not in st.session_state or not isinstance(st.session_state.theme, str):
                st.session_state.theme = "light"  # Default theme

            # Function to toggle theme
            if st.session_state.theme == "light":
                if st.button(":material/dark_mode:", key="theme_btn_dark"):
                    st.session_state.theme = "dark"
                    st.rerun()
            else:
                if st.button(":material/light_mode:", key="theme_btn_light"):
                    st.session_state.theme = "light"
                    st.rerun()

            # Display the current theme
            #st.write(f"Current Theme: {st.session_state.theme}")
            #st.image(f"./assets/godsinwhite_team_{st.session_state.theme}.png", width=200)

            # Apply theme-specific styles with proper Streamlit element targeting
            if st.session_state.theme == "dark":
                with open("styles_dark.css") as f:
                    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
            else:
                with open("styles_light.css") as f:
                    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

        with col2t:
            # Language selection
            lang = st.selectbox(
                "Language",
                options=['en', 'de'],
                format_func=lambda x: {'en': 'English', 'de': 'Deutsch'}[x],
                index=(0 if st.session_state['lang'] == 'en' else 1),
                label_visibility="collapsed"
            )

            st.session_state.lang = lang

            if st.session_state.lang == 'en':
                from locales.en import translations
            elif st.session_state.lang == 'de':
                from locales.de import translations

            _lang = translations[st.session_state.lang]

        # Add pages
        if is_subscribed:
            pages.append(
                st.Page(
                    "pages/Experts_Chat.py",
                    title=_lang["Experts Chat"],
                    icon=":material/chat:"
                )
            )
        
        if st.user.is_logged_in:
            pages.append(
                st.Page(
                    "pages/Account.py",
                    title=_lang["Account"],
                    icon=":material/account_circle:"
                )
            )

        if not is_subscribed:
            pages.append(
                st.Page(
                    "pages/Pricing.py",
                    title=_lang["Pricing"],
                    icon=":material/sell:"
                )
            )
            
        pages.append(
            st.Page(
                "pages/Help.py",
                title=_lang["Help"],
                icon=":material/help:"
            )
        )
        pages.append(
            st.Page(
                "pages/About.py",
                title=_lang["About"],
                icon=":material/info:"
            )
        )

page = st.navigation(pages)
page.run()