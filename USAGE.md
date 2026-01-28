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

### Example 1: Quick Security Scan

```bash
python aasrf.py \\
  --target http://localhost:18789 \\
  --test-suite basic \\
  --report
```

### Example 2: Comprehensive Assessment

```bash
python aasrf.py \\
  --target http://localhost:18789 \\
  --test-suite full \\
  --report \\
  --output detailed_report.html \\
  --verbose
```

### Example 3: Single Module Test

```bash
python aasrf.py \\
  --target http://localhost:18789 \\
  --module data_exfiltration \\
  --report
```

## Command Reference

| Option | Description |
|--------|-------------|
| `--target` | Target URL (required) |
| `--auth-token` | Authentication token |
| `--test-suite` | Test suite: basic, full, custom |
| `--module` | Specific module to run |
| `--report` | Generate HTML report |
| `--output` | Output filename |
| `--verbose` | Verbose output |
| `--version` | Show version |

## Output

Reports are generated in the `reports/` directory with:
- Executive summary
- Vulnerability details
- Evidence snippets
- Severity ratings
- Remediation guidance
