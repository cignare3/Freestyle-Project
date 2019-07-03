<!-- 
After "cloning" the repo onto your computer, choose a familiar download location like the Desktop.

Environment Setup
Create and activate a new Anaconda virtual environment:

conda create -n backtest python=3.7 # (first time only)
conda activate stocks-env
From within the virtual environment, install the required packages specified in the "requirements.txt" file you created:

pip install -r requirements.txt


You will need to change the path of the data written to CSV files on line 22 and 100 to correspond to your local computer.  

You will need to create a .env file in the project repository and insert your API key like in the example below.

ALPHAVANTAGE_API_KEY="abc123" 

Input Requirements:
Once you have the environment running, you will be prompted for the number of securities that you will hold in your portfolio.  

From Here you will enter the ticker symbol i.e. "MSFT" and the weight i.e. .25 = 25% of that ticker in your portfolio.  

Once you have reached the number of securities you specified in the first step, you will be prompted to input the number of days you would like to administer your backtest starting from today and going backwards. 

 Once you have input these characteristics, the system will calculate you custom portfolio return, standard devation, sharpe ratio, skew and kurtosis over that time period.  You will also be given a visual display of the growth of $1 invested in the porfolio over time.   -->

