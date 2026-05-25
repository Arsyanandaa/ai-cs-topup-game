# ai-cs-topup-game
# AI Customer Service - Top Up Game

![CI/CD Pipeline](https://github.com/Arsyanandaa/ai-cs-topup-game/actions/workflows/ci-cd.yml/badge.svg)

AI Customer Service chatbot untuk layanan top up game, dilengkapi CI/CD pipeline penuh.

## Tech Stack
- Python + FastAPI
- Docker
- GitHub Actions (CI/CD)

## Pipeline Stages
| Stage | Deskripsi |
|-------|-----------|
| Automated Testing | Unit test + linting (flake8) otomatis |
| Security Gate | Scan kerentanan kode dengan Bandit |
| Deploy Staging | Deploy otomatis setelah security pass |
| Deploy UAT | Deploy dengan manual approval |
| Deploy Production | Deploy final ke production |

## Git Flow Strategy
- `main` — production-ready code, direct push diblokir
- `develop` — integrasi semua fitur
- `feature/xxx` — pengembangan fitur baru
- `hotfix/xxx` — fix bug darurat

## Cara Jalankan Lokal
pip install -r requirements.txt
uvicorn app.main:app --reload