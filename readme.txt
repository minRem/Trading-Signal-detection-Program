In our project proposal, we designed an application to detect trading signals realtime.
However, we cannot find a free realtime stock price API, so instead we use an API that gives
us the daily closing price of stock, and our program will check any trading signals from 5 different
indicators calculated from the closing prices. Other indicators are not available because either they
require data other than closing price(such as volume, which is not given by the API we use), or they
require all the historical data(data from the day they were publicly listed), such as KDJ.
The five indicators we use are: Fibonacci ma, ma5 and ma10, MTM, ROC, W%R.
This program requires java development kit and python to run. The installers of those are included.
Our program may be unstable with python 3.11 so python 3.10 is recommended.
Before running the program, run pip.bat to install the API for stock prices,  then use run.bat to start
the program.