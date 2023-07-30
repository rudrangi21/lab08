#!/usr/bin/env python3

import cgitb
import cgi
import pymysql
cgitb.enable()
form = cgi.FieldStorage()
name = str(form.getvalue('name'))
print("Content-Type:text/html;charset=utf-8")
print()

print("<html>")
print("<head>")
print("""<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">""")
print("<title>lab08</title>")
print("</head>")
print("<body>")
print("""  
    <nav class="navbar navbar-expand-lg navbar-lightbg-light">
        <a class="navbar-brand" href="http://localhost/mainpage.html">Lab08</a>
        <div class="collapse navbar-collapse" >
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link" href="http://localhost/mainpage.html">Add record </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="http://localhost/deletepage.html">Delete record </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="http://localhost/records.py">view record</a>
            </li>
          </ul>
        </div>
    </nav>


 """)
print("<div class='container'>")
print("<h2>{} record deleted successfully </h2>".format(name))
print("</div>")
print("</body>")
print("</html>")



sql_conn = pymysql.connect(db='student_grades',user='root',passwd='Rudrangi03@',host='localhost')
sql_conn_cursor = sql_conn.cursor()
sql_conn_cursor.execute("delete from student_grades where student_name = '{}'".format(name))
sql_conn.commit()
