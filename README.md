# Simple Repository

This is a simple Python project with some test cases. I connected it to SonarQube to get me the code coverage of the repository. So far it's only telling me python files code coverage

## How to run

To run the main program:


I followed this video mainly to get SonarQube active (https://youtu.be/3zs_S-xvH-M)
First I made sure docker was running then ran the commands, `docker pull sonarqube`
and `docker run -d --name sonarqube-db -e POSTGRES_USER=sonar -e POSTGRES_PASSWORD=sonar -e POSTGRES_DB=sonarqube postgres:alpine`

Then I ran `pytest --cov=. --cov-report=xml` to get an xml report of the python test cases.
*I am not sure why I had to do this. I thought SonarQube would be able to do it for me.*


Next I ran `/Users/eleanorfoley/Documents/WPI/MQP/sonar-scanner-6.2.1.4610-macosx-aarch64/bin/sonar-scanner \
  -Dsonar.projectKey=week1test \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.token=sqp_847fbaa192f7c87a62d5afe7df0b74832385f7dd`

  This was the last step