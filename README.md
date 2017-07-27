# Welcome to AppManager

## How to use project in my computer ?

1. Open a terminal and create folder for project.

2. Clone this repositories:
```
  user@ubuntu:~/newfolder$ git clone https://github.com/gopjak36/my-first-blog.git
```

3. Install virtualenv package:
  ```
    user@ubuntu:~/newfolder$ pip install virtualenv
  ```

4. Create new virtualenv without additional packages from python:
  ```
    user@ubuntu:~/newfolder$ virtualenv newvenv --no-site-package
  ```

5. Open virtualenv:
```
  user@ubuntu:~/newfolder$ source newvenv/bin/active
```

6. Install Django from requirements.txt:
```
  (newvenv)user@ubuntu:~/newfolder$ pip install -r requirements.txt
```

7. Create database:
```
  (newvenv)user@ubuntu:~/newfolder$ python manage.py migrate
```

8. Run project:
```
  (newvenv)user@ubuntu:~/newfolder$ python manage.py runserver
```