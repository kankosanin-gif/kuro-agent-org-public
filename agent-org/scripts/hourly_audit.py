#!/usr/bin/env python3
import datetime as dt
import json
import subprocess
from pathlib import Path

ROOT = Path('/Users/Antares/.openclaw/workspace')
OUT = ROOT / 'agent-org' / 'reports' / 'hourly-status.md'


def run(cmd, cwd=ROOT):
    try:
        p = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, timeout=20)
        return p.returncode, p.stdout.strip(), p.stderr.strip()
    except Exception as e:
        return 1, '', str(e)


def main():
    now = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S %Z')

    rc1, gs_out, _ = run(['git', 'status', '--short'])
    rc2, lg_out, _ = run(['git', 'log', '--oneline', '-n', '3'])

    summary = 'OK'
    if rc1 != 0 or rc2 != 0:
        summary = 'WARN: git check failed'

    lines = []
    lines.append(f'# Hourly Report — {now}')
    lines.append('')
    lines.append(f'- Topline: **{summary}**')
    lines.append('- Emergency: **None**')
    lines.append('')
    lines.append('## Git Working Tree')
    lines.append('```')
    lines.append(gs_out or '(clean)')
    lines.append('```')
    lines.append('')
    lines.append('## Recent Commits')
    lines.append('```')
    lines.append(lg_out or '(no commits)')
    lines.append('```')
    lines.append('')
    lines.append('## Next')
    lines.append('- Continue portfolio-first execution plan')
    lines.append('- Maintain boundary/security controls')

    OUT.write_text('\n'.join(lines), encoding='utf-8')

    # Trigger hook runner after each hourly report generation
    run(['python3', str(ROOT / 'agent-org' / 'hooks' / 'run_hooks.py')])


if __name__ == '__main__':
    main()
