"""Put a diagram into each guide: HTML with inline styles, drawn from a small JSON spec, so it reflows on phones,
stays readable at any width and its text counts as content. (A 1200 px image shrinks to unreadable text on a phone.)

    python3 tools/site/make_diagrams.py            # insert or refresh the figure of every guide that has a spec
    python3 tools/site/make_diagrams.py --check    # validate the specs, change nothing

Specs live in content/guides/diagrams/<guide id>.json (English guides only; the Korean figures are translated by hand). Three kinds, chosen for what the guide explains:

    {"kind": "flow", "title": "...", "steps": [{"title": "...", "note": "..."}, ...], "before": "...", "caption": "..."}
        Ordered stages (study order, a pipeline, a request's path). Cards wrap: three a row on desktop, one on phones.
    {"kind": "decide", "title": "...", "questions": [{"ask": "...", "yes": "..."}, ...], "otherwise": "...", ...}
        A decision ladder: the first question answered yes gives the answer; "otherwise" ends the ladder.
    {"kind": "layers", "title": "...", "layers": [{"name": "...", "items": ["...", ...]}, ...], ...}
        Stacked bands from top to bottom (a hierarchy, a stack, layers of control).

"before" is the text of the <h2> or <h3> the figure goes in front of. The figure sits between the comment lines
<!-- figure --> and <!-- /figure -->, so running this again replaces it instead of adding a second one.
"""
import argparse
import glob
import html
import json
import os
import re
import sys

HERE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
GUIDES = os.path.join(HERE, 'content', 'guides', 'en')
SPECS = os.path.join(HERE, 'content', 'guides', 'diagrams')
INK, MUTED, VIOLET, AMBER = '#1c1b29', '#5d5a72', '#5b4b9e', '#c9952e'
BOX = 'border-radius:12px;padding:12px 14px;box-sizing:border-box'
KINDS = {'flow': 'steps', 'decide': 'questions', 'layers': 'layers'}
START, END = '<!-- figure -->', '<!-- /figure -->'
e = html.escape


def flow(spec):
    cards = []
    for i, s in enumerate(spec['steps'], 1):
        dot = AMBER if i == 1 else VIOLET
        cards.append(
            f'<div style="flex:1 1 200px;{BOX};background:#fff;border:1px solid #d9d4ec">'
            f'<div style="display:inline-block;width:26px;height:26px;line-height:26px;border-radius:50%;background:{dot};'
            f'color:#fff;text-align:center;font-weight:700;font-size:14px">{i}</div>'
            f'<div style="margin:6px 0 2px;font-weight:700;color:{INK}">{e(s["title"])}</div>'
            f'<div style="font-size:14px;line-height:1.5;color:{MUTED}">{e(s.get("note", ""))}</div></div>')
    return '<div style="display:flex;flex-wrap:wrap;gap:10px">' + ''.join(cards) + '</div>'


def decide(spec):
    rows = []
    for q in spec['questions']:
        rows.append(
            '<div style="display:flex;flex-wrap:wrap;gap:8px;align-items:stretch">'
            f'<div style="flex:3 1 260px;{BOX};background:#fff;border:2px solid {VIOLET};color:{INK}">{e(q["ask"])}</div>'
            f'<div style="flex:2 1 180px;{BOX};background:#fbf3e2;border:1px solid {AMBER};color:{INK}">'
            f'<span style="font-size:13px;font-weight:700;color:{AMBER}">YES &#8594;</span><br>'
            f'<strong>{e(q["yes"])}</strong></div></div>'
            f'<div style="margin:4px 0 4px 18px;font-size:13px;font-weight:700;color:{MUTED}">&#8595; no</div>')
    rows.append(f'<div style="{BOX};background:#fbf3e2;border:1px solid {AMBER};color:{INK}">'
                f'<span style="font-size:13px;font-weight:700;color:{AMBER}">OTHERWISE &#8594;</span><br>'
                f'<strong>{e(spec["otherwise"])}</strong></div>')
    return ''.join(rows)


def layers(spec):
    shades = ['#f1eef9', '#e8e4f5', '#ded9f1', '#d4cdec', '#c9c1e7', '#bfb6e2']
    bands = []
    for i, layer in enumerate(spec['layers']):
        items = ' · '.join(e(x) for x in layer.get('items', []))
        bands.append(
            f'<div style="display:flex;flex-wrap:wrap;gap:4px 14px;{BOX};background:{shades[i % len(shades)]};'
            f'border:1px solid #d9d4ec;margin-bottom:6px">'
            f'<div style="flex:0 1 190px;font-weight:700;color:{VIOLET}">{e(layer["name"])}</div>'
            f'<div style="flex:1 1 240px;font-size:15px;line-height:1.55;color:{INK}">{items}</div></div>')
    return ''.join(bands)


DRAW = {'flow': flow, 'decide': decide, 'layers': layers}


def figure(spec):
    """The whole figure: title, diagram, caption, between the START and END markers."""
    return (f'{START}\n<div style="margin:24px 0;padding:16px;border-radius:14px;background:#f7f6fb;border:1px solid #e4e2ee;'
            f'font-size:16px;line-height:1.5">'
            f'<div style="margin:0 0 12px;font-weight:700;font-size:17px;color:{INK}">{e(spec["title"])}</div>'
            f'{DRAW[spec["kind"]](spec)}'
            f'<div style="margin:12px 0 0;font-size:13px;color:{MUTED}">{e(spec["caption"])}</div></div>\n{END}\n')


def problems(spec, page=None):
    """What is wrong with a spec (empty list when it is fine). page: the guide's HTML, to check "before"."""
    kind = spec.get('kind')
    if kind not in KINDS:
        return ['kind must be one of %s' % ', '.join(KINDS)]
    out = ['missing ' + k for k in ('title', 'before', 'caption', KINDS[kind]) if not spec.get(k)]
    n = len(spec.get(KINDS[kind]) or [])
    if not 2 <= n <= 7:
        out.append('%s: 2 to 7 entries, not %d' % (KINDS[kind], n))
    if kind == 'decide' and not spec.get('otherwise'):
        out.append('missing otherwise')
    if page is not None and spec.get('before') and not anchor(page, spec['before']):
        out.append('no <h2>/<h3> "%s" in the guide' % spec['before'])
    return out


def anchor(page, heading):
    """Position of the <h2>/<h3> whose text is `heading`, or None."""
    for m in re.finditer(r'<h[23][^>]*>(.*?)</h[23]>', page):
        if html.unescape(re.sub('<[^>]+>', '', m.group(1))).strip() == heading.strip():
            return m.start()
    return None


def insert(page, spec):
    """The guide's HTML with its figure in front of spec["before"] (an older figure is taken out first)."""
    page = re.sub(re.escape(START) + r'.*?' + re.escape(END) + r'\n?', '', page, flags=re.S)
    at = anchor(page, spec['before'])
    return page[:at] + figure(spec) + page[at:]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()
    changed, bad = 0, 0
    for path in sorted(glob.glob(os.path.join(SPECS, '*.json'))):
        gid = os.path.basename(path)[:-5]
        page_path = os.path.join(GUIDES, gid + '.html')
        with open(path, encoding='utf-8') as f:
            spec = json.load(f)
        page = open(page_path, encoding='utf-8').read() if os.path.exists(page_path) else ''
        errs = problems(spec, page) if page else ['no guide ' + gid]
        if errs:
            bad += 1
            print('%s: %s' % (gid, '; '.join(errs)), file=sys.stderr)
            continue
        new = insert(page, spec)
        if new != page and not args.check:
            with open(page_path, 'w', encoding='utf-8') as f:
                f.write(new)
            changed += 1
    print('%d guides updated, %d specs with problems' % (changed, bad))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
