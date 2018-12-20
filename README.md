# BarkerCode
Barker Code Cross Correlation Analysis

## Intro

This repo uses Numpy to calculate auto-correlation results of [Barker Codes] (https://en.wikipedia.org/wiki/Barker_code)

Two example Barker Sequences (7 and 13) are generated with each specific sequence lasting for 1 micro-second and plotted using Numpy and can be seen below:

## Barker Sequences

![Data](assets/barkercode7.PNG)

![Data](assets/barkercode13.PNG)

Each micro-second contains ten data points for better accuracy and precision.

When autocorrelated, the Barker Sequences produces a peak pulse with minimum sidelobes.

## Auto-Correlation of Barker Sequences

![Data](assets/barkercode7.PNG)

![Data](assets/barkercode13.PNG)


## Application

Barker Pulses can be used in radar detection and ranging to improve range resolution. For example, taking a sample radar return signal from a 13-Length Barker pulse and plotting its return energy shows:

![Data](assets/signal_strength.PNG)

From the graph, it is diffcult to where or how many targets have been detected. Auto-correlating with the known Barker template shows the following:

![Data](assets/auto_correlation.PNG)

From the graph, 3 clear targets were detected in the return signal.
