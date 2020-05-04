# CitizenLab Applied NLP Engineer Assignment

## Introduction

The goal of this assignment is to expand this web application, to make it easier and faster for city administrators to process citizen ideas.

## The data set

The data is contained in `leuven_ideas.csv`. It's a subset of anonymized ideas sourced from a real CitizenLab project for the city of Leuven.  The new local government used these ideas, provided by citizens, to shape the action plan for the current legislature. Next to the idea title and body, there's metadata on author, votes and publication data. For some ideas, there are associated topics, which were chosen by citizens from a predefined list on entry. The original ideas are in Dutch, but a machine translated English version is provided as well. You're allowed to make use of the English version, if you want.

## The web app

The basic web application in this repository is there to assist the user in processing these ideas. On the homepage all ideas are listed and the user can edit the associated topics, with autocomplete suggestions. Topics can also be removed by clicking on them.

The end goal of the city administrator, the target user of this application, is to process the inputs in order to come to some form of report or summary that's useful to policy makers. Your goal is to augment the application to help them as much as possible to reach that goal quickly and qualitatively.

The starting structure of the application looks like this. You're free to make any changes you want.
```
/app
  routes.py         The endpoint definitions of the Flask app
  ideas.py          The operations on the data, currently with pandas
  /static
    ideas.js        Some React for interactively editing topics
    style.css       Minimal styling
  /templates
    layout.html     The main html skeleton of the app
    ideas.html      The homepage that lists all ideas
    insights.html   The insights page to help the user understand the data
```

## The assignment

It's your job to provide the user with more powerful functionalities to help her with processing. How you do this exactly, is up to you.

Here are a few challenges you could take on. Try doing one thing rather well, instead of having unfinished business all over the place. Quality over quantity!

* Improve the autocomplete suggestions
* Add a button to automatically add topics
* Add useful insights to the empty insights page
* ... Surprise us!

## Getting started

1. Click [here](https://github.com/CitizenLabDotCo/cl-assignment-applied-nlp/generate) or click the green `Use this template` button on top to make a private copy of this repository on your own account.

2. Git clone your own repository on your machine.

3. Run the base application.
```sh
pip install -r requirements.txt
flask run
```

## Rules

* You have **3 hours** to get as far as you can.
* While this app provides you with a rough starting point, you can use **any mix of languages, libraries, frameworks, databases, ...** you want.
* If you base some of your work on **existing code snippets**, StackOverflow answers, gists or tutorials, add a link to them in your code comments. We don't consider this a weakness.
* Your end deliverable is a **working web application**. While you can use notebooks or any prototyping tool you want, in the end we need to see it in action in the app.
* You've **written** all code that doesn't include such a comment **yourself**.
* Add a **README.md** file with instructions on how to run your application and a very short description of the work you did
* Share your **private GitHub repository** with koen@citizenlab.co (username kogre). We'll only take commits within the 3 hour limit into account.

## Evaluation

We will evaluate your solution over these axis:

* **Architecture** How did you structure it all?
* **Solution** To what extent does this help the user to accomplish their task?
* **Model** How are you interpreting the data? Why did you adopt that specific algorithm?
* **Process** While maybe not clear from the code, we'll talk a lot about how you went about it in the interview. If you used some scripts or notebooks, make sure to include them in your repo.

Time is short, so here's some things we explicitly won't care about. Just this once ;)
* Polishment of the UI, as long as it works
* Responsiveness, accessibility, standards
* Performance is not too important, as long as it's reasonably usable. A long startup time is totally fine.

If you've impressed us with your work, we'll invite you for a discussion. The conversation about the way you've got there will be at least as important as the result of the assignment itself.

Thank you and good luck!
