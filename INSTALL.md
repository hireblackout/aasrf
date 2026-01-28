# Installation Guide

## System Requirements

- Python 3.10 or higher
- Docker (optional, for sandbox tests)
- 4GB RAM minimum
- Linux/macOS/Windows (WSL2)

## Step 1: Clone Repository

```bash
git clone https://github.com/hireblackout/aasrf.git
cd aasrf
```

## Step 2: Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Configuration

```bash
cp config.example.yaml config.yaml
# Edit config.yaml with your target settings
```

## Step 5: Verify Installation

```bash
python aasrf.py --version
python aasrf.py --check-deps
```

## Optional: Docker Setup

```bash
docker build -t aasrf:latest .
docker run -it aasrf:latest --help
```

## Troubleshooting

### Issue: ModuleNotFoundError

```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Issue: Permission Denied

```bash
chmod +x aasrf.py
```

### Issue: SSL Certificate Errors

Edit config.yaml and set `verify_ssl: false` (not recommended for production)
