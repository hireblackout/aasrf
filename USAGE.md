# Usage Guide

## Basic Commands

### Run Basic Tests
```bash
python aasrf.py --target http://localhost:18789 --test-suite basic
```

### Run Prompt Injection Tests
```bash
python aasrf.py --target http://localhost:18789 --module prompt_injection
```

### Run Supply Chain Tests
```bash
python aasrf.py --target http://localhost:18789 --module supply_chain
```

### Generate Report
```bash
python aasrf.py --target http://localhost:18789 --test-suite full --report --output report.html
```

## Advanced Usage

### Custom Attack Payloads
```bash
python aasrf.py --target http://localhost:18789 --payload-file custom_payloads.json
```

### Specific Vulnerability Testing
```bash
python aasrf.py --target http://localhost:18789 --cve CVE-2025-XXXX
```

### Defense Validation
```bash
python aasrf.py --target http://localhost:18789 --validate-defenses
```

## Configuration

Edit `config.yaml`:

```yaml
target:
  url: http://localhost:18789
  auth_token: "your_token_here"
  
testing:
  aggressive: false
  delay_between_tests: 2
  timeout: 30
  
reporting:
  format: html
  verbose: true
```

## Examples

See `examples/` directory for complete scenarios.
