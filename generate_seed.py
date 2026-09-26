import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "corporate_hindi.settings")
django.setup()

from dash.models import Category, Author, team

def escape_str(s):
    if s is None:
        return '""'
    return repr(s)

with open('final_seed.py', 'w', encoding='utf-8') as f:
    f.write('import os\n')
    f.write('import django\n\n')
    f.write('os.environ.setdefault("DJANGO_SETTINGS_MODULE", "corporate_hindi.settings")\n')
    f.write('django.setup()\n\n')
    f.write('from dash.models import Category, Author, team\n')
    f.write('from django.utils.text import slugify\n\n')
    
    # Categories
    f.write('print("Seeding Categories...")\n')
    f.write('wanted_categories = [\n')
    categories = Category.objects.filter(status='Enabled').order_by('display_order')
    for c in categories:
        f.write(f'    {{"title": {escape_str(c.title)}, "slug": {escape_str(c.slug)}, "display_order": {c.display_order}}},\n')
    f.write(']\n\n')
    f.write('''for idx, cat_data in enumerate(wanted_categories):
    title = cat_data["title"]
    c, created = Category.objects.get_or_create(
        title=title,
        defaults={
            'slug': cat_data["slug"] or slugify(title, allow_unicode=True),
            'meta_title': title,
            'meta_description': title,
            'meta_keywords': title,
            'description': title,
            'status': 'Enabled',
            'display_order': cat_data["display_order"],
            'show_in_nav': True
        }
    )
    if not created:
        c.display_order = cat_data["display_order"]
        c.status = 'Enabled'
        c.show_in_nav = True
        c.save()
    print(f"Category {title}: {'Created' if created else 'Updated'}")

# Disable categories that are not in wanted list
Category.objects.exclude(title__in=[c["title"] for c in wanted_categories]).update(status='Disabled', show_in_nav=False)
\n''')

    # Authors
    f.write('print("\\nSeeding Authors...")\n')
    f.write('authors_data = [\n')
    for a in Author.objects.all():
        f.write(f'    {{"name": {escape_str(a.name)}, "email": {escape_str(a.email)}, "slug": {escape_str(a.slug)}, "designation": {escape_str(a.designation)}, "description": {escape_str(a.description)}}},\n')
    f.write(']\n\n')
    f.write('''for auth in authors_data:
    if not auth["email"]:
        continue
    a, created = Author.objects.get_or_create(
        email=auth["email"],
        defaults={
            "name": auth["name"],
            "designation": auth["designation"],
            "slug": auth["slug"] or slugify(auth["name"], allow_unicode=True),
            "description": auth["description"]
        }
    )
    if not created:
        a.name = auth["name"]
        a.designation = auth["designation"]
        a.description = auth["description"]
        a.save()
    print(f"Author {auth['name']}: {'Created' if created else 'Updated'}")
\n''')

    # Team
    f.write('print("\\nSeeding Team...")\n')
    f.write('team_data = [\n')
    for t in team.objects.all().order_by('display_order'):
        f.write(f'    {{"name": {escape_str(t.name)}, "designation": {escape_str(t.designation)}, "display_order": {t.display_order}}},\n')
    f.write(']\n\n')
    f.write('''for idx, t_data in enumerate(team_data):
    t, created = team.objects.get_or_create(
        name=t_data["name"],
        defaults={
            "designation": t_data["designation"],
            "display_order": t_data["display_order"] if t_data["display_order"] is not None else (idx + 1),
            "status": "Enabled"
        }
    )
    if not created:
        t.designation = t_data["designation"]
        t.display_order = t_data["display_order"] if t_data["display_order"] is not None else (idx + 1)
        t.save()
    print(f"Team Member {t_data['name']}: {'Created' if created else 'Updated'}")

print("\\nSeeding Complete!")
''')

