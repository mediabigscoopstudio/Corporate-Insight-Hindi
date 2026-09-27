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

# 1. Update Index Page
index_file = "template/main/index.html"
with open(index_file, "r") as f:
    content = f.read()

index_meta = """{% block 'meta' %}
<meta name="description" content="Corporate Insight: व्यापार और उद्योग जगत की ताज़ा खबरें, बाज़ार के रुझान, और कॉर्पोरेट जगत के अंदरूनी विश्लेषण।">
<meta name="keywords" content="Corporate news, Business updates, Indian market trends, Business analysis, Hindi business news">
<meta name="author" content="Corporate Insight">

<!-- Open Graph / Facebook -->
<meta property="og:type" content="website">
<meta property="og:url" content="{{ request.build_absolute_uri }}">
<meta property="og:title" content="Corporate Insight | जहां हर कहानी कुछ बदल देती है">
<meta property="og:description" content="Corporate Insight: व्यापार और उद्योग जगत की ताज़ा खबरें, बाज़ार के रुझान, और कॉर्पोरेट जगत के अंदरूनी विश्लेषण।">
<meta property="og:image" content="{{ request.scheme }}://{{ request.get_host }}/static/main/logo/logo.webp">

<!-- Twitter -->
<meta property="twitter:card" content="summary_large_image">
<meta property="twitter:url" content="{{ request.build_absolute_uri }}">
<meta property="twitter:title" content="Corporate Insight | जहां हर कहानी कुछ बदल देती है">
<meta property="twitter:description" content="Corporate Insight: व्यापार और उद्योग जगत की ताज़ा खबरें, बाज़ार के रुझान, और कॉर्पोरेट जगत के अंदरूनी विश्लेषण।">
<meta property="twitter:image" content="{{ request.scheme }}://{{ request.get_host }}/static/main/logo/logo.webp">
{% endblock 'meta' %}"""

content = insert_or_replace_block(content, "meta", index_meta)
# also replace the title to match
content = insert_or_replace_block(content, "title", "{% block 'title' %}Corporate Insight | जहां हर कहानी कुछ बदल देती है{% endblock 'title' %}")

with open(index_file, "w") as f:
    f.write(content)

# 2. Update Article Page
article_file = "template/main/articles/article.html"
with open(article_file, "r") as f:
    content = f.read()

article_meta = """{% block 'meta' %}
<meta name="description" content="{{ data.meta_description|default:data.tldr }}">
<meta name="keywords" content="{{ data.meta_keywords }}">
<meta name="author" content="{{ data.author.name|default:'संपादकीय' }}">

<!-- Open Graph / Facebook -->
<meta property="og:type" content="article">
<meta property="og:url" content="{{ request.build_absolute_uri }}">
<meta property="og:title" content="{{ data.title }} | Corporate Insight">
<meta property="og:description" content="{{ data.meta_description|default:data.tldr }}">
{% if data.thumbnail_image %}
<meta property="og:image" content="{{ request.scheme }}://{{ request.get_host }}{{ data.thumbnail_image.url }}">
{% else %}
<meta property="og:image" content="{{ request.scheme }}://{{ request.get_host }}/static/main/logo/logo.webp">
{% endif %}

<!-- Twitter -->
<meta property="twitter:card" content="summary_large_image">
<meta property="twitter:url" content="{{ request.build_absolute_uri }}">
<meta property="twitter:title" content="{{ data.title }} | Corporate Insight">
<meta property="twitter:description" content="{{ data.meta_description|default:data.tldr }}">
{% if data.thumbnail_image %}
<meta property="twitter:image" content="{{ request.scheme }}://{{ request.get_host }}{{ data.thumbnail_image.url }}">
{% else %}
<meta property="twitter:image" content="{{ request.scheme }}://{{ request.get_host }}/static/main/logo/logo.webp">
{% endif %}
{% endblock 'meta' %}"""

content = insert_or_replace_block(content, "meta", article_meta)
content = insert_or_replace_block(content, "title", "{% block 'title' %}{{ data.title }} | Corporate Insight{% endblock 'title' %}")

with open(article_file, "w") as f:
    f.write(content)

# 3. Update Category Page
category_file = "template/main/articles/category.html"
with open(category_file, "r") as f:
    content = f.read()

cat_meta = """{% block 'meta' %}
<meta name="description" content="{{ data.meta_description|default:data.title|add:' से जुड़ी नवीनतम खबरें और विस्तृत कवरेज।' }}">
<meta name="keywords" content="{{ data.meta_keywords|default:data.title|add:', Corporate Insight, News, Business' }}">

<!-- Open Graph / Facebook -->
<meta property="og:type" content="website">
<meta property="og:url" content="{{ request.build_absolute_uri }}">
<meta property="og:title" content="{{ data.title }} | Corporate Insight">
<meta property="og:description" content="{{ data.meta_description|default:data.title|add:' से जुड़ी नवीनतम खबरें और विस्तृत कवरेज।' }}">
<meta property="og:image" content="{{ request.scheme }}://{{ request.get_host }}/static/main/logo/logo.webp">

<!-- Twitter -->
<meta property="twitter:card" content="summary_large_image">
<meta property="twitter:url" content="{{ request.build_absolute_uri }}">
<meta property="twitter:title" content="{{ data.title }} | Corporate Insight">
<meta property="twitter:description" content="{{ data.meta_description|default:data.title|add:' से जुड़ी नवीनतम खबरें और विस्तृत कवरेज।' }}">
<meta property="twitter:image" content="{{ request.scheme }}://{{ request.get_host }}/static/main/logo/logo.webp">
{% endblock 'meta' %}"""

content = insert_or_replace_block(content, "meta", cat_meta)
content = insert_or_replace_block(content, "title", "{% block 'title' %}{{ data.title }} | Corporate Insight{% endblock 'title' %}")

with open(category_file, "w") as f:
    f.write(content)

# 4. Global generic updater for remaining pages
generic_meta = """{% block 'meta' %}
<meta name="description" content="Corporate Insight: व्यापार और उद्योग जगत की ताज़ा खबरें, बाज़ार के रुझान, और कॉर्पोरेट जगत के अंदरूनी विश्लेषण।">

<!-- Open Graph / Facebook -->
<meta property="og:type" content="website">
<meta property="og:url" content="{{ request.build_absolute_uri }}">
<meta property="og:title" content="Corporate Insight">
<meta property="og:description" content="Corporate Insight: व्यापार और उद्योग जगत की ताज़ा खबरें, बाज़ार के रुझान, और कॉर्पोरेट जगत के अंदरूनी विश्लेषण।">
<meta property="og:image" content="{{ request.scheme }}://{{ request.get_host }}/static/main/logo/logo.webp">

<!-- Twitter -->
<meta property="twitter:card" content="summary_large_image">
<meta property="twitter:url" content="{{ request.build_absolute_uri }}">
<meta property="twitter:title" content="Corporate Insight">
<meta property="twitter:description" content="Corporate Insight: व्यापार और उद्योग जगत की ताज़ा खबरें, बाज़ार के रुझान, और कॉर्पोरेट जगत के अंदरूनी विश्लेषण।">
<meta property="twitter:image" content="{{ request.scheme }}://{{ request.get_host }}/static/main/logo/logo.webp">
{% endblock 'meta' %}"""

for fpath in ["template/main/about.html", "template/main/support.html", "template/main/author.html", "template/main/legal/terms.html", "template/main/legal/privacy.html", "template/main/legal/cookies.html"]:
    if os.path.exists(fpath):
        with open(fpath, "r") as f:
            c = f.read()
        c = insert_or_replace_block(c, "meta", generic_meta)
        c = c.replace("Corporate Impact", "Corporate Insight")
        with open(fpath, "w") as f:
            f.write(c)

print("SEO update completed.")
