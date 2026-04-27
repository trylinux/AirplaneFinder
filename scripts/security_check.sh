#!/usr/bin/env bash
# Pre-deploy security audit.
#
# Run from the project root (or from anywhere — the script cd's to the
# project root itself):
#
#     bash scripts/security_check.sh
#
# Wire this into whatever deploy flow you have:
#   - manual:           run before each `git pull && systemctl restart …`
#   - GitHub Actions:   step `- run: bash scripts/security_check.sh`
#   - Makefile target:  `audit:` rule
#
# Exit code 0 = clean, non-zero = something to look at before deploying.

set -euo pipefail

# Move to project root regardless of where the user invoked this from.
cd "$(dirname "${BASH_SOURCE[0]}")/.."

REQS=requirements.txt

if [[ ! -f "$REQS" ]]; then
    echo "ERROR: $REQS not found (run from project root)" >&2
    exit 2
fi

echo "════════════════════════════════════════════════════════"
echo "  Security audit  ($(date -u +%Y-%m-%dT%H:%M:%SZ))"
echo "════════════════════════════════════════════════════════"

# ── pip-audit ────────────────────────────────────────────────
# pip-audit checks every pinned package against the Python Packaging
# Advisory Database (PyPI vulnerabilities) and reports CVEs by severity.
# We install it on demand into a throwaway venv so the app's own venv
# stays clean — pip-audit doesn't need to be a runtime dependency.

echo
echo "→ Running pip-audit on $REQS"
echo "  (CVE check against PyPI Advisory Database)"
echo

if command -v pip-audit >/dev/null 2>&1; then
    # User has it globally (via pipx or a separate venv). Just use it.
    pip-audit -r "$REQS" --strict
else
    # No global pip-audit. Spin up a temp venv just for this run.
    echo "  pip-audit not installed globally — using a one-shot temp venv."
    AUDIT_VENV="$(mktemp -d)/audit-venv"
    python3 -m venv "$AUDIT_VENV"
    # shellcheck disable=SC1091
    "$AUDIT_VENV/bin/pip" install --quiet --upgrade pip pip-audit
    "$AUDIT_VENV/bin/pip-audit" -r "$REQS" --strict
    rm -rf "$AUDIT_VENV"
fi

# ── Outdated package summary ─────────────────────────────────
# Optional: if there's a project venv at .venv, list packages with newer
# versions available. Doesn't fail the audit — just gives visibility.

echo
echo "→ Outdated packages in .venv (informational only)"
echo

if [[ -x ".venv/bin/pip" ]]; then
    .venv/bin/pip list --outdated --format=columns || true
else
    echo "  (no .venv/bin/pip found — skipping outdated check)"
fi

echo
echo "════════════════════════════════════════════════════════"
echo "  Audit complete. Review findings above before deploying."
echo "════════════════════════════════════════════════════════"
