class Enumeration(object):
    """
    http://djangosnippets.org/snippets/1647/
    A small helper class for more readable enumerations,
    and compatible with Django's choice convention.
    You may just pass the instance of this class as the choices
    argument of model/form fields.

    Example:
    MY_ENUM = Enumeration([
    (100, 'MY_NAME', 'My verbose name'),
    (200, 'MY_AGE', 'My verbose age'),
    ])
    assert MY_ENUM.MY_AGE == 100
    assert MY_ENUM[1] == (200, 'My verbose age')
    """

    def __init__(self, enum_list):
        self.enum_list = [(item[0], item[2]) for item in enum_list]
        self.enum_dict = {}
        for item in enum_list:
            self.enum_dict[item[1]] = (item[0], item[2])

    def __contains__(self, v):
        return (v in self.enum_list)

    def __len__(self):
        return len(self.enum_list)

    def __getitem__(self, v):
        if isinstance(v, basestring):
            # FIXME: maybe better to return tuple (value, text)
            return self.enum_dict[v][0]
        elif isinstance(v, int):
            return self.enum_list[v]

    def __getattr__(self, name):
        return self.enum_dict[name][0]

    def __iter__(self):
        return self.enum_list.__iter__()

    def __deepcopy__(self, name):
        # HACK: for filters; but from another point of view enum it's a
        # singleton
        return self

    def get_name_by_value(self, v):
        for value, name in self.enum_list:
            if v == value:
                return name
        raise BaseException("No such value")

    def all_except(self, *names):
        # maybe can be a better solution
        return tuple(v[0] for k, v in self.enum_dict.items() if k not in names)

    # FIXME: rename to 'values'
    @property
    def values(self):
        return [el[0] for el in self.enum_list]
