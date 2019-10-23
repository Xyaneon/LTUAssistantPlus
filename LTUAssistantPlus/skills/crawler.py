import requests
from bs4 import BeautifulSoup
from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
def add_staff(tx, name, title, department, email, phone, office):
    tx.run("MERGE (a:Staff {name: $name, title: $title, department: $department, email: $email, phone: $phone, office: $office}) ",
           name=name, title=title, email=email, phone=phone, office=office, department=department)
def print_staff(tx):
    for record in tx.run("MATCH (a:Staff)"
                         "RETURN a.name ORDER BY a.name"):
        print(record["a.name"])

page = requests.get(
    'https://www.ltu.edu/facultyandstaff/department/?_cid=20&_opt=dept&_brand=/arts_sciences/mathematics_computer_science/index.asp')
soup = BeautifulSoup(page.content, 'html.parser')

with driver.session() as session:
    for staff_li in soup.find_all('li', class_='fs-list-item'):
        # For all staff
        staff_name = staff_li.find('div', class_='col-md-3').text.strip()
        title_block = staff_li.find('div', class_='col-md-4')
        title = title_block.find('span', class_='text-bigger').text.strip()
        department_title = title_block.find_all('span')[1].text.strip()
      # print(staff_name)
       # print(title)
       # print(department_title)
        contact_block = staff_li.find_all('div', class_='col-md-3')[1]
        email = contact_block.find('a').text

        spans = contact_block.find_all('span')
        phone = None
        office = None
        if len(spans) == 2:
            phone = spans[0].text.replace('P', '').strip()
            office = spans[1].text.replace('O ', '')
           # print(phone)
          #  print(office)
        elif len(spans) == 1:
            phone = spans[0].text.replace('P', '').strip()
           # print(phone)
        session.write_transaction(add_staff, staff_name, title, department_title, email, phone or "", office or "")
    session.read_transaction(print_staff)
driver.close()