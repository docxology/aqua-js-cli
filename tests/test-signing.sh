#!/bin/sh

test_description='Test file verification functionality'

notarize="repo/dist/aqua.js notarize"
verify="repo/dist/aqua.js verify"

. ./tests/sharness/sharness.sh

test_expect_success 'Setup test environment' '
    ln -s $(git rev-parse --show-toplevel) ./repo &&
    cp repo/README.md README.md &&
    cp repo/LICENSE LICENSE &&
    cp repo/notarize.js notarize.js
'

test_expect_success 'Check README.md'  '
    test -f README.md
'

test_expect_success 'Create AQUA file for README.md' '
    $notarize README.md &&
    test -f README.md.aqua.json
'

test_expect_success 'Sign README.md' '
    $notarize README.md  --sign cli &&
    test -f README.md.aqua.json
'



test_expect_success 'Check notarize.js'  '
    test -f notarize.js
'

test_expect_success 'Create AQUA file for notarize.js' '
    $notarize notarize.js &&
    test -f notarize.js.aqua.json
'


test_expect_success 'Witness notarize.js.aqua.json' '
    $notarize notarize.js  --sign did &&
    test -f notarize.js.aqua.json
'

# Cleanup
test_expect_success 'Cleanup test files' '
    rm -f README.md.aqua.json &&
    rm -f LICENSE.aqua.json &&
    rm -f notarize.js.aqua.json &&
    rm -f README.md &&
    rm -f LICENSE &&
    rm -f notarize.js &&
    rm -f actual_output
'

test_done 