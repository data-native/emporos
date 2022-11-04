# Emporos
A management service to design and maintain autonomous trading agents capable of reasoning, planning and execution of trades against a chosen market provider.



## Features
* Accept trading orders that can be parametrized for optimal execution
* Manage the connection to the selected trading backend provider
* Optimize trading executions against the provider
* Provide a simulated interface that can be used to provide real-world trading behaviour to backtesting agents
*  

# Components
Component | Role | Focus
------ | ------- | -----------
Emporos | Management of autonomous trading agents | Creation, benchmarking, management and monitoring of trading agents for different markets 
Trader | Execution of trading plans | Enact optimized trading interactions
Allocator | Generate allocation strategies | Define, optimize and maintain allocation strategies for trading agents under changing market conditions
Planner | Compilation of trading plans | Build executable trading plans based on action plans defined by a trading agent

## Emporos
Management component that integrates across all other subscomponents

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

## Trader
Execution of trading plans against the given backend provider.
Receives optimized trading plans and ensures their proper execution against the provider, 
managing connections, timeouts, retries and trading configuration.

Main concepts:
* Receive parametrized execution plan
* Execute execution plan against the trading API
* Manage the connection through the trading-backend provider
* 

Feature | Focus 
------ | -----------

## Allocator
Provides compute support for trading agents to reach an optimal asset allocation strategy, that can then be scheduled in concrete actions through the agent. 

Main concepts:
* Receive wealth management target plans
* Ingest relevant market data to situate the allocation task

Feature | Focus 
------ | -----------
Parse wealth management target plans | 
Ingest relevant market and asset data | 
Retrieve risk estimates for relevant markets, assets |
Compute a set of allocation strategies | 
Benchmark the allocation strategies |
Compile and return the optimal allocation strategy |


## Planner 
Create a intermediary or optimized trading plan based on a chosen set of actions by an agent. The resulting trading plan can be used by the agent to validate the costs associated with a set of actions at a point in time against the market. 

Once approved, the planner can compile an optimized, final trading plan that is passed to the Trader for execution against the market.

Feature | Focus 
------ | -----------
Provide a cost profile for a chosen set of actions by an agent | Provide key parameters fast to allow the agent to receive feedback often before settling on final strategy
Compile an optimized trading plan | Empower the `Trader` to choose an optimal execution strategy for placing a given trade target on the market


# The problem with current quantative trading
* Linear models where widely used and have decaying alpha
*
