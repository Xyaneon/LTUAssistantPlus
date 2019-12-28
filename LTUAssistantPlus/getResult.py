from neo4j_db import run_command, connect
# to find the node with someproperty
# eg: who is the department chair
#start n=node() match n where has (n.title) return n.name
def find_properties(property, text):
    driver = connect()
    data = []
    with driver.session() as session:
        #print ("MATCH (n)  where n."+property+" = '"+text+"' return n.name")
        result = session.run("MATCH (n)  where n."+property+" = '"+text+"' return n.name")
        for record in result:
            data.append(str(record))
    driver.close()
    return data

#What concentrations are available for a Bachelor’s of Science in Computer Science?
def getConcentration(property,type):
    driver = connect()
    data = []
    with driver.session() as session:
        # print("MATCH(n:"+property+") where n.node_type = '"+type+"' return n.name")
        result= session.run("MATCH(n:"+property+") where n.node_type = '"+type+"' return n.name")
        for record in result:
            data.append(str(record))
    driver.close()
    return data


#get office
def getOffice(name):
    driver = connect()
    data = []
    with driver.session() as session:
        #print ("MATCH (n)  where n.name contains '"+name+"' return n.office")
        #MATCH (n)  where n.name contains 'Chung' return n.office
        result = session.run("MATCH (n)  where n.name contains '"+name+"' return n.office")
        for record in result:
            data.append(str(record))
    driver.close()
    return data

from services.assistant_services import AssistantServices

def voiceCommand():
    services = AssistantServices(text_only_mode=False)
    (success, sentence) = services.user_interaction_service.greet_user_and_ask_for_command(services.settings_service.username.capitalize())
    return success, sentence

def q1():
    return find_properties('title','Department Chair')

def q2():
    return getOffice("Chung")

def q3():
    return getConcentration('Concentration','Bachelor')

def extractCommand(text):

    keywords ={ "Department Chair":q1,"dr.":q2,"chung":q2,"chow":q2,"bachelor":q3}

    for k in keywords:
        if k.lower() in text.lower():
            print(k,keywords[k].__name__)
            return keywords[k]
    print("No valid command found")
    return None

def main():
    command = None
    while command is None:
        _, text = voiceCommand()
        print("Text extracted from voice:", text)
        command = extractCommand(text)
    data = command()

    services = AssistantServices(text_only_mode=False)
    
    #services.user_interaction_service.speak("The result is")
    for value in data:
        value = value.split("'")[-2]
        print(value)
        services.user_interaction_service.speak(value)

