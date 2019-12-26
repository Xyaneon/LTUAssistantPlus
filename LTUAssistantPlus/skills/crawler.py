import requests
from bs4 import BeautifulSoup
import re

# Everything under this - should get put into a function called: scrape_department_staff

from skills.neo4j_db import *


def scrape_department_staff(link: str):
    driver = connect()

    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')

    # session = driver.create_session()
    # for staff_li..
    #   more code...
    # session.cleanup()
    # def session()
    #    session = driver.create_session()
    #    yield session
    #    session.cleanup()

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
            session.write_transaction(
                add_staff, staff_name, title, department_title, email, phone or "", office or "")
        session.read_transaction(print_staff)
    driver.close()


def scrape_bacholor_computer_science_minor(link: str):
    # Tabs - Minor/Dual Major, Concentrations, Curriculum, Careers
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Minor/Dual Major tab
    #  Major: Core courses (name, credits, required?)
    #  Minor: Basic option information (What are the minor options?)
    #  Transferring credit requirement
    #  Dual major requirements

    major_minor_tab = soup.find('div', id='minor-major')
    major_minor_table = major_minor_tab.find('table')
    major_course_row = major_minor_table.find_all('tr')[2]
    for major_course in major_course_row.find_all('span'):

        (name, credits) = re.match(
            r'^.\.\s(.*)\s\((\d+).*$', major_course.text).group(1, 2)
        print(name)
        print(credits)
        required = True
    minor_course_row = major_minor_table.find_all('tr')[4]
    minor_course_text = minor_course_row.text

    for minor_course in minor_course_text.split(')'):
        minor_course = minor_course.strip('\n')
        m = re.match(r'\d+\. (.*) \((\d+)', minor_course)
        if m == None:
            continue
        (name, credits) = m.group(1, 2)
       # print(name)
       # print(credits)
    minor_completion_paragraphs = major_minor_tab.find_all('p', class_='p2')
    minor_completion_option_1_2 = minor_completion_paragraphs[1].text
    options = minor_completion_option_1_2.split(':')
    option_1 = options[1].replace('Option 2', '').strip()
    option_2 = options[2].strip()
    option_2_a = minor_completion_paragraphs[2].text
    option_2_b = minor_completion_paragraphs[3].text
    minor_completion_option_3 = minor_completion_paragraphs[4].text.replace(
        'Option 3:', '').strip()
    transfer = minor_completion_paragraphs[5].text
    dual = major_minor_tab.find_all('div')[2].text.strip()
    print(option_1)
    print(option_2)
    print(option_2_a)
    print(option_2_b)
    print(minor_completion_option_3)
    print(transfer)
    print(dual)
    #get the concentration
    bachelarCs=getConcentrations(soup)
    #get the curriculum
    bachelarCsCurriculum=getCurriculum(soup)

    
    careers = soup.find('div', id='careers')
    paras = careers.find_all('p')
    
    last_element = None
    career_options = []
    options_complete = False
    aspects_paragraph = None
    industries_paragraph = None
    import bs4
    for c in paras[0].contents:
        if type(c) == bs4.element.Tag and type(last_element) == bs4.element.Tag:
            options_complete = True
        elif type(c) == bs4.element.NavigableString and not options_complete:
            career_options.append(c.string)
        elif type(c) == bs4.element.NavigableString and options_complete:
            if aspects_paragraph == None:
                aspects_paragraph = c.string
            elif industries_paragraph == None:
                industries_paragraph = c.string

        last_element = c
    
    print(career_options)
    #print(aspects_paragraph.split(' aspects of ')[1].split(','))
    print(aspects_paragraph)
    #print(industries_paragraph.split(' such as ')[1].split(','))
    print(industries_paragraph)
    salary_para = paras[1].text
    average_salary = salary_para
    # average_salary = salary_para.split('$')[1].replace(',', '').replace('.', '')
    print(average_salary)
    # Careers
    #  List career options
    #  List aspects
    #  List industries
    #  Annual average starting salary

    driver = connect()

    with driver.session() as session:
        i=0
        type1=['Software Engineering','Game Software Development','Business Software Development','Scientific Software Development']
        for cs in bachelarCs:
                session.write_transaction(add_concentration, cs["name"],cs["description"],"Bachelor",type1[i])
                i+=1
    driver.close()

 
 # ^.\.\s(.*)\s\((\d+).*$
    # Concentrations
    #  For each: name and description
def getConcentrations(soup):
    concentrations = soup.find('div', id='concentrations')
    concentration_ps = concentrations.find_all('p', recursive=False)
    concentration_divs = concentrations.find_all('div', recursive=False)
    concentration_array = []
    for i, concentration_desc in enumerate(concentration_divs):
        concentration_array.append({
            'name': concentration_ps[i+1].text,
            'description': concentration_desc.text
        })
    return concentration_array



# Curriculum
    #  For each concentration
    #    For each school year
    #       For each semester
    #         Course #, subject, credit count
def getCurriculum(soup):
    curriculum = soup.find('div', id='curriculum')
    curriculum_array = []
    for group in curriculum.find_all('div', class_='panel-group'):
        years = []
        for year in group.find_all('div', class_='panel'):
            semesters = []
            for semester in year.find_all('table'):
                courses = []
                semester_rows = semester.find_all('tr')
                for i, course in enumerate(semester_rows):
                    if i == 0 or i == len(semester_rows)-1:
                        continue
                    cells = course.find_all('td')
                    courses.append({
                        'number': cells[0].text.strip(),
                        'subject': cells[1].text,
                        'credits': cells[2].text
                    })

                semesters.append({
                    'name': semester.find('h4').text,
                    'courses': courses,
                    'total_credits': sum([int(x['credits']) for x in courses if x['credits'].isdigit()])
                })

            years.append({
                'name': year.find('div', class_='panel-heading').text.strip(),
                'semesters': semesters
            })
        curriculum_array.append({
            'name': group.get('id').replace(' Concentration', ''),
            'years': years
        })
    return curriculum_array

def createCourse(values):
    headers = ['Course Number', 'Subject', 'Credit']
    course = {}
    if len(values) > 0:
        course[headers[0]] = values[0].text

    if len(values) > 1:
        course[headers[1]] = values[1].text

    if len(values) > 2:
        course[headers[2]] = values[2].text

    return course

def scrape_master_computerScience(link: str):
    # Tabs -, Concentrations, Admissions Requirements, Curriculum
    page = requests.get(link)
    #content = page.content
    content = page.text.replace('&nbsp;', ' ')
    soup = BeautifulSoup(content, 'html.parser')
    # #concentrations
    
    columns = soup.select('div#concentrations > div > div')

    col1 = columns[0]
    col1_p=col1.find_all('p')
    col2= columns[1]
    col2_p=col2.find_all('p')
    concentration_array = [
        {
            'name':'concentration' ,
            'description':col1_p[0].text 
        },
        {
            'name':col1_p[1].text,
            'description':col1_p[2].text+ col1_p[3].text
        },
        {
            'name':col2_p[0].text,
            'description':col2_p[1].text+ col2_p[2].text+ col2_p[3].text +col2_p[4].text
        }
    ]

    driver = connect()

    with driver.session() as session:
        types2 = ["Intelligent Systems","Data Science"]

        i=0 
        for cs in concentration_array[1:]:
                session.write_transaction(add_concentration, cs["name"],cs["description"],"Master",types2[i])
                i+=1
    driver.close()


    # print(concentration_array)

    admissons_ps = soup.select('div#admissions p')

    # print('admission ps', [x.text[0:20] for x in admissons_ps])

    admissions4567= ' '.join([x.text for x in admissons_ps[4:7]])

    requirementDict = {
        'requirementText':admissons_ps[0].text ,
        'requirements': [
        admissons_ps[1].text,
        admissons_ps[2].text,
        admissons_ps[3].text,
        admissions4567
        ],
        'tranferRequirment':admissons_ps[9].text,
        'termporaryAccepted':admissons_ps[10].text
    }
    # print(requirementDict)

    #get the curriculum
    MasterCurriculum=soup.select('div#curriculum p')
    overview=MasterCurriculum[0].text

    tables = []
    for table_i in soup.find_all("table"):
        table = []
        for tr in table_i.find_all("tr"):
            tds = tr.find_all("td")
            course = createCourse(tds)
            table.append(course)
        tables.append(table)
    # print(overview)
    # track=soup.select('div#accordion > div > div')
    # track1=track.find('a').text
    # type(track)

    for i, table in  enumerate(tables):
        #print("Table "+ str(i))
        for course in table:
            course_text="\t"
            for k,v in course.items():
                course_text+=k+": "+v+", "
            print(course_text[:-2])
    driver = connect()

    with driver.session() as session:
        for course in tables[0]:
            if len(course) == 3:
                session.write_transaction(add_master, course["Course Number"],course["Subject"],course["Credit"])
        session.read_transaction(print_staff)
    driver.close()


def scrape_direct_Entry():
    link = "https://www.ltu.edu/arts_sciences/mathematics_computer_science/4plus1-bscs.asp#requirements"

    # Tabs -, Concentrations, Admissions Requirements, Curriculum
    page = requests.get(link)
    #content = page.content
    content = page.text.replace('&nbsp;', ' ')
    soup = BeautifulSoup(content, 'html.parser')
    # #concentrations
    for table in soup.find_all("table"):
        table.extract()
    print("ABOUT DATA")
    for r in soup.find_all("div",id="about"):
        print(r.text)

    print("REQUIREMENTS DATA")
    for r in soup.find_all("div",id="requirements"):
        print(r.text)

def scrape():
    scrape_department_staff('https://www.ltu.edu/facultyandstaff/department/?_cid=20&_opt=dept&_brand=/arts_sciences/mathematics_computer_science/index.asp')
    scrape_master_computerScience('https://www.ltu.edu/arts_sciences/mathematics_computer_science/graduate-computer-science.asp')

    scrape_bacholor_computer_science_minor('https://www.ltu.edu/arts_sciences/mathematics_computer_science/bachelor-of-computer-science.asp#minor-major')
    scrape_direct_Entry()

if __name__ == "__main__":
    clean_graph()
    create_nodes()
    scrape()
    create_relationships()
