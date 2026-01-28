# Contributing to AASRF

Thank you for your interest in contributing to the AI Assistant Security Research Framework!

## Code of Conduct

- Use this tool ethically and legally
- Follow responsible disclosure practices
- Respect privacy and data protection laws
- No malicious use

## How to Contribute

### Reporting Vulnerabilities

If you find a security issue in AASRF itself:
1. **Do not** open a public issue
2. Email: security@[your-domain]
3. Include detailed reproduction steps
4. Allow 90 days for response

### Adding New Tests

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-test-module`
3. Add your test module to appropriate directory (`attacks/`, `defenses/`)
4. Follow existing code structure and naming conventions
5. Add documentation
6. Submit pull request

### Code Style

- Follow PEP 8 for Python code
- Use type hints where appropriate
- Add docstrings to all functions/classes
- Keep functions focused and modular

### Testing Your Contributions

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Check code style
flake8 .
black --check .
```

### Pull Request Process

1. Update README.md with details of changes
2. Update USAGE.md if adding new features
3. Ensure all tests pass
4. Request review from maintainers

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
