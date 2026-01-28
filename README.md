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

## Testing Modules

### 1. Prompt Injection (15 vectors)
- Direct command injection
- Role hijacking
- Context escape
- Encoded injection (Base64)
- Multi-step injection
- Jailbreak via email
- Tool chaining attacks
- Memory poisoning
- And more...

### 2. Supply Chain (5 vectors)
- Malicious skill installation
- Dependency confusion
- Extension verification bypass
- Remote code loading
- Permission escalation

### 3. Data Exfiltration (8 vectors)
- Browser credentials (Evelyn Stealer technique)
- SSH key theft
- Environment variables
- Screenshot capture
- Clipboard monitoring
- Cryptocurrency wallets
- Session token theft
- Email exfiltration

## Legal & Ethical Guidelines

1. **Authorization Required**: Only test systems you own or have written permission to test
2. **No Harm**: Do not cause damage or disruption
3. **Responsible Disclosure**: Report findings to vendors responsibly
4. **Compliance**: Follow all applicable laws and regulations

## References

- [Trend Micro - Evelyn Stealer Analysis](https://www.trendmicro.com/en_us/research/26/a/analysis-of-the-evelyn-stealer-campaign.html)
- [Koi.ai - VS Code Malware](https://www.koi.ai/blog/the-vs-code-malware-that-captures-your-screen)
- [Snyk - ClawdBot Security Analysis](https://snyk.io/articles/clawdbot-ai-assistant/)
- OWASP LLM Top 10

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

## License

MIT License - See [LICENSE](LICENSE)

---

**⚠️ For Authorized Security Research Only ⚠️**
