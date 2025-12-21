# Corpus Core - SaaS

<div align="center">
  <img src="assets/godsinwhite_team_light.png" alt="Corpus Core - SaaS" width="400"/>
  
  **A reusable Streamlit SaaS template**
  
  [![Streamlit](https://img.shields.io/badge/Streamlit-1.48.0-FF4B4B.svg)](https://streamlit.io)
  [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
  [![License](https://img.shields.io/badge/License-Proprietary-red.svg)](LICENSE)
</div>

## 🏥 Overview

Corpus Core - SaaS is a Streamlit-based SaaS template with secure authentication and Stripe-backed subscriptions. It includes example pages and feature gating patterns you can reuse across projects.

### Key Features

- **🔐 Secure Authentication**: OAuth integration with Google/Microsoft/GitHub login
- **💳 Premium Subscription**: Stripe-powered payment system with free trial
- **🌍 Multi-language Support**: English and German localization
- **🎨 Theme Support**: Light and dark mode themes
- **📱 Responsive Design**: Mobile-friendly interface

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Streamlit account for authentication
- Stripe account for payment processing (optional for development)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/aizech/corpus-core-saas.git
   cd corpus-core-saas
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .streamlit/secrets-example.toml .streamlit/secrets.toml
   cp .streamlit/config-example.toml .streamlit/config.toml
   ```

5. **Set up authentication and payment**
   - Configure Auth0 credentials in `.streamlit/secrets.toml`
   - Add Stripe API keys for payment processing
   - Update configuration settings as needed

6. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 📁 Project Structure

```
corpus-core-saas/
├── assets/                     # Static assets and images
│   ├── godsinwhite_logo_*.png  # Logo variants
│   └── godsinwhite_team_*.png  # Team images
├── locales/                    # Internationalization
│   ├── en.py                   # English translations
│   └── de.py                   # German translations
├── pages/                      # Application pages
│   ├── Home.py                 # Main dashboard
│   ├── Trial.py                # Trial page
│   ├── Premium.py              # Premium page
│   ├── Account.py              # User account management
│   ├── Pricing.py              # Subscription plans
│   ├── Help.py                 # Help and support
│   └── About.py                # About page
├── .streamlit/                 # Streamlit configuration
│   ├── config.toml             # App configuration
│   └── secrets.toml            # API keys and secrets
├── styles_*.css                # Theme stylesheets
├── config.py                   # Application configuration
├── app.py                    # Main application entry point
└── requirements.txt            # Python dependencies
```

## 🔧 Configuration

### Environment Variables

Configure the following in `.streamlit/secrets.toml`:

```toml
# Authentication
[auth0]
domain = "your-auth0-domain"
client_id = "your-client-id"
client_secret = "your-client-secret"

# Payment Processing
stripe_api_key = "your-stripe-live-key"
stripe_api_key_test = "your-stripe-test-key"
testing_mode = false

# Application Settings
[general]
company_name = "Corpus Core - SaaS"
support_email = "support@corpusanalytica.com"
```

### Application Settings

Modify `config.py` to customize:
- Company information
- Logo and asset paths
- Application URLs
- Agent configurations

## 🎯 Features

### Authentication & Authorization
- OAuth 2.0 integration with Auth0
- Support for Google, Microsoft and GitHub login
- Session management and user profiles
- Premium subscription validation

### User Experience
- **Responsive Design**: Works on desktop and mobile devices
- **Theme Support**: Light and dark mode options
- **Internationalization**: English and German language support
- **Accessibility**: WCAG compliant interface

## 💳 Subscription Management

The platform uses Stripe for subscription management. There you can define your own plans and prices.  
Here you can find the Stripe documentation: https://stripe.com/docs  
Examples: 

- **Free Trial**: 14-day trial with basic features
- **Premium Plan**: Full access to all premium features
- **Automatic Billing**: Recurring subscription management
- **Usage Tracking**: Monitor API usage and limits

## 🔒 Security & Compliance

- **Data Encryption**: All data encrypted in transit and at rest
- **Secure Authentication**: OAuth 2.0 with industry standards
- **Audit Logging**: Comprehensive activity tracking
- **Privacy Controls**: User data management and deletion

## 🌍 Internationalization

Currently supported languages:
- **English** (en)
- **German** (de)

To add a new language:
1. Create a new file in `locales/` (e.g., `fr.py`)
2. Add translations following the existing format
3. Update language selection in `login.py`

## 🎨 Theming

The application supports light and dark themes:
- `styles_light.css` - Light theme styles
- `styles_dark.css` - Dark theme styles
- `styles_common.css` - Common styles for both themes

Users can toggle themes using the theme switcher in the sidebar.

## 🚀 Deployment

### Local Development
```bash
streamlit run app.py
```

### Production Deployment
1. Set up production environment variables
2. Configure domain and SSL certificates
3. Deploy using your preferred hosting platform
4. Set up monitoring and logging

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

## 📊 Monitoring & Analytics

- **User Analytics**: Track user engagement and feature usage
- **Performance Monitoring**: Application performance metrics
- **Error Tracking**: Comprehensive error logging
- **Health Checks**: System status monitoring

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is proprietary software. All rights reserved.

## 📞 Support

- **Email**: support@corpusanalytica.com
- **Website**: https://www.corpusanalytica.com/
- **Support Portal**: https://www.corpusanalytica.com/support

---

<div align="center">
  <p><strong>Corpus Core - SaaS</strong></p>
  <p>A reusable SaaS template by Corpus Analytica</p>
</div>
