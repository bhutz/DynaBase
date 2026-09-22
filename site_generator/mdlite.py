"""
A tiny, purpose-built Markdown-subset renderer - not a general Markdown
library (none is installed, and pulling one in for one file felt like
overkill). Handles exactly what sample_data/data_sources.md uses:
'# ' / '## ' headers, nested '-' bullet lists (2-space indent per level),
and plain paragraph lines. Nothing else is supported.
"""

import re


def render(text):
    out = []
    stack = []  # depths of currently-open <ul>s; each has one open <li> pending a close

    def close_all():
        while stack:
            out.append('</li></ul>')
            stack.pop()

    for line in text.split('\n'):
        if line.strip() == '':
            continue

        header_match = re.match(r'^(#{1,6})\s+(.*)$', line)
        bullet_match = re.match(r'^(\s*)-\s+(.*)$', line)

        if header_match:
            close_all()
            level = len(header_match.group(1))
            out.append(f'<h{level}>{escape(header_match.group(2))}</h{level}>')
            continue

        if bullet_match:
            depth = len(bullet_match.group(1)) // 2
            content = escape(bullet_match.group(2).rstrip())
            if not stack or depth > stack[-1]:
                out.append('<ul>')
                stack.append(depth)
            else:
                while stack and stack[-1] > depth:
                    out.append('</li></ul>')
                    stack.pop()
                out.append('</li>')
            out.append(f'<li>{content}')
            continue

        close_all()
        out.append(f'<p>{escape(line.strip())}</p>')

    close_all()
    return '\n'.join(out)


def escape(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
