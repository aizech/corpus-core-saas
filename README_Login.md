# Setting Up Google OAuth Client for Streamlit Authentication

This guide provides step-by-step instructions to set up Google OAuth authentication for your Streamlit app, including troubleshooting for common errors.

## 1. Create a Google Cloud Project

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Click on the project dropdown at the top and select "New Project"
3. Enter a project name (e.g., "My Streamlit App") and click "Create"
4. Wait for the project to be created and select it from the dropdown

## 2. Configure the OAuth Consent Screen

1. In your Google Cloud project, navigate to "APIs & Services" > "OAuth consent screen"
2. Select "External" user type (unless you have a Google Workspace) and click "Create"
3. Fill in the required fields:
   - App name: Your app name (e.g., "My Subscription App")
   - User support email: Your email address
   - Developer contact information: Your email address
4. Click "Save and Continue"
5. On the "Scopes" page, click "Save and Continue" (no additional scopes needed)
6. On the "Test users" page, add your email address, then click "Save and Continue"
7. Review your settings and click "Back to Dashboard"

## 3. Create OAuth Client ID

1. Navigate to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "OAuth client ID"
3. Select "Web application" as the application type
4. Name your OAuth client (e.g., "Streamlit Client")
5. Add authorized redirect URIs - **this is critical and must be exact**:
   - For local development: `http://localhost:8501/oauth2callback`
   - For production: `https://[your-app-name].streamlit.app/oauth2callback`
6. Click "Create"
7. A popup will display your **Client ID** and **Client Secret** - save these securely

## 4. Configure Streamlit Secrets

1. Create or edit `.streamlit/secrets.toml` in your project root
2. Add the following configuration:

```toml
# Main auth section (required)
[auth]
cookie_secret = "your_random_string_here"

# Google-specific auth configuration
[auth.google]
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"

# Choose the appropriate redirect URI based on your environment
# For local development:
redirect_uri = "http://localhost:8501/oauth2callback"
# For deployed app (uncomment when deploying):
# redirect_uri = "https://your-app-name.streamlit.app/oauth2callback"
```

3. Replace placeholders with your actual values

## 5. Streamlit App Implementation

Here's a basic implementation for your login.py:

```python
import streamlit as st
from st_paywall import add_auth

st.title("My Subscription App")

if not st.user.is_logged_in:
    st.write("Please log in to access this app")
    st.write("You'll be redirected to Google for authentication")
    if st.button("Log in"):
        st.login()
else:
    add_auth(required=True)
    st.write("Welcome to the premium content!")
```

## 6. Run Your App

Run your Streamlit app with:

```
streamlit run login.py
```

## Common Errors and Troubleshooting

### Error: "The OAuth client was not found" (401: invalid_client)

**Cause**: Missing or incorrect OAuth configuration in secrets.toml

**Solution**:
- Ensure the `[auth.google]` section is not commented out (no # prefix)
- Verify client_id and client_secret are correct
- Check for typos in the configuration

### Error: "redirect_uri_mismatch" (400)

**Cause**: The redirect URI in your secrets.toml doesn't exactly match what's configured in Google Cloud Console

**Solution**:
1. Check your Google Cloud Console settings:
   - Go to "APIs & Services" > "Credentials"
   - Edit your OAuth client
   - Verify the authorized redirect URIs
2. Update your secrets.toml to use the exact same URI:
   - For local: `http://localhost:8501/oauth2callback`
   - For deployed: `https://your-app-name.streamlit.app/oauth2callback`

### Error: "Error: invalid_request" 

**Cause**: Misconfiguration in the auth section of secrets.toml

**Solution**:
- Ensure you have both `[auth]` and `[auth.google]` sections
- Verify the server_metadata_url is correct
- Check that cookie_secret is defined

# Setting Up Microsoft Authentication

This section provides step-by-step instructions for setting up Microsoft authentication for your Streamlit app.

## 1. Register an Application in Microsoft Azure

1. Sign in to the [Azure Portal](https://portal.azure.com/)
2. Navigate to **Azure Active Directory** > **App registrations** > **New registration**
3. Enter the following information:
   - **Name**: Your app name (e.g., "My Streamlit App")
   - **Supported account types**: Choose the appropriate option (typically "Accounts in any organizational directory and personal Microsoft accounts")
   - **Redirect URI**: Select "Web" and enter:
     - For local development: `http://localhost:8501/oauth2callback`
     - For production: `https://[your-app-name].streamlit.app/oauth2callback`
4. Click **Register**

## 2. Configure Authentication

1. In your newly registered app, go to **Authentication** in the left menu
2. Under **Implicit grant and hybrid flows**, check the boxes for:
   - **Access tokens**
   - **ID tokens**
3. Click **Save**

## 3. Create a Client Secret

1. Go to **Certificates & secrets** in the left menu
2. Under **Client secrets**, click **New client secret**
3. Add a description and select an expiration period
4. Click **Add**
5. **IMPORTANT**: Copy the **Value** of the secret immediately (you won't be able to see it again)

## 4. Get Your Application (Client) ID

1. Go to **Overview** in the left menu
2. Copy the **Application (client) ID** value

## 5. Configure Streamlit Secrets for Microsoft

Add the Microsoft configuration to your `.streamlit/secrets.toml` file:

```toml
# Existing auth section
[auth]
cookie_secret = "your_random_string_here"

# Microsoft auth configuration
[auth.microsoft]
client_id = "YOUR_MICROSOFT_CLIENT_ID"
client_secret = "YOUR_MICROSOFT_CLIENT_SECRET"
server_metadata_url = "https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration"

# Choose the appropriate redirect URI based on your environment
# For local development:
redirect_uri = "http://localhost:8501/oauth2callback"
# For deployed app (uncomment when deploying):
# redirect_uri = "https://your-app-name.streamlit.app/oauth2callback"
```

## 6. Update Your Streamlit App for Multiple Providers

To support both Google and Microsoft authentication:

```python
import streamlit as st
from st_paywall import add_auth

st.title("My Subscription App")

if not st.user.is_logged_in:
    st.write("Please log in to access this app")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Login with Google"):
            st.login(provider="google")
    with col2:
        if st.button("Login with Microsoft"):
            st.login(provider="microsoft")
else:
    add_auth(required=True)
    st.write(f"Welcome to the premium content, {st.user.email}!")
```

## Common Microsoft Authentication Errors

### Error: "AADSTS700054: The response_type 'token' is not enabled for the application"

**Solution**: Make sure you've enabled "Access tokens" in the Authentication settings

### Error: "AADSTS90072: The redirect URI is not registered for the client application"

**Solution**: Double-check that your redirect URI in secrets.toml exactly matches what's registered in Azure

### Error: "The application was not found in the directory"

**Solution**: Verify your client_id is correct and that the application is registered in the correct directory

## Important Notes

- **Security**: Keep your client secret secure and never commit it to public repositories
- **Deployment**: When deploying, update the redirect URI to match your deployed app URL
- **Testing Mode**: The OAuth consent screen is in "Testing" mode by default, limiting to test users
- **Publishing**: If you plan to publish your app publicly, you'll need to submit it for verification
- **Multiple Environments**: For apps that run in both local and production environments, consider using environment variables or conditional logic to select the appropriate redirect URI
