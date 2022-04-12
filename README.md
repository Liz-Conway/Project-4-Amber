![Amber logo](static/images/amber-logo.png)
# Amber - Hippotherapy measurement tool

## Table of Contents
<details>
<summary>## [Overview](#overview)</summary>
### [Who is this app for?](#who-for)
### [What does it do?](#what-do)
</details>
## [Screen Mockup](#mockup)
## [Features](#features)
### [Known Bugs](#known-bugs)
### [Future features](#future-features)
## [Data Model](#data-model)
### [Entity Model](#entity-model)
### [Entity Relationship Model](#erd)
### [Python Structure](#python-structure)
## [UX](#ux)
### [Storyboard](#storyboard)
### [Personas](#personas)
### [Customer Journey Maps](#cjm)
### [Wireframes](#wireframes)
### [Flow Chart](#flow-chart)
#### [Key](#flow-key)
### [Site Map](#site-map)
### [Accessibility](#accessibility)
## [Design Decisions](#design-decisions)
### [Colours](#colours)
### [Usability](#usability)
## [Software Development Process](#software-development)
### [Agile Methodology](#agile)
### [Project Planning](#planning)
### [Version control](#git)
### [Testing](#testing)
### [Documentation](#documentation)
### [Deployment](#deployment)
## [Technology Used](#technology)
### [Some of the technology used](#technology-used)
## [Contributing](#contributing)
### [Clone](#clone)
### [Fork](#fork)
### [Clone versus Fork](#clone-fork)
## [Credit](#credit)


## <a id="overview"></a>Overview
Hippotherapy is the practise of performing Occupational Therapy exercises, whilst mounted on a horse.  Hippotherapy improves neurological function, sensory processing by providing carefully constructed graded motor and sensory input.  It is during ambulation that the horse provides rhythmic movement which in turn stimulates the anterior, and posterior swinging movements, this encourages proper balance, posture, and strengthening of core muscles which are required for daily functional tasks from climbing stairs, writing, speaking, listening and engaging in the world successfully. 

Hippotherapy can also shorten recovery time and ensure correct development of the paraspinal muscles.  Multifaceted swinging movement and rhythm of the horse’s gait effects the bones of the patient’s girdle twice more strongly than the gait of the individual patient.  The therapeutic benefit needs to be measured and Natalia OT has created an application that measures this precisely.   

Using Amber as a Hippotherapy measurement tool will serve to prove the therapeutic benefits of Hippotherapy as an essential and much required occupational therapy for people with special needs, brain injuries, etc.; shortening the recovery time of medical and surgical treatment. 

### <a id="who-for"></a>Who is this app for?
This web-based app is for all Occupational Therapists who are involved in providing Hippotherapy sessions to clients.
 
 
### <a id="what-do"></a>What does it do?
Amber measures and records the therapeutic benefits of Hippotherapy.
  
 
 ## <a id="how-work"></a>How does it work
Amber captures, documents and records Key Performance Indicators for individual Hippotherapy sessions and displays the results in an straightforward manner.


## <a id="mockup"></a>Screen Mockup

![Mockup of screen](documentation/mockup/mockup.png)

## <a id="features"></a>Features


### <a id="known-bugs"></a>Known Bugs

### <a id="future-features"></a>Future feature
Since Amber is a "real-life" project, this section will be used to "de-scope" some of the Use Cases and User Stories.  This will provide a Minimum Viable Product for the end-user which will also meet the criteria for examination by Code Institute. 


## <a id="data-model"></a>Data model

### <a id="entity-diagram"></a>Entity Diagram

### <a id="erd"></a>Entity Relationship Diagram

### <a id="python-structure"></a>Python structure

## <a id="ux"></a>UX

### <a id="storyboard"></a>Storyboard

### <a id="personas"></a>Personas

### <a id="cjm"></a>Customer Journey Maps

### <a id="wireframes"></a>Wireframes


## <a id="flow-chart"></a>Flow chart
### <a id="flow-key"></a>Key

|Type|Symbol|
| --- | --- |
|Input | ![Input symbol](documentation/flow-chart/input.png)|
|Output |![Output symbol](documentation/flow-chart/output.png)|
|Process |![Process symbol](documentation/flow-chart/process.png)|
|Code |![Code symbol](documentation/flow-chart/code.png)|



<img alt="Flow chart for Amber" src="documentation/flow-chart/hitchhikers-flow-chart.png" width="100%">

### <a id="site-map"></a>Site Map

### <a id="accessibility"></a>Accessibility

## <a id="design-decisions"></a>Design Decisions


### <a id="colours"></a>Colours
The main colours for the Amber application were deliberately chosen to invoke specific emotional reponses from the user.
*white* - Amber is first and foremost a clinical application.  Therefore the background is deliberately set to white.  White is perceived to be a sterile and clinical colour.  The predominance of this colour on every page enforces this idea of Amber being a tool for serious clinicians.
*orange* - Orange is associated with both energy and warmth.  This colour is used throughout the Amber application to invoke a welcoming feeling from the user, as well as to show that there a certain vibrancy about the application.
*blue* - Blue is a colour that makes people feel safe.  Websites often use the colour blue when they want to make their users trust them.

The use of colours in the Amber application should make the user feel welcomed and trusting.  Whilst at the same time the user knows that this is not a "fun" app, but a serious tool that will be used by professionals.

### <a id="usability"></a>Usability
- **Suitability for purpose**
    
- **Ease of use**
    
- **Information Display** 
    

## <a id="software-development"></a>Software Development Process

### <a id="agile"></a>Agile methodology
The use cases were arranged as Epics, the Epics were broken down into User Stories.  Acceptance criteria were developed for every User Story.

[Trello](https://trello.com/b/0wEVCThe/amber-p4-ci-project) was used as the Agile tool for managing this project.  Each User Story was embodied in a trello card.  Each of these cards was added to a Kanban board.  The Kanban board was set up with a number of lists:
* Story
* ToDo
* Doing always - iteration
* In Process (Code the ... / Test the ...)
* Testing
* Code review
* Done

When a Story is being coded it is moved from the **ToDo** list into the **In Process** list.  When the code is finished for a story it is moved into the **Testing** list.  Once a story has been tested it is moved to the **Code Review** list.  When the code has been reviewed with the mentor is it moved to the **Done** list and is completed.

At the end of the project, all User Stories will be in the **Done** list and the project will be finished.

### <a id="planning"></a>Project Planning
The Amber project's User Stories have been allocated into Sprints.  The stories in each Sprint will go through the full process of *ToDo* **>** *In Process* **>** *Testing* **>** *Code Review* **>** *Done*, before the next Sprint begins.

<img src="static/documentation/agile-planning/Amber-board-story-map.png" alt="User Story Map Sprint plan" width="100%"/>


### <a id="git"></a>Version Control 
**Git** is used for version control of this project
- Git commit message prefix convention denoting the type of change made in this commit:
    - DOC: Documentation
    - FEAT: Feature
    - FIX: Bugfix
    - STYLE: Changes to CSS
    - REFACTOR: Where changes are made that do not change the functionality.
- Git messages will be no longer than 50 characters long.

**GitHub** is used as the central version control repository for this project.

### <a id="testing"></a>Testing 
Testing is documented in the [Testing document](documentation/test/TESTING.md)

### <a id="vakidation"></a>Validation
Source code was validated with [PEP8 Validator](http://pep8online.com/).


### <a id="documentation"></a>Documentation  
- README.md :  Comprehensive overview of the Hitchhikers Guide to the Red planet application detailing how it works, what its features are, the technologies involved and all the design decisions that were made in creating this command line application.
- [Vision doc](static/documentation/requirements/vision-doc-amber.docx) :  Business needs and feature list.
 

### <a id="deployment"></a>Deployment
This project is deployed to [Heroku](https://amber-ci.herokuapp.com/)

1. Push the code to Github using `git push`.

2. Go to the [Heroku Dashboard](https://dashboard.heroku.com/apps)

3. In the Heroku Dashboard, click on the *Create new app* button.

![Create new App](static/documentation/deploy/heroku-create-new-app.png)


4. Enter an app name (*amber-ci*) and region (*Europe*) and click the *Create app* button.

![Create app](static/documentation/deploy/heroku-create-app.png)


5. Click on *Settings* tab

![Heroku Settings](static/documentation/deploy/heroku-settings.png)

6. In the 'Config Vars' section, click on *Reveal Config Vars*.  Add a key of **PORT** and a value of **8000**.  Click *Add* button.

![Reveal config vars](static/documentation/deploy/heroku-reveal-config-vars.png)
![Config vars](static/documentation/deploy/heroku-config-vars.png)

7. In the 'Build Packs' section, click on *Add Build Pack* button.  Select **Python**.  Click *Save Changes* button.

![Build Packs section](static/documentation/deploy/heroku-add-buildpack.png)
![Python & nodejs buildpacks](static/documentation/deploy/heroku-buildpacks.png)

8. Click on *Add Build Pack* button again and select **nodejs**. Click *Save Changes* button.

![Build packs added](static/documentation/deploy/heroku-buildpacks-added.png)

9. Click on *Deploy* tab.

![Heroku deploy tab](static/documentation/deploy/heroku-deploy.png)

10. Choose Deployment Method *Github*.

![Heroku deployment method](static/documentation/deploy/heroku-deployment-method.png)

11. In *Connect to Github* section, type **Hitchhiker** in the *repo-name* box and click *Search* button.

![Search github](static/documentation/deploy/heroku-search-github.png)

12. Click the *Connect* button next to **Liz-Conway/Project-3-Python**.

![Connect to github](static/documentation/deploy/heroku-hitchhiker-connect.png)

13. Heroku app is now connected to the Github repository.

![Heroku connected to Github](static/documentation/deploy/heroku-connected-github.png)

14. Go to *Manual deploy* section, ensure the branch to deploy is **main**.  Click on *Deploy Branch* button.

![Manual deploy app](static/documentation/deploy/heroku-manual-deploy.png)

15. Once the app is successfully deployed click on the *view* button, or navigate to [Amber application](https://amber-ci.herokuapp.com/) to run the application.

![App successfully deployed](static/documentation/deploy/heroku-successful-deploy.png)

16. Once the app has been deployed you can access it by navigating to [Amber application](https://amber-ci.herokuapp.com/) to run the application.

## <a id="technology"></a>Technology Used

### <a id="technology-used"></a>Some of the technology used includes:
- [Django](https://www.djangoproject.com)
	- Django is a high-level Python web framework that is used to develop the Amber application. 

- [Heroku](https://heroku.com/)
    - **Heroku** is used to host and run the Amber application.


## <a id="contributing"></a>Contributing

### <a id="clone"></a>Clone
1. Firstly you will need to clone this repository by running the `git clone https://github.com/Liz-Conway/Project-4-Amber.git` command
2. After you've that you'll need to make sure that you have a package manager such as **npm**  installed
   You can get **npm** by installing Node from [here](https://nodejs.org/en/)
3. Make sure that you have **python 3** installed. You can install this by running the following: `npm install -g python3` .  This also may require sudo on Mac/Linux
4. Make sure that you have **Django** installed. You can install this by running the following: `pip install django`  This also may require sudo on Mac/Linux
5. Once **Django** is installed run `python3 manage.py runserver` in the root directory (the one where manage.py is).
6. Navigate to http://127.0.0.1:8000/amber-ci in your browser to run the Amber application.
7. Make changes to the code and if you think it belongs in here then just submit a pull request.

### <a id="fork"></a>Fork
1. Log into [Github](https://github.com/)
2. Search for **Amber** and choose to go to `Liz-Conway/Project-4-Amber`.
3. Click on the *Fork* button on the top right hand side of the screen.
4. This will make a copy of **Amber** in your github account.
5. In your version of Amber click on the `Code` button and copy the clone text.
6. Then, you will need to clone this repository by pasting the command you just copied into a terminal window on your computer and running it.  This will create a copy of Amber from your github account onto your computer.
7. After you've done that you'll need to make sure that you have a package manager such as **npm**  installed
   You can get **npm** by installing Node from [here](https://nodejs.org/en/)
8. Make sure that you have **python3** installed. You can install this by running the following: `npm install -g python3`  This also may require sudo on Mac/Linux
9. Make sure that you have **Django** installed. You can install this by running the following: `pip install -g django`  This also may require sudo on Mac/Linux
10. Once **Django** is installed run `python3 manage.py runserver` in the root directory (the one where manage.py is).
11. Navigate to http://127.0.0.1:8000/amber-ci in your browser to run the Amber application.
12. Make changes to the code and run `git push` to save those changes to your github account.


### <a id="clone-fork"></a>Cloning versus Forking
The major difference between cloning and forking is where your updates go when you perform a `git push`.

With cloning you are pushing the updates to the `Liz-Conway/Project-4-Amber` repo on github.

With forking you are pushing the updates to your own Amber repo on github.


## <a id="credit"></a>Credit

| Code purpose                    | Author               | Link                                                                                 |
| ------------------------------- | -------------------- | ------------------------------------------------------------------------------------ |
| Validate a date string          | kite.com             | https://www.kite.com/python/answers/how-to-validate-a-date-string-format-in-python   |
| Skip first line in a file       | kite.com             | https://www.kite.com/python/answers/how-to-skip-the-first-line-of-a-file-in-python   |
| Format dates in Python          | Nicholas Samuel      | https://stackabuse.com/how-to-format-dates-in-python/                                |
| Python Errors                   | TutorialsTeacher.com | https://www.tutorialsteacher.com/python/error-types-in-python                        |
| Check if a string is an integer | Pratik Kinage        | https://www.pythonpool.com/python-check-if-string-is-integer/                        |
| Run a python file from another  | Delftstack           | https://www.delftstack.com/howto/python/python-run-another-python-script/            |
| How to colourise text in python | Stack Overflow       | https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal |
|How to pad out strings in Python| Delftstack |https://www.delftstack.com/howto/python/python-pad-string-with-spaces/|
