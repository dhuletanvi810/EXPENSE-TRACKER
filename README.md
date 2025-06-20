# EXPENSE-TRACKER

*COMPANY*: HEX SOFTWARES

*NAME*: TANVI NILESH DHULE

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: KAPTAN

*DESCRIPTION*:
Project Title: Expense Tracker using Python and JSON

This project is a simple yet effective console-based Expense Tracker built using Python. The main goal of the application is to allow users to record daily expenses, organize them by category, and view summaries — all while saving the data in a persistent way using a JSON file.
The tracker operates entirely through a text-based menu system, which makes it easy to interact with. When the program starts, it checks if a file named expenses.json exists. If it does, the file is loaded, and any previously saved expenses are accessible. If the file is not found, a new list is created, allowing users to start fresh. This makes the application data-friendly and usable across multiple sessions without losing any entries.

The user is presented with four main options:
Add Expense – The user enters the amount and category (e.g., food, travel, shopping). This information is stored in a dictionary and appended to the expenses list. The list is then written back to the expenses.json file.
View Expenses – Displays all saved expenses in a clear format showing the amount and its associated category.
Show Summary – Calculates and displays the total amount spent and breaks it down category-wise, helping the user understand spending habits.
Exit – Ends the program gracefully.

This project uses Python libraries like json for file handling and os to check the file’s existence. The use of json.dump() and json.load() allows for easy saving and reading of the expenses, making it a simple and lightweight form of data storage.
One of the key learning outcomes while developing this application was understanding how to persist user data between program runs. Normally, once a Python program ends, all variables and data are lost. Using JSON made it possible to store data in a structured format that can be reloaded every time the app is used.
Additionally, creating a menu system using while True: and conditionals helped in building interactive and user-friendly command-line tools. It taught the importance of input validation, looping, and basic exception handling (which can be added for further robustness).
Although the tracker currently saves only the amount and category, it could easily be extended by adding timestamps, filtering options, or even user login features. The program could alo be turned into graphical desktop app using Tkinter, or a basic web app using Flask or Django.

Overall, the Expense Tracker was a valuable project to understand how everyday problems like budgeting can be solved through code. It demonstrates how Python’s simplicity and powerful standard libraries can be used to create practical applications that go beyond classroom examples. The logic behind reading and writing JSON files, organizing data in lists and dictionaries, and structuring a clean menu flow forms a strong foundation for building more complex financial or record-keeping systems in the future.
This project not only solidifies basic programming skills but also introduces the mindset of building tools that users can rely on for daily tasks.


*OUTPUT*
![Image](https://github.com/user-attachments/assets/c5365465-ab6d-46cd-95aa-0dfa48427b72)
![Image](https://github.com/user-attachments/assets/213674f4-bf6a-4296-80a5-51ad88b12ae9)
![Image](https://github.com/user-attachments/assets/d0c8fe7c-7b4a-40d6-84da-b3ce3cc33806)
![Image](https://github.com/user-attachments/assets/e304196b-59e4-4380-9304-26ab3083673c)
