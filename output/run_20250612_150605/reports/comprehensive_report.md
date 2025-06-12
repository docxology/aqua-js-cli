# Aqua JS CLI Comprehensive Test Report

**Generated:** 2025-06-12 15:12:14
**Run Directory:** `/Users/tetra/Documents/GitHub/aqua-js-cli/output/run_20250612_150605`

## Summary

- **Overall Success Rate:** 45/52 (86.5%)
- **Setup:** 3/3
- **State Management:** 10/10
- **Existing File Scenarios:** 3/7
- **README Examples:** 23/24
- **Test Suite:** 6/8

## Setup Results

### npm_install ✅ PASS

**Command:** `npm install`
**Timestamp:** 2025-06-12T15:06:10.464576

**Output:**
```

> aqua@1.0.10 prepare
> npm run build


> aqua@1.0.10 build
> tsup

CLI Building entry: aqua.ts
CLI Using tsconfig: tsconfig.json
CLI tsup v8.5.0
CLI Using tsup config: /Users/tetra/Documents/GitHub/aqua-js-cli/tsup.config.ts
CLI Target: node18
CLI Cleaning output folder
CJS Build start
CJS dist/aqua.js     1.11 MB
CJS dist/aqua.js.map 5.00 MB
CJS ⚡️ Build success in 359ms
DTS Build start
DTS ⚡️ Build success in 1040ms
DTS dist/aqua.d.ts 20.00 B

up to date, audited 731 packages in 5s

104 pack...
```

### npm_build ✅ PASS

**Command:** `npm run build`
**Timestamp:** 2025-06-12T15:06:12.699307

**Output:**
```

> aqua@1.0.10 build
> tsup

CLI Building entry: aqua.ts
CLI Using tsconfig: tsconfig.json
CLI tsup v8.5.0
CLI Using tsup config: /Users/tetra/Documents/GitHub/aqua-js-cli/tsup.config.ts
CLI Target: node18
CLI Cleaning output folder
CJS Build start
CJS dist/aqua.js     1.11 MB
CJS dist/aqua.js.map 5.00 MB
CJS ⚡️ Build success in 463ms
DTS Build start
DTS ⚡️ Build success in 1243ms
DTS dist/aqua.d.ts 20.00 B

```

### check_dist ✅ PASS

**Command:** `ls -la dist/`
**Timestamp:** 2025-06-12T15:06:12.716046

**Output:**
```
total 12544
drwxr-xr-x@  5 tetra  staff      160 Jun 12 15:06 .
drwxr-xr-x@ 35 tetra  staff     1120 Jun 12 15:06 ..
-rw-r--r--@  1 tetra  staff       20 Jun 12 15:06 aqua.d.ts
-rwxr-xr-x@  1 tetra  staff  1165836 Jun 12 15:06 aqua.js
-rw-r--r--@  1 tetra  staff  5247144 Jun 12 15:06 aqua.js.map

```

## State Management Results

### fresh_file_notarize ✅ PASS

**Command:** `./dist/aqua.js notarize test_fresh_file.txt`
**Timestamp:** 2025-06-12T15:06:13.286230

**Output:**
```
- Writing new file revision 0xf3cc25d4f3cf6c46f1e02f2eace7c1fd711a10dc5134f1608fbdd7d7f288568e to test_fresh_file.txt.aqua.json

```

### fresh_file_verify ✅ PASS

**Command:** `./dist/aqua.js verify test_fresh_file.txt.aqua.json`
**Timestamp:** 2025-06-12T15:06:13.551662

**Output:**
```
file name test_fresh_file.txt.aqua.json
-> reading pure file test_fresh_file.txt
Checking aqua file: test_fresh_file.txt.aqua.json
-> reading aqua file test_fresh_file.txt.aqua.json
✅ All revisions verified successfully


```

### modify_file_step1 ✅ PASS

**Command:** `./dist/aqua.js notarize test_modify_file.txt`
**Timestamp:** 2025-06-12T15:06:13.960059

**Output:**
```
- Writing new file revision 0x4dbced08be6848b62514e14ef5636ecac76d9d710c8f65b0126ad97a5dd2a71c to test_modify_file.txt.aqua.json

```

### modify_file_step2 ✅ PASS

**Command:** `echo 'Modified content' >> test_modify_file.txt`
**Timestamp:** 2025-06-12T15:06:13.979263

### modify_file_step3 ✅ PASS

**Command:** `./dist/aqua.js notarize test_modify_file.txt`
**Timestamp:** 2025-06-12T15:06:14.216435

### modify_file_verify ✅ PASS

**Command:** `./dist/aqua.js verify test_modify_file.txt.aqua.json -v`
**Timestamp:** 2025-06-12T15:06:14.451527

**Output:**
```
file name test_modify_file.txt.aqua.json
-> reading pure file test_modify_file.txt
Checking aqua file: test_modify_file.txt.aqua.json
-> reading aqua file test_modify_file.txt.aqua.json
 ➡️  1.Verifying Revision: 0x4dbced08be6848b62514e14ef5636ecac76d9d710c8f65b0126ad97a5dd2a71c
	 📄 Type: File.
	 ❌ Error verifying revision type:file with hash 0x4dbced08be6848b62514e14ef5636ecac76d9d710c8f65b0126ad97a5dd2a71c - 
 isSuccess false - isScalarSuccess true 
  

 ❌ One or more revision verification fai...
```

### content_fresh_notarize ✅ PASS

**Command:** `./dist/aqua.js notarize --content test_content_file.txt`
**Timestamp:** 2025-06-12T15:06:14.718907

**Output:**
```
- Writing new file revision 0xf3018933704bf58334b0946484b21d160bc4bd8828a52526885d9153881f6ef6 to test_content_file.txt.aqua.json

```

### content_verify ✅ PASS

**Command:** `./dist/aqua.js verify test_content_file.txt.aqua.json`
**Timestamp:** 2025-06-12T15:06:14.960219

**Output:**
```
file name test_content_file.txt.aqua.json
✅ All revisions verified successfully


```

**Error:**
```
✓ File test_content_file.txt skipped: content already exists in revision 0xf3018933704bf58334b0946484b21d160bc4bd8828a52526885d9153881f6ef6

```

### scalar_fresh_notarize ✅ PASS

**Command:** `./dist/aqua.js notarize --scalar test_scalar_file.txt`
**Timestamp:** 2025-06-12T15:06:15.195397

**Output:**
```
- Writing new file revision 0x8c5bb6bb7b9b1962e456d1f1a54d1c5ea1490745869b0713c325f1efe2238f7d to test_scalar_file.txt.aqua.json

```

### scalar_verify ✅ PASS

**Command:** `./dist/aqua.js verify test_scalar_file.txt.aqua.json`
**Timestamp:** 2025-06-12T15:06:15.491522

**Output:**
```
file name test_scalar_file.txt.aqua.json
-> reading pure file test_scalar_file.txt
Checking aqua file: test_scalar_file.txt.aqua.json
-> reading aqua file test_scalar_file.txt.aqua.json
✅ All revisions verified successfully


```

## Existing File Scenarios

### existing_license_basic ❌ FAIL

**Command:** `./dist/aqua.js notarize ./LICENSE`
**Timestamp:** 2025-06-12T15:06:16.689899

**Output:**
```
[31m❌ file ./LICENSE has already been notarized[0m

```

### existing_readme_basic ❌ FAIL

**Command:** `./dist/aqua.js notarize ./README.md`
**Timestamp:** 2025-06-12T15:06:17.099582

**Output:**
```
[31m❌ file ./README.md has already been notarized[0m

```

### existing_license_content ❌ FAIL

**Command:** `./dist/aqua.js notarize --content ./LICENSE`
**Timestamp:** 2025-06-12T15:06:17.523087

**Output:**
```
[31m❌ file ./LICENSE has already been notarized[0m

```

### existing_license_scalar ❌ FAIL

**Command:** `./dist/aqua.js notarize --scalar ./LICENSE`
**Timestamp:** 2025-06-12T15:06:18.021932

**Output:**
```
[31m❌ file ./LICENSE has already been notarized[0m

```

### existing_license_sign ✅ PASS

**Command:** `./dist/aqua.js notarize --sign cli ./LICENSE`
**Timestamp:** 2025-06-12T15:06:18.726378

**Output:**
```
✅ AquaTree signed succesfully

```

### existing_license_verify ✅ PASS

**Command:** `./dist/aqua.js verify LICENSE.aqua.json`
**Timestamp:** 2025-06-12T15:06:19.307296

**Output:**
```
file name LICENSE.aqua.json
-> reading pure file ./LICENSE
Checking aqua file: ./LICENSE.aqua.json
-> reading aqua file ./LICENSE.aqua.json
✅ All revisions verified successfully


```

### existing_readme_verify ✅ PASS

**Command:** `./dist/aqua.js verify README.md.aqua.json`
**Timestamp:** 2025-06-12T15:06:19.657920

**Output:**
```
file name README.md.aqua.json
-> reading pure file ./README.md
Checking aqua file: ./README.md.aqua.json
-> reading aqua file ./README.md.aqua.json
✅ All revisions verified successfully


```

## README Examples Results

### witness_eth_license ❌ FAIL

**Command:** `./dist/aqua.js notarize ./LICENSE --witness eth`
**Timestamp:** 2025-06-12T15:11:19.674075

**Error:**
```
Command timed out after 300s
```

### form_genesis ✅ PASS

**Command:** `./dist/aqua.js notarize example-form.json --form example-form.json`
**Timestamp:** 2025-06-12T15:11:19.908192

**Output:**
```
- Writing new form revision 0xbae6c56ded92c0d006d0b8a79335f0ee3c4cf2396ffac3fab3fdbbb45ff865b9 to example-form.json.aqua.json

```

### form_revision ✅ PASS

**Command:** `./dist/aqua.js notarize LICENSE --form example-form.json`
**Timestamp:** 2025-06-12T15:11:20.092019

**Output:**
```
✅ Form  revision created succesfully

```

### verify_test_scalar_file.txt ✅ PASS

**Command:** `./dist/aqua.js verify test_scalar_file.txt.aqua.json`
**Timestamp:** 2025-06-12T15:11:20.272364

**Output:**
```
file name test_scalar_file.txt.aqua.json
-> reading pure file test_scalar_file.txt
Checking aqua file: test_scalar_file.txt.aqua.json
-> reading aqua file test_scalar_file.txt.aqua.json
✅ All revisions verified successfully


```

### verify_verbose_test_scalar_file.txt ✅ PASS

**Command:** `./dist/aqua.js verify test_scalar_file.txt.aqua.json -v`
**Timestamp:** 2025-06-12T15:11:20.476406

**Output:**
```
file name test_scalar_file.txt.aqua.json
-> reading pure file test_scalar_file.txt
Checking aqua file: test_scalar_file.txt.aqua.json
-> reading aqua file test_scalar_file.txt.aqua.json
 ➡️  1.Verifying Revision: 0x8c5bb6bb7b9b1962e456d1f1a54d1c5ea1490745869b0713c325f1efe2238f7d
	 📄 Type: File.
	 ✅ ⏺️  Scalar revision verified
  

 ✅ All revisions verified successfully


```

### verify_ignore_merkle_test_scalar_file.txt ✅ PASS

**Command:** `./dist/aqua.js verify test_scalar_file.txt.aqua.json --ignore-merkle-proof`
**Timestamp:** 2025-06-12T15:11:20.740921

**Output:**
```
file name test_scalar_file.txt.aqua.json
-> reading pure file test_scalar_file.txt
Checking aqua file: test_scalar_file.txt.aqua.json
-> reading aqua file test_scalar_file.txt.aqua.json
✅ All revisions verified successfully


```

### verify_README.md ✅ PASS

**Command:** `./dist/aqua.js verify README.md.aqua.json`
**Timestamp:** 2025-06-12T15:11:20.963956

**Output:**
```
file name README.md.aqua.json
-> reading pure file ./README.md
Checking aqua file: ./README.md.aqua.json
-> reading aqua file ./README.md.aqua.json
✅ All revisions verified successfully


```

### verify_verbose_README.md ✅ PASS

**Command:** `./dist/aqua.js verify README.md.aqua.json -v`
**Timestamp:** 2025-06-12T15:11:21.280790

**Output:**
```
file name README.md.aqua.json
-> reading pure file ./README.md
Checking aqua file: ./README.md.aqua.json
-> reading aqua file ./README.md.aqua.json
 ➡️  1.Verifying Revision: 0xd84c2a49f59d4ec637a77c9e16f46480d24e227d1c350759606c596a3e8725b8
	 📄 Type: File.
	 ✅ ⏺️  Scalar revision verified
  

 ✅ All revisions verified successfully


```

### verify_ignore_merkle_README.md ✅ PASS

**Command:** `./dist/aqua.js verify README.md.aqua.json --ignore-merkle-proof`
**Timestamp:** 2025-06-12T15:11:21.642781

**Output:**
```
file name README.md.aqua.json
-> reading pure file ./README.md
Checking aqua file: ./README.md.aqua.json
-> reading aqua file ./README.md.aqua.json
✅ All revisions verified successfully


```

### verify_example-form.json ✅ PASS

**Command:** `./dist/aqua.js verify example-form.json.aqua.json`
**Timestamp:** 2025-06-12T15:11:21.883764

**Output:**
```
file name example-form.json.aqua.json
-> reading pure file example-form.json
Checking aqua file: example-form.json.aqua.json
-> reading aqua file example-form.json.aqua.json
✅ All revisions verified successfully


```

### verify_verbose_example-form.json ✅ PASS

**Command:** `./dist/aqua.js verify example-form.json.aqua.json -v`
**Timestamp:** 2025-06-12T15:11:22.219270

**Output:**
```
file name example-form.json.aqua.json
-> reading pure file example-form.json
Checking aqua file: example-form.json.aqua.json
-> reading aqua file example-form.json.aqua.json
 ➡️  1.Verifying Revision: 0xbae6c56ded92c0d006d0b8a79335f0ee3c4cf2396ffac3fab3fdbbb45ff865b9
	 📝 Type: Form.
		 ✅ The following fields were verified:
		 ✅ ✅ forms_date_of_birth: October 2, 1945

		 ✅ ✅ forms_name: Martin Hellman

	 ✅ 🌿 Tree  revision verified
  

 ✅ All revisions verified successfully


```

### verify_ignore_merkle_example-form.json ✅ PASS

**Command:** `./dist/aqua.js verify example-form.json.aqua.json --ignore-merkle-proof`
**Timestamp:** 2025-06-12T15:11:22.422002

**Output:**
```
file name example-form.json.aqua.json
-> reading pure file example-form.json
Checking aqua file: example-form.json.aqua.json
-> reading aqua file example-form.json.aqua.json
✅ All revisions verified successfully


```

### verify_LICENSE ✅ PASS

**Command:** `./dist/aqua.js verify LICENSE.aqua.json`
**Timestamp:** 2025-06-12T15:11:22.687226

**Output:**
```
file name LICENSE.aqua.json
-> reading pure file ./LICENSE
Checking aqua file: ./LICENSE.aqua.json
-> reading aqua file ./LICENSE.aqua.json
-> reading pure file example-form.json
Checking aqua file: example-form.json.aqua.json
-> reading aqua file example-form.json.aqua.json
✅ All revisions verified successfully


```

### verify_verbose_LICENSE ✅ PASS

**Command:** `./dist/aqua.js verify LICENSE.aqua.json -v`
**Timestamp:** 2025-06-12T15:11:22.952236

**Output:**
```
file name LICENSE.aqua.json
-> reading pure file ./LICENSE
Checking aqua file: ./LICENSE.aqua.json
-> reading aqua file ./LICENSE.aqua.json
-> reading pure file example-form.json
Checking aqua file: example-form.json.aqua.json
-> reading aqua file example-form.json.aqua.json
 ➡️  1.Verifying Revision: 0xd2d0207144043d6d23153dd1f48515670c22ab42cf4e38102180c901f1051b30
	 📄 Type: File.
	 ✅ ⏺️  Scalar revision verified
  

 ➡️  2.Verifying Revision: 0x17e5d1c6e79f299d6cde34417e413cfe86cded18f1b85f8e...
```

### verify_ignore_merkle_LICENSE ✅ PASS

**Command:** `./dist/aqua.js verify LICENSE.aqua.json --ignore-merkle-proof`
**Timestamp:** 2025-06-12T15:11:23.223512

**Output:**
```
file name LICENSE.aqua.json
-> reading pure file ./LICENSE
Checking aqua file: ./LICENSE.aqua.json
-> reading aqua file ./LICENSE.aqua.json
-> reading pure file example-form.json
Checking aqua file: example-form.json.aqua.json
-> reading aqua file example-form.json.aqua.json
✅ All revisions verified successfully


```

### verify_test_modify_file.txt ✅ PASS

**Command:** `./dist/aqua.js verify test_modify_file.txt.aqua.json`
**Timestamp:** 2025-06-12T15:11:23.418247

**Output:**
```
file name test_modify_file.txt.aqua.json
-> reading pure file test_modify_file.txt
Checking aqua file: test_modify_file.txt.aqua.json
-> reading aqua file test_modify_file.txt.aqua.json
	 ❌ Error verifying revision type:file with hash 0x4dbced08be6848b62514e14ef5636ecac76d9d710c8f65b0126ad97a5dd2a71c - 
 isSuccess false - isScalarSuccess true 


```

### verify_verbose_test_modify_file.txt ✅ PASS

**Command:** `./dist/aqua.js verify test_modify_file.txt.aqua.json -v`
**Timestamp:** 2025-06-12T15:11:23.642119

**Output:**
```
file name test_modify_file.txt.aqua.json
-> reading pure file test_modify_file.txt
Checking aqua file: test_modify_file.txt.aqua.json
-> reading aqua file test_modify_file.txt.aqua.json
 ➡️  1.Verifying Revision: 0x4dbced08be6848b62514e14ef5636ecac76d9d710c8f65b0126ad97a5dd2a71c
	 📄 Type: File.
	 ❌ Error verifying revision type:file with hash 0x4dbced08be6848b62514e14ef5636ecac76d9d710c8f65b0126ad97a5dd2a71c - 
 isSuccess false - isScalarSuccess true 
  

 ❌ One or more revision verification fai...
```

### verify_ignore_merkle_test_modify_file.txt ✅ PASS

**Command:** `./dist/aqua.js verify test_modify_file.txt.aqua.json --ignore-merkle-proof`
**Timestamp:** 2025-06-12T15:11:23.849620

**Output:**
```
file name test_modify_file.txt.aqua.json
-> reading pure file test_modify_file.txt
Checking aqua file: test_modify_file.txt.aqua.json
-> reading aqua file test_modify_file.txt.aqua.json
	 ❌ Error verifying revision type:file with hash 0x4dbced08be6848b62514e14ef5636ecac76d9d710c8f65b0126ad97a5dd2a71c - 
 isSuccess false - isScalarSuccess true 


```

### verify_test_fresh_file.txt ✅ PASS

**Command:** `./dist/aqua.js verify test_fresh_file.txt.aqua.json`
**Timestamp:** 2025-06-12T15:11:24.036125

**Output:**
```
file name test_fresh_file.txt.aqua.json
-> reading pure file test_fresh_file.txt
Checking aqua file: test_fresh_file.txt.aqua.json
-> reading aqua file test_fresh_file.txt.aqua.json
✅ All revisions verified successfully


```

### verify_verbose_test_fresh_file.txt ✅ PASS

**Command:** `./dist/aqua.js verify test_fresh_file.txt.aqua.json -v`
**Timestamp:** 2025-06-12T15:11:24.272531

**Output:**
```
file name test_fresh_file.txt.aqua.json
-> reading pure file test_fresh_file.txt
Checking aqua file: test_fresh_file.txt.aqua.json
-> reading aqua file test_fresh_file.txt.aqua.json
 ➡️  1.Verifying Revision: 0xf3cc25d4f3cf6c46f1e02f2eace7c1fd711a10dc5134f1608fbdd7d7f288568e
	 📄 Type: File.
	 ✅ ⏺️  Scalar revision verified
  

 ✅ All revisions verified successfully


```

### verify_ignore_merkle_test_fresh_file.txt ✅ PASS

**Command:** `./dist/aqua.js verify test_fresh_file.txt.aqua.json --ignore-merkle-proof`
**Timestamp:** 2025-06-12T15:11:24.467862

**Output:**
```
file name test_fresh_file.txt.aqua.json
-> reading pure file test_fresh_file.txt
Checking aqua file: test_fresh_file.txt.aqua.json
-> reading aqua file test_fresh_file.txt.aqua.json
✅ All revisions verified successfully


```

### verify_test_content_file.txt ✅ PASS

**Command:** `./dist/aqua.js verify test_content_file.txt.aqua.json`
**Timestamp:** 2025-06-12T15:11:24.690308

**Output:**
```
file name test_content_file.txt.aqua.json
✅ All revisions verified successfully


```

**Error:**
```
✓ File test_content_file.txt skipped: content already exists in revision 0xf3018933704bf58334b0946484b21d160bc4bd8828a52526885d9153881f6ef6

```

### verify_verbose_test_content_file.txt ✅ PASS

**Command:** `./dist/aqua.js verify test_content_file.txt.aqua.json -v`
**Timestamp:** 2025-06-12T15:11:24.884227

**Output:**
```
file name test_content_file.txt.aqua.json
 ➡️  1.Verifying Revision: 0xf3018933704bf58334b0946484b21d160bc4bd8828a52526885d9153881f6ef6
	 📄 Type: File.
	 ✅ ⏺️  Scalar revision verified
  

 ✅ All revisions verified successfully


```

**Error:**
```
✓ File test_content_file.txt skipped: content already exists in revision 0xf3018933704bf58334b0946484b21d160bc4bd8828a52526885d9153881f6ef6

```

### verify_ignore_merkle_test_content_file.txt ✅ PASS

**Command:** `./dist/aqua.js verify test_content_file.txt.aqua.json --ignore-merkle-proof`
**Timestamp:** 2025-06-12T15:11:25.149745

**Output:**
```
file name test_content_file.txt.aqua.json
✅ All revisions verified successfully


```

**Error:**
```
✓ File test_content_file.txt skipped: content already exists in revision 0xf3018933704bf58334b0946484b21d160bc4bd8828a52526885d9153881f6ef6

```

## Test Suite Results

### make_test ❌ FAIL

**Command:** `make test`
**Timestamp:** 2025-06-12T15:11:50.693314

**Output:**
```
cd tests && ./test-content-revision.sh  -v
Current Path: /Users/tetra/Documents/GitHub/aqua-js-cli/tests
expecting success: 
	ln -s $(git rev-parse --show-toplevel) ./repo
	cp repo/README.md README.md

ok 1 - Setup test environment

expecting success: 
    $notarize README.md --content &&
    test -f README.md.aqua.json

- Writing new file revision 0x0a9006626d9d46ac277c80765b2e2f223c6298b05451db516dbdd1e83cf2e7e3 to README.md.aqua.json
ok 2 - Create initial AQUA file for README with content par...
```

**Error:**
```
make: *** [tests/test-witness.sh] Error 1

```

### test-forms ✅ PASS

**Command:** `./test-forms.sh`
**Timestamp:** 2025-06-12T15:11:52.673646

**Output:**
```
ok 1 - Setup test environment
ok 2 - Verify test files exist
ok 3 - Notarize initial form
ok 4 - Notarize attestation form
ok 5 - Verify initial form
ok 6 - Delete date_of_birth field
ok 7 - Verify after deletion
ok 8 - Update date_of_birth field
ok 9 - Final verification
ok 10 - Cleanup test files
# passed all 10 test(s)
1..10

```

### test-content-revision ✅ PASS

**Command:** `./test-content-revision.sh`
**Timestamp:** 2025-06-12T15:11:53.139855

**Output:**
```
Current Path: /Users/tetra/Documents/GitHub/aqua-js-cli/tests
ok 1 - Setup test environment
ok 2 - Create initial AQUA file for README with content parameter
ok 3 - Check README.md.aqua.json contains a content
ok 4 - Check README.md.aqua.json contains a content
# passed all 4 test(s)
1..4

```

### test-linking ✅ PASS

**Command:** `./test-linking.sh`
**Timestamp:** 2025-06-12T15:11:55.206244

**Output:**
```
ok 1 - Setup test environment
ok 2 - Create AQUA file for README.md
ok 3 - Create AQUA file for LICENSE
ok 4 - Create AQUA file for notarize.ts
ok 5 - Create link between files
ok 6 - Verify linked README.md
ok 7 - Cleanup test files
# passed all 7 test(s)
1..7

```

### test-file-revisions ✅ PASS

**Command:** `./test-file-revisions.sh`
**Timestamp:** 2025-06-12T15:11:56.212274

**Output:**
```
Current Path: /Users/tetra/Documents/GitHub/aqua-js-cli/tests
ok 1 - Setup test environment
ok 2 - Copy README.md to README2.md
ok 3 - Create initial AQUA file for README
ok 4 - Modify README.md content by removing first character
ok 5 - Notarize modified README.md
ok 6 - Verify README.md after all modifications
ok 7 - Cleanup test files
# passed all 7 test(s)
1..7

```

### test-signing ✅ PASS

**Command:** `./test-signing.sh`
**Timestamp:** 2025-06-12T15:11:58.120121

**Output:**
```
ok 1 - Setup test environment
ok 2 - Check README.md
ok 3 - Create AQUA file for README.md
ok 4 - Sign README.md
ok 5 - Check notarize.ts
ok 6 - Create AQUA file for notarize.ts
ok 7 - Witness notarize.ts.aqua.json
ok 8 - Cleanup test files
# passed all 8 test(s)
1..8

```

### test-witness ❌ FAIL

**Command:** `./test-witness.sh`
**Timestamp:** 2025-06-12T15:12:14.485553

**Output:**
```
ok 1 - Setup test environment
ok 2 - Check README.md
ok 3 - Create AQUA file for README.md
ok 4 - Witness README.md
ok 5 - Verify witnessed README.md
ok 6 - Remove revision from README.md
ok 7 - Check notarize.ts
ok 8 - Create AQUA file for notarize.ts
ok 9 - Witness notarize.ts TSA
ok 10 - Verify notarize.ts
ok 11 - Check LICENSE
ok 12 - Create AQUA file for LICENSE
ok 13 - Create AQUA file for formatter.ts
not ok 14 - Create AQUA file for README.md
#	
#	    $notarize README.md &&
#	    test -f...
```

### test-verify ✅ PASS

**Command:** `./test-verify.sh`
**Timestamp:** 2025-06-12T15:12:14.942403

**Output:**
```
ok 1 - Setup test environment
ok 2 - Check README.md
ok 3 - Create AQUA file for README.md
ok 4 - Verify the output of verify.js
ok 5 - Cleanup test files
# passed all 5 test(s)
1..5

```

