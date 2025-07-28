from web.models import Event, Resource, ResourceCategory


def create_resource_categories() -> None:
    categories: list[str] = [
        "Beginner Resources",
        "Web Development",
        "Data Science",
        "Machine Learning",
        "DevOps",
        "Scientific Computing",
    ]
    for category_name in categories:
        ResourceCategory.objects.get_or_create(name=category_name)


def create_resources() -> None:
    resources: list[dict[str, str]] = [
        # Beginner Resources
        {
            "name": "Python for Everybody",
            "description": "A free online course for beginners to learn Python.",
            "url": "https://www.py4e.com/",
            "category": "Beginner Resources",
        },
        {
            "name": "Real Python",
            "description": "A comprehensive resource for learning Python with tutorials, articles, and courses.",
            "url": "https://realpython.com/",
            "category": "Beginner Resources",
        },
        {
            "name": "Switching to Python",
            "description": "A guide to help you transition to Python from other programming languages.",
            "url": "https://realpython.com/switching-to-python/",
            "category": "Beginner Resources",
        },
        {
            "name": "Python.org",
            "description": "The official Python website with documentation, tutorials, and resources.",
            "url": "https://www.python.org/",
            "category": "Beginner Resources",
        },
        {
            "name": "Python Tutorial",
            "description": "The official Python tutorial for beginners.",
            "url": "https://docs.python.org/3/tutorial/introduction.html",
            "category": "Beginner Resources",
        },
        {
            "name": "Automate the Boring Stuff with Python",
            "description": "A practical introduction to Python for total beginners.",
            "url": "https://automatetheboringstuff.com/",
            "category": "Beginner Resources",
        },
        {
            "name": "Essential Reads for Any Python Programmer",
            "description": "A curated list of must-read books and resources for Python developers.",
            "url": "http://notesbyanerd.com/2017/12/29/essential-reads-for-any-python-programmer/",
            "category": "Beginner Resources",
        },
        {
            "name": "Python Guide",
            "description": "A comprehensive guide to Python programming.",
            "url": "https://docs.python-guide.org/",
            "category": "Beginner Resources",
        },
        {
            "name": "What does Pythonic mean?",
            "description": "A discussion on what it means for code to be 'Pythonic'.",
            "url": "https://stackoverflow.com/questions/25011078/what-does-pythonic-mean",
            "category": "Beginner Resources",
        },
        {
            "name": "PEP 20 - The Zen of Python",
            "description": "The Zen of Python, by Tim Peters.",
            "url": "https://www.python.org/dev/peps/pep-0020/",
            "category": "Beginner Resources",
        },
        {
            "name": "PEP 8 - Style Guide for Python Code",
            "description": "The official style guide for Python code.",
            "url": "https://www.python.org/dev/peps/pep-0008/",
            "category": "Beginner Resources",
        },
        # Web Development
        {
            "name": "Django",
            "description": "Official documentation for Django, a high-level Python web framework.",
            "url": "https://docs.djangoproject.com/en/stable/",
            "category": "Web Development",
        },
        {
            "name": "FastAPI",
            "description": "Official documentation for FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints.",
            "url": "https://fastapi.tiangolo.com/",
            "category": "Web Development",
        },
        {
            "name": "Flask",
            "description": "Official documentation for Flask, a lightweight WSGI web application framework.",
            "url": "https://flask.palletsprojects.com/",
            "category": "Web Development",
        },
        {
            "name": "Streamlit",
            "description": "Official documentation for Streamlit, a framework for building data apps in Python.",
            "url": "https://docs.streamlit.io/",
            "category": "Web Development",
        },
        {
            "name": "Dash",
            "description": "Official documentation for Dash, a productive Python framework for building web applications.",
            "url": "https://dash.plotly.com/",
            "category": "Web Development",
        },
        # Data Science
        {
            "name": "NumPy",
            "description": "A fundamental package for scientific computing with Python.",
            "url": "https://numpy.org/",
            "category": "Data Science",
        },
        {
            "name": "Pandas",
            "description": "A powerful data analysis and manipulation library for Python.",
            "url": "https://pandas.pydata.org/",
            "category": "Data Science",
        },
        {
            "name": "Matplotlib",
            "description": "A plotting library for the Python programming language and its numerical mathematics extension NumPy.",
            "url": "https://matplotlib.org/",
            "category": "Data Science",
        },
        {
            "name": "Seaborn",
            "description": "A Python visualization library based on Matplotlib that provides a high-level interface for drawing attractive statistical graphics.",
            "url": "https://seaborn.pydata.org/",
            "category": "Data Science",
        },
        {
            "name": "Plotly",
            "description": "A graphing library for Python that makes interactive, publication-quality graphs online.",
            "url": "https://plotly.com/python/",
            "category": "Data Science",
        },
        {
            "name": "polars",
            "description": "A fast DataFrame library implemented in Rust and designed for performance.",
            "url": "https://pola.rs/",
            "category": "Data Science",
        },
        # Machine Learning and Artificial Intelligence
        {
            "name": "TensorFlow",
            "description": "An end-to-end open source platform for machine learning.",
            "url": "https://www.tensorflow.org/",
            "category": "Machine Learning",
        },
        {
            "name": "PyTorch",
            "description": "An open source machine learning framework that accelerates the path from research to production.",
            "url": "https://pytorch.org/",
            "category": "Machine Learning",
        },
        {
            "name": "Keras",
            "description": "An open-source software library that provides a Python interface for neural networks.",
            "url": "https://keras.io/",
            "category": "Machine Learning",
        },
        {
            "name": "Scikit-learn",
            "description": "A machine learning library for Python that features various classification, regression, and clustering algorithms.",
            "url": "https://scikit-learn.org/",
            "category": "Machine Learning",
        },
        {
            "name": "XGBoost",
            "description": "An optimized distributed gradient boosting library designed to be highly efficient, flexible, and portable.",
            "url": "https://xgboost.readthedocs.io/en/latest/",
            "category": "Machine Learning",
        },
        # DevOps and Automation
        {
            "name": "Ansible",
            "description": "An open-source automation tool for software provisioning, configuration management, and application deployment.",
            "url": "https://www.ansible.com/",
            "category": "DevOps",
        },
        {
            "name": "SaltStack",
            "description": "An open-source software for event-driven IT automation, remote task execution, and configuration management.",
            "url": "https://saltstack.com/",
            "category": "DevOps",
        },
        {
            "name": "Selenium",
            "description": "A suite of tools for automating web browsers.",
            "url": "https://www.selenium.dev/",
            "category": "DevOps",
        },
        {
            "name": "Fabric",
            "description": "A Python library and command-line tool for streamlining the use of SSH for application deployment.",
            "url": "https://www.fabfile.org/",
            "category": "DevOps",
        },
        # Scientific Computing
        {
            "name": "Jupyter",
            "description": "An open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and narrative text.",
            "url": "https://jupyter.org/",
            "category": "Scientific Computing",
        },
        {
            "name": "Matplotlib",
            "description": "A plotting library for the Python programming language and its numerical mathematics extension NumPy.",
            "url": "https://matplotlib.org/",
            "category": "Scientific Computing",
        },
        {
            "name": "SymPy",
            "description": "A Python library for symbolic mathematics.",
            "url": "https://www.sympy.org/",
            "category": "Scientific Computing",
        },
        {
            "name": "SciPy",
            "description": "A Python library used for scientific and technical computing.",
            "url": "https://www.scipy.org/",
            "category": "Scientific Computing",
        },
        {
            "name": "Biopython",
            "description": "A set of tools for biological computation.",
            "url": "https://biopython.org/",
            "category": "Scientific Computing",
        },
    ]

    for resource in resources:
        category: ResourceCategory = ResourceCategory.objects.get(name=resource["category"])
        Resource.objects.get_or_create(
            name=resource["name"],
            description=resource["description"],
            url=resource["url"],
            category=category,
        )


def create_events() -> None:
    events: list[dict[str, str]] = [
        {
            "name": "Coffee and Code",
            "description": "Join us to talk code, work on coding projects, share knowledge, or just hang out.",
            "start_date_time": "2025-08-04T07:00:00",
            "end_date_time": "2025-08-04T09:00:00",
            "location": "Indaba Coffee, Spokane",
            "url": "https://www.meetup.com/python-spokane/events/308977832",
        },
        {
            "name": "Spokane Python User Group Monthly Meetup",
            "description": "Join us for our monthly meetup to discuss Python, share knowledge, and network with fellow Python enthusiasts.",
            "start_date_time": "2025-08-15T18:00:00",
            "end_date_time": "2025-08-15T20:00:00",
            "location": "Spokane Public Library, Downtown Branch",
            "url": "https://www.meetup.com/python-spokane/events/309061819",
        },
        {
            "name": "Coffee and Code",
            "description": "Join us to talk code, work on coding projects, share knowledge, or just hang out.",
            "start_date_time": "2025-07-03T07:00:00",
            "end_date_time": "2025-07-03T08:00:00",
            "location": "Indaba Coffee, Spokane",
            "url": "https://www.meetup.com/python-spokane/events/306382746",
        },
        {
            "name": "Python Workshop: Data Analysis with Pandas",
            "description": "A hands-on workshop where you will learn how to use Pandas for data analysis in Python.",
            "start_date_time": "2025-07-22T10:00:00",
            "end_date_time": "2025-07-22T12:00:00",
            "location": "Intellitect, Spokane",
            "url": "https://www.meetup.com/python-spokane/events/308298845",
        },
        {
            "name": "Coffee and Code",
            "description": "Join us to talk code, work on coding projects, share knowledge, or just hang out.",
            "start_date_time": "2025-06-03T07:00:00",
            "end_date_time": "2025-06-03T08:00:00",
            "location": "Indaba Coffee, Spokane",
            "url": "https://www.meetup.com/python-spokane/events/306382744",
        },
        {
            "name": "Python for Beginners",
            "description": "An introductory workshop for those new to Python programming.",
            "start_date_time": "2025-06-29T10:00:00",
            "end_date_time": "2025-06-29T12:00:00",
            "location": "Limelight, Spokane",
            "url": "https://www.meetup.com/python-spokane/events/308298845",
        },
        {
            "name": "Coffee and Code",
            "description": "Join us to talk code, work on coding projects, share knowledge, or just hang out.",
            "start_date_time": "2025-05-03T07:00:00",
            "end_date_time": "2025-05-03T08:00:00",
            "location": "Indaba Coffee, Spokane",
            "url": "https://www.meetup.com/python-spokane/events/306382744",
        },
        {
            "name": "Advanced Python Techniques",
            "description": "A workshop for experienced Python developers to learn advanced techniques and best practices.",
            "start_date_time": "2025-05-15T10:00:00",
            "end_date_time": "2025-05-15T12:00:00",
            "location": "Intellitect, Spokane",
            "url": "https://www.meetup.com/python-spokane/events/308298845",
        },
        {
            "name": "Coffee and Code",
            "description": "Join us to talk code, work on coding projects, share knowledge, or just hang out.",
            "start_date_time": "2025-04-03T07:00:00",
            "end_date_time": "2025-04-03T08:00:00",
            "location": "Indaba Coffee, Spokane",
            "url": "https://www.meetup.com/python-spokane/events/306382744",
        },
        {
            "name": "Python in Data Science",
            "description": "A workshop focused on using Python for data science applications.",
            "start_date_time": "2025-04-20T10:00:00",
            "end_date_time": "2025-04-20T12:00:00",
            "location": "Limelight, Spokane",
            "url": "https://www.meetup.com/python-spokane/events/308298845",
        },
    ]

    for event in events:
        Event.objects.get_or_create(
            name=event["name"],
            description=event["description"],
            start_date_time=event["start_date_time"],
            end_date_time=event["end_date_time"],
            location=event["location"],
            url=event["url"],
        )


def run() -> None:
    create_resource_categories()
    create_resources()
    create_events()
