"""Guides: hand-written articles in content/guides/{en,ko}/<slug>.html, published in content/guides/PUBLISHED.txt order.

Source format (from hyunhp/blogger-publisher guides/, which wrote them for Blogger): header comment lines
(`<!-- Tags: ... -->`, `<!-- Tistory post title: ... -->`, `<!-- Cover: ... -->`, `<!-- lang: xx -->`), then HTML with
inline styles. Rendering drops every comment line, turns the old blog label links into cert-bank links, and replaces the
blog's practice section (the last h2 whose section links blog labels) with links into the question bank.
The prose is edited in the source files themselves (cert-bank owns its copies).
"""
import html, re, urllib.parse

KINDS = {"en": [("guide-", "Study guides"), ("compare-", "Comparisons"), ("mistakes-", "Common mistakes")],
         "ko": [("guide-", "학습 가이드"), ("compare-", "개념 비교"), ("mistakes-", "자주 하는 실수")]}
TXT = {
    "en": {"read_other": "이 글을 한국어로 읽기", "practise_p": "Practise in the question bank: every question explains each "
           "option, right and wrong. Start with the domain you just studied, then take a timed mock exam.",
           "page": "{code} exam page", "all": "All {n:,} {code} questions", "mock": "Timed mock exam",
           "plan": "{days}-day study plan", "by_dom": "By domain", "list_h1": "Guides", "read": "Read the guide",
           "list_lead": "Hand-written guides to certification exams: what each exam really asks, a study order, and the "
                        "traps that cost the most points. Every guide links to the practice questions for its exam.",
           "guides_h2": "Guides for this exam"},
    "ko": {"read_other": "Read this guide in English", "practise_p": "문제은행에서 연습하십시오. 모든 문제에 정답과 오답 보기마다 "
           "해설이 있습니다. 방금 공부한 도메인부터 시작하고, 그다음 시간 제한이 있는 모의고사를 보십시오.",
           "page": "{code} 시험 안내", "all": "{code} 문제 전체 {n:,}개", "mock": "시간 제한 모의고사",
           "plan": "{days}일 학습 계획", "by_dom": "도메인별", "list_h1": "가이드", "read": "가이드 읽기",
           "list_lead": "자격증 시험을 위해 직접 쓴 가이드입니다. 시험이 실제로 묻는 것, 학습 순서, 점수를 가장 많이 잃는 함정을 "
                        "정리했고, 가이드마다 해당 시험의 연습 문제로 이어집니다.",
           "guides_h2": "Guides for this exam"},
}
VENDOR_LABEL = {"AWS": "aws", "Palantir": "palantir", "Azure": "azure", "Microsoft Azure": "azure",
                "Google Cloud": "gcp", "Databricks": "databricks", "HashiCorp": "hashicorp"}


def norm(name):
    """Domain names as blog labels lost commas and used '&' ('Security & Compliance and Governance')."""
    return re.sub(r"\b(and|&)\b|[^a-z0-9]+", " ", name.lower().replace("&", " and ")).split()


def parse(text):
    meta = dict(re.findall(r"^<!-- ([A-Za-z ]+): (.*?) -->$", text, re.M))
    body = "\n".join(l for l in text.split("\n") if not l.lstrip().startswith("<!--")).strip()
    return meta, body


class Guides:
    def __init__(self, root, specs, bank_count, study_days, load_text):
        self.specs, self.bank_count, self.study_days = specs, bank_count, study_days
        order = [l.strip() for l in load_text("content/guides/PUBLISHED.txt").split("\n") if l.strip() and not l.startswith("#")]
        self.items = []
        for slug in order:
            g = {"slug": slug, "lang": {}}
            for lang in ("en", "ko"):
                try:
                    meta, body = parse(load_text(f"content/guides/{lang}/{slug}.html"))
                except FileNotFoundError:
                    continue
                g["lang"][lang] = {"title": meta["Tistory post title"], "body": body, "tags": meta.get("Tags", "")}
            tags = [t.strip() for t in g["lang"]["en"]["tags"].split(",")]
            g["exams"] = [t for t in tags if t in specs]
            g["vendors"] = [VENDOR_LABEL[t] for t in tags if t in VENDOR_LABEL]
            self.items.append(g)

    def path(self, slug, lang):
        return ("ko/" if lang == "ko" else "") + f"guides/{slug}/"

    def for_exam(self, code):
        return [g for g in self.items if code in g["exams"]]

    # -------------------------------------------------------- links
    def label_href(self, label, exams, up):
        label = urllib.parse.unquote(label)
        if label in self.specs:
            return f"{up}exams/{label.lower()}/"
        want = norm(label)
        for code in exams or list(self.specs):
            for d in self.specs[code]["domains"]:
                if norm(d["name"]) == want:
                    return f"{up}#exam={code}&amp;d={d['code']}"
        if label in VENDOR_LABEL:
            return f"{up}exams/#{VENDOR_LABEL[label]}"
        return f"{up}guides/"

    def practice(self, lang, exams, up, intro=True):
        t = TXT[lang]
        out = [f"<p>{t['practise_p']}</p>"] if intro else []
        out.append("<ul>")
        for code in exams:
            n = self.bank_count(code)
            days = self.study_days(code)
            parts = [f'<a href="{up}exams/{code.lower()}/">{t["page"].format(code=code)}</a>',
                     f'<a href="{up}#exam={code}">{t["all"].format(code=code, n=n)}</a>',
                     f'<a href="{up}#mock={code}">{t["mock"]}</a>']
            if days:
                parts.append(f'<a href="{up}study.html#exam={code}">{t["plan"].format(days=days)}</a>')
            out.append("<li>" + " · ".join(parts) + "</li>")
            doms = " · ".join(f'<a href="{up}#exam={code}&amp;d={d["code"]}">{html.escape(d["name"])}</a>'
                              for d in self.specs[code]["domains"])
            out.append(f"<li>{t['by_dom']}{' (' + code + ')' if len(exams) > 1 else ''}: {doms}</li>")
        return out

    def render_body(self, g, lang, up):
        """The blog's practice list (the last <ul> of blog label links) becomes question bank links. Items that say more
        than a label (e.g. "Patterns 2, 4 and 5: Design Secure Architectures") are kept, pointing into the bank.
        If the list stood alone under its heading, a short intro paragraph goes before it."""
        body = g["lang"][lang]["body"]
        exams = g["exams"]
        lists = [m for m in re.finditer(r"<ul>(?:(?!</ul>).)*search/label/(?:(?!</ul>).)*</ul>", body, re.S)]
        if lists:
            m = lists[-1]
            keep = [li for li in re.findall(r"<li>.*?</li>", m.group(0), re.S)
                    if re.search(r"<a [^>]*>[^<]*:\s", li)]
            before = body[:m.start()]
            alone = bool(re.search(r"</h2>\s*$", before))
            new = self.practice(lang, exams, up, intro=alone) + keep + ["</ul>"]
            body = before + "\n".join(new) + body[m.end():]
        body = re.sub(r'href="https://bigdatabreakthroughs\.blogspot\.com/search/label/([^"]+)"',
                      lambda m: f'href="{self.label_href(m.group(1), exams, up)}"', body)
        assert "blogspot.com" not in body, f"{g['slug']} ({lang}): a blog link is left"
        return body

    def description(self, body, lang="en"):
        first = re.search(r"<p>(.*?)</p>", body, re.S).group(1)
        text = html.unescape(re.sub(r"<[^>]+>", "", first)).strip()
        cap = 160 if lang == "en" else 110   # Korean packs more meaning per character
        if len(text) > cap:
            text = text[:cap - 3].rsplit(" ", 1)[0].rstrip(",;:.") + "…"
        return text
