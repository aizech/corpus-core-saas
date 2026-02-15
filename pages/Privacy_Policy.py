import streamlit as st
from config import config

# Set page config
icon_image = f"{config.LOGO_ICON_PATH}{st.session_state.theme}.png"
st.set_page_config(
    page_title=f"{config.APP_NAME} - Privacy Policy",
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

st.markdown(f"# {_lang['Privacy Policy']}")

if lang == "de":
    st.markdown("""
Dieses Dokument ist eine **Vorlage**. Ersetze den Inhalt durch deine eigene Datenschutzerklärung.

## 1. Welche Daten wir verarbeiten
Beschreibe z.B. Kontodaten, Nutzungsdaten, Zahlungsdaten (Stripe), Logs.

## 2. Zweck der Verarbeitung
Z.B. Bereitstellung des Dienstes, Abrechnung, Support, Sicherheit.

## 3. Rechtsgrundlagen
Füge die passenden Rechtsgrundlagen (DSGVO) hinzu.

## 4. Weitergabe an Dritte
Z.B. Zahlungsanbieter (Stripe), Hosting, Analytics.

## 5. Aufbewahrung & Löschung
Definiere Aufbewahrungsfristen.

## 6. Kontakt
Gib Kontakt und ggf. Datenschutzbeauftragten an.
""")
else:
    st.markdown("""
This document is a **template**. Replace the content with your own Privacy Policy.

## 1. Data we process
For example: account data, usage data, payment data (Stripe), logs.

## 2. Purpose of processing
For example: providing the service, billing, support, security.

## 3. Legal basis
Add the appropriate legal bases (GDPR/other).

## 4. Sharing with third parties
For example: payment provider (Stripe), hosting, analytics.

## 5. Retention & deletion
Define retention periods.

## 6. Contact
Provide contact details and (if applicable) a DPO contact.
""")
