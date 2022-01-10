## Introduction

Pymetrix can export two types of data:

1. Time Series
2. Aggregate

in two types of modes:

1. Snapshot
2. Live Stream


## Data Types

### 1. Time Series

Pymetrix can export time series data with the following format:

```json
{
   "message" : {
      "id" : "Test",
      "nodes" : [
         {
            "callers" : [
               {
                  "caller" : null,
                  "time" : "2022-01-09 18:26:51.410001"
               }
            ],
            "hits" : 1,
            "id" : "Home",
            "time" : "2022-01-09 18:26:51.409901"
         },
         {
            "callers" : [
               {
                  "caller" : null,
                  "time" : "2022-01-09 18:27:02.361461"
               }
            ],
            "hits" : 1,
            "id" : "Blog",
            "time" : "2022-01-09 18:27:02.361310"
         },
         ...
      ]
   },
   "response" : 200
}
```

which can be obtained by:

1. calling the ``time_series()`` method
2. iterating over the ``pipeline(data="time_series", mode="live")`` generator method, or calling the ``pipeline(data="time_series", mode="snapshot")`` method and accessing the values of the ``node`` key 

in the ``metricman`` object.

**Note that the [``pipeline()`` method is still buggy](notes.md#2-dont-use-pipeline-yet).**

### 2. Aggregate

Pymetrix can also export the aggregated hits data in the following format:

```json
{
   "message" : [
      {
         "hits" : 1,
         "id" : "Home"
      },
      {
         "hits" : 1,
         "id" : "Blog"
      }
      ...
   ],
   "response" : 200
}
```

which can be obtained by:

1. calling the ``aggregate()`` method
2. iterating over the ``pipeline(data="aggregate", mode="live")`` generator method, or calling the ``pipeline(data="aggregate", mode="snapshot")`` method 

in the ``metricman`` object.

**Note that the [``pipeline()`` method is still buggy](notes.md#2-dont-use-pipeline-yet).**

## Modes

### 1. Live

This mode gives the live data of the targets. The live data can be either time series or aggregate.

### 2. Snapshot

This mode gives the data of the targets UPTO the time when the method is called. As with the live mode, the data can be either time series or aggregate.