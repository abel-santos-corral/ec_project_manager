class Project:
    def __init__(self, project_key, project_name, project_initials, project_full_name, component_prefix, project_id):
        self.project_key = project_key
        self.project_name = project_name
        self.project_initials = project_initials
        self.project_full_name = project_full_name
        self.component_prefix = component_prefix
        self.project_id = project_id

    def to_dict(self):
        return {
            'project_key': self.project_key,
            'project_name': self.project_name,
            'project_initials': self.project_initials,
            'project_full_name': self.project_full_name,
            'component_prefix': self.component_prefix,
            'project_id': self.project_id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['project_key'],
            data['project_name'],
            data['project_initials'],
            data['project_full_name'],
            data['component_prefix'],
            data['project_id']
        )
