from pathlib import Path

class Config:
    COMPANY = "CorpusCoreSaaS"
    COMPANY_URL = "https://www.corpusanalytica.com/"

    SUPPORT_URL = "https://www.corpusanalytica.com/support"

    # --- Constants & Directories ---
    APP_NAME      = "Corpus Core - SaaS"
    APP_ICON      = ":material/smart_toy:"
    APP_URL       = "https://www.corpusanalytica.com/"
    CONTACT_EMAIL = "support@corpusanalytica.com"

    THIS_DIR      = Path(__file__).parent
    #STYLES_DIR    = THIS_DIR / "styles"
    #CSS_FILE      = THIS_DIR / "styles" / "custom.css"
    ASSETS_DIR    = THIS_DIR / "assets"
    
    APP_DESCRIPTION = "Corpus Core - SaaS is a reusable Streamlit SaaS template with authentication, subscriptions, and page-level access control"

    PAGES = [
        {
            "path": "pages/Home.py",
            "title_key": "Home",
            "icon": ":material/home:",
            "access": "public",
        },
        {
            "path": "pages/Terms_of_Service.py",
            "title_key": "Terms of Service",
            "icon": ":material/gavel:",
            "access": "public",
            "url_path": "terms-of-service",
        },
        {
            "path": "pages/Privacy_Policy.py",
            "title_key": "Privacy Policy",
            "icon": ":material/privacy_tip:",
            "access": "public",
            "url_path": "privacy-policy",
        },
        {
            "path": "pages/Trial.py",
            "title_key": "Trial",
            "icon": ":material/diagnosis:",
            "access": "logged_in",
        },
        {
            "path": "pages/Premium.py",
            "title_key": "Premium",
            "icon": ":material/chat:",
            "access": "subscribed",
        },
        {
            "path": "pages/Account.py",
            "title_key": "Account",
            "icon": ":material/account_circle:",
            "access": "logged_in",
        },
        {
            "path": "pages/Pricing.py",
            "title_key": "Pricing",
            "icon": ":material/sell:",
            "access": "logged_in",
        },
        {
            "path": "pages/Help.py",
            "title_key": "Help",
            "icon": ":material/help:",
            "access": "public",
        },
        {
            "path": "pages/About.py",
            "title_key": "About",
            "icon": ":material/info:",
            "access": "public",
        },
    ]

    MENU_ITEMS = {
        'Get Help': f"{APP_URL}/help",
        'Report a bug': f"{APP_URL}/about",
        'About': "## This is the " + APP_NAME + " App!  Made with " + ":heart: by " + COMPANY
    }

    MASTER_AGENT_ICON = ASSETS_DIR / "godsinwhite_team_light.png"

    #LOGO_TEXT_PATH = ASSETS_DIR / "godsinwhite_logo_text_light.png"
    #LOGO_TEXT_PATH = ASSETS_DIR / "godsinwhite_logo_text_"
    LOGO_TEXT_PATH = ASSETS_DIR / "godsinwhite_team_"
    LOGO_ICON_PATH = ASSETS_DIR / "godsinwhite_logo_"
    LOGO_TEAM_PATH = ASSETS_DIR / "godsinwhite_team_"

    LEAD_AGENT_NAME = "Chief Doctor"
    TEAM_AGENT_NAME = "Specialists"

# Create a single instance to be imported by other modules
config = Config()
