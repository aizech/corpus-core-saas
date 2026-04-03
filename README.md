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

See it live in action here: https://corpus-core.streamlit.app/

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

### 📊 Feature Comparison

| Feature | Free Tier | Premium Tier | Enterprise |
|---------|-----------|--------------|------------|
| **Authentication** | Google/Microsoft/GitHub OAuth | ✅ All OAuth providers | ✅ Custom SSO |
| **User Management** | Up to 3 users | Unlimited users | Unlimited + SAML |
| **Core Features** | Basic functionality | All premium features | Custom features |
| **API Access** | Limited | Full API access | Priority API |
| **Support** | Community | Email support | Dedicated support |
| **Customization** | Basic themes | Full theming | White-label |
| **Storage** | 1GB | 100GB | Unlimited |
| **Analytics** | Basic metrics | Advanced analytics | Custom reports |

### 🔐 Authentication & Authorization
- **OAuth 2.0 Integration**: Auth0-powered secure authentication
- **Multiple Providers**: Google, Microsoft, GitHub login options
- **Session Management**: Secure token handling and automatic refresh
- **Role-Based Access**: Premium subscription validation and feature gating
- **Security Compliance**: Industry-standard OAuth implementation

### 🎨 User Experience
- **Responsive Design**: Optimized for desktop, tablet, and mobile devices
- **Theme Support**: Light and dark mode with smooth transitions
- **Internationalization**: English and German language support
- **Accessibility**: WCAG 2.1 compliant interface components
- **Progressive Enhancement**: Works without JavaScript, enhanced with it

### 💳 Subscription Management
- **Stripe Integration**: Secure payment processing with multiple currencies
- **Flexible Plans**: Free trial, premium monthly/annual subscriptions
- **Automatic Billing**: Recurring subscription management with dunning
- **Usage Tracking**: Monitor API usage, storage, and active users
- **Upgrade/Downgrade**: Seamless plan changes with prorated billing

### 🔒 Security & Compliance
- **Data Encryption**: AES-256 encryption at rest and TLS 1.3 in transit
- **Secure Authentication**: OAuth 2.0 with PKCE and state validation
- **Audit Logging**: Comprehensive activity tracking and security events
- **Privacy Controls**: GDPR-compliant data management and user rights
- **Regular Security Updates**: Automated dependency scanning and updates

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

### 📸 Deployment Screenshots

#### Login & Authentication
```
┌─────────────────────────────────────┐
│  🏥 Corpus Core - SaaS              │
│  ┌─────────────────────────────────┐ │
│  │   Sign in with Google          │ │
│  │   Sign in with Microsoft       │ │
│  │   Sign in with GitHub          │ │
│  └─────────────────────────────────┘ │
│                                     │
│  New to Corpus Core? Start Trial → │
└─────────────────────────────────────┘
```

#### Premium Dashboard
```
┌─────────────────────────────────────┐
│  📊 Dashboard                      │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐   │
│  │Users│ │Usage│ │Revenue│ │Support│ │
│  │ 156 │ │892GB│ │$4,291│ │  12   │ │
│  └─────┘ └─────┘ └─────┘ └─────┘   │
│                                     │
│  📈 Usage Analytics                 │
│  ██████████░░░░ 89% of 1TB          │
└─────────────────────────────────────┘
```

#### Account Management
```
┌─────────────────────────────────────┐
│  👤 Account Settings                │
│                                     │
│  📧 Email: user@example.com         │
│  💳 Plan: Premium ($29/mo)          │
│  📅 Member since: Jan 15, 2024      │
│                                     │
│  ┌─────────────────────────────────┐ │
│  │   Upgrade to Enterprise         │ │
│  │   Download Invoice (PDF)        │ │
│  │   Cancel Subscription            │ │
│  └─────────────────────────────────┘ │
└─────────────────────────────────────┘
```

### Local Development

```bash
# Start development server
streamlit run app.py

# Access at http://localhost:8501
# Uses .streamlit/secrets-example.toml by default
```

### Production Deployment

#### Option 1: Streamlit Cloud (Recommended)
1. **Connect Repository**
   - Link GitHub repository to Streamlit Cloud
   - Configure build command: `streamlit run app.py`

2. **Environment Setup**
   ```toml
   # In Streamlit Cloud secrets
   [auth0]
   domain = "your-auth0-domain"
   client_id = "your-client-id"
   client_secret = "your-client-secret"
   
   stripe_api_key = "sk_live_..."
   testing_mode = false
   ```

3. **Deploy**
   - Automatic deployment on git push
   - Custom domain: `https://your-app.streamlit.app`
   - SSL certificate included

#### Option 2: Docker Deployment

```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8501

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
```

```yaml
# docker-compose.yml
version: '3.8'

services:
  corpus-core:
    build: .
    ports:
      - "8501:8501"
    environment:
      - AUTH0_DOMAIN=${AUTH0_DOMAIN}
      - AUTH0_CLIENT_ID=${AUTH0_CLIENT_ID}
      - AUTH0_CLIENT_SECRET=${AUTH0_CLIENT_SECRET}
      - STRIPE_API_KEY=${STRIPE_API_KEY}
    volumes:
      - ./data:/app/data
    restart: unless-stopped
    networks:
      - corpus-network

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - corpus-core
    restart: unless-stopped
    networks:
      - corpus-network

networks:
  corpus-network:
    driver: bridge
```

#### Option 3: Cloud Platform Deployment

##### AWS ECS Deployment
```bash
# Build and push to ECR
aws ecr create-repository --repository-name corpus-core-saas
docker build -t corpus-core-saas .
docker tag corpus-core-saas:latest <account>.dkr.ecr.<region>.amazonaws.com/corpus-core-saas:latest
docker push <account>.dkr.ecr.<region>.amazonaws.com/corpus-core-saas:latest

# Deploy to ECS
aws ecs create-cluster --cluster-name corpus-core
aws ecs register-task-definition --cli-input-json file://task-definition.json
aws ecs create-service --cluster corpus-core --service-name corpus-core-service --task-definition corpus-core:1
```

##### Google Cloud Run
```bash
# Build and deploy
gcloud builds submit --tag gcr.io/PROJECT-ID/corpus-core-saas
gcloud run deploy corpus-core-saas --image gcr.io/PROJECT-ID/corpus-core-saas --platform managed

# Set environment variables
gcloud run services update corpus-core-saas --set-env-vars "AUTH0_DOMAIN=your-domain,STRIPE_API_KEY=your-key"
```

### Production Configuration

#### Nginx Reverse Proxy
```nginx
# nginx.conf
server {
    listen 80;
    server_name your-domain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name your-domain.com;

    ssl_certificate /etc/nginx/ssl/cert.pem;
    ssl_certificate_key /etc/nginx/ssl/key.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512;

    location / {
        proxy_pass http://corpus-core:8501;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # WebSocket support for Streamlit
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

#### Environment Variables
```bash
# Production .env
AUTH0_DOMAIN=your-auth0-domain.auth0.com
AUTH0_CLIENT_ID=your-client-id
AUTH0_CLIENT_SECRET=your-client-secret

STRIPE_API_KEY=sk_live_your_stripe_key
STRIPE_WEBHOOK_SECRET=whsec_your_webhook_secret

GENERAL_COMPANY_NAME=Your Company
GENERAL_SUPPORT_EMAIL=support@yourcompany.com

# Monitoring
SENTRY_DSN=https://your-sentry-dsn
LOG_LEVEL=INFO
```

### Monitoring & Maintenance

#### Health Checks
```bash
# Application health
curl -f http://localhost:8501/_stcore/health

# Database connectivity
curl -f http://localhost:8501/api/health/db

# External services
curl -f http://localhost:8501/api/health/auth0
curl -f http://localhost:8501/api/health/stripe
```

#### Backup Strategy
```bash
#!/bin/bash
# backup.sh
DATE=$(date +%Y%m%d_%H%M%S)

# Backup database
pg_dump corpus_core > "backup_db_${DATE}.sql"

# Backup user data
tar -czf "backup_data_${DATE}.tar.gz" data/

# Upload to cloud storage (AWS S3 example)
aws s3 cp "backup_db_${DATE}.sql" s3://your-backup-bucket/database/
aws s3 cp "backup_data_${DATE}.tar.gz" s3://your-backup-bucket/data/

# Cleanup old backups (keep 30 days)
find /backups -name "*.sql" -mtime +30 -delete
find /backups -name "*.tar.gz" -mtime +30 -delete
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
