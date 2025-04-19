# European Commission Project Manager

This project will help manage a European Commission project. EC projects use Jira from Atlassian, and this application retrieves CSV and JSON files from there, incorporates the information into the app, and performs data mining.

# Table of Contents

1. [Technical Details](#technical-details)
2. [PEC 3 Solution](#pec-3-solution)
3. [Third Example](#third-example)
4. [Fourth Example](#fourth-examplehttpwwwfourthexamplecom)

# Technical Details

## VS Code Setup

To set up VS Code and have the environment ready, follow these steps.

### Create the virtual environment

First, go to the project folder and run:

``` 
python3 -m venv venv
```

### Activate the virtual environment

It depends on the operating system (OS).

__Linux__

```
source venv/bin/activate
```

__Windows (Power shell)__

```
venv\Scripts\Activate.ps1
```

__Windows (Command prompt)__

```
venv\Scripts\activate
```

### Install dependencies

In this case, it's not necessary, but we leave it commented to reuse in other projects:

```
pip install -r requerimientos.txt
```

### Setup configuration

For this execute:

```
pip install -e .
```

### Execute tha APP

To execute the app we must use:

```
python -m app.main
```

# Releases

## Get release data

To get one release by id:

```
https://citnet.tech.ec.europa.eu/CITnet/jira/rest/api/2/version/389637
```
