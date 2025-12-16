import streamlit as st
from st_paywall import add_auth
import stripe
import sys
import os
from langfuse import get_client

# Add the parent directory to the path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import config


def get_available_languages():
    """Get all available languages from the locales directory."""
    locales_dir = os.path.join(os.path.dirname(__file__), 'locales')
    languages = []
    
    if os.path.exists(locales_dir):
        for file in os.listdir(locales_dir):
            if file.endswith('.py') and not file.startswith('__'):
                lang_code = file[:-3]  # Remove .py extension
                languages.append(lang_code)
    
    # Sort languages for consistent ordering
    languages.sort()
    return languages


def get_language_display_names():
    """Get display names for languages."""
    display_names = {
        'en': 'English',
        'de': 'Deutsch',
        'fr': 'Français',
        'es': 'Español',
        'it': 'Italiano',
        'pt': 'Português',
        'nl': 'Nederlands',
        'ru': 'Русский',
        'zh': '中文',
        'ja': '日本語',
        'ko': '한국어',
        'ar': 'العربية'
    }
    return display_names


# Set Stripe API key from secrets
STRIPE_ENABLED = st.secrets.get("stripe_enabled", True)
if STRIPE_ENABLED:
    if st.secrets.get("testing_mode", False):
        stripe.api_key = st.secrets.get("stripe_api_key_test", "")
    else:
        stripe.api_key = st.secrets.get("stripe_api_key", "")
else:
    stripe.api_key = None

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
    page_title=f"{config.APP_NAME}", 
    page_icon=icon_image,
    layout="centered",
    initial_sidebar_state="expanded"
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

# Display CorpusCoreSaaS team image in sidebar above all pages
#with st.sidebar:
#    st.image(f"{config.LOGO_TEXT_PATH}{st.session_state.theme}.png", width=250)

def is_email_subscribed_to_product(email):
    """
    Check if an email is subscribed to any product.
    Returns True if subscribed, False if not subscribed or if there's an API error.
    """
    # If Stripe is disabled, default to free tier
    if not STRIPE_ENABLED or not stripe.api_key:
        return False
    
    try:
        # Try to list customers by email
        customers = stripe.Customer.list(email=email, limit=10)
        
        for customer in customers.data:
            try:
                # Check if customer has any active subscriptions
                subscriptions = stripe.Subscription.list(
                    customer=customer['id'], 
                    status='active',
                    limit=10
                )
                
                # If any active subscription exists, consider them subscribed
                if subscriptions.data:
                    return True
                    
            except stripe.error.StripeError as e:
                # Log the error but continue checking other customers
                st.error(f"Error checking subscriptions for customer {customer['id']}: {str(e)}")
                continue
                
    except stripe.error.PermissionError:
        # Handle permission errors gracefully
        st.warning("Unable to verify subscription status due to API permissions. Defaulting to free tier.")
        return False
        
    except stripe.error.StripeError as e:
        # Handle other Stripe API errors
        st.error(f"Stripe API error: {str(e)}")
        return False
        
    except Exception as e:
        # Handle any other unexpected errors
        st.error(f"Unexpected error checking subscription: {str(e)}")
        return False
    
    return False


def _build_pages(_lang, is_logged_in, is_subscribed):
    pages = []
    for page_def in config.PAGES:
        access = page_def.get("access", "public")
        if access == "public":
            allowed = True
        elif access == "logged_in":
            allowed = is_logged_in
        elif access == "subscribed":
            allowed = is_logged_in and is_subscribed
        else:
            allowed = False

        if not allowed:
            continue

        title_key = page_def.get("title_key")
        title = _lang.get(title_key, title_key)

        pages.append(
            st.Page(
                page_def["path"],
                title=title,
                icon=page_def.get("icon"),
                url_path=page_def.get("url_path"),
            )
        )
    return pages


# Add pages
pages = _build_pages(_lang, st.user.is_logged_in, False)


if st.user.is_logged_in:
    with st.sidebar:
        is_subscribed = is_email_subscribed_to_product(st.user.email)

        pages = _build_pages(_lang, st.user.is_logged_in, is_subscribed)
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
            #st.image(f"{config.LOGO_TEAM_PATH}{st.session_state.theme}.png", width=200)

            # Apply theme-specific styles with proper Streamlit element targeting
            if st.session_state.theme == "dark":
                with open("styles_dark.css") as f:
                    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
            else:
                with open("styles_light.css") as f:
                    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

        with col2t:
            # Language selection - dynamically get available languages
            available_languages = get_available_languages()
            display_names = get_language_display_names()
            
            # Create format function that handles unknown languages gracefully
            def format_language(lang_code):
                return display_names.get(lang_code, lang_code.upper())
            
            # Ensure current language is in available languages, fallback to first available
            current_lang = st.session_state.get('lang', 'en')
            if current_lang not in available_languages and available_languages:
                current_lang = available_languages[0]
                st.session_state.lang = current_lang
            
            # Get current language index
            try:
                current_index = available_languages.index(current_lang) if current_lang in available_languages else 0
            except (ValueError, IndexError):
                current_index = 0
            
            lang = st.selectbox(
                "Language",
                options=available_languages,
                format_func=format_language,
                index=current_index,
                label_visibility="collapsed"
            )

            st.session_state.lang = lang

            if st.session_state.lang == 'en':
                from locales.en import translations
            elif st.session_state.lang == 'de':
                from locales.de import translations

            _lang = translations[st.session_state.lang]

page = st.navigation(pages)
page.run()