from django import template
from customhtml.models import CustomHtml

register = template.Library()

def render_html(custom_pk):
    html = CustomHtml.objects.get(pk = custom_pk)
    return {'html' : html}

register.inclusion_tag('../templates/custom_html.html')(render_html)
