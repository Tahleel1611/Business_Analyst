# Deployment

Local: `docker compose up --build`. The compose file starts PostgreSQL, API, and Streamlit. The API and dashboard default to demo mode, so the database may be replaced with a real loader later.

For AWS, build and push `Dockerfile.api` and `Dockerfile.streamlit` to ECR, run them as ECS Fargate services behind an ALB, use RDS PostgreSQL privately, inject `DATABASE_URL` through Secrets Manager, and configure GitHub Actions OIDC. No AWS account credentials or infrastructure are present in this workspace, so cloud deployment is not claimed complete.
