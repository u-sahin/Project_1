### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)


## Installation  <a name="installation"></a>

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages.

"""pip install matplotlib pandas numpy"""


## Project Motivation <a name="motivation"></a>

For this project, I was interestested in using Stack Overflow data from 2017 to better understand:
Therefore I went ahead and try to answer three questions about the data.

    1. How is the average Salary and JobSatisfaction distributed by the wished WorkStart?
    2. Is the salary dependent on the programming language learned and which programming language is the most and least learned?
    2. What are the average Salaries and JobSatisfactions by Methodology?
    

## File Descriptions <a name="files"></a>

To answer the questions mentioned in [2. Project Motivation](#motivation), I created three separate files.
    
    1. The first question is handled in the file [Workstart_JobSatisfaction_Salary.ipynb].
    2. The second question is handled in the file [HaveWorkedLanguage_Salary.ipynb].
    3. The third question is handled in the file [Methodology_JobSatisfaction_Salary.ipynb].

Each of the files use the data from Stack Overflow as a basis and creates/manages dataframes as needed for the above mentioned questions.
Each step is addtionally commented to ensure that developers and users are able to follow the logic.


## Results <a name="results"></a>
The main findings of the code can be found at the post available [here](https://uemitsahin.medium.com/insight-into-the-data-8b650b0ff4a0).


## Licensing, Authors, Acknowledgements, etc. <a name="licensing"></a>
Must give credit to Stack Overflow for the data.  You can find the Licensing for the data and other descriptive information at the Kaggle link available [here](https://www.kaggle.com/stackoverflow/so-survey-2017/data).  
Otherwise, feel free to use the code here as you would like! 