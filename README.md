# Flask factory quick start

🌶️ A Flask snippets repository using the application factories pattern.


Feel free to clone, fork, or/and change this snippet! 😄

## How to run

```
$ FLASK_APP=myapp/app.py flask run
```

## How the application is structured



The application uses the factory pattern to build a Flask app. The ```app.py``` has the ```create_app``` factory that is automatically identified by Flask. The ```blueprint``` folder is where the application's [Blueprints](https://flask.palletsprojects.com/en/master/blueprints/#blueprints) are defined. The ```extensions``` folder is where the extensions factories are defined.

### The project structure

```
.
├── myapp  (MAIN PACKAGE)
│   ├── app.py  (APP FACTORIES)
│   ├── blueprints  (BLUEPRINTS)
│   │   ├── __init__.py
│   │   └── helloworld  
│   │       ├── __init__.py
│   │       └── helloworld.py
│   ├── extensions  (EXTENSIONS FACTORIES)
│   │   └── __init__.py
│   └── __init__.py
├── README.md
├── .gitignore
└── LICENSE
```



> That structure is highly inspered by [Flask's Application Factories Pattern](https://flask.palletsprojects.com/en/master/patterns/appfactories/)
and [Arquitetura Definitiva para o Projeto Web com Python e Flask](https://www.youtube.com/watch?v=-qWySnuoaTM) ([repository](https://github.com/codeshow/003-arquitetura-flask)) created by [@rochacbruno](https://github.com/rochacbruno).
