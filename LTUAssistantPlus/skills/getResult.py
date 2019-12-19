from neo4j_db import run_command, connect
# to find the node with someproperty
# eg: who is the department chair
#start n=node() match n where has (n.title) return n.name
def find_properties(property, text):
    driver = connect()
    with driver.session() as session:
        print ("MATCH (n)  where n."+property+" = '"+text+"' return n.name")
        result = session.run("MATCH (n)  where n."+property+" = '"+text+"' return n.name")
        for record in result:
            print(str(record))
    driver.close()

#to find the node with a specific property
# match (n:person)where n.name=”alice” return n

#multi level search through relationship
# match(na:bank{id:‘001’})-[re1]->(nb:company)-[re2]->(nc:people) return na,re1,nb,re2,nc

def main():
    find_properties('title','Department Chair')


main()