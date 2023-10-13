from django import template

register = template.Library()

forbidden_words = ["life", "your", "rich", "animal"]


@register.filter()
def words(value):
    finder = value.split()
    for i in finder:
        if isinstance(i, str):
            if i.lower().replace(".", "").replace(",", "").replace(";", "").replace(":", "") in forbidden_words:
                finder[finder.index(i)] = (i[0] + (len(i[1:-2]) * "*") + i[-1])  # (_[0] + len(_[1:]) * "*")
            else:
                continue
        else:
            continue
    return " ".join(finder)
