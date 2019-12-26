
from neo4j import GraphDatabase

def connect():
    return GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "123456"))

# Creating the db
    #Adding the nodes
        #Add the staff
        #Add the bachelor 
        #Add the master
def add_staff(tx, name, title, department, email, phone, office):
    tx.run("MERGE (a:Staff {name: $name, title: $title, department: $department, email: $email, phone: $phone, office: $office}) ",
           name=name, title=title, email=email, phone=phone, office=office, department=department)

#add the bachelor tabs
def add_bachelor(tx, course_number, subject, credits):
    tx.run("MERGE (a:BachelorCurriculum {course_number: $course_number, subject: $subject, credits: $credits}) ",
           course_number=course_number, subject=subject, credits=credits)

#add the master tabs under DataScience concentration
def add_master(tx, course_number, subject, credits):
    tx.run("MERGE (a:MasterCurriculum{course_number: $course_number, subject: $subject, credits: $credits}) ",
           course_number=course_number, subject=subject, credits=credits)

#add simple node
def add_node(tx, name,node_type=None):
    if not node_type:
        tx.run("MERGE (a:"+name+"{name:$name})",name=name)
    else:
        tx.run("MERGE (a:"+name+"{name:$name,node_type:$node_type})",name=name,node_type=node_type)

def add_concentration(tx, name, intro, node_type,node_type2):
    tx.run("MERGE (a:Concentration{name: $name, intro: $intro,node_type: $node_type,node_type2: $node_type2})",name=name,intro=intro,node_type=node_type,node_type2=node_type2)

def create_nodes():
    driver = connect()
    with driver.session() as session:
        session.write_transaction(add_node,"DepartmentOfMathematicAndComputerScience")
        session.write_transaction(add_node,"DepartmentStaff")
        session.write_transaction(add_node,"Minors")
        session.write_transaction(add_node,"BachelorsDegree")
        session.write_transaction(add_node,"MasterDegree")
        session.write_transaction(add_node,"ComputerScience","Bachelor")
        session.write_transaction(add_node,"ComputerScience","Master")
        session.write_transaction(add_node,"UndergraduateCertificate")
    driver.close()

def clean_graph():
    driver = connect()
    with driver.session() as session:
        session.write_transaction(run_command, "MATCH (n) DETACH DELETE n")
    driver.close()

def create_relationships():
    driver = connect()
    with driver.session() as session:
        session.write_transaction(run_command, "MATCH (a:DepartmentStaff),(b:Staff) CREATE (a)-[r:contains]->(b)")
        session.write_transaction(run_command, "MATCH (a:DepartmentOfMathematicAndComputerScience),(b:MasterDegree) CREATE (a)-[r:contains]->(b)")
        # DataScience to MasterCurriculum
        session.write_transaction(run_command, "MATCH (a:Concentration  {node_type: 'Master', node_type2:'Data Science'}),(b:MasterCurriculum) CREATE (a)-[r:contains]->(b)")
        session.write_transaction(run_command, "MATCH (a:DepartmentOfMathematicAndComputerScience),(b:DepartmentStaff) CREATE (a)-[r:contains]->(b)")
        session.write_transaction(run_command, "MATCH (a:DepartmentOfMathematicAndComputerScience),(b:Minors) CREATE (a)-[r:contains]->(b)")
        session.write_transaction(run_command, "MATCH (a:DepartmentOfMathematicAndComputerScience),(b:BachelorsDegree) CREATE (a)-[r:contains]->(b)")
        session.write_transaction(run_command, "MATCH (a:Minors),(b:BachelorsDegree) CREATE (a)-[r:contains]->(b)")
        session.write_transaction(run_command, "MATCH (a:DepartmentStaff),(b:BachelorsDegree) CREATE (a)-[r:contains]->(b)")
        # session.write_transaction(run_command, "MATCH (a:BachelorsDegree),(b:Concentration) CREATE (a)-[r:contains]->(b)")
        #New added
        session.write_transaction(run_command, "MATCH (a:BachelorsDegree),(b:ComputerScience {node_type: 'Bachelor'}) CREATE (a)-[r:contains]->(b)")
        session.write_transaction(run_command, "MATCH (a:ComputerScience {node_type: 'Master'}),(b:Concentration  {node_type: 'Master'}) CREATE (a)-[r:contains]->(b)")
        session.write_transaction(run_command, "MATCH (a:ComputerScience {node_type: 'Bachelor'}),(b:Concentration  {node_type: 'Bachelor'}) CREATE (a)-[r:contains]->(b)")
        session.write_transaction(run_command, "MATCH (a:MasterDegree),(b:ComputerScience {node_type: 'Master'}) CREATE (a)-[r:contains]->(b)")
        session.write_transaction(run_command, "MATCH (a:ComputerScienceMaster),(b:Concentration {node_type: 'Master'}) CREATE (a)-[r:contains]->(b)")

    driver.close()

def run_command(tx,command):
    tx.run(command)

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