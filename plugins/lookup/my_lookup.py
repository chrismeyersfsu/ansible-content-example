from ansible.plugins.lookup import LookupBase

DOCUMENTATION = """
    lookup: my_lookup
    author: Chris Meyers
    short_description: it is a lookup
    description:
        - must have this otherwise galaxy will fail to import
"""


class LookupModule(LookupBase):
    def run(self, terms, variables, **kwargs):
        return ['lookup_from_user_dir']
