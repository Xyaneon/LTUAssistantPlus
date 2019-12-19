
from neo4j import GraphDatabase

def connect():
    return GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "123456"))

# Creating the db
    #Adding the nodes
        #Add the staff
        #Add the master curiculum
        #Add the bachelor curiculm
def add_staff(tx, name, title, department, email, phone, office):
    tx.run("MERGE (a:Staff {name: $name, title: $title, department: $department, email: $email, phone: $phone, office: $office}) ",
           name=name, title=title, email=email, phone=phone, office=office, department=department)

#add the bachelor tabs
def add_bachelor(tx, course_number, subject, credits):
    tx.run("MERGE (a:BachelorCurriculum {course_number: $course_number, subject: $subject, credits: $credits}) ",
           course_number=course_number, subject=subject, credits=credits)

#add the master tabs
def add_master(tx, course_number, subject, credits):
    tx.run("MERGE (a:MasterCurriculum{course_number: $course_number, subject: $subject, credits: $credits}) ",
           course_number=course_number, subject=subject, credits=credits)

#add simple node
def add_node(tx, name):
    tx.run("MERGE (a:"+name+"{name:$name})",name=name)

def add_concentration(tx, name, intro):
    tx.run("MERGE (a:Concentration{name: $name, intro: $intro})",name=name,intro=intro)

def create_nodes():
    driver = connect()
    with driver.session() as session:
        session.write_transaction(add_node,"DepartmentOfMathematicAndComputerScience")
        session.write_transaction(add_node,"DepartmentStaff")
        session.write_transaction(add_node,"Minors")
        session.write_transaction(add_node,"BachelorsDegree")
        session.write_transaction(add_node,"ComputerScience")
        session.write_transaction(add_node,"MasterScience")
        session.write_transaction(add_node,"ComputerScience")
        session.write_transaction(add_node,"UndergraduateCertificate")
    driver.close()

def print_staff(tx):
    for record in tx.run("MATCH (a:Staff)"
                         "RETURN a.name ORDER BY a.name"):
        print(record["a.name"])
    
    #Formate the nodes:
        #Department of Mathematic and Computer Science:
            #Department Staff--Done
                #Direct Entry MSCS( 2 times)
                #
                #
            #Bachelor's Degree:
                #Computer Science:
                    #Minor/Dual Major
                    #concentrations-Text
                    #admission requirement-Text
                    #curiculum:
                        #4 concentrations:
                            #semesters:
                                #course number, subjuet and credits
            #Minors:
                #Bachelor's Degree:
                #Computer Science:
                    #Minor/Dual Major
                    #concentrations-Text(?)
                    #admission requirement-Text
                    #curiculum:
                        #4 concentrations:
                            #semesters:
                                #course number, subjuet and credits
            #Undergraduate Certificate:
                #Computer Science
            #Master's Degrees:
                #Computer Science:
                    #concentrations-Text
                    #admission requirement-Text
                    #curiculum
                ##Direct Entry MSCS( 2 times)