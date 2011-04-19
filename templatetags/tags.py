from django import template
from icemac.truncatetext import truncate

register = template.Library()

@register.simple_tag
def active(request, pattern):
	import re
	if re.search(pattern, request.path):
		return 'selected'
	return ''

@register.simple_tag
def wrap(text, width=80):
	lines = []
	for paragraph in text.split('\n'):
		line = []
		len_line = 0
		for word in paragraph.split(' '):
			len_word = len(word)
			if len_line + len_word <= width:
				line.append(word)
				len_line += len_word + 1
			else:
				lines.append(' '.join(line))
				line = [word]
				len_line = len_word + 1
		lines.append(' '.join(line))
	return '\n'.join(lines)

@register.simple_tag
def trunk(text, length, ellipsis='...'):
	return truncate(text, length, ellipsis).replace(' '+ellipsis, ellipsis)
