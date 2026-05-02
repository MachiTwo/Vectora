#!/bin/bash
# Export GitHub Secrets to environment variables for CI/CD
# This script converts GitHub secrets into env vars for build/test steps

# Create temporary .env file for the workflow
ENV_FILE=".env.ci"

# Export all known secrets as env vars
# (GitHub automatically injects ${{ secrets.NAME }} but we make them explicit)

cat > "$ENV_FILE" << 'EOF'
# APIs
GOOGLE_API_KEY=${{ secrets.GOOGLE_API_KEY }}
VOYAGE_API_KEY=${{ secrets.VOYAGE_API_KEY }}
GEMINI_API_KEY=${{ secrets.GEMINI_API_KEY }}

# Database
MONGODB_URI=${{ secrets.MONGODB_URI }}

# Auth
JWT_SECRET=${{ secrets.JWT_SECRET }}
GITHUB_TOKEN=${{ secrets.GITHUB_TOKEN }}

# Cloud Services
SUPABASE_URL=${{ secrets.SUPABASE_URL }}
SUPABASE_ANON_KEY=${{ secrets.SUPABASE_ANON_KEY }}
SUPABASE_SERVICE_KEY=${{ secrets.SUPABASE_SERVICE_KEY }}

# Email
RESEND_API_KEY=${{ secrets.RESEND_API_KEY }}

# CDN
CLOUDFLARE_API_TOKEN=${{ secrets.CLOUDFLARE_API_TOKEN }}

# Deployment
FLY_API_TOKEN=${{ secrets.FLY_API_TOKEN }}
EOF

echo "Created $ENV_FILE with secrets template"

# In workflow, use:
# - name: Load secrets
#   run: |
#     source scripts/export_secrets_to_env.sh
#     # Now all secrets are available as env vars
