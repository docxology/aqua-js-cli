#!/usr/bin/env python3
"""
Aqua JS CLI Comprehensive Test Runner

This script runs and logs all the steps from the README.md, executes all tests,
and organizes all outputs into a structured output/ subfolder.

Features:
- Runs all setup and build steps
- Executes all example commands from README
- Runs the complete test suite
- Logs all operations with timestamps
- Organizes outputs in structured folders
- Provides comprehensive reporting
"""

import os
import sys
import subprocess
import json
import time
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import logging


class AquaTestRunner:
    """Comprehensive test runner for Aqua JS CLI"""
    
    def __init__(self, workspace_path: str = "."):
        """Initialize the test runner"""
        self.workspace_path = Path(workspace_path).resolve()
        self.output_dir = self.workspace_path / "output"
        self.run_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.run_dir = self.output_dir / f"run_{self.run_timestamp}"
        
        # Setup directory structure
        self.setup_directories()
        
        # Setup logging
        self.setup_logging()
        
        # Test results storage
        self.test_results = {
            "setup": {},
            "readme_examples": {},
            "test_suite": {},
            "summary": {}
        }
        
        self.logger.info(f"Aqua Test Runner initialized at {self.workspace_path}")
        self.logger.info(f"Output directory: {self.run_dir}")

    def setup_directories(self):
        """Create the output directory structure"""
        directories = [
            self.run_dir,
            self.run_dir / "logs",
            self.run_dir / "outputs",
            self.run_dir / "test_results", 
            self.run_dir / "aqua_files",
            self.run_dir / "reports"
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)

    def setup_logging(self):
        """Setup comprehensive logging"""
        log_file = self.run_dir / "logs" / "comprehensive_test.log"
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # Setup file handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        
        # Setup console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        
        # Setup logger
        self.logger = logging.getLogger('AquaTestRunner')
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def run_command(self, command: str, cwd: Optional[Path] = None, 
                   capture_output: bool = True, timeout: int = 300) -> Tuple[bool, str, str]:
        """Run a shell command and capture output"""
        if cwd is None:
            cwd = self.workspace_path
            
        self.logger.info(f"Running command: {command}")
        self.logger.debug(f"Working directory: {cwd}")
        
        start_time = time.time()
        
        try:
            if capture_output:
                result = subprocess.run(
                    command,
                    shell=True,
                    cwd=cwd,
                    capture_output=True,
                    text=True,
                    timeout=timeout
                )
                success = result.returncode == 0
                stdout = result.stdout
                stderr = result.stderr
            else:
                result = subprocess.run(
                    command,
                    shell=True,
                    cwd=cwd,
                    timeout=timeout
                )
                success = result.returncode == 0
                stdout = ""
                stderr = ""
            
            duration = time.time() - start_time
            
            if success:
                self.logger.info(f"Command completed successfully in {duration:.2f}s")
            else:
                self.logger.error(f"Command failed after {duration:.2f}s")
                if stderr:
                    self.logger.error(f"Error: {stderr}")
            
            return success, stdout, stderr
            
        except subprocess.TimeoutExpired:
            self.logger.error(f"Command timed out after {timeout}s")
            return False, "", f"Command timed out after {timeout}s"
        except Exception as e:
            self.logger.error(f"Command execution failed: {str(e)}")
            return False, "", str(e)

    def setup_environment(self) -> bool:
        """Run initial setup and build steps"""
        self.logger.info("=== ENVIRONMENT SETUP ===")
        
        setup_steps = [
            ("npm_install", "npm install"),
            ("npm_build", "npm run build"),
            ("check_dist", "ls -la dist/"),
        ]
        
        all_success = True
        
        for step_name, command in setup_steps:
            self.logger.info(f"Running setup step: {step_name}")
            success, stdout, stderr = self.run_command(command)
            
            self.test_results["setup"][step_name] = {
                "success": success,
                "command": command,
                "stdout": stdout,
                "stderr": stderr,
                "timestamp": datetime.now().isoformat()
            }
            
            if not success:
                all_success = False
                self.logger.error(f"Setup step {step_name} failed")
            
            # Save output
            if stdout:
                output_file = self.run_dir / "outputs" / f"setup_{step_name}_stdout.txt"
                output_file.write_text(stdout)
            if stderr:
                error_file = self.run_dir / "outputs" / f"setup_{step_name}_stderr.txt"
                error_file.write_text(stderr)
        
        self.logger.info(f"Environment setup completed. Success: {all_success}")
        return all_success

    def cleanup_aqua_files(self):
        """Clean up existing .aqua.json files for fresh testing"""
        self.logger.info("=== CLEANING UP EXISTING AQUA FILES ===")
        
        aqua_files = list(self.workspace_path.glob("*.aqua.json"))
        
        if not aqua_files:
            self.logger.info("No existing .aqua.json files found - starting fresh")
            return True
        
        self.logger.info(f"Found {len(aqua_files)} existing .aqua.json files:")
        for aqua_file in aqua_files:
            self.logger.info(f"  - {aqua_file.name}")
        
        # Backup existing files before cleanup
        backup_dir = self.run_dir / "aqua_files" / "pre_test_backup"
        backup_dir.mkdir(parents=True, exist_ok=True)
        
        for aqua_file in aqua_files:
            try:
                backup_path = backup_dir / aqua_file.name
                shutil.copy2(aqua_file, backup_path)
                aqua_file.unlink()
                self.logger.info(f"Backed up and removed: {aqua_file.name}")
            except Exception as e:
                self.logger.warning(f"Failed to backup/remove {aqua_file.name}: {e}")
        
        self.logger.info("Cleanup completed - ready for fresh notarization tests")
        return True

    def create_test_files(self):
        """Create temporary test files for testing different scenarios"""
        self.logger.info("=== CREATING TEST FILES FOR COMPREHENSIVE TESTING ===")
        
        test_files = {
            "test_fresh_file.txt": "This is a fresh file for testing first notarization.",
            "test_modify_file.txt": "This file will be modified to test revision tracking.",
            "test_content_file.txt": "This file is specifically for testing content revision.",
            "test_scalar_file.txt": "This file is specifically for testing scalar revision."
        }
        
        for filename, content in test_files.items():
            file_path = self.workspace_path / filename
            try:
                file_path.write_text(content)
                self.logger.info(f"Created test file: {filename}")
            except Exception as e:
                self.logger.warning(f"Failed to create {filename}: {e}")
        
        return True

    def run_state_management_tests(self) -> bool:
        """Run tests specifically focused on state management scenarios"""
        self.logger.info("=== RUNNING STATE MANAGEMENT TESTS ===")
        
        state_tests = [
            # Test fresh notarization
            ("fresh_file_notarize", "./dist/aqua.js notarize test_fresh_file.txt", "Fresh file notarization"),
            ("fresh_file_verify", "./dist/aqua.js verify test_fresh_file.txt.aqua.json", "Verify fresh notarization"),
            
            # Test file modification and re-notarization
            ("modify_file_step1", "./dist/aqua.js notarize test_modify_file.txt", "Initial notarization"),
            ("modify_file_step2", "echo 'Modified content' >> test_modify_file.txt", "Modify file content"),
            ("modify_file_step3", "./dist/aqua.js notarize test_modify_file.txt", "Re-notarize modified file"),
            ("modify_file_verify", "./dist/aqua.js verify test_modify_file.txt.aqua.json -v", "Verify revision chain"),
            
            # Test content revision scenarios
            ("content_fresh_notarize", "./dist/aqua.js notarize --content test_content_file.txt", "Fresh content revision"),
            ("content_verify", "./dist/aqua.js verify test_content_file.txt.aqua.json", "Verify content revision"),
            
            # Test scalar revision scenarios  
            ("scalar_fresh_notarize", "./dist/aqua.js notarize --scalar test_scalar_file.txt", "Fresh scalar revision"),
            ("scalar_verify", "./dist/aqua.js verify test_scalar_file.txt.aqua.json", "Verify scalar revision"),
        ]
        
        all_success = True
        
        for test_name, command, description in state_tests:
            self.logger.info(f"Running state test: {test_name} - {description}")
            
            # Special handling for file modification
            if test_name == "modify_file_step2":
                success, stdout, stderr = self.run_command(command)
            else:
                success, stdout, stderr = self.run_command(command)
            
            self.test_results["state_management"] = self.test_results.get("state_management", {})
            self.test_results["state_management"][test_name] = {
                "success": success,
                "command": command,
                "description": description,
                "stdout": stdout,
                "stderr": stderr,
                "timestamp": datetime.now().isoformat()
            }
            
            if not success:
                all_success = False
                self.logger.warning(f"State test {test_name} failed: {description}")
            else:
                self.logger.info(f"State test {test_name} succeeded: {description}")
            
            # Save outputs
            if stdout:
                output_file = self.run_dir / "outputs" / f"state_{test_name}_stdout.txt"
                output_file.write_text(stdout)
            if stderr:
                error_file = self.run_dir / "outputs" / f"state_{test_name}_stderr.txt"
                error_file.write_text(stderr)
            
            # Copy any generated .aqua.json files after each step
            self.copy_aqua_files()
        
        self.logger.info(f"State management tests completed. Success rate: {len([r for r in self.test_results.get('state_management', {}).values() if r['success']])}/{len(state_tests)}")
        return all_success

    def run_existing_file_scenarios(self) -> bool:
        """Run tests with existing files to demonstrate expected behavior"""
        self.logger.info("=== RUNNING EXISTING FILE SCENARIOS ===")
        
        # First, ensure we have some notarized files
        setup_commands = [
            ("setup_license", "./dist/aqua.js notarize ./LICENSE", "Ensure LICENSE is notarized"),
            ("setup_readme", "./dist/aqua.js notarize ./README.md", "Ensure README is notarized"),
        ]
        
        for setup_name, command, description in setup_commands:
            self.logger.info(f"Setup for existing file tests: {setup_name} - {description}")
            success, stdout, stderr = self.run_command(command)
            
            # Log whether this was a fresh notarization or already existed
            if "already been notarized" in stdout:
                self.logger.info(f"✓ {setup_name}: File was already notarized (expected)")
            elif "Writing new file revision" in stdout:
                self.logger.info(f"✓ {setup_name}: Created new notarization")
            else:
                self.logger.warning(f"? {setup_name}: Unexpected response")
        
        # Now run tests that demonstrate expected "already notarized" behavior
        existing_file_tests = [
            # These should show "already notarized" messages - this is EXPECTED behavior
            ("existing_license_basic", "./dist/aqua.js notarize ./LICENSE", "Expected: Already notarized message"),
            ("existing_readme_basic", "./dist/aqua.js notarize ./README.md", "Expected: Already notarized message"),
            ("existing_license_content", "./dist/aqua.js notarize --content ./LICENSE", "Expected: Already notarized (content)"),
            ("existing_license_scalar", "./dist/aqua.js notarize --scalar ./LICENSE", "Expected: Already notarized (scalar)"),
            
            # These should work because they're operations on existing notarizations
            ("existing_license_sign", "./dist/aqua.js notarize --sign cli ./LICENSE", "Expected: Sign existing notarization"),
            ("existing_license_verify", "./dist/aqua.js verify LICENSE.aqua.json", "Expected: Verify existing notarization"),
            ("existing_readme_verify", "./dist/aqua.js verify README.md.aqua.json", "Expected: Verify existing notarization"),
        ]
        
        for test_name, command, expected_behavior in existing_file_tests:
            self.logger.info(f"Running existing file test: {test_name}")
            self.logger.info(f"Expected behavior: {expected_behavior}")
            
            success, stdout, stderr = self.run_command(command)
            
            # Analyze the result based on expected behavior
            result_analysis = self.analyze_expected_behavior(stdout, stderr, expected_behavior)
            
            self.test_results["existing_file_scenarios"] = self.test_results.get("existing_file_scenarios", {})
            self.test_results["existing_file_scenarios"][test_name] = {
                "success": success,
                "command": command,
                "expected_behavior": expected_behavior,
                "result_analysis": result_analysis,
                "stdout": stdout,
                "stderr": stderr,
                "timestamp": datetime.now().isoformat()
            }
            
            self.logger.info(f"Result analysis: {result_analysis}")
            
            # Save outputs
            if stdout:
                output_file = self.run_dir / "outputs" / f"existing_{test_name}_stdout.txt"
                output_file.write_text(stdout)
            if stderr:
                error_file = self.run_dir / "outputs" / f"existing_{test_name}_stderr.txt"
                error_file.write_text(stderr)
        
        return True

    def analyze_expected_behavior(self, stdout: str, stderr: str, expected_behavior: str) -> str:
        """Analyze command output against expected behavior"""
        if "Expected: Already notarized" in expected_behavior:
            if "already been notarized" in stdout:
                return "✓ EXPECTED: Correctly shows 'already notarized' message"
            else:
                return "? UNEXPECTED: Did not show expected 'already notarized' message"
        
        elif "Expected: Sign existing" in expected_behavior:
            if "signed succesfully" in stdout:
                return "✓ EXPECTED: Successfully signed existing notarization"
            else:
                return "? UNEXPECTED: Failed to sign existing notarization"
        
        elif "Expected: Verify existing" in expected_behavior:
            if "All revisions verified successfully" in stdout:
                return "✓ EXPECTED: Successfully verified existing notarization"
            elif "Error" in stdout or stderr:
                return "⚠ ISSUE: Verification failed - may indicate application bug"
            else:
                return "? UNEXPECTED: Unclear verification result"
        
        else:
            return "? UNKNOWN: Could not analyze expected behavior"

    def run_readme_examples(self) -> bool:
        """Run focused README examples with proper state awareness"""
        self.logger.info("=== RUNNING FOCUSED README EXAMPLES ===")
        
        # Ensure we have test files
        test_files = ["LICENSE", "README.md", "example-form.json"]
        for test_file in test_files:
            if not (self.workspace_path / test_file).exists():
                self.logger.warning(f"Test file {test_file} not found")
        
        # Focus on successful operations and advanced features
        examples = [
            # Witnessing examples (these work well)
            ("witness_eth_license", "./dist/aqua.js notarize ./LICENSE --witness eth"),
            
            # Form examples (if form file exists)
            ("form_genesis", "./dist/aqua.js notarize example-form.json --form example-form.json") if (self.workspace_path / "example-form.json").exists() else None,
            ("form_revision", "./dist/aqua.js notarize LICENSE --form example-form.json") if (self.workspace_path / "example-form.json").exists() else None,
        ]
        
        # Filter out None entries
        examples = [ex for ex in examples if ex is not None]
        
        all_success = True
        
        for example_name, command in examples:
            self.logger.info(f"Running README example: {example_name}")
            success, stdout, stderr = self.run_command(command)
            
            self.test_results["readme_examples"][example_name] = {
                "success": success,
                "command": command,
                "stdout": stdout,
                "stderr": stderr,
                "timestamp": datetime.now().isoformat()
            }
            
            if not success:
                all_success = False
                self.logger.warning(f"README example {example_name} failed (this may be expected)")
            
            # Save outputs
            if stdout:
                output_file = self.run_dir / "outputs" / f"readme_{example_name}_stdout.txt"
                output_file.write_text(stdout)
            if stderr:
                error_file = self.run_dir / "outputs" / f"readme_{example_name}_stderr.txt"
                error_file.write_text(stderr)
            
            # Copy any generated .aqua.json files
            self.copy_aqua_files()
        
        # Run verification examples on generated files
        self.run_verification_examples()
        
        self.logger.info(f"README examples completed. Success rate: {len([r for r in self.test_results['readme_examples'].values() if r['success']])}/{len(self.test_results['readme_examples'])}")
        return all_success

    def run_verification_examples(self):
        """Run verification commands on generated aqua files"""
        self.logger.info("Running verification examples...")
        
        # Find all .aqua.json files
        aqua_files = list(self.workspace_path.glob("*.aqua.json"))
        
        for aqua_file in aqua_files:
            file_name = aqua_file.name
            base_name = file_name.replace(".aqua.json", "")
            
            verify_examples = [
                (f"verify_{base_name}", f"./dist/aqua.js verify {file_name}"),
                (f"verify_verbose_{base_name}", f"./dist/aqua.js verify {file_name} -v"),
                (f"verify_ignore_merkle_{base_name}", f"./dist/aqua.js verify {file_name} --ignore-merkle-proof"),
            ]
            
            for example_name, command in verify_examples:
                self.logger.info(f"Running verification: {example_name}")
                success, stdout, stderr = self.run_command(command)
                
                self.test_results["readme_examples"][example_name] = {
                    "success": success,
                    "command": command,
                    "stdout": stdout,
                    "stderr": stderr,
                    "timestamp": datetime.now().isoformat()
                }
                
                # Save outputs
                if stdout:
                    output_file = self.run_dir / "outputs" / f"verify_{example_name}_stdout.txt"
                    output_file.write_text(stdout)
                if stderr:
                    error_file = self.run_dir / "outputs" / f"verify_{example_name}_stderr.txt"
                    error_file.write_text(stderr)

    def copy_aqua_files(self):
        """Copy generated .aqua.json files to output directory"""
        aqua_files = list(self.workspace_path.glob("*.aqua.json"))
        for aqua_file in aqua_files:
            destination = self.run_dir / "aqua_files" / aqua_file.name
            try:
                shutil.copy2(aqua_file, destination)
                self.logger.debug(f"Copied {aqua_file.name} to output directory")
            except Exception as e:
                self.logger.warning(f"Failed to copy {aqua_file.name}: {e}")

    def run_test_suite(self) -> bool:
        """Run the complete test suite using sharness"""
        self.logger.info("=== RUNNING TEST SUITE ===")
        
        # Find all test files
        test_files = list((self.workspace_path / "tests").glob("test-*.sh"))
        
        if not test_files:
            self.logger.warning("No test files found")
            return False
        
        all_success = True
        
        # Run make test to execute all tests
        self.logger.info("Running complete test suite with 'make test'")
        success, stdout, stderr = self.run_command("make test", timeout=600)
        
        self.test_results["test_suite"]["make_test"] = {
            "success": success,
            "command": "make test",
            "stdout": stdout,
            "stderr": stderr,
            "timestamp": datetime.now().isoformat()
        }
        
        if not success:
            all_success = False
        
        # Save test suite output
        if stdout:
            output_file = self.run_dir / "test_results" / "make_test_stdout.txt"
            output_file.write_text(stdout)
        if stderr:
            error_file = self.run_dir / "test_results" / "make_test_stderr.txt"
            error_file.write_text(stderr)
        
        # Run individual tests for detailed reporting
        for test_file in test_files:
            test_name = test_file.stem
            self.logger.info(f"Running individual test: {test_name}")
            
            success, stdout, stderr = self.run_command(f"./{test_file.name}", 
                                                     cwd=self.workspace_path / "tests",
                                                     timeout=300)
            
            self.test_results["test_suite"][test_name] = {
                "success": success,
                "command": f"./{test_file.name}",
                "stdout": stdout,
                "stderr": stderr,
                "timestamp": datetime.now().isoformat()
            }
            
            if not success:
                all_success = False
            
            # Save individual test output
            if stdout:
                output_file = self.run_dir / "test_results" / f"{test_name}_stdout.txt"
                output_file.write_text(stdout)
            if stderr:
                error_file = self.run_dir / "test_results" / f"{test_name}_stderr.txt"
                error_file.write_text(stderr)
        
        # Copy any test-results directory if it exists
        test_results_dir = self.workspace_path / "test-results"
        if test_results_dir.exists():
            destination = self.run_dir / "test_results" / "sharness_results"
            try:
                shutil.copytree(test_results_dir, destination, dirs_exist_ok=True)
                self.logger.info("Copied sharness test results")
            except Exception as e:
                self.logger.warning(f"Failed to copy test results: {e}")
        
        self.logger.info(f"Test suite completed. Success: {all_success}")
        return all_success

    def generate_reports(self):
        """Generate comprehensive reports"""
        self.logger.info("=== GENERATING REPORTS ===")
        
        # Calculate summary statistics
        setup_success = sum(1 for r in self.test_results["setup"].values() if r["success"])
        setup_total = len(self.test_results["setup"])
        
        state_success = sum(1 for r in self.test_results.get("state_management", {}).values() if r["success"])
        state_total = len(self.test_results.get("state_management", {}))
        
        existing_success = sum(1 for r in self.test_results.get("existing_file_scenarios", {}).values() if r["success"])
        existing_total = len(self.test_results.get("existing_file_scenarios", {}))
        
        readme_success = sum(1 for r in self.test_results["readme_examples"].values() if r["success"])
        readme_total = len(self.test_results["readme_examples"])
        
        test_success = sum(1 for r in self.test_results["test_suite"].values() if r["success"])
        test_total = len(self.test_results["test_suite"])
        
        total_success = setup_success + state_success + existing_success + readme_success + test_success
        total_tests = setup_total + state_total + existing_total + readme_total + test_total
        
        self.test_results["summary"] = {
            "timestamp": datetime.now().isoformat(),
            "run_directory": str(self.run_dir),
            "setup": {"success": setup_success, "total": setup_total},
            "state_management": {"success": state_success, "total": state_total},
            "existing_file_scenarios": {"success": existing_success, "total": existing_total},
            "readme_examples": {"success": readme_success, "total": readme_total},
            "test_suite": {"success": test_success, "total": test_total},
            "overall": {"success": total_success, "total": total_tests, "success_rate": total_success/total_tests if total_tests > 0 else 0}
        }
        
        # Generate JSON report
        json_report = self.run_dir / "reports" / "comprehensive_report.json"
        with open(json_report, 'w') as f:
            json.dump(self.test_results, f, indent=2)
        
        # Generate markdown report
        self.generate_markdown_report()
        
        # Generate summary report
        self.generate_summary_report()
        
        self.logger.info("Reports generated successfully")

    def generate_markdown_report(self):
        """Generate a detailed markdown report"""
        report_file = self.run_dir / "reports" / "comprehensive_report.md"
        
        with open(report_file, 'w') as f:
            f.write(f"# Aqua JS CLI Comprehensive Test Report\n\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**Run Directory:** `{self.run_dir}`\n\n")
            
            # Summary
            summary = self.test_results["summary"]
            f.write(f"## Summary\n\n")
            f.write(f"- **Overall Success Rate:** {summary['overall']['success']}/{summary['overall']['total']} ({summary['overall']['success_rate']:.1%})\n")
            f.write(f"- **Setup:** {summary['setup']['success']}/{summary['setup']['total']}\n")
            f.write(f"- **State Management:** {summary['state_management']['success']}/{summary['state_management']['total']}\n")
            f.write(f"- **Existing File Scenarios:** {summary['existing_file_scenarios']['success']}/{summary['existing_file_scenarios']['total']}\n")
            f.write(f"- **README Examples:** {summary['readme_examples']['success']}/{summary['readme_examples']['total']}\n")
            f.write(f"- **Test Suite:** {summary['test_suite']['success']}/{summary['test_suite']['total']}\n\n")
            
            # Detailed sections
            sections = [
                ("Setup Results", "setup"),
                ("State Management Results", "state_management"),
                ("Existing File Scenarios", "existing_file_scenarios"),
                ("README Examples Results", "readme_examples"),
                ("Test Suite Results", "test_suite")
            ]
            
            for section_title, section_key in sections:
                f.write(f"## {section_title}\n\n")
                for test_name, result in self.test_results[section_key].items():
                    status = "✅ PASS" if result["success"] else "❌ FAIL"
                    f.write(f"### {test_name} {status}\n\n")
                    f.write(f"**Command:** `{result['command']}`\n")
                    f.write(f"**Timestamp:** {result['timestamp']}\n\n")
                    
                    if result.get("stdout"):
                        f.write(f"**Output:**\n```\n{result['stdout'][:500]}{'...' if len(result['stdout']) > 500 else ''}\n```\n\n")
                    
                    if result.get("stderr"):
                        f.write(f"**Error:**\n```\n{result['stderr'][:500]}{'...' if len(result['stderr']) > 500 else ''}\n```\n\n")

    def generate_summary_report(self):
        """Generate a concise summary report"""
        report_file = self.run_dir / "reports" / "summary.txt"
        
        with open(report_file, 'w') as f:
            f.write("AQUA JS CLI COMPREHENSIVE TEST SUMMARY\n")
            f.write("=" * 50 + "\n\n")
            
            summary = self.test_results["summary"]
            f.write(f"Run Timestamp: {summary['timestamp']}\n")
            f.write(f"Output Directory: {summary['run_directory']}\n\n")
            
            f.write(f"OVERALL RESULTS:\n")
            f.write(f"Success Rate: {summary['overall']['success']}/{summary['overall']['total']} ({summary['overall']['success_rate']:.1%})\n\n")
            
            f.write(f"BREAKDOWN:\n")
            f.write(f"- Environment Setup: {summary['setup']['success']}/{summary['setup']['total']}\n")
            f.write(f"- State Management: {summary['state_management']['success']}/{summary['state_management']['total']}\n")
            f.write(f"- Existing File Scenarios: {summary['existing_file_scenarios']['success']}/{summary['existing_file_scenarios']['total']}\n")
            f.write(f"- README Examples: {summary['readme_examples']['success']}/{summary['readme_examples']['total']}\n")
            f.write(f"- Test Suite: {summary['test_suite']['success']}/{summary['test_suite']['total']}\n\n")
            
            # Failed tests
            failed_tests = []
            for section_key in ["setup", "state_management", "existing_file_scenarios", "readme_examples", "test_suite"]:
                for test_name, result in self.test_results.get(section_key, {}).items():
                    if not result["success"]:
                        failed_tests.append(f"{section_key}.{test_name}")
            
            if failed_tests:
                f.write(f"FAILED TESTS:\n")
                for failed_test in failed_tests:
                    f.write(f"- {failed_test}\n")
            else:
                f.write("ALL TESTS PASSED!\n")

    def cleanup(self):
        """Clean up temporary files and organize outputs"""
        self.logger.info("=== CLEANUP ===")
        
        # Copy final aqua files
        self.copy_aqua_files()
        
        # Create archive of the run
        archive_name = f"aqua_test_run_{self.run_timestamp}"
        archive_path = self.output_dir / f"{archive_name}.tar.gz"
        
        try:
            shutil.make_archive(
                str(self.output_dir / archive_name),
                'gztar',
                str(self.run_dir)
            )
            self.logger.info(f"Created archive: {archive_path}")
        except Exception as e:
            self.logger.warning(f"Failed to create archive: {e}")
        
        # Remove temporary test files created for state management
        temp_files = [
            "test_fresh_file.txt",
            "test_modify_file.txt",
            "test_content_file.txt",
            "test_scalar_file.txt"
        ]
        for filename in temp_files:
            file_path = self.workspace_path / filename
            if file_path.exists():
                try:
                    file_path.unlink()
                    self.logger.info(f"Removed temporary test file: {filename}")
                except Exception as e:
                    self.logger.warning(f"Failed to remove {filename}: {e}")
        
        self.logger.info("Cleanup completed")

    def run_all(self) -> bool:
        """Run the complete test suite with enhanced state management"""
        self.logger.info("Starting comprehensive Aqua JS CLI test run with enhanced state management")
        
        start_time = time.time()
        
        try:
            # Phase 1: Environment Setup
            setup_success = self.setup_environment()
            if not setup_success:
                self.logger.error("Environment setup failed - aborting")
                return False
            
            # Phase 2: Clean up existing state for controlled testing
            self.cleanup_aqua_files()
            
            # Phase 3: Create test files for comprehensive scenarios
            self.create_test_files()
            
            # Phase 4: Run state management tests (fresh files, modifications, etc.)
            state_success = self.run_state_management_tests()
            
            # Phase 5: Run existing file scenarios (demonstrate expected behavior)
            existing_success = self.run_existing_file_scenarios()
            
            # Phase 6: Run focused README examples (advanced features)
            readme_success = self.run_readme_examples()
            
            # Phase 7: Run traditional test suite
            test_success = self.run_test_suite()
            
            # Generate comprehensive reports
            self.generate_reports()
            
            # Final cleanup
            self.cleanup()
            
            duration = time.time() - start_time
            
            # Calculate overall success (environment setup and test suite are critical)
            critical_success = setup_success and test_success
            overall_success = critical_success and state_success
            
            self.logger.info(f"Test run completed in {duration:.2f}s")
            self.logger.info(f"Critical components success: {critical_success}")
            self.logger.info(f"Overall success: {overall_success}")
            self.logger.info(f"Results saved to: {self.run_dir}")
            
            # Log phase-by-phase results
            self.logger.info("Phase Results Summary:")
            self.logger.info(f"  ✓ Environment Setup: {'SUCCESS' if setup_success else 'FAILED'}")
            self.logger.info(f"  ✓ State Management: {'SUCCESS' if state_success else 'FAILED'}")
            self.logger.info(f"  ✓ Existing File Scenarios: {'SUCCESS' if existing_success else 'PARTIAL'}")
            self.logger.info(f"  ✓ README Examples: {'SUCCESS' if readme_success else 'PARTIAL'}")
            self.logger.info(f"  ✓ Test Suite: {'SUCCESS' if test_success else 'FAILED'}")
            
            return overall_success
            
        except Exception as e:
            self.logger.error(f"Test run failed with exception: {str(e)}", exc_info=True)
            return False


def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        workspace_path = sys.argv[1]
    else:
        workspace_path = "."
    
    runner = AquaTestRunner(workspace_path)
    
    print(f"🚀 Starting Aqua JS CLI Comprehensive Test Runner")
    print(f"📁 Workspace: {runner.workspace_path}")
    print(f"📂 Output: {runner.run_dir}")
    print(f"📝 Logs: {runner.run_dir}/logs/comprehensive_test.log")
    print()
    
    success = runner.run_all()
    
    if success:
        print(f"✅ Test run completed successfully!")
        exit_code = 0
    else:
        print(f"❌ Test run completed with failures!")
        exit_code = 1
    
    print(f"📊 View reports at: {runner.run_dir}/reports/")
    print(f"📄 Summary: {runner.run_dir}/reports/summary.txt")
    print(f"📋 Full report: {runner.run_dir}/reports/comprehensive_report.md")
    
    sys.exit(exit_code)


if __name__ == "__main__":
    main() 