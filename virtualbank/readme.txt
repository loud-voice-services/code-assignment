README - Loud Voice Services - Virtual Bank 

----------------------------BEGIN------------------------------------
pull the project from git
open project folder (virtualbank)
mvn clean (needs maven installed)
mvn package (needs maven installed)

----------------------------DOCKER-----------------------------------
start docker
docker build -f Dockerfile -t virtual-bank .    (in project folder)
docker run -p 8085:8085 virtual-bank

test the application using the configured docker url, normal cases are http://192.168.99.100:8085

----------------------------DATA BASE--------------------------------
to access h2 database
http://192.168.99.100:8085/h2-console
jdbc-url: jdbc:h2:mem:testdb
user:     sa
password: password

----------------------------SWAGGER----------------------------------
to access swagger
http://192.168.99.100:8085/swagger-ui.html

----------------------------ENDPOINTS--------------------------------
http://192.168.99.100:8085/
http://192.168.99.100:8085/login
http://192.168.99.100:8085/accounts  (to create users)
http://192.168.99.100:8085/private *
http://192.168.99.100:8085/accounts/deposit *
http://192.168.99.100:8085/accounts/withdraw *
http://192.168.99.100:8085/accounts/balance *

* needs login, send the fields username and password to create an account, sample:
curl -d "email=elio@test.com&password=123" -X POST http://192.168.99.100:8085/accounts

