from contact import Contact


def main():
    contact = Contact(name='chi nguyen', email='chivitc1@gmail.com')
    contact2 = Contact(name='phong nguyen', email='phong@gmail.com')

    print()
    print("Contact list:")
    for idx, c in enumerate(Contact.all_contacts):
        print(str(idx + 1), '. ', c.name, '\t', c.email)


if __name__ == '__main__':
    main()
