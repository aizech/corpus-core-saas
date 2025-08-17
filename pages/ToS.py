"""
Terms of Service Page
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
    page_title=f"{config.APP_NAME} - Terms of Service",
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
        # Terms of Service  
        
        """, unsafe_allow_html=True)

height = 50
st.markdown(f'<div style="height: {height}px;"></div>', unsafe_allow_html=True)

# --- Content ---
st.markdown("""

The GodsinWhite Agent Interface is a web-based platform that provides users with access to artificial intelligence (AI) tools and resources. By using the GodsinWhite Agent Interface, you agree to be bound by these Terms of Service. If you do not agree with these Terms, you must discontinue use of the GodsinWhite Agent Interface immediately.

1. **Agreement to Terms**
These Terms of Service constitute a legally binding agreement made between you, whether personally or on behalf of an entity ("you"), and GodsinWhite ("Company," "we," "us," or "our"), concerning your access to and use of the GodsinWhite Agent Interface website as well as any other media form, media channel, mobile website, or mobile application related, linked, or otherwise connected thereto (collectively, the "Site"). You agree that by accessing the Site, you have read, understood, and agreed to be bound by all of these Terms of Service.

2. **Intellectual Property Rights**
The GodsinWhite Agent Interface is protected by copyright, trademark, and other laws of Germany and foreign countries. Except as expressly provided in these Terms of Service, GodsinWhite and its licensors exclusively own all right, title and interest in and to the GodsinWhite Agent Interface, including all associated intellectual property rights. You will not remove, alter or obscure any copyright, trademark, service mark or other proprietary rights notices incorporated in or accompanying the GodsinWhite Agent Interface.

3. **User Content**
You are solely responsible for all code, video, images, information, data, text, software, music, sound, photographs, graphics, messages or other materials ("Content") that you upload, post, publish or display (hereinafter, "upload") or otherwise provide or transmit to or through the GodsinWhite Agent Interface. You agree not to upload any Content that is confidential or proprietary to a third party without that third party's express written permission.

4. **Prohibited Conduct**
You agree not to use the GodsinWhite Agent Interface to:

- upload, post or transmit any Content that: (i) infringes any patent, trademark, trade secret, copyright or other proprietary rights of any party; (ii) is illegal, harmful, threatening, abusive, harassing, tortious, defamatory, vulgar, obscene, libelous, invasive of another's privacy, hateful, or racially, ethnically or otherwise objectionable; (iii) you do not have a right to upload under any law or under contractual or fiduciary relationships; or (iv) contains software viruses or any other computer code, files or programs designed to interrupt, destroy or limit the functionality of any computer software or hardware or telecommunications equipment;
- stalk, harass, bully or harm another individual;
- impersonate any person or entity, or falsely state or otherwise misrepresent your affiliation with a person or entity;
- forge headers or otherwise manipulate identifiers in order to disguise the origin of any Content transmitted through the GodsinWhite Agent Interface;
- create a false identity or impersonate another person or entity;
- upload, post or transmit any Content that contains any viruses, Trojan horses, worms, time bombs, cancelbots or other computer programming routines that are intended to damage, detrimentally interfere with, surreptitiously intercept or expropriate any system, data or personal information;
- upload, post or transmit any Content that is spam or junk mail;
- upload, post or transmit any Content that contains any unsolicited or unauthorized advertising, promotional materials, "junk mail," "spam," "chain letters," "pyramid schemes," or any other form of solicitation; or
- interfere with or disrupt the GodsinWhite Agent Interface or servers or networks connected to the GodsinWhite Agent Interface, or disobey any requirements, procedures, policies or regulations of networks connected to the GodsinWhite Agent Interface.

5. **Links**
The GodsinWhite Agent Interface may contain links to other websites ("Linked Sites"). The Linked Sites are not under the control of GodsinWhite and GodsinWhite is not responsible for the contents of any Linked Site, including without limitation any link contained in a Linked Site, or any changes or updates to a Linked Site. GodsinWhite is providing these links to you only as a convenience, and the inclusion of any link does not imply endorsement by GodsinWhite of the site or any association with its operators.

6. **Disclaimers**
THE GODSINWHITE AGENT INTERFACE IS PROVIDED "AS IS" AND ON AN "AS AVAILABLE" BASIS WITHOUT WARRANTIES OF ANY KIND EITHER EXPRESS OR IMPLIED. TO THE FULLEST EXTENT PERMISSIBLE PURSUANT TO APPLICABLE LAW, GODSINWHITE DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. GODSINWHITE DOES NOT WARRANT THAT THE GODSINWHITE AGENT INTERFACE WILL BE UNINTERRUPTED OR ERROR-FREE, NOR DOES GODSINWHITE MAKE ANY WARRANTY AS TO THE RESULTS THAT MAY BE OBTAINED FROM USE OF THE GODSINWHITE AGENT INTERFACE OR AS TO THE ACCURACY, RELIABILITY OR CONTENT OF ANY INFORMATION, SERVICE, OR MERCHANDISE PROVIDED THROUGH THE GODSINWHITE AGENT INTERFACE.

7. **Limitation of Liability**
IN NO EVENT WILL GODSINWHITE BE LIABLE TO YOU OR ANY OTHER PARTY FOR ANY DAMAGES, INCLUDING BUT NOT LIMITED TO DIRECT, INDIRECT, SPECIAL, INCIDENTAL, CONSEQUENTIAL OR PUNITIVE DAMAGES (INCLUDING, BUT NOT LIMITED TO, DAMAGES FOR LOSS OF BUSINESS PROFITS, BUSINESS INTERRUPTION, LOSS OF BUSINESS INFORMATION, OR OTHER PECUNIARY LOSS) ARISING OUT OF THE USE OF OR INABILITY TO USE THE GODSINWHITE AGENT INTERFACE, EVEN IF GODSINWHITE HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. BECAUSE SOME JURISDICTIONS DO NOT ALLOW THE EXCLUSION OR LIMITATION OF LIABILITY FOR CONSEQUENTIAL OR INCIDENTAL DAMAGES, THE ABOVE LIMITATION MAY NOT APPLY TO YOU.

8. **Indemnification**
You agree to defend, indemnify and hold harmless GodsinWhite, its officers, directors, employees and agents from and against any and all claims, damages, obligations, losses, liabilities, costs or debt, and expenses (including but not limited to attorney's fees) arising from: (i) your use of and access to the GodsinWhite Agent Interface; (ii) your violation of any term of these Terms of Service; (iii) your violation of any third party right, including without limitation any copyright, property, or privacy right; or (iv) any claim that your Content caused damage to a third party. This defense and indemnification obligation will survive these Terms of Service and your use of the GodsinWhite Agent Interface.

9. **Governing Law**
These Terms of Service and any action related thereto will be governed by the laws of Germany without regard to its conflict of law provisions. The exclusive jurisdiction and venue of any action with respect to the subject matter of these Terms of Service will be the courts of Germany, and each of the parties hereto waives any objection to jurisdiction and venue in such courts.

10. **Entire Agreement**
These Terms of Service constitute the entire agreement between you and GodsinWhite regarding the use of the GodsinWhite Agent Interface, superseding any prior agreements between you and GodsinWhite relating to the GodsinWhite Agent Interface.

11. **Severability**
If any provision of these Terms of Service is held to be invalid or unenforceable, such provision will be stricken and the remaining provisions will be enforced to the fullest extent under law.

12. **No Waiver**
The failure of GodsinWhite to exercise or enforce any right or provision of these Terms of Service will not operate as a waiver of such right or provision. The section titles in these Terms of Service are for convenience only and have no legal or contractual effect.

""")

height = 50
st.markdown(f'<div style="height: {height}px;"></div>', unsafe_allow_html=True)

