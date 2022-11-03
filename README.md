# Emporos
An automated trading manager that optimizes the execution of trades against a chosen trading platform. 

## Features
* Accept trading orders that can be parametrized for optimal execution
* Manage the connection to the selected trading backend provider
* Optimize trading executions against the provider
* Provide a simulated interface that can be used to provide real-world trading behaviour to backtesting agents
*  

## Components
Component | Role | Focus
------ | ------- | -----------
Trader | Management of autonomous trading agents | Creation, benchmarking, management and monitoring of trading agents for different markets 

### Trader

Main concepts:
* Don't try predicting the market
* Focus on predicting if a given strategy is profitable (Metalabeling)
* Use ML to compute the propability of return with many, many features
    * Technical / macro-econonomic indicators
    * Alternative data
    * Model from [Blog on tail reaper hedge fund](http://epchan.blogspot.com)

Feature | Focus 
------ | -----------
Metalabeling | Create a probabilistic estimate of strategy returns

# The problem with current quantative trading
* Linear models where widely used and have decaying alpha
* 