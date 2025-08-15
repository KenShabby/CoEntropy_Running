Objective: An application that allows the user to fine tune their training zones
based on the common heart rate tracking methods. The default zones are based on 
the book: Advanced Marathoning by Pete Pfitzinger and Scott Douglas.

Implemented Features:

- Calculate ideal training heart rate zones for common segment types.
    - User has a choice of heart rate calculation methods, maximum heart rate,
      heart rate reserve (maximum - resting heart rate), and lactate threshhold
      heart rate (typicaly found using a heart rate monitor or lab test). If you
      don't know any of these, the simple method of 220 minus age is used to
      estimate maximum heart rate.
      
- Implement a more friendly front-end. This is coming along with the new CLI
  based system.

Desired Features:

- Generate individual run plans.
- Generate entire training plans.

Running:

- Clone to the directory of your choice
- run `python CoEntropy_Running/main.py`
