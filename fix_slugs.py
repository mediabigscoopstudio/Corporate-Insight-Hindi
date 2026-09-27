import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'corporate_hindi.settings')
django.setup()

from dash.models import Article, Category, Author
from django.utils.text import slugify

def fix_all():
    print("Fixing empty slugs...")
    
    # Articles
    articles = Article.objects.filter(slug__in=["", "-", "-1", "-2"])
    for a in articles:
        if a.title:
            new_slug = slugify(a.title, allow_unicode=True)
            if not new_slug:
                new_slug = f"article-{a.id}"
            
            # Ensure unique
            base = new_slug
            count = 1
            while Article.objects.filter(slug=new_slug).exclude(pk=a.pk).exists():
                new_slug = f"{base}-{count}"
                count += 1
                
            a.slug = new_slug
            a.save(update_fields=['slug'])
            print(f"Fixed Article ID {a.id}: {new_slug}")
            
    print("Done!")

if __name__ == '__main__':
    fix_all()
