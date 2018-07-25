import json

class Contact:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def full_name(self):
        return ("{} {}".format(self.firstname, self.lastname))


class ContactEncoder(json.JSONEncoder):
    def default(self, obj):
        """Override"""
        if isinstance(obj, Contact):
            return {'is_contact': True,
                    'firstname': obj.firstname,
                    'lastname': obj.lastname}
        return super().default(obj)

def decode_contact(dic):
    if dic.get('is_contact'):
        return Contact(firstname=dic.get('firstname'), lastname=dic.get('lastname'))
    else:
        return dic

def main():
    c = Contact("John", "Bui")
    s = json.dumps(c, cls=ContactEncoder)
    print(s)

    data = ('{"is_contact": true, "firstname": "John", "lastname": "Bui", "full_name": "John Bui"}')
    c2 = json.loads(data, object_hook=decode_contact)
    print(c2.full_name)


if __name__ == '__main__':
    main()
