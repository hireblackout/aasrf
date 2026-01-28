# AI Assistant Security Research Framework (AASRF)

**Ethical Security Research Tool for Testing AI Assistant Vulnerabilities**

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)

## ⚠️ DISCLAIMER

This tool is for **authorized security research and testing only**. Use only on systems you own or have explicit permission to test. Unauthorized access to computer systems is illegal.

## Overview

A comprehensive security testing framework for AI assistants (ClawdBot, Moltbot, etc.) that demonstrates:

- Prompt injection vulnerabilities
- Supply chain attack vectors
- Command execution risks
- Data exfiltration simulation
- Multi-agent coordination exploits

## Features

- 🔴 **Prompt Injection Tests**: 15+ attack vectors
- 🟠 **Supply Chain Analysis**: Skill/extension vetting
- 🟡 **Sandbox Escape Tests**: Container breakout simulation
- 🟢 **Defense Validation**: Security control testing
- 🔵 **Reporting**: Detailed vulnerability reports

## Architecture

```
aasrf/
├── core/                 # Core testing engine
├── attacks/              # Attack modules
│   ├── prompt_injection/
│   ├── supply_chain/
│   └── data_exfiltration/
├── defenses/            # Defense validation
├── reports/             # Generated reports
└── configs/             # Test configurations
```

## Quick Start

```bash
# Clone repository
git clone https://github.com/hireblackout/aasrf.git
cd aasrf

# Install dependencies
pip install -r requirements.txt

# Run basic tests
python aasrf.py --target http://localhost:18789 --test-suite basic

# Run full assessment
python aasrf.py --target http://localhost:18789 --test-suite full --report
```

## Installation

See [INSTALL.md](INSTALL.md) for detailed setup instructions.

## Usage Examples

See [USAGE.md](USAGE.md) for comprehensive examples.

## Legal & Ethical Guidelines

1. **Authorization Required**: Only test systems you own or have written permission to test
2. **No Harm**: Do not cause damage or disruption
3. **Responsible Disclosure**: Report findings to vendors responsibly
4. **Compliance**: Follow all applicable laws and regulations

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

## License

MIT License - See [LICENSE](LICENSE)

## References

- Snyk ClawdBot Security Analysis
- Trend Micro Evelyn Stealer Research
- OWASP LLM Top 10
