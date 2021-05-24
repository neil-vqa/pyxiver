"""
Sample script
"""

import pyxiver
import pprint

printer = pprint.PrettyPrinter()

# Provide query - all params are optional except for the search string (e.g. "black hole")
query = pyxiver.get_all('black hole',
                        search_field="ti",
                        max_results=2,
                        sort_by='submittedDate',
                        sort_order='descending')

# Verbose content
verbose_content = query.verbose
printer.pprint(verbose_content)

# Minimal content - provides only the title, summary, id, and category
minimal_content = query.minimal
printer.pprint(minimal_content)

