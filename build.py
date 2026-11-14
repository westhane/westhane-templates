#!/usr/bin/env python3
"""Pack plugins/westhane/WesthaneTemplates into dist/WesthaneTemplates.json.

The output is a JSON array holding one plugin tiddler; drag it onto a
TiddlyWiki to install or upgrade. No Node.js needed. (With Node TiddlyWiki
installed, the plugin folder also loads directly from a wiki's plugins/.)
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PLUGIN = ROOT / "plugins" / "westhane" / "WesthaneTemplates"


def read_tid(path):
    head, _, text = path.read_text(encoding="utf-8").partition("\n\n")
    fields = {}
    for line in head.splitlines():
        key, _, value = line.partition(": ")
        fields[key] = value
    fields["text"] = text
    return fields


def main():
    info = json.loads((PLUGIN / "plugin.info").read_text(encoding="utf-8"))
    tiddlers = {}
    for tid in sorted(PLUGIN.rglob("*.tid")):
        t = read_tid(tid)
        title = t.pop("title")
        if title in tiddlers:
            raise SystemExit(f"duplicate title {title} in {tid}")
        tiddlers[title] = t
    plugin = dict(info, type="application/json",
                  text=json.dumps({"tiddlers": tiddlers}, ensure_ascii=False))
    out = ROOT / "dist" / f"{info['name']}.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps([plugin], ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{out.relative_to(ROOT)}: {len(tiddlers)} tiddlers, v{info['version']}")


if __name__ == "__main__":
    main()
