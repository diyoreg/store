from django import template
from pages.models import Category, Subcategory


register = template.Library()


@register.simple_tag()
def get_categories_data():
    categories = Category.objects.all()
    data = {category: category.categories.all for category in categories}
    return data
