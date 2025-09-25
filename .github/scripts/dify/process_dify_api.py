"""GitHub Action helper to push changed files into a Dify workflow."""

from __future__ import annotations

import json
import mimetypes
import os
import sys
from pathlib import Path
from typing import Iterable, List, Optional


EXCLUDED_PREFIXES = (
    "build/",
    ".prompt/",
    ".gitbook/",
    ".github/",
)
EXCLUDED_DIRS = {"build", ".prompt", ".gitbook", ".github"}
EXCLUDED_NAMES = {"README.md", "SUMMARY.md"}


def load_requests():
    try:
        import requests  # type: ignore
    except ImportError as exc:  # pragma: no cover
        print("The 'requests' package is required to call the Dify API.", file=sys.stderr)
        raise SystemExit(1) from exc
    return requests


def should_skip(path: str) -> bool:
    normalized = path.strip().replace("\\", "/")
    print(f"normalized: {normalized}")
    if not normalized:
        return True
    root_segment = normalized.split("/", 1)[0]
    if root_segment + "/" in EXCLUDED_PREFIXES:
        return True
    if normalized.startswith(EXCLUDED_PREFIXES):
        return True
    parts = [segment for segment in normalized.split("/") if segment]
    if any(segment in EXCLUDED_DIRS for segment in parts[:-1]):
        return True
    if Path(normalized).name in EXCLUDED_NAMES:
        return True
    return False


def gather_changed_files(raw: str) -> List[str]:
    candidates: List[str] = []
    for line in raw.splitlines():
        entry = line.strip()
        print(f"should_skip {entry} {should_skip(entry)}")
        if not entry or should_skip(entry):
            continue
        if not Path(entry).is_file():
            print(f"Skipping '{entry}' (not a file)")
            continue
        candidates.append(entry)
    return candidates


def detect_mime(path: Path) -> str:
    mime, _ = mimetypes.guess_type(path.name)
    return mime or "text/plain"


def upload_file(path: Path, user: str, api_key: str, requests_mod) -> Optional[str]:
    upload_url = os.getenv("DIFY_UPLOAD_URL", "https://ai-agent.blockpi.org/v1/files/upload")
    headers = {"Authorization": f"Bearer {api_key}"}
    mime = detect_mime(path)

    try:
        with path.open("rb") as stream:
            files = {"file": (path.name, stream, mime)}
            data = {"user": user, "type": "TXT"}
            response = requests_mod.post(
                upload_url,
                headers=headers,
                files=files,
                data=data,
                timeout=60,
            )
    except requests_mod.exceptions.RequestException as exc:
        print(f"HTTP error while uploading '{path}': {exc}")
        return None

    if response.status_code == 201:
        payload = response.json()
        file_id = payload.get("id")
        print(f"Uploaded '{path}' (id={file_id})")
        return file_id

    print(f"Failed to upload '{path}'. Status: {response.status_code}. Body: {response.text}")
    return None


def run_workflow(file_id: str, user: str, api_key: str, response_mode: str, requests_mod) -> Optional[dict]:
    workflow_url = os.getenv("DIFY_WORKFLOW_URL", "https://ai-agent.blockpi.org/v1/workflows/run")
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    payload = {
        "inputs": {
            "orig_mail": [
                {
                    "transfer_method": "local_file",
                    "upload_file_id": file_id,
                    "type": "document",
                }
            ]
        },
        "response_mode": response_mode,
        "user": user,
    }

    try:
        response = requests_mod.post(
            workflow_url,
            headers=headers,
            data=json.dumps(payload),
            timeout=60,
        )
    except requests_mod.exceptions.RequestException as exc:
        print(f"HTTP error while executing workflow for file id {file_id}: {exc}")
        return None
    if response.status_code == 200:
        print(f"Workflow executed for file id {file_id}")
        return response.json()

    print(f"Workflow failed for file id {file_id}. Status: {response.status_code}. Body: {response.text}")
    return None


def ensure_api_key(raw_key: Optional[str]) -> str:
    key = (raw_key or "app-1Gg1wuRzZyRMxaNP7iaJz6Jx").strip()
    if not key:
        print("Missing Dify API key. Set DIFY_APP_KEY or provide a non-empty default.", file=sys.stderr)
        sys.exit(1)
    return key


def process_files(files: Iterable[str], user: str, api_key: str, response_mode: str, requests_mod) -> None:
    for raw_path in files:
        path = Path(raw_path)
        print(f"Processing '{path}'")
        file_id = upload_file(path, user, api_key, requests_mod)
        if not file_id:
            continue
        result = run_workflow(file_id, user, api_key, response_mode, requests_mod)
        if result is not None:
            try:
                rendered = json.dumps(result, ensure_ascii=False)
            except (TypeError, ValueError):
                rendered = str(result)
            print(f"Workflow response: {rendered}")


def main() -> None:
    changed = os.getenv("CHANGED_FILES", "")
    if not changed.strip():
        print("No changed files provided. Exiting.")
        return

    files = gather_changed_files(changed)
    if not files:
        print("No eligible files to process after applying filters.")
        return

    api_key = ensure_api_key(os.getenv("DIFY_APP_KEY"))
    user = os.getenv("DIFY_USER", "difyuser")
    response_mode = os.getenv("DIFY_RESPONSE_MODE", "blocking")

    requests_mod = load_requests()

    print(f"::group::Modified files ({len(files)})")
    for fp in files:
        print(f" - {fp}")
    print("::endgroup::")

    process_files(files, user, api_key, response_mode, requests_mod)


if __name__ == "__main__":
    main()
