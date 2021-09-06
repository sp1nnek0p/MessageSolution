import sqlite3
import os

def query_db(dbpathname, query):
    try:
        sqlconnection = sqlite3.connect(dbpathname)
        cursor = sqlconnection.cursor()
        cursor.execute(query)
    except:
        print("ERROR: DB Connection or Query Failed")
    return dict(cursor.fetchall())

if __name__ == "__main__":
    # NOTE: Make sure the message.db is in the same folder or the DB Connection will fail
    dbpath = os.path.dirname(os.path.realpath(__file__)) + "\message.db"
    cypher = query_db(dbpath, 'SELECT * FROM cypher')
    message = query_db(dbpath, 'SELECT * FROM message')
    # Sort the Message Dictionary based on the time stamps (keys)
    sorteditems = dict(sorted(message.items()))
    # Write message to lastMessage variable
    lastMessage = ""
    for item in sorteditems.values():
        lastMessage += str(cypher[item])
    # Print The Message to CLI
    print(lastMessage)
    # Output the Message to a file on drive
    with open(os.path.dirname(os.path.realpath(__file__)) + '\message.txt', 'w') as f:
        f.write(lastMessage)
