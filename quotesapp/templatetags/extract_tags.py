from django import template

register = template.Library()

@register.filter(name='tags')
def tags(quote_tags):
    return ', '.join([str(tag.tag) for tag in quote_tags.all()])
