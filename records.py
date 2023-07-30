#!/usr/bin/env python3

import cgitb
import cgi
import pymysql
cgitb.enable()
sql_conn = pymysql.connect(db='student_grades',user='root',passwd='Rudrangi03@',host='localhost')
sql_conn_cursor = sql_conn.cursor()
sql_conn_cursor.execute("select * from student_grades")
data = sql_conn_cursor.fetchall()

print("Content-Type:text/html;charset=utf-8")
print()
print("<html>")
print("<head>")
print("""<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">""")
print("<style>")
print("table, th, td {")
print("border:1px solid black;")
print("}")
print("</style>")
print("<title>lab08</title>")
print("</head>")
print("<body>")
print("""  
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="http://localhost/mainpage.html">Lab08</a>
        <div class="collapse navbar-collapse" >
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link" href="http://localhost/mainpage.html">Add record </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="http://localhost/deletepage.html">Delete record </a>
            </li>
          </ul>
        </div>
    </nav>


 """)
print("<div class='container '>")
print("<table style='width:100%'>")
print("<tr>")
print("<th>name</th>")
print("<th>average</th>")
print("</tr>")
for user in data:
    print("<tr>")
    print("<td>{}</td>".format(user[0]))
    print("<td>{}</td>".format(int(user[1] + user[2] + 2*user[3]) / int(4)))
    print("</tr>")

print("</table>")
print("</div>")
print("</body>")
print("</html>")


