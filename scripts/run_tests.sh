#!/bin/bash

# Aqua JS CLI Comprehensive Test Runner Wrapper
# 
# This script provides an easy way to run the comprehensive test suite
# for the Aqua JS CLI project.

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

echo -e "${BLUE}🚀 Aqua JS CLI Comprehensive Test Runner${NC}"
echo -e "${BLUE}===========================================${NC}"
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Error: Python 3 is required but not installed.${NC}"
    echo "Please install Python 3.6 or later and try again."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo -e "${GREEN}✅ Python version: $PYTHON_VERSION${NC}"

# Check if Node.js is available
if ! command -v node &> /dev/null; then
    echo -e "${RED}❌ Error: Node.js is required but not installed.${NC}"
    echo "Please install Node.js and try again."
    exit 1
fi

NODE_VERSION=$(node --version)
echo -e "${GREEN}✅ Node.js version: $NODE_VERSION${NC}"

# Check if npm is available
if ! command -v npm &> /dev/null; then
    echo -e "${RED}❌ Error: npm is required but not installed.${NC}"
    echo "Please install npm and try again."
    exit 1
fi

NPM_VERSION=$(npm --version)
echo -e "${GREEN}✅ npm version: $NPM_VERSION${NC}"

echo ""
echo -e "${YELLOW}📁 Project root: $PROJECT_ROOT${NC}"
echo -e "${YELLOW}🐍 Running Python test script...${NC}"
echo ""

# Change to project root and run the Python script
cd "$PROJECT_ROOT"

if python3 "$SCRIPT_DIR/run_comprehensive_tests.py" "$PROJECT_ROOT"; then
    echo ""
    echo -e "${GREEN}✅ All tests completed successfully!${NC}"
    echo -e "${GREEN}📊 Check the output/ directory for detailed results.${NC}"
    exit 0
else
    echo ""
    echo -e "${RED}❌ Some tests failed.${NC}"
    echo -e "${YELLOW}📊 Check the output/ directory for detailed results and error logs.${NC}"
    exit 1
fi 