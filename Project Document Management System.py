"""new_shipments = [("apples", 5), ("bananas", 10), ("pears", 7) ]

for item in new_shipments:
    print(item)
    print(item[0])
    print(type(item))
    print(type(item[0]))
    print(type(item[1]))"""

#x = (type(''),type(int))
#print(type(x))
#x = input('please enter the name of new item and quantity:')

#def update_documents(documents,new_docs):

documents = { 
    "Project Plan": "Draft",
    "Risk Register": "Final",
    "Meeting Minutes": "Approved"
             }

New_docs = [("Project Plan", "Final"), ("Budget Report", "Draft"), ("Risk Register", "Approved")]

for x in New_docs:
    if x[0] in documents.keys():
        documents.update({x[0]:x[1]})
    if x[0] not in documents.keys():
        documents.update({x[0]:x[1]}) 
print(documents)




