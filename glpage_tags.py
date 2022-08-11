from django import template
from glpage.models import category
from django.db.models import Count

register = template.Library()


@register.simple_tag()
def get_category():
    return category.objects.all()

@register.inclusion_tag('glpage/list_categories.html')
def show_category():
    categories = category.objects.annotate(cnt=Count('buy'))
    return {"category": categories}
