import couchdb2
from rest_framework.response import Response

server = couchdb2.Server(href='http://localhost:5984/', username='admin', password='morgan2d', use_session=True, ca_file=None)
db = server.get('test', check=True)

result = []
for id in db.ids():
    result.append(id)
finalobject = []
for i in range(len(result)):
    finalobject.append(db.get(result[i], rev=None, revs_info=False, default=None, conflicts=False))
doc = db.get(result[3], rev=None, revs_info=False, default=None, conflicts=False)

def get_result(self):
    return Response(finalobject)
# in  views return 
# return Response(finalobject)