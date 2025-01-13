# Indiana University Programmer/Analyst Assessment

In the attached code_problem.zip, you will find the file, systemList.txt, which lists all the system-provided alerts in sunapsis. The code_problem directory represents the root for the sunapsis website.  The ioffice/alerts directory contains all of the files in systemList.txt and several extras, which are custom alerts written by a client institution for their own use. We would like to move all of the custom alerts into a new ioffice/institution/alerts directory, while leaving the files contained in systemList.txt in their original location (in ioffice/alerts).  You can use whatever language you are most familiar with, and assume that the application has proper permissions to perform any file operations you need to use.


## Prerequisite:  
   - Download and install Python from the [official Python website](https://www.python.org/). 
   - Verify the installation by running one of the following commands in your terminal or command prompt:
     ```bash
     python --version
     ``` 
   - You should see the installed Python version as the output (e.g., `Python 3.x.x`).


## How to Run the Script

1. **Navigate to the `src` Directory**:  
   ```bash
   cd src
   python Alert.py
   ```