import os
import re

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Regex to match /article/{{ var.slug }}/ or /article/{{ var.slug }}
    # Also handles whitespace inside the tags
    pattern = re.compile(r'/article/\{\{\s*([a-zA-Z0-9_.]+)\.slug\s*\}\}/?')
    
    def replacer(match):
        var = match.group(1)
        return f"/{{{{ {var}.category.slug }}}}/{{{{ {var}.slug }}}}/"

    new_content = pattern.sub(replacer, content)

    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

for root, dirs, files in os.walk('template'):
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))

