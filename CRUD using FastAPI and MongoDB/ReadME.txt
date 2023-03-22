Course.json - Contains sample data to be inserted in MongoDB Collections.


Script.py - This is a script which will insert the data from course.json to database_assignment schema and assignment_collection Collection.


main.py - This file contains the following API

1 - To get list of courses - http://127.0.0.1:8000/courselist (GET Method)

2 - To get course overview - http://127.0.0.1:8000/overview (GET Method)

3 - To get details of a chapter - http://127.0.0.1:8000/chapter/algebra (GET Method)

4 - To rate a chapter - http://127.0.0.1:8000/rating/algebra/5 (POST Method)