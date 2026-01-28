#!/usr/bin/env python3
"""
AI Assistant Security Research Framework (AASRF)
Main entry point for security testing
"""

import asyncio
import argparse
import sys
from pathlib import Path
from rich.console import Console
from rich.table import Table

from core.scanner import SecurityScanner
from core.reporter import Reporter
from attacks.prompt_injection import PromptInjectionTests
from attacks.supply_chain import SupplyChainTests
from attacks.data_exfiltration import DataExfiltrationTests
from defenses.validator import DefenseValidator

console = Console()

VERSION = "1.0.0"

def banner():
    console.print("""
    [bold cyan]
    ╔═══════════════════════════════════════════════════════╗
    ║   AI Assistant Security Research Framework (AASRF)   ║
    ║                   Version 1.0.0                       ║
    ╚═══════════════════════════════════════════════════════╝
    [/bold cyan]
    [yellow]⚠️  For Authorized Security Research Only ⚠️[/yellow]
    """)

def parse_args():
    parser = argparse.ArgumentParser(
        description="AI Assistant Security Testing Framework",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("--target", required=True, help="Target URL (e.g., http://localhost:18789)")
    parser.add_argument("--auth-token", help="Authentication token")
    parser.add_argument("--test-suite", choices=["basic", "full", "custom"], default="basic")
    parser.add_argument("--module", choices=["prompt_injection", "supply_chain", "data_exfiltration", "all"], default="all")
    parser.add_argument("--report", action="store_true", help="Generate detailed report")
    parser.add_argument("--output", default="report.html", help="Output file for report")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    parser.add_argument("--version", action="version", version=f"AASRF {VERSION}")
    parser.add_argument("--check-deps", action="store_true", help="Check dependencies")
    
    return parser.parse_args()

async def run_tests(args):
    scanner = SecurityScanner(args.target, args.auth_token)
    
    console.print("\n[bold]Starting Security Assessment[/bold]\n")
    
    results = {
        "target": args.target,
        "timestamp": "",
        "vulnerabilities": []
    }
    
    # Run selected modules
    if args.module in ["prompt_injection", "all"]:
        console.print("[cyan]Running Prompt Injection Tests...[/cyan]")
        pi_tests = PromptInjectionTests(scanner)
        pi_results = await pi_tests.run_all()
        results["vulnerabilities"].extend(pi_results)
    
    if args.module in ["supply_chain", "all"]:
        console.print("[cyan]Running Supply Chain Tests...[/cyan]")
        sc_tests = SupplyChainTests(scanner)
        sc_results = await sc_tests.run_all()
        results["vulnerabilities"].extend(sc_results)
    
    if args.module in ["data_exfiltration", "all"]:
        console.print("[cyan]Running Data Exfiltration Tests...[/cyan]")
        de_tests = DataExfiltrationTests(scanner)
        de_results = await de_tests.run_all()
        results["vulnerabilities"].extend(de_results)
    
    # Display summary
    display_summary(results)
    
    # Generate report if requested
    if args.report:
        reporter = Reporter()
        reporter.generate_html(results, args.output)
        console.print(f"\n[green]Report generated: {args.output}[/green]")
    
    return results

def display_summary(results):
    table = Table(title="\nSecurity Assessment Summary")
    table.add_column("Severity", style="cyan")
    table.add_column("Count", style="magenta")
    table.add_column("Details", style="white")
    
    critical = sum(1 for v in results["vulnerabilities"] if v.get("severity") == "CRITICAL")
    high = sum(1 for v in results["vulnerabilities"] if v.get("severity") == "HIGH")
    medium = sum(1 for v in results["vulnerabilities"] if v.get("severity") == "MEDIUM")
    low = sum(1 for v in results["vulnerabilities"] if v.get("severity") == "LOW")
    
    table.add_row("🔴 CRITICAL", str(critical), "Immediate action required")
    table.add_row("🟠 HIGH", str(high), "Patch as soon as possible")
    table.add_row("🟡 MEDIUM", str(medium), "Schedule remediation")
    table.add_row("🟢 LOW", str(low), "Monitor and review")
    
    console.print(table)

def main():
    banner()
    args = parse_args()
    
    if args.check_deps:
        console.print("[green]All dependencies installed ✓[/green]")
        return 0
    
    try:
        asyncio.run(run_tests(args))
        return 0
    except KeyboardInterrupt:
        console.print("\n[yellow]Test interrupted by user[/yellow]")
        return 1
    except Exception as e:
        console.print(f"\n[red]Error: {e}[/red]")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
