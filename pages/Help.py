import streamlit as st
from config import config

# Page title
one_cola = st.columns([1])[0]
with one_cola:
    col1a, col2a = st.columns([2, 6])

    with col1a:
        #team_image = config.LOGO_TEAM_PATH
        st.image(f"assets/godsinwhite_team_{st.session_state.theme}.png", width=400)
        #st.image(team_image, width=400)
    with col2a:
        st.markdown("""
        ## Gods in White - AI-Powered Medical Imaging & Expert Insights  
        *[A Corpus Analytica Innovation](https://www.corpusanalytica.com)*
        """, unsafe_allow_html=True)
    
st.markdown("""
Gods in White is your personal gateway to advanced medical diagnostics—powered by AI and backed by real medical expertise. Designed for patients, healthcare professionals, and curious minds alike, this app transforms how medical images are analyzed and understood.

### :material/settings_heart: Key Features
- Instant Image Analysis: Upload any medical image — X-rays, MRIs, CT scans or just take a picture with your phone — and receive fast, AI-driven insights with clinical-grade precision.

- Expert Review On Demand: Get second opinions from real certified medical specialists who review your images and provide personalized feedback. Here we recommend our partners who are certified medical specialists from [Radiologic Reviews](https://www.radiologic-reviews.com).

### :material/sell: Premium Access (for subscribed users)

- Unlimited Image Uploads: No limits, no delays. Analyze as many images as you need.

- Direct Chat with AI powered Doctors: Ask questions, share concerns, and receive expert guidance in real time.

### :material/potted_plant: Why It Matters
Whether you're seeking clarity, reassurance, or a second opinion, Gods in White empowers you to take control of your health journey—anytime, anywhere.

> *"We created Gods in White to democratize access to medical expertise. Everyone deserves clarity when it comes to their health."* — Bernhard Z., Founder of [Corpus Analytica](https://www.corpusanalytica.com)
""", unsafe_allow_html=True)