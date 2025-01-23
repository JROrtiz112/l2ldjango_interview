from django import template
from l2l.utils.datetime_utils import formatDate

register = template.Library()

@register.filter(name="l2l_dt")
def l2l_dt(dateObject):
    try:
        return formatDate(dateObject)
    except(TypeError) as e:
        return e