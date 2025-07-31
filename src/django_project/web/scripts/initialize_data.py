from datetime import datetime
from zoneinfo import ZoneInfo

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
            "description": "Grab some coffee and write code, together. Every first Monday of the month, local tech enthusiasts meet at a coffee shop to collaborate on code, or just talk tech.",
            "start_date_time": "2025-10-06T07:00:00",
            "end_date_time": "2025-10-06T08:00:00",
            "location": "Indaba Coffee",
            "url": "https://www.meetup.com/python-spokane/events/308944537",
        },
        {
            "name": "Coffee and Code",
            "description": "Grab some coffee and write code, together. Every first Monday of the month, local tech enthusiasts meet at a coffee shop to collaborate on code, or just talk tech.",
            "start_date_time": "2025-09-01T07:00:00",
            "end_date_time": "2025-09-01T08:00:00",
            "location": "Indaba Coffee",
            "url": "https://www.meetup.com/python-spokane/events/310155895",
        },
        {
            "name": "Coffee and Code",
            "description": "Grab some coffee and write code, together. Every first Monday of the month, local tech enthusiasts meet at a coffee shop to collaborate on code, or just talk tech.",
            "start_date_time": "2025-08-04T07:00:00",
            "end_date_time": "2025-08-04T08:00:00",
            "location": "Indaba Coffee",
            "url": "https://www.meetup.com/python-spokane/events/308977832",
        },
        {
            "name": "Coffee and Code",
            "description": "Grab some coffee and write code, together. Every first Monday of the month, local tech enthusiasts meet at a coffee shop to collaborate on code, or just talk tech.",
            "start_date_time": "2025-07-07T07:00:00",
            "end_date_time": "2025-07-07T08:00:00",
            "location": "Indaba Coffee",
            "url": "https://www.meetup.com/python-spokane/events/306382747",
        },
        {
            "name": "Coffee and Code",
            "description": "Grab some coffee and write code, together. Every first Monday of the month, local tech enthusiasts meet at a coffee shop to collaborate on code, or just talk tech.",
            "start_date_time": "2025-06-02T07:00:00",
            "end_date_time": "2025-06-02T08:00:00",
            "location": "Indaba Coffee",
            "url": "https://www.meetup.com/python-spokane/events/306382746",
        },
        {
            "name": "Coffee and Code",
            "description": "Grab some coffee and write code, together. Every first Monday of the month, local tech enthusiasts meet at a coffee shop to collaborate on code, or just talk tech.",
            "start_date_time": "2025-05-05T07:00:00",
            "end_date_time": "2025-05-05T08:00:00",
            "location": "Indaba Coffee",
            "url": "https://www.meetup.com/python-spokane/events/306382744",
        },
        {
            "name": "Coffee and Code",
            "description": "Grab some coffee and write code, together. Every first Monday of the month, local tech enthusiasts meet at a coffee shop to collaborate on code, or just talk tech.",
            "start_date_time": "2025-04-07T07:00:00",
            "end_date_time": "2025-04-07T08:00:00",
            "location": "Indaba Coffee",
            "url": "https://www.meetup.com/python-spokane/events/306368361",
        },
        {
            "name": "Coffee and Code",
            "description": "Grab some coffee and write code, together. Every first Monday of the month, local tech enthusiasts meet at a coffee shop to collaborate on code, or just talk tech.",
            "start_date_time": "2025-03-03T07:00:00",
            "end_date_time": "2025-03-03T08:00:00",
            "location": "Indaba Coffee",
            "url": "https://www.meetup.com/python-spokane/events/305925589",
        },
        {
            "name": "Coffee and Code",
            "description": "Grab some coffee and write code, together. Every first Monday of the month, local tech enthusiasts meet at a coffee shop to collaborate on code, or just talk tech.",
            "start_date_time": "2025-02-03T07:00:00",
            "end_date_time": "2025-02-03T08:00:00",
            "location": "Indaba Coffee",
            "url": "https://www.meetup.com/python-spokane/events/305609285",
        },
        {
            "name": "Coffee and Code",
            "description": "Grab some coffee and write code, together. Every first Monday of the month, local tech enthusiasts meet at a coffee shop to collaborate on code, or just talk tech.",
            "start_date_time": "2025-01-06T07:00:00",
            "end_date_time": "2025-01-06T08:00:00",
            "location": "Indaba Coffee",
            "url": "https://www.meetup.com/python-spokane/events/305044389",
        },
        {
            "name": "Getting started with Pulumi",
            "description": "Ready to streamline your infrastructure management? Join us for our next meetup where we'll dive deep into Infrastructure as Code (IaC) using Pulumi with Python examples!",
            "start_date_time": "2025-07-23T17:30:00",
            "end_date_time": "2025-07-23T19:00:00",
            "location": "IntelliTect",
            "url": "https://www.meetup.com/python-spokane/events/309061819",
        },
        {
            "name": "GitHub Copilot Global Bootcamp",
            "description": "Spokane Python User Group Update: Join Spokane DevOps Meetup This Month!",
            "start_date_time": "2025-06-19T13:00:00",
            "end_date_time": "2025-06-19T16:00:00",
            "location": "IntelliTect",
            "url": "https://www.meetup.com/python-spokane/events/308298845",
        },
        {
            "name": "From Data to Dream Home: A Data Scientist's Workflow in Python",
            "description": """What does a data scientist actually do from start to finish? In this demo, we walk through a full data science workflow using a real estate use case: finding the optimal house to buy.
We'll cover data collection, exploratory analysis, feature engineering, model building, and interpretation — all with hands-on Python code. Along the way, you’ll see how tools like Pandas, scikit-learn, and visualization libraries come together to solve a real-world problem.
Whether you're a data practitioner or just curious about applied data science, this talk will bring the process to life through a practical and engaging example around real estate.""",
            "start_date_time": "2025-05-20T17:30:00",
            "end_date_time": "2025-05-20T19:30:00",
            "location": "Burbity Workspaces - Sullivan Valley Commons",
            "url": "https://www.meetup.com/python-spokane/events/307606946",
        },
        {
            "name": "Community Show & Tell",
            "description": "Join us for an interactive Show & Tell event in collaboration with Launchpad INW! This is a relaxed and informal gathering where members of our local tech community are invited to present interesting projects, innovative ideas, or anything they're currently passionate about. Whether you're a seasoned developer, a budding entrepreneur, or just curious about the tech landscape, this event is for you! Come to present, network with fellow tech enthusiasts, or just discover the amazing things being built right here in Spokane.",
            "start_date_time": "2025-04-23T17:30:00",
            "end_date_time": "2025-04-23T19:30:00",
            "location": "Fuel Coworking",
            "url": "https://www.meetup.com/python-spokane/events/307187069",
        },
        {
            "name": "Join Us for a Special Python & Rust Meetup!",
            "description": "Are you interested in starting your next project in Python or Rust but unsure where to begin? Whether you're new to coding or looking to explore a new language, this event is for you!",
            "start_date_time": "2025-03-18T17:30:00",
            "end_date_time": "2025-03-18T19:30:00",
            "location": "Limelyte Technology Group, Inc.",
            "url": "https://www.meetup.com/python-spokane/events/306366620",
        },
        {
            "name": "Spokane Python User Group Monthly Meetup",
            "description": "This months meetup will be on a Wednesday 01/22. We are diverting from our regularly schedule date to join with the Spokane Go Users Group for an informal show and tell.",
            "start_date_time": "2025-01-22T17:30:00",
            "end_date_time": "2025-01-22T19:30:00",
            "location": "Limelyte Technology Group, Inc.",
            "url": "https://www.meetup.com/python-spokane/events/304921795",
        },
        {
            "name": "2024 Holiday Hangout",
            "description": "Hello Pythonistas! Join us for a jolly good time as our tech community comes together to celebrate the holiday season in style! Whether you're a coder, designer, tinkerer, or tech enthusiast, we’re all about festive cheer and good vibes.No presentation or topic this month, just a cool hang with your friends in the local tech community.",
            "start_date_time": "2024-12-17T18:00:00",
            "end_date_time": "2024-12-17T20:00:00",
            "location": "No-Li Brewhouse",
            "url": "https://www.meetup.com/python-spokane/events/304949560",
        },
    ]

    # Use ZoneInfo for timezone handling instead of pytz
    for event in events:
        # Parse and localize to PDT, then convert to UTC and format as ISO string
        start_dt = datetime.fromisoformat(event["start_date_time"]).replace(tzinfo=ZoneInfo("America/Los_Angeles"))
        end_dt = datetime.fromisoformat(event["end_date_time"]).replace(tzinfo=ZoneInfo("America/Los_Angeles"))
        event["start_date_time"] = start_dt.astimezone(ZoneInfo("UTC")).isoformat()
        event["end_date_time"] = end_dt.astimezone(ZoneInfo("UTC")).isoformat()

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
