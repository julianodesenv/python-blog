from django import template

register = template.Library()

@register.filter(name='plural_of_comment')
def plural_of_comment(number):
    try:
        num_comments = int(number)
        if num_comments == 0:
            return f'Nenhum comentário'
        elif num_comments == 1:
         return f'{number} comentário'
        else:
           return f'{number} comentário(s)'
    except:
        return f'{number} comentário(s)'
