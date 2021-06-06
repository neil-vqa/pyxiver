# pyXiver


### WIP

**pyXiver** (pyCHIver) is a wrapper for the arXiv public API.

Thank you to arXiv for use of its open access interoperability.

*This project is NOT connected to arXiv (arxiv.org) and Cornell University.*

### Example

```python
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
```

### Query Params

- **query**: Query string to search arXiv

- **search_field**: Search fields listed below

| Prefix  | Explanation |
| ------- | ----------- |
| ti  | title  |
| au  | author  |
| all | all fields (default) |

*For more fields, please visit https://arxiv.org/help/api/user-manual#query_details*

- **max_results**: Count of articles to be returned (default is 10)

- **sort_by**: Sort by "relevance", "lastUpdatedDate", "submittedDate" (default is relevance)

- **sort_order**: Order by "ascending" or "descending" (default is descending)

### Example response from query above
```
VERBOSE

[{'arxiv:comment': {'#text': 'Submitted to MNRAS. 30 pages, 26 figures. '
                             'Trinity code available at:\n'
                             '  https://github.com/HaowenZhang/TRINITY '
                             'Comments welcome!',
                    '@xmlns:arxiv': 'http://arxiv.org/schemas/atom'},
  'arxiv:primary_category': {'@scheme': 'http://arxiv.org/schemas/atom',
                             '@term': 'astro-ph.GA',
                             '@xmlns:arxiv': 'http://arxiv.org/schemas/atom'},
  'author': [{'name': 'Haowen Zhang'},
             {'name': 'Peter Behroozi'},
             {'name': 'Marta Volonteri'},
             {'name': 'Joseph Silk'},
             {'name': 'Xiaohui Fan'},
             {'name': 'Philip F. Hopkins'},
             {'name': 'Jinyi Yang'},
             {'name': 'James Aird'}],
  'category': {'@scheme': 'http://arxiv.org/schemas/atom',
               '@term': 'astro-ph.GA'},
  'id': 'http://arxiv.org/abs/2105.10474v1',
  'link': [{'@href': 'http://arxiv.org/abs/2105.10474v1',
            '@rel': 'alternate',
            '@type': 'text/html'},
           {'@href': 'http://arxiv.org/pdf/2105.10474v1',
            '@rel': 'related',
            '@title': 'pdf',
            '@type': 'application/pdf'}],
  'published': '2021-05-21T17:26:51Z',
  'summary': 'We present Trinity, a flexible empirical model that '
             'self-consistently infers\n'
             'the statistical connection between dark matter haloes, galaxies, '
             'and\n'
             'supermassive black holes (SMBHs). Trinity is constrained by '
             'galaxy observables\n'
             "from $0 < z < 10$ (galaxies' stellar mass functions, specific "
             'and cosmic SFRs,\n'
             'quenched fractions, and UV luminosity functions) and SMBH '
             'observables from $0 <\n'
             'z < 6.5$ (quasar luminosity functions, quasar probability '
             'distribution\n'
             'functions, active black hole mass functions, local SMBH '
             'mass-bulge mass\n'
             'relations, and the observed SMBH mass distributions of high '
             'redshift bright\n'
             'quasars). The model includes full treatment of observational '
             'systematics (e.g.,\n'
             'AGN obscuration and errors in stellar masses). From these data, '
             'Trinity infers\n'
             'the average SMBH mass, SMBH accretion rate, merger rate, and '
             'Eddington ratio\n'
             'distribution as functions of halo mass, galaxy stellar mass, and '
             'redshift. Key\n'
             'findings include: 1) the normalization of the SMBH mass-bulge '
             'mass relation\n'
             'increases only mildly from $z=0$ to $z=3$, but decreases more '
             'strongly from\n'
             '$z=3$ to $z=10$; 2) The AGN radiative$+$kinetic efficiency is '
             '$\\sim$0.04-0.07,\n'
             'and does not show significant redshift dependence given the '
             'existing data\n'
             'constraints; 3) AGNs show downsizing, i.e., the Eddington ratios '
             'of more\n'
             'massive SMBHs start to decrease earlier than those of lower-mass '
             'objects; 4)\n'
             'The average ratio between average SMBH accretion rate and SFR is '
             '$\\sim10^{-3}$\n'
             'for low-mass galaxies, which are primarily star-forming. This '
             'ratio increases\n'
             'to $\\sim10^{-1}$ for the most massive haloes below $z\\sim1$, '
             'where star\n'
             'formation is quenched but SMBHs continue to accrete.',
  'title': 'Trinity I: Self-Consistently Modeling the Dark Matter\n'
           '  Halo-Galaxy-Supermassive Black Hole Connection from $z=0-10$',
  'updated': '2021-05-21T17:26:51Z'},
 {'arxiv:comment': {'#text': 'PhD thesis, The University of Edinburgh, 195 '
                             'pages, 2 figures.\n'
                             '  Includes: integrated discussion of colour '
                             'states and impulse observables; new\n'
                             '  discussion of wavefunctions; new results for '
                             'radiation kernels for\n'
                             '  Reissner-Nordstr\\"{o}m black holes; '
                             'corrections of minor typos from published\n'
                             '  papers',
                    '@xmlns:arxiv': 'http://arxiv.org/schemas/atom'},
  'arxiv:primary_category': {'@scheme': 'http://arxiv.org/schemas/atom',
                             '@term': 'hep-th',
                             '@xmlns:arxiv': 'http://arxiv.org/schemas/atom'},
  'author': {'name': 'Ben Maybee'},
  'category': [{'@scheme': 'http://arxiv.org/schemas/atom', '@term': 'hep-th'},
               {'@scheme': 'http://arxiv.org/schemas/atom', '@term': 'gr-qc'}],
  'id': 'http://arxiv.org/abs/2105.10268v1',
  'link': [{'@href': 'http://arxiv.org/abs/2105.10268v1',
            '@rel': 'alternate',
            '@type': 'text/html'},
           {'@href': 'http://arxiv.org/pdf/2105.10268v1',
            '@rel': 'related',
            '@title': 'pdf',
            '@type': 'application/pdf'}],
  'published': '2021-05-21T10:39:18Z',
  'summary': 'On-shell scattering amplitudes have proven to be useful tools '
             'for tackling\n'
             'the two-body problem in general relativity. This thesis outlines '
             'how to compute\n'
             'relevant classical observables that are themselves on-shell, '
             'directly from\n'
             'amplitudes; examples considered are the momentum impulse, total '
             'radiated\n'
             'momentum, and angular impulse for spinning particles. As '
             'applications we derive\n'
             'results relevant for black hole physics, computing in the '
             'post-Minkowskian\n'
             'expansion of GR, and construct a worldsheet effective action for '
             'the leading\n'
             'spin interactions of Kerr black holes.',
  'title': 'On-Shell Physics of Black Holes',
  'updated': '2021-05-21T10:39:18Z'}]

***************************************************************************************************

MINIMAL  

[{'category': 'astro-ph.GA',
  'id': 'http://arxiv.org/abs/2105.10474v1',
  'summary': 'We present Trinity, a flexible empirical model that '
             'self-consistently infers\n'
             'the statistical connection between dark matter haloes, galaxies, '
             'and\n'
             'supermassive black holes (SMBHs). Trinity is constrained by '
             'galaxy observables\n'
             "from $0 < z < 10$ (galaxies' stellar mass functions, specific "
             'and cosmic SFRs,\n'
             'quenched fractions, and UV luminosity functions) and SMBH '
             'observables from $0 <\n'
             'z < 6.5$ (quasar luminosity functions, quasar probability '
             'distribution\n'
             'functions, active black hole mass functions, local SMBH '
             'mass-bulge mass\n'
             'relations, and the observed SMBH mass distributions of high '
             'redshift bright\n'
             'quasars). The model includes full treatment of observational '
             'systematics (e.g.,\n'
             'AGN obscuration and errors in stellar masses). From these data, '
             'Trinity infers\n'
             'the average SMBH mass, SMBH accretion rate, merger rate, and '
             'Eddington ratio\n'
             'distribution as functions of halo mass, galaxy stellar mass, and '
             'redshift. Key\n'
             'findings include: 1) the normalization of the SMBH mass-bulge '
             'mass relation\n'
             'increases only mildly from $z=0$ to $z=3$, but decreases more '
             'strongly from\n'
             '$z=3$ to $z=10$; 2) The AGN radiative$+$kinetic efficiency is '
             '$\\sim$0.04-0.07,\n'
             'and does not show significant redshift dependence given the '
             'existing data\n'
             'constraints; 3) AGNs show downsizing, i.e., the Eddington ratios '
             'of more\n'
             'massive SMBHs start to decrease earlier than those of lower-mass '
             'objects; 4)\n'
             'The average ratio between average SMBH accretion rate and SFR is '
             '$\\sim10^{-3}$\n'
             'for low-mass galaxies, which are primarily star-forming. This '
             'ratio increases\n'
             'to $\\sim10^{-1}$ for the most massive haloes below $z\\sim1$, '
             'where star\n'
             'formation is quenched but SMBHs continue to accrete.',
  'title': 'Trinity I: Self-Consistently Modeling the Dark Matter\n'
           '  Halo-Galaxy-Supermassive Black Hole Connection from $z=0-10$'},
 {'category': 'hep-th',
  'id': 'http://arxiv.org/abs/2105.10268v1',
  'summary': 'On-shell scattering amplitudes have proven to be useful tools '
             'for tackling\n'
             'the two-body problem in general relativity. This thesis outlines '
             'how to compute\n'
             'relevant classical observables that are themselves on-shell, '
             'directly from\n'
             'amplitudes; examples considered are the momentum impulse, total '
             'radiated\n'
             'momentum, and angular impulse for spinning particles. As '
             'applications we derive\n'
             'results relevant for black hole physics, computing in the '
             'post-Minkowskian\n'
             'expansion of GR, and construct a worldsheet effective action for '
             'the leading\n'
             'spin interactions of Kerr black holes.',
  'title': 'On-Shell Physics of Black Holes'}]

```

### Tests

```commandline
coverage run --source=pyxiver -m pytest

coverage report
```

### License

MIT License

Copyright (c) 2021 Neil Van

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
