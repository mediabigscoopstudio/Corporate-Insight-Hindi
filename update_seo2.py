import os
import re

def insert_or_replace_block(content, block_name, new_content):
    pattern = re.compile(r'\{%\s*block\s+[\'"]?' + block_name + r'[\'"]?\s*%\}.*?\{%\s*endblock\s+[\'"]?' + block_name + r'[\'"]?\s*%\}', re.DOTALL)
    if pattern.search(content):
        return pattern.sub(new_content, content)
    else:
        # If the block doesn't exist, we insert it after {% extends ... %}
        extends_pattern = re.compile(r'\{%\s*extends\s+[^%]+%\}')
        match = extends_pattern.search(content)
        if match:
            return content[:match.end()] + "\n\n" + new_content + content[match.end():]
        return content

def add_og(content):
    # we just need to ensure og:site_name and og:locale are there if not already
    new_tags = """
<meta property="og:site_name" content="Corporate Insight">
<meta property="og:locale" content="hi_IN">
"""
    if "og:site_name" not in content:
        content = content.replace("<!-- Twitter -->", new_tags + "\n<!-- Twitter -->")
    return content

for root, dirs, files in os.walk('template/main'):
    for file in files:
        if file.endswith('.html'):
            fpath = os.path.join(root, file)
            with open(fpath, "r") as f:
                c = f.read()
            if "{% block 'meta' %}" in c:
                c = add_og(c)
                with open(fpath, "w") as f:
                    f.write(c)

