from django import template

register = template.Library()

@register.filter(name='render_post_body_as_template')
def render_post_body_as_template(value):
    return template.Template(value).render(template.Context())

@register.filter(name="add_class")
def add_class(value, arg):
    return value.as_widget(attrs={"class": arg})
