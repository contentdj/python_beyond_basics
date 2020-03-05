def tag(name, **attributes):
  result = '<' + name
  for k, v in attributes.items():
    result += ' {k}="{v}"'.format(k=k, v=str(v))
  result += '>'
  return result

print(tag('img', src="monet.jpg", alt="Sunrise by Claude Monet", border=1))

