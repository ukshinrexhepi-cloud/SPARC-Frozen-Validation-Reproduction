from pathlib import Path
import hashlib
import re
import sys

ROOT = Path(__file__).resolve().parent
SUMS = ROOT / "SHA256SUMS.txt"

def sha256_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()

failures = []
count = 0
for line in SUMS.read_text(encoding="utf-8").splitlines():
    match = re.match(r"^([0-9a-f]{64})  (.+)$", line)
    if match is None:
        continue
    count += 1
    expected = match.group(1)
    path = ROOT / match.group(2)
    if not path.is_file():
        failures.append(f"MISSING: {path.relative_to(ROOT)}")
    elif sha256_file(path) != expected:
        failures.append(f"HASH MISMATCH: {path.relative_to(ROOT)}")

print("Checked files:", count)
if failures:
    print("STATUS: FAIL")
    for item in failures:
        print("-", item)
    sys.exit(1)
print("STATUS: PASS")
