
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







