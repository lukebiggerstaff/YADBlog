from django import template

register = template.Library()

@register.filter
def render_post_body_as_template(value):
    return template.Template(value).render(template.Context())

