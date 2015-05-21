import json
import os.path
import re
import sys

def parse_class(node, scope, abstract):
	tags.append(str(node['title']) + '\xcc' + str(32 if abstract else 1) + '\xce' + str(scope) + '\n')
	with open(os.path.join(sys.argv[1], node['link'] + '.html')) as dom:
		cls = dom.read()
	inherited = cls.find('<h2>Inherited Members</h2>')
	if inherited < 0:
		inherited = cls.find('<div class="footer-wrapper">')
	cons = cls.find('<h2>Constructors</h2>', 0, inherited)
	if cons < 0:
		cons = inherited
	func = cls.find('<h2>Public Functions</h2>', 0, inherited)
	if func < 0:
		func = cons
	field = cls.find('<h2>Variables</h2>', 0, func)
	scope += '.' + node['title']
	childs = a.findall(cls[field:func])
	for child in childs:
		parse_field(child[1], child[0], scope)
	childs = a.findall(cls[func:cons])
	for child in childs:
		parse_method(child[1], child[0], scope)
	childs = a.findall(cls[cons:inherited])
	for child in childs:
		parse_method(child[1], child[0], scope)

def parse_enum(node):
	tags.append(str(node['title']) + '\xcc2\xce' + str(scope) + '\n')
	with open(os.path.join(sys.argv[1], node['link'] + '.html')) as dom:
		cls = dom.read()
	inherited = cls.find('<div class="footer-wrapper">')
	field = cls.find('<h2>Variables</h2>', 0, func)
	if func < 0:
		func = inherited
	childs = a.findall(cls[field:func])
	scope += '.' + node['title']
	for child in childs:
		tags.append(title + '\xcc4\xce' + str(scope) + '\n')

def parse_field(title, link, scope):
	with open(os.path.join(sys.argv[1], link)) as dom:
		cls = dom.read()
	start = cls.find('<div class="signature-CS sig-block">')
	start = cls.find('<', start + 1)
	end = cls.find('<', start + 1)
	tags.append(title + '\xcc8\xce' + str(scope) + '\xcf' + strip_tags(cls[start:end]) + '\n')

def parse_method(title, link, scope):
	if title.startswith('operator '):
		return
	with open(os.path.join(sys.argv[1], link)) as dom:
		cls = dom.read()
	start = cls.find('<div class="signature-CS sig-block">')
	end = cls.find('</div>', start)
	sig = cls.find('<', start + 1)
	args = cls.find('(', start)
	tags.append(title + '\xcc128\xcd' + strip_tags(cls[args:end]) + '\xce' + str(scope) + '\xcf' + strip_tags(cls[start:sig]) + '\n')

def parse_namespace(ns):
	tags.append(str(ns['title']) + '\xcc256\n')
	for node in ns['children']:
		if node['title'] == 'Classes':
			for child in node['children']:
				parse_class(child, ns['title'], False)
		elif node['title'] == 'Interfaces':
			for child in node['children']:
				parse_class(child, ns['title'], True)
		elif node['title'] == 'childerations':
			for child in node['children']:
				parse_child(child)
		elif node['title'].startswith(ns['title']):
			parse_namespace(node)
		elif node['children'] is list:
			for child in node['children']:
				parse_other(child)

def parse_other(node):
	tags.append(str(ns['title']) + '\xcc0\n')

def strip_tags(s):
	return c.sub(' ', b.sub('', s)).rstrip('; ')

tags = []
a = re.compile(r'<a href="([^"]*)">([^<]*)</a>')
b = re.compile(r'<[^<]+>')
c = re.compile(r'\s+')
with open(os.path.join(sys.argv[1], 'docdata/toc.json'), 'r') as fin:
	toc = json.load(fin)
for ns in toc['children']:
	if ns['title'] != 'Other':
		parse_namespace(ns)
tags.sort()
with open(sys.argv[2], 'w') as fout:
	for tag in tags:
		fout.write(tag)
