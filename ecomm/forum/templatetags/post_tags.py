from django import template
from .. models import Question


register = template.Library()


@register.inclusion_tag('forum/blog.html')
def show_new_questions(count=5):
    new_questions = Question.objects.order_by('-asked',)
    return {'new_questions':new_questions}