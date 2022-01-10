## Introduction

Being the nascent library that it is at the moment, Pymetrix is by no means fully optimized. I am working actively on it, and any help is ABSOLUTELY WELCOME! 😁

That being said, these are some of my notes for getting the best results out of Pymetrix.

### 1. Time Series > Aggregate

Time Series Data is a lot more meaningful than aggregated hits data. You can aggregate them over pipelines, stream them into databases...  you are only limited by your imagination as to what you can do with them.

Also, performance wise, Pymetrix processes and exports time series data faster than aggregated hits data. This is because the aggregation method is built atop the time series method. This essentially means that when you export your data in aggregated form, it is essentially doing the following things:

1. Retrieve the time series data
2. Aggregate the data according to the targets/endpoint names<span style="color:red">*</span>
3. Exporting the aggregated data

Step 2 is the most tedious process, and is the extra step in aggregation. Being implemented in Python, it's a given that it'll be slow. Hence to speed up your workflow for large number of entries, exporting time series data is recommended. Also, time series data has a consistent format, which may not be the case with aggregated data, depending on which type of aggregation you want to do.

<span style="color:red">\*</span>**UPDATE**: Now the basic hit count comes directly with the time series format. Still, what I told above still holds for other kind of aggregates. 

### 2. Don't use ``pipeline()`` yet

The ``pipeline()`` method is a method that'll greatly reduce your workload, and I am working actively on it. That being said, don't use it just yet - there are plenty of bugs in it, and I don't think that it'll be good for you to implement something into your code that's buggy. So please give me some time to work on it and use the ``time_series()`` and ``aggregate()`` methods instead.

