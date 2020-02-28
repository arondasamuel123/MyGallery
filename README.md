# Django Photo Gallery
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description
This a web application built using Python, Django and Postgresql.The app allows you view photos that interest me. You can click on a single photos to expand it and view the details of the photo. The photo details appear on a modal within the same route as the main page. You can also search different categories of photos e.g Travel, Food. Copy a link to the photo to share with my friends.You can view the location based on the location they were taken.


## Author

Samuel Aronda


## DB diagram
![](images/PhotoGallery.png)

# Installation

## Clone
    
```bash
    git clone https://github.com/arondasamuel123/MyGallery.git
    
```
##  Create virtual environment
```bash
    python3.6 -m venv --without-pip
    
```
## Activate virtual and install requirements.txt
```bash
   $ source virtual/bin/activate
   $ pip install - requirements.txt
    
```
## Run initial migration
```bash
   $ python3.6 manage.py makemigrations gallery
   $ python3.6 manage.py migrate
    
```


## Run app
```bash
   $ python3 manage.py runserver
    
```

## Test class

```bash
    $ python3 manage.py test
```
## Known Bugs


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Technologies Used
    Python Shell
    Python 3.6
    Django
    Materialize
    HTML
    CSS
    PostgreSQL



## License
[LICENSE](LICENSE)




