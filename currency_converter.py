# -*- coding: utf-8 -*-
import re
def currency_coverter(str):
	#Add more if needed
	currency_mapping = {'£': 'BP', '$': 'USD', 'RMB': 'RMB', '¥': 'CY'}
	alternator = ''
	alternator = '|'.join(x for x in currency_mapping)
	alternator = re.sub(r'\|$', '', alternator)
	alternator = re.sub(r'\$', '\$', alternator)

	if re.search('((?:' + alternator + ')\s*[-]?[\d.]+[\d.,]*|[-]?[\d.]+[\d.,]*(?:\s*' + '(?:' + alternator + ')))', str):
		tmp = re.search('((?:' + alternator + ')\s*[-]?[\d.]+[\d.,]*|[-]?[\d.]+[\d.,]*(?:\s*' + '(?:' + alternator + ')))', str).group(1)
	
		for x in currency_mapping:
			if re.search('\\' + x, tmp):
				tmp = re.sub('\\' + x, '', tmp)
				tmp = currency_mapping[x] + ' ' + tmp
	else:
		tmp = str

	tmp = re.sub(r'[,]|\.$', '', tmp)
	tmp = re.sub(r'\s+', ' ', tmp)

	return tmp

currency_coverter('.23,67$')
currency_coverter('$ .23,67')
currency_coverter('.23,67     ¥')
currency_coverter('¥.23,67')
currency_coverter('.23,67£')
currency_coverter('£344')
currency_coverter('.23,67')
