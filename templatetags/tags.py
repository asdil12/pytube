from django import template
from icemac.truncatetext import truncate
import locale

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

@register.simple_tag
def limits(text, length):
	return text[:length]

@register.simple_tag
def ksep(num, enc="de_DE.UTF-8"):
	try:
		locale.setlocale(locale.LC_ALL, enc)
		form = int(''.join(num))
		return locale.format('%d', form, True)
	except:
		return ''.join(num)
