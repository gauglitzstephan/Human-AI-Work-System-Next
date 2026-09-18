"""Bounded integrity verification; no assertion of behavior or deployment."""
from pathlib import Path
import hashlib
import json
import re
import sys
import yaml

here = Path(__file__).resolve().parent
root = here.parents[1]
manifest = json.loads((here / 'source_manifest.json').read_text())
base_paths = set(manifest['base_paths'])
errors = []
checked = []

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

for rel, identity in manifest['candidate_sources'].items():
    p = root / rel
    if not p.is_file() or digest(p) != identity['sha256']:
        errors.append('Candidate source identity mismatch: ' + rel)
    checked.append(rel)

skill = root / 'skills/system-development/SKILL.md'
front = yaml.safe_load(skill.read_text().split('---', 2)[1])
if front.get('name') != 'system-development' or not isinstance(front.get('description'), str):
    errors.append('Invalid skill metadata')
if len(front.get('description', '')) > 1024:
    errors.append('Description exceeds 1024 characters')

links = 0
for rel in manifest['candidate_sources']:
    p = root / rel
    if p.suffix != '.md':
        continue
    for link in re.findall(r'\]\(([^)]+)\)', p.read_text()):
        if '://' in link or link.startswith('#'):
            continue
        target = (p.parent / link.split('#')[0]).resolve()
        try:
            target_rel = str(target.relative_to(root))
        except ValueError:
            errors.append('Link escapes repository: ' + rel + ': ' + link)
            continue
        if not target.exists() and target_rel not in base_paths:
            errors.append('Unresolved link: ' + rel + ': ' + link)
        links += 1

for rel, expected in manifest['protected_local_sources'].items():
    if digest(root / rel) != expected:
        errors.append('Protected source changed: ' + rel)

package = json.loads((root / '.codex-plugin/plugin.json').read_text())
if package['version'] != '0.2.3' or package['skills'] != './skills/':
    errors.append('Package version or skill location mismatch')

packet = json.loads((here / 'evidence_manifest.json').read_text())
for rel, expected in packet.items():
    if digest(here / rel) != expected:
        errors.append('Evidence artifact changed: ' + rel)

result = {'status': 'PASS' if not errors else 'FAIL',
          'candidate_source_files': len(checked), 'resolved_links': links,
          'evidence_files': len(packet), 'errors': errors,
          'claim_limit': 'Source/packet identity and link integrity only; no behavior, selection, installation or outcome claim.'}
print(json.dumps(result, indent=2))
sys.exit(bool(errors))
