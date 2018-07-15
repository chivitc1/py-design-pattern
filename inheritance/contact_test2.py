from inheritance.contact import Contact, Supplier


def main():
    c = Contact('Some body', 'sb@gmail.com')

    s = Supplier('Supplier1', 'supplier1@gmail.com')

    print(c.name, c.email)

    print(s.name, s.email)

    c.all_contacts

    try:
        c.order("I need food")
    except Exception as ex:
        print('Exception occur: ', ex)

    s.order('I order a Pizza')


if __name__ == '__main__':
    main()