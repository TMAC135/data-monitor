## About this Project

The objective for this project is collecting some useful information on the web and mining the potential relation behind these data. Finally, we will present the result of the analysis on the web.

### Main Components
- Web Crawler
  - CNN news
  - Housing price in big cities like Beijing, ShangHai
  - Other interesting topics
- Data Analysis  
  - Using python science packages: Numpy,Pandas,Matplotlib to preprocess the
raw data from previous step
  - Using python sklearn package and apply machine learning algorithms to build the
  model
  - For new data, present the predicted result
- Presentation
  - The total project is based on the microframework in python - flask, the users will easily negate to any module they like
  - Possibly add some permission management

### Functionality for each package
  - **config**: The configuration files for the project, including the MySQL and MongoDB connections,flask server.
  - **controllers**: Handling different requests and render templates for different scenes.
  - **dbhelper**: The basic wrapper of database, like query,execute in torndb, find, remove in pymongo.
  - **models**: Models for different functionalities in this project.
  - **dao**： The intermediary layer between dbhelper and model, any logic related to interacting with database is in this layer
  - **objects**: The intermediary layer between dao and models, here we can define the type and values returned from dao.
  - **web_crawler**: Crawling for different websites and store to database.
  - **utils**: Utility function for this project.
  - **auto_process**: Python script files under this package, executed under crontab in linux for certain purpose.
  - **sync**: Deploy the project to the server.
  - **data**: Data files.
  - **test**: The unit test part of the function or class in the project.
  - **notebooks**: ipython notebooks for data analysis.
  - **logs**: log files.
  - **server.py**: The entrance of the project.

### Notice 
