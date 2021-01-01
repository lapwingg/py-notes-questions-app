# Py notes / questions App

Project made for pass a subject Effective programming in python 2020/2021. The app is written in PyQt5 and can be used as desktop application. The app supports keeping and learning new things which you are discovering when you work or study any technology. With this app you can make text notes (and back to them later), type technology that you use to work and ask question for yourself about technologies on which you currently work. Due to requirement: 300 lines of code, this is very simple implementation of app. It only does a small piece of functionalities which the app should do to completely support of that topic and layout of app should be better than current. The pylint inspection returns 10/10 rating of code of this app.


pylint src/ --verbose --disable=no-name-in-module,import-error,too-few-public-methods,invalid-name

no-name-in-module -> doesn't see PyQt5 classes

import-error -> configuration errors

invalid-name -> in overriding external method in inheritance


## What can be done in next releases?

- Note, Technology and Question scheme should be related of each other. Note should categorize by Technologies, Question should be related to Note and Technology
- After above point will be done, it makes sense to write logic for filtering in the notes, technologies and questions view
- Note view: not only text, related technologies and questions 
- Technology view: storing info when technology is updated, then notes and questions should be marked as archived until updated respectively
- Question view: related notes to question or some explanation of answer, statistic if user knows well answer of that question
- Quiz view: storing old quizzes, statistics, customizing new quizzes

