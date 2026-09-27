import re

schema = """
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Corporate Insight",
    "url": "{{ request.scheme }}://{{ request.get_host }}",
    "logo": "{{ request.scheme }}://{{ request.get_host }}/static/main/logo/logo.webp",
    "sameAs": [
      "https://www.linkedin.com/company/corporate-insight",
      "https://twitter.com/corporateinsight"
    ]
  }
  </script>
"""

with open('template/main/base.html', 'r') as f:
    content = f.read()

if 'application/ld+json' not in content:
    content = content.replace("</head>", schema + "\n</head>")
    with open('template/main/base.html', 'w') as f:
        f.write(content)
