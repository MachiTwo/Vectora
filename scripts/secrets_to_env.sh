#!/bin/bash
# Convert GitHub Secrets to .env file for CI/CD builds
# This creates a .env file so the code reads config the same way locally and in CI

# Determine target env file
ENV_FILE="${1:-.env.ci}"

# Create .env from GitHub Secrets
cat > "$ENV_FILE" << EOF
# Generated from GitHub Secrets - do not commit to git
# This file is created during CI/CD to match local development experience

# APIs
GOOGLE_API_KEY=${{ secrets.GOOGLE_API_KEY }}
VOYAGE_API_KEY=${{ secrets.VOYAGE_API_KEY }}
GEMINI_API_KEY=${{ secrets.GEMINI_API_KEY }}

# Database
MONGODB_URI=${{ secrets.MONGODB_URI }}

# Auth
JWT_SECRET=${{ secrets.JWT_SECRET }}

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

echo "Created $ENV_FILE from GitHub Secrets"

# Usage in workflow:
# - name: Create .env from secrets
#   run: bash scripts/secrets_to_env.sh .env
#
# Then godotenv.Load(".env") will find and load all secrets
