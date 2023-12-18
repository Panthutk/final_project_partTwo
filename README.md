# Final project for 2023's 219114/115 Programming I
## Contains file
  * database.py
  * project_manage.py
  * persons.csv
  * login.csv
  * to.md
  * proposal.md
  * Readme.md
## How to run this program?
  - You need to  login as student role first then save the csv by exit the program in terminal to allow the csv to update the run it again then you will allow to used other part of this program
## Tables detailing
 - I only used two csv file that you give but most of it will update person.csv only role in login.csv will update as same as type in person.csv. In person.csv it table will create the following column by using the add_column that I create in database.py
    * `project` project name
    * `detail` project detail
    * `member1` member 1 name
    * `member1_msg` member 1 invitation message
    * `member2_msg` member 2 invitation message
    * `member2` member 2 name
    * `advisor` advisor of this project
    * `advisor_status` advisor status default when summit is pending
    * `advisor_msg` advisor message to following project
    * `status1` status of invitation from lead to member 1
    * `status2` status of invitation from lead to member 2
    * `submit` submit it will tricker when choose submit to pending then wait for the advisor to check it
## A list of missing features and outstanding bugs, detailing actions for a particular role you have not implemented together with known bugs
 * A program require to fully run until exit the program to update the csv if it not or any error pop up you will lost all process and need to redo again
 * The advisor Im not sure much clear much about the instruction so I used the faculty role as advisor.