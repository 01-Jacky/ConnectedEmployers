from bs4 import BeautifulSoup
from collections import namedtuple

class Data(object):
    """ Data Store Class """

    def __init__(self):
        # Constructor a list of connections for the Data instance
        self.connection_list = []
        Connection = namedtuple('Connection', ['name', 'title', 'company'])

        html_doc = open('test_data/my_connection_sample.html')
        soup = BeautifulSoup(html_doc, 'html.parser')

        person_container = soup.findAll("a", {"class": "mn-person-info__link ember-view"})
        for person in person_container:
            name = person.find("span", {"class": "mn-person-info__name"}).string.strip()
            raw_occupation = person.find("span", {"class": "mn-person-info__occupation"}).string.strip()

            raw_occupation = raw_occupation.replace(" at ", "-").replace("@","-")       # Could have done regex too
            str_arr = raw_occupation.split("-")

            if len(str_arr) > 1:
                title = str_arr[0]
                company = str_arr[1].strip()
            else:
                title = str_arr[0]
                company = "unknown"

            self.connection_list.append(Connection(name, title, company))



#  Ad-hoc testing
if __name__ == '__main__':
    data = Data()
    count = 0

    for connection in data.connection_list:
        print("%s - %s - %s" % (connection.company, connection.name, connection.title))
        count += 1