import streamlit as st
from config import config

# Set page config
icon_image = f"{config.LOGO_ICON_PATH}{st.session_state.theme}.png"
st.set_page_config(
    page_title=f"{config.APP_NAME} - Terms of Service",
    page_icon=icon_image,
    initial_sidebar_state="expanded",
)

# Language selection
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

st.markdown(f"# {_lang['Terms of Service']}")

if lang == "de":
    st.markdown("""
Dieses Dokument ist eine **Vorlage**. Ersetze den Inhalt durch deine eigenen Nutzungsbedingungen.

## 1. Geltungsbereich
Beschreibe, für welches Produkt und welche Nutzer diese Bedingungen gelten.

## 2. Nutzung des Dienstes
Definiere erlaubte und untersagte Nutzung, Kontopflichten, usw.

## 3. Abonnements & Zahlungen
Beschreibe Preise, Abrechnung, Kündigung, Rückerstattungen.

## 4. Haftungsausschluss
Füge passende Haftungs- und Gewährleistungsausschlüsse hinzu.

## 5. Kontakt
Gib eine Kontaktadresse an.
""")
else:
    st.markdown("""
This document is a **template**. Replace the content with your own Terms of Service.

## 1. Scope
Describe which product and which users these terms apply to.

## 2. Use of the Service
Define acceptable use, prohibited use, account responsibilities, etc.

## 3. Subscriptions & Payments
Describe pricing, billing, cancellation, refunds.

## 4. Disclaimers
Add appropriate warranty and liability disclaimers.

## 5. Contact
Provide a contact address.
""")
