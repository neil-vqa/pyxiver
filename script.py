# import requests
# import xmltodict
# import json
import pprint

printer = pprint.PrettyPrinter()
#
# base_url = 'http://export.arxiv.org/api/query?'
# query_params = 'search_query=all:electron&start=0&max_results=1'
# request_url = f'{base_url}{query_params}'
#
# r = requests.get(request_url)
# xml_response = r.text
# processed_json = json.loads(json.dumps(xmltodict.parse(xml_response)))
# printer.pprint(processed_json)
# printer.pprint(processed_json['feed']['entry']['summary'])
#
# # print(processed_json['feed'])

import pyxiver

query = pyxiver.get_all('black hole', max_results=2, sort_by='submittedDate')
# print(query.content)
data = query.content
# printer.pprint(data['feed']['entry'][0])
printer.pprint(data)
print(type(data))