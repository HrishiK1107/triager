# reports/templatetags/reports_extras.py
from django import template

register = template.Library()

@register.filter
def get_cvss_badge_class(score):
    try:
        score = float(score)
        if score < 4.0:
            return "bg-primary"
        elif score < 7.0:
            return "bg-warning text-dark"
        elif score < 9.0:
            return "bg-danger"
        else:
            return "bg-dark"
    except:
        return "bg-secondary"
