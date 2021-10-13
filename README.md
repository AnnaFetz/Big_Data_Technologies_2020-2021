# bdt2021
This section of the project gathers data from the two main APIs [coinmarketcap](https://coinmarketcap.com/), [financialmodelingprep](https://financialmodelingprep.com/), 
writes records on cosmos db, which are used for prediction and written into redis. 

### Data Ingestion : 
- `price insertion` : folder of the function ingesting data from the APIs and inserting it to CosmosDB. 
  - `__init.py__` : code deployed to Azure, containing the access key to our DB and creates a document for every gathered index from the APIs. These documents are then added to the respective colletion in the DB. 
  A timer request has been defined in order to automatically run the code hourly. The function is defined in `function.json`
### Model and Predictions 
- `Timer Trigger1` : folder of the function reading data from our DB's collections and computing predictions. 
  - `Managers.py` : contains two different classes, DataManager() and ModelManager(), which respectively reduce dataset's columns into the needed values and groups them by date, and performs the ideal training with them .
  - `Data_managing.py`: connects to the DB and passes each collection to the Data Manager and creates a training set for predictions 
  - `SARIMA.py`: computes cross correlation between predictors, ideal time-lag and granger-causality. Outputs a new very small dataframe.
  - `redisOperations.py` : contains the basic read-write operations to Redis 
### How to start
Firstly, add Visual Studio Code's Azure Functions' extentions available [here](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions) and install the requirements through pip install -r requirements.txt and activate the virtual environment if required.

#### - Once in VS : 
- Go to the Azure extension, then on the left menu select functions and the Local Project bdt2021.
- There, you will find two functions: Timer Trigger1 and Price Insertion 
- If all requirements are satisfied:
  1.  You can run the project on the `___init__.py` file of the TimerTrigger1, which will collect new data. <b> Warning: </b> this will update the whole pipeline and update the WebApp as well!
  2. The best option would be to test via WebApp, as explained [here](https://github.com/msergen/btc_pub)

