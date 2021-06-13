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

# Verbose content - multiple papers
verbose_content = query.verbose
printer.pprint(verbose_content)

# Minimal content - provides only the title, summary, id, and category
minimal_content = query.minimal
printer.pprint(minimal_content)


# Provide the abstract URL found as the "id" key from the list of articles fetched through get_all()
query_one = pyxiver.get_one('http://arxiv.org/abs/2106.05901v1')

# Verbose content - single paper
verbose_content = query_one.verbose
printer.pprint(verbose_content)

# Minimal content - provides only the title, authors, published date, and summary
minimal_content = query_one.minimal
printer.pprint(minimal_content)
