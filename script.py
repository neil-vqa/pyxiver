import pyxiver
import pprint

printer = pprint.PrettyPrinter()

query = pyxiver.get_all('black hole', max_results=2, sort_by='submittedDate')
# print(query.content)
data = query.content
# printer.pprint(data['feed']['entry'][0])
printer.pprint(data)
print(type(data))
