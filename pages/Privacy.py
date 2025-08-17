"""
Privacy Policy Page
This page provides information about the GodsinWhite Agent Interface.
"""

import os
import streamlit as st
import sys
import datetime

# Add the parent directory to the path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import config

# Set page config
st.set_page_config(
    page_title=f"{config.APP_NAME} - Privacy Policy",
    page_icon=config.LOGO_ICON_PATH,
    layout="wide",
)

# Logo in sidebar
st.logo(config.LOGO_TEXT_PATH,
    size="large",
    icon_image=config.LOGO_ICON_PATH
)

# Page title
one_cola = st.columns([1])[0]
with one_cola:
    col1a, col2a = st.columns([2, 6])

    with col1a:
        team_image = config.LOGO_TEAM_PATH
        st.image(team_image, width=400)
    with col2a:
        st.markdown("""
        # Privacy Policy  
        
        """, unsafe_allow_html=True)

height = 50
st.markdown(f'<div style="height: {height}px;"></div>', unsafe_allow_html=True)

# --- Content ---
st.markdown("""

We are committed to protecting your privacy. Authorized employees within the company on a need to know basis only use any information collected from individual customers. We constantly review our systems and data to ensure the best possible service to our customers.

We will not sell, share, or rent your personal information to any third party or use your e-mail address for unsolicited mail. Any emails sent by this Company will only be in connection with the provision of agreed services and products.

We use IP addresses to analyse trends, administer the site, track user s movement, and gather broad demographic information for aggregate use. IP addresses are not linked to personally identifiable information.

This website contains links to other sites. Please be aware that we are not responsible for the privacy practices of such other sites. We encourage our users to be aware when they leave our site and to read the privacy statements of each and every web site that collects personally identifiable information. This privacy statement applies solely to information collected by this Web site.

We do not store credit card details nor do we share customer details with any 3rd parties.

### Information Collection and Use

We are the sole owner of the information collected on this site. We will not sell, share, or rent this information to others in ways different from what is disclosed in this statement. We collect information from our users at several different points on our website.

### Order

We request information from the user on our order form. Here a user must provide contact information (like name and shipping address) and financial information (like credit card number, expiration date). This information is used for billing purposes and to fill customer s orders. If we have trouble processing an order, this contact information is used to get in touch with the user.

### Cookies

A cookie is a piece of data stored on the user s hard drive containing information about the user. Usage of a cookie is in no way linked to any personally identifiable information while on our site. Once the user closes their browser, the cookie simply terminates. For instance, by setting a cookie on our site, the user would not have to log in a password more than once, thereby saving time while on our site. If a user rejects the cookie, they may still use our site. The only drawback to this is that the user will be limited in some areas of our site. For example, the user will not be able to participate in any of our sweepstakes, contests or monthly drawings that may take place. Cookies can also enable us to track and target the interests of our users to enhance the experience on our site.

### Log Files

We use IP addresses to analyse trends, administer the site, track user s movement, and gather broad demographic information for aggregate use. IP addresses are not linked to personally identifiable information.

### Sharing

We will share aggregated demographic information with our partners and advertisers. This is not linked to any personal information that can identify any individual person.

We use an outside shipping company to ship orders, and a credit card processing company to bill users for goods and services. These companies do not retain, share, store or use personally identifiable information for any secondary purposes.

We partner with another party to provide specific services. When the user signs up for these services, we will share names, or other contact information that is necessary for the third party to provide these services. These parties are not allowed to use personally identifiable information except for the purpose of providing these services.

### Links

This web site contains links to other sites. Please be aware that we are not responsible for the privacy practices of such other sites. We encourage our users to be aware when they leave our site and to read the privacy statements of each and every web site that collects personally identifiable information. This privacy statement applies solely to information collected by this Web site.

### Security

This website takes every precaution to protect our users information. When users submit sensitive information via the website, your information is protected both online and off-line. When our registration/order form asks users to enter sensitive information (such as credit card number and/or social security number), that information is encrypted and is protected with the best encryption software in the industry - SSL. While on a secure page, such as our order form, the lock icon on the bottom of Web browsers such as Netscape Navigator and Microsoft Internet Explorer becomes locked, as opposed to un-locked, or open, when you are just surfing.

If you have any questions about the security at our website, you can send an email to [info@watunga.com](mailto:info@watunga.com).

### Notification of Changes

If we decide to change our privacy policy, we will post those changes on this page so our users are always aware of what information we collect, how we use it, and under what circumstances, if any, we disclose it. If at any point we decide to use personally identifiable information in a manner different from that stated at the time it was collected, we will notify users by way of an email. Users will have a choice as to whether or not we use their information in this different manner. We will use information in accordance with the privacy policy under which the information was collected.

### Contact

If you have any questions about this privacy policy, the practices of this site, or your dealings with this site, you can contact us at [info@watunga.com](mailto:info@watunga.com).

""")

height = 50
st.markdown(f'<div style="height: {height}px;"></div>', unsafe_allow_html=True)

