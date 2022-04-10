from http.client import HTTPConnection
conn=HTTPConnection("https://www.w3resource.com/python-exercises/python-basic-exercise-101.php")
conn.request("GET","/")
resp=conn.getresponse()
results=resp.read()
print(results)