import streamlit as st
import stripe
from st_paywall import add_auth

# Page title
one_cola = st.columns([1])[0]
with one_cola:
    col1a, col2a = st.columns([2, 6])

    with col1a:
        # team_image = config.LOGO_TEAM_PATH
        st.image(f"assets/godsinwhite_team_{st.session_state.theme}.png", width=400)
        # st.image(team_image, width=400)
    with col2a:
        st.markdown(
            """
        # Account
        """,
            unsafe_allow_html=True,
        )


# Set Stripe API key from secrets
STRIPE_ENABLED = st.secrets.get("stripe_enabled", True)
if STRIPE_ENABLED:
    if st.secrets.get("testing_mode", False):
        stripe.api_key = st.secrets.get("stripe_api_key_test", "")
    else:
        stripe.api_key = st.secrets.get("stripe_api_key", "")
else:
    stripe.api_key = None


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
                    customer=customer["id"], status="active", limit=10
                )

                # If any active subscription exists, consider them subscribed
                if subscriptions.data:
                    return True

            except stripe.error.StripeError as e:
                # Log the error but continue checking other customers
                st.error(
                    f"Error checking subscriptions for customer {customer['id']}: {str(e)}"
                )
                continue

    except stripe.error.PermissionError:
        # Handle permission errors gracefully
        st.warning(
            "Unable to verify subscription status due to API permissions. Defaulting to free tier."
        )
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


is_subscribed = is_email_subscribed_to_product(st.user.email)

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
    # st.markdown(f"## Welcome {st.user.name}")

    if is_subscribed:
        account_type = _lang["Premium (Paid)"]
    else:
        account_type = _lang["Free (Trial)"]

    avatar = st.user.picture

    account_container = st.container()
    with account_container:
        # st.markdown(f"<div style='font-size: 24px;'><img src='{avatar}' style='width: 34px; height: 34px; border-radius: 50%; margin-bottom: 15px;'></div> {st.user.name} ({st.user.email})", unsafe_allow_html=True)

        col1s, col2s, col3s, col4s = st.columns(
            [0.1, 0.3, 0.4, 0.2], vertical_alignment="bottom"
        )
        with col1s:
            if st.user.is_logged_in:
                avatar = st.user.picture
                st.markdown(
                    f"<div style='font-size: 24px; margin-top: -22px;'><img src='{avatar}' style='width: 34px; height: 34px; border-radius: 50%; margin-bottom: 15px;'></div>",
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f"<div style='font-size: 24px; margin-top: -22px; margin-bottom: 15px;'>:material/account_circle:</div>",
                    unsafe_allow_html=True,
                )
        with col2s:
            # is_subscribed = is_email_subscribed_to_product(st.user.email)
            # color = "red" if not is_subscribed else "green"
            color = "grey"
            if is_subscribed:
                account_type = _lang["Premium (Paid)"]
            else:
                account_type = _lang["Free (Trial)"]

            st.markdown(
                f"<div style='margin-top: -22px;'>{st.user.name}</div>",
                unsafe_allow_html=True,
            )
            st.markdown(
                f"<div style='margin-top: -18px; color:{color}; font-size: 12px'>{account_type}</div>",
                unsafe_allow_html=True,
            )
        with col3s:
            # Only show Manage Subscription link for premium users
            if is_subscribed:
                st.markdown(
                    "<a href='https://billing.stripe.com/p/login/7sY4gA2m110Vanb3Op0Fi00' target='_blank'>Manage Subscription</a>",
                    unsafe_allow_html=True,
                )
            st.markdown(
                f"<div style='margin-top: -18px; color:{color}; font-size: 12px'>{st.user.email}</div>",
                unsafe_allow_html=True,
            )
        with col4s:
            if st.button(_lang["Sign out"], key="sign_out", type="secondary"):
                st.logout()

    st.markdown("---")

    if is_subscribed:
        st.markdown(
            f"*{_lang['Thank you for being a Valued Subscriber!']}*",
            unsafe_allow_html=True,
        )

        st.markdown(
            """

**{_lang['Dear']} {st.user.name},**

{_lang['We want to extend our heartfelt thanks for placing your trust in Gods in White and the Corpus Analytica mission. Your subscription empowers us to continue building a platform where cutting-edge technology meets compassionate care.']}.

{_lang['With your support, you have access to:']}:

- 🧠 {_lang['Unlimited medical image analysis']}

- 💬 {_lang['Direct chat with expert AI doctors']}

{_lang['Your commitment helps us bring clarity, confidence, and convenience to healthcare—one image, one consultation, one life at a time.']}.

> *"{_lang['Every subscriber strengthens our vision: to make expert medical guidance accessible to everyone, everywhere.']}"* — Bernhard Z., Founder of Corpus Analytica

{_lang['Thank you for being part of this journey. We\'re honored to support yours.']}

{_lang['Warm regards, The Corpus Analytica Team']}
            
            """,
            unsafe_allow_html=True,
        )

    else:
        # st.markdown(f"**{_lang['You are a']} {account_type} {_lang['subscriber']}.**")
        st.markdown(f"**{_lang['Thank you for being a Valued Subscriber!']}**")
        st.markdown("---")
        st.markdown(
            f"""    
## :material/star: {_lang['Unlock the Power of Expert Medical Insight']}

**{_lang['Dear']} {st.user.name},**

{_lang['Imagine having instant access to world-class physicians, AI-powered medical image analysis, and second opinions from specialists across the globe—all in one place.']}

{_lang['That\'s what Gods in White offers.']}

{_lang['By subscribing, you\'ll gain:']}

- 🧠 {_lang['Unlimited access to medical image analysis']}

- 💬 {_lang['Direct chat with expert AI doctors']}

{_lang['Whether you\'re seeking clarity, reassurance, or a deeper understanding of your health, our platform is built to support you—securely, intelligently, and compassionately.']}

{_lang['Join the movement toward smarter, more accessible healthcare. Your journey to peace of mind starts here.']}

:material/lock_open: {_lang['Upgrade to experience the future of digital health.']}

            """,
            unsafe_allow_html=True,
        )
        add_auth(
            required=False,  # Don't stop the app for non-subscribers
            show_redirect_button=True,
            subscription_button_text="Upgrade",
            # button_color="#4CAF50",  # Green button
            button_color="#cb785c",
            use_sidebar=False,  # Show button in main section
        )

        st.markdown(
            _lang["Warm regards, **The Corpus Analytica Team**"], unsafe_allow_html=True
        )

else:
    st.markdown(_lang["Please login first"])
    st.markdown("---")
    st.stop()
