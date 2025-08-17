import streamlit as st
from config import config

# Set page config
icon_image = f"{config.LOGO_ICON_PATH}{st.session_state.theme}.png"
st.set_page_config(
    page_title="GodsinWhite Home", 
    page_icon=icon_image,
    #layout="wide",
    #initial_sidebar_state="collapsed"
)

if st.user.is_logged_in:
    one_cola = st.columns([1])[0]
    with one_cola:
        col1a, col2a = st.columns([2, 6])

        with col1a:
            #team_image = config.LOGO_TEAM_PATH
            st.image(f"assets/godsinwhite_team_{st.session_state.theme}.png", width=400)
            #st.image(team_image, width=400)
        with col2a:
            st.markdown("""
            # Welcome to GodsinWhite  
            GodsinWhite is a platform for creating, assembling and reusing AI-Agents and Tools for medical purposes.
            """, unsafe_allow_html=True)

        st.markdown(f"Nice to see you, {st.user.name}")
        #st.image(st.user.picture)
        #st.markdown(" ")
        #st.markdown("You are logged in")
        
else:
    #st.markdown("Please login first")
    st.markdown(" ")
