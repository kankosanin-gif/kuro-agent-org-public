#!/usr/bin/env python3
import json
from datetime import datetime
from pathlib import Path

ROOT = Path('/Users/Antares/.openclaw/workspace')


def read_text(rel):
    p = ROOT / rel
    if not p.exists():
        return ''
    return p.read_text(encoding='utf-8', errors='ignore')


def append_markdown(rel, title, body):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with p.open('a', encoding='utf-8') as f:
        f.write(f"\n## [{ts}] {title}\n{body}\n")


def already_fired(rel, hook_id, stamp):
    p = ROOT / rel
    if not p.exists():
        return False
    txt = p.read_text(encoding='utf-8', errors='ignore')
    return f"{hook_id}:{stamp}" in txt


def mark_fired(rel, hook_id, stamp):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('a', encoding='utf-8') as f:
        f.write(f"{hook_id}:{stamp}\n")


def main():
    cfg_path = ROOT / 'agent-org/hooks/hooks.json'
    state_path = 'agent-org/reports/hook-state.log'
    if not cfg_path.exists():
        return

    cfg = json.loads(cfg_path.read_text(encoding='utf-8'))
    hooks = cfg.get('hooks', [])

    for h in hooks:
        if not h.get('enabled', True):
            continue

        trigger = h.get('when', {})
        if trigger.get('type') != 'contains':
            continue

        rel = trigger.get('file')
        base_text = read_text(rel)
        if not base_text:
            continue

        must_contain = trigger.get('text', '')
        if must_contain and must_contain not in base_text:
            continue

        # Optional any-match
        any_list = h.get('if_any', [])
        if any_list and not any(t in base_text for t in any_list):
            continue

        stamp = datetime.now().strftime('%Y-%m-%d-%H')
        hook_id = h.get('id', 'unknown')
        if already_fired(state_path, hook_id, stamp):
            continue

        act = h.get('action', {})
        if act.get('type') == 'append_markdown':
            append_markdown(
                act.get('file', 'agent-org/reports/action-queue.md'),
                f"HOOK:{hook_id}",
                act.get('body', '')
            )
            mark_fired(state_path, hook_id, stamp)


if __name__ == '__main__':
    main()
