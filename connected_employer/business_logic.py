import data

class BusinessLogic(object):
    """ Business logic holding data store instances """

    data = data.Data()


if __name__ == '__main__':
    business_logic = BusinessLogic()

    print(len(business_logic.data.connection_list))

    for connection in sorted(business_logic.data.connection_list, key=lambda x: x.company):
        print("%s - %s - %s" % (connection.company, connection.name, connection.title))
