# Scripts Directory

This directory contains automation scripts for testing and validating the Aqua JS CLI project.

## 🚀 Comprehensive Test Runner

The comprehensive test runner executes all steps from the main README.md, runs the complete test suite, and generates detailed reports with organized outputs.

### Files

- **`run_comprehensive_tests.py`** - Main Python script that orchestrates all testing
- **`run_tests.sh`** - Shell script wrapper for easy execution
- **`requirements.txt`** - Python dependencies (all standard library)

### Quick Start

```bash
# Run from project root - easiest method
./scripts/run_tests.sh

# Or run Python script directly
python3 scripts/run_comprehensive_tests.py

# Or run from scripts directory
cd scripts
python3 run_comprehensive_tests.py ..
```

### What It Does

#### 🔧 Environment Setup
- Runs `npm install`
- Runs `npm run build` 
- Verifies dist directory creation
- Logs all setup steps

#### 📖 README Examples
- Executes all example commands from the main README.md
- Tests basic notarization
- Tests signing with CLI
- Tests witnessing with ETH
- Tests content and scalar revisions
- Tests form operations (if form files exist)
- Runs verification commands on generated files
- Captures all outputs and errors

#### 🧪 Test Suite
- Runs `make test` for complete test execution
- Runs individual test files for detailed reporting:
  - `test-content-revision.sh`
  - `test-file-revisions.sh` 
  - `test-forms.sh`
  - `test-linking.sh`
  - `test-signing.sh`
  - `test-verify.sh`
  - `test-witness.sh`
- Captures all test outputs and results

#### 📊 Output Organization

All outputs are organized in timestamped directories under `output/`:

```
output/
└── run_YYYYMMDD_HHMMSS/
    ├── logs/
    │   └── comprehensive_test.log    # Complete execution log
    ├── outputs/
    │   ├── setup_*_stdout.txt        # Setup command outputs
    │   ├── readme_*_stdout.txt       # README example outputs
    │   └── verify_*_stdout.txt       # Verification outputs
    ├── test_results/
    │   ├── make_test_stdout.txt      # Complete test suite output
    │   ├── test-*_stdout.txt         # Individual test outputs
    │   └── sharness_results/         # Copied sharness test results
    ├── aqua_files/
    │   └── *.aqua.json              # Generated aqua files
    └── reports/
        ├── comprehensive_report.json # Complete results in JSON
        ├── comprehensive_report.md   # Detailed markdown report
        └── summary.txt               # Concise summary
```

### 📋 Reports Generated

#### 1. Summary Report (`summary.txt`)
- Overall success rate
- Breakdown by test category
- List of failed tests
- Quick overview for CI/CD

#### 2. Comprehensive Report (`comprehensive_report.md`)
- Detailed results for each test
- Command outputs and errors
- Timestamps and execution details
- Formatted for easy reading

#### 3. JSON Report (`comprehensive_report.json`)
- Machine-readable complete results
- Suitable for automated processing
- Contains all test data and metadata

### 🔧 Configuration

The test runner is designed to work out-of-the-box with the Aqua JS CLI project structure:

- **Workspace Detection**: Automatically detects project root
- **File Discovery**: Finds test files and example files automatically
- **Dependency Checking**: Verifies Node.js, npm, and Python availability
- **Error Handling**: Graceful failure handling with detailed logging

### 📝 Logging

The script provides comprehensive logging at multiple levels:

- **Console Output**: Progress indicators and summary information
- **File Logging**: Complete debug information in `logs/comprehensive_test.log`
- **Structured Output**: Individual output files for each command
- **Error Capture**: Separate stderr capture for debugging

### 🎯 Use Cases

#### Development Workflow
```bash
# Run after making changes to verify everything still works
./scripts/run_tests.sh
```

#### CI/CD Integration
```bash
# Run in CI pipeline
python3 scripts/run_comprehensive_tests.py
exit_code=$?

# Check summary for quick results
cat output/run_*/reports/summary.txt

# Exit with appropriate code
exit $exit_code
```

#### Debugging Issues
```bash
# Run tests and examine detailed outputs
./scripts/run_tests.sh

# Check specific test outputs
cat output/run_*/outputs/readme_*_stderr.txt
cat output/run_*/test_results/test-*_stderr.txt

# Review comprehensive log
cat output/run_*/logs/comprehensive_test.log
```

### 🛠️ Requirements

- **Python 3.6+** (uses only standard library)
- **Node.js 14+** (per main project requirements)
- **npm** (for package management)
- **Make** (for running test suite)
- **Sharness** (for test framework, as per main README)

### 🚨 Notes

- Some README examples may fail in certain environments (e.g., blockchain operations) - this is expected
- The script differentiates between critical failures (setup, core tests) and acceptable failures (some examples)
- All outputs are preserved for debugging even when tests fail
- Generated `.aqua.json` files are automatically copied to output directory
- The script creates archives of test runs for long-term storage

### 🔍 Troubleshooting

#### Common Issues

1. **Python not found**: Install Python 3.6+ and ensure it's in PATH
2. **Node.js/npm not found**: Install Node.js which includes npm
3. **Test failures**: Check individual test outputs in `test_results/` directory
4. **Permission errors**: Ensure script files are executable (`chmod +x`)
5. **Sharness not found**: Install sharness as described in main README

#### Debug Mode

For additional debugging, check the comprehensive log file which contains detailed execution information:

```bash
cat output/run_*/logs/comprehensive_test.log
```

### 📈 Integration

This test runner can be integrated into various workflows:

- **Pre-commit hooks**: Run quick tests before commits
- **CI/CD pipelines**: Full validation on pull requests
- **Release testing**: Comprehensive validation before releases
- **Development cycles**: Regular validation during development 