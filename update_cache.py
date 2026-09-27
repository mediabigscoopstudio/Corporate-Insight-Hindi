import re

with open('template/main/index.html', 'r') as f:
    content = f.read()

if '{% load cache %}' not in content:
    # insert after extends
    content = content.replace('{% extends "main/base.html" %}', '{% extends "main/base.html" %}\n{% load cache %}')
    # wrap the main body inside block 'content' with a cache
    # block 'content' usually starts after css
    pattern = re.compile(r'\{%\s*block\s+[\'"]?content[\'"]?\s*%\}')
    match = pattern.search(content)
    if match:
        content = content[:match.end()] + "\n{% cache 600 homepage_content %}\n" + content[match.end():]
        # and close it before endblock content
        content = content.replace("{% endblock 'content' %}", "{% endcache %}\n{% endblock 'content' %}")
    
    with open('template/main/index.html', 'w') as f:
        f.write(content)
