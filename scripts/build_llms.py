#!/usr/bin/env python3
"""Build llms.txt / llms-full.txt for AI crawlers (llmstxt.org convention).

Usage:
    python scripts/build_llms.py [site_dir]

Reads mkdocs.yml nav + docs/*.md frontmatter, writes:
    <site_dir>/llms.txt       curated index, one line per chapter
    <site_dir>/llms-full.txt  full book concatenated in nav order
"""
import re
import sys
import pathlib
import urllib.parse

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://caozhiyi.cc/network-book/"
REPO = "https://github.com/caozhiyi/network-book"

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)


class _L(yaml.SafeLoader):
    """SafeLoader that tolerates mkdocs' !!python/name: tags."""

    pass


_L.add_multi_constructor(
    "tag:yaml.org,2002:python/name:",
    lambda loader, suffix, node: suffix,
)


def load_meta(rel):
    raw = (ROOT / "docs" / rel).read_text(encoding="utf-8")
    m = FM_RE.match(raw)
    meta = yaml.load(m.group(1), Loader=_L) if m else {}
    return meta or {}, (raw[m.end():] if m else raw)


def page_url(rel):
    slug = rel.rsplit(".", 1)[0]
    if slug == "index":
        return SITE
    return SITE + urllib.parse.quote(slug) + "/"


def iter_nav(nav, depth=1):
    """Yield (kind, title, value, depth): kind in {'section', 'page'}."""
    for item in nav:
        if isinstance(item, str):
            yield "page", None, item, depth
            continue
        (title, val), = item.items()
        if isinstance(val, list):
            yield "section", title, val, depth
        else:
            yield "page", title, val, depth


def chapter_title(meta, nav_title, rel):
    return meta.get("seo_title") or meta.get("title") or nav_title or pathlib.Path(rel).stem


def build_index(nav):
    lines = [
        "# 云网络：从隔离到连接 (Cloud Network: From Isolation to Connection)",
        "",
        "> 一本讲透云网络的开源书。每个云产品，都是对一个真实约束的回答：从物理网络与数据中心、",
        "> VLAN/VxLAN 多租户隔离、VPC 内部通信、公网接入与负载均衡，到 VPC 互联、混合云专线、",
        "> 全球加速、DDoS/WAF 安全防护与可观测治理。作者：曹智轶 (caozhiyi)。",
        "",
        "## 基本信息",
        "",
        f"- 在线阅读: {SITE}",
        f"- GitHub 源码: {REPO}",
        "- 许可协议: CC BY-NC-SA 4.0",
        "- 语言: 简体中文",
        "",
        "## 全书目录",
    ]

    def walk(items, depth):
        nonlocal lines
        for kind, title, val, _ in iter_nav(items, depth):
            if kind == "section":
                lines += ["", f"{'#' * (depth + 2)} {title}"]
                walk(val, depth + 1)
                continue
            meta, _ = load_meta(val)
            t = chapter_title(meta, title, val)
            d = meta.get("description")
            lines.append(f"- [{t}]({page_url(val)}): {d}" if d else f"- [{t}]({page_url(val)})")

    walk(nav, 1)
    return "\n".join(lines) + "\n"


def build_full(nav):
    parts = [
        "# 云网络：从隔离到连接 (Cloud Network: From Isolation to Connection)",
        "",
        f"> 全文合并版。在线版: {SITE} · 源码: {REPO} · CC BY-NC-SA 4.0",
    ]
    for kind, title, val, depth in iter_nav(nav):
        if kind == "section":
            parts += ["", f"{'#' * 2} {title}"]
            parts += build_full_section(val)
        else:
            meta, body = load_meta(val)
            t = chapter_title(meta, title, val)
            parts += ["", f"{'#' * 3} {t}", "", f"[在线阅读: {page_url(val)}]", "", body.rstrip()]
    return "\n".join(parts) + "\n"


def build_full_section(pages):
    out = []
    for kind, title, val, _ in iter_nav(pages):
        if kind == "section":
            continue
        meta, body = load_meta(val)
        t = chapter_title(meta, title, val)
        out += ["", f"{'#' * 3} {t}", "", f"[在线阅读: {page_url(val)}]", "", body.rstrip()]
    return out


def main():
    out_dir = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ROOT / "site")
    out_dir.mkdir(parents=True, exist_ok=True)
    cfg = yaml.load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"), Loader=_L)
    nav = cfg["nav"]
    idx = build_index(nav)
    full = build_full(nav)
    (out_dir / "llms.txt").write_text(idx, encoding="utf-8")
    (out_dir / "llms-full.txt").write_text(full, encoding="utf-8")
    print(f"llms.txt {len(idx)//1024}KB, llms-full.txt {len(full)//1024}KB -> {out_dir}")


if __name__ == "__main__":
    main()
