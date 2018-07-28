# Basic machine learning algorithm

The general idea is to make predictions or classifications about future data
by using knowledge gained from past data

Some important machine learning applications include computer vision (such as image
classification or facial recognition), product recommendation, identifying spam, and
speech recognition

## Our problem to solve

given an RGB color definition,
what name would humans identify that color as?

## Build a classifier that attempts to divide the RGB space into the basic colors:
• Red
• Purple
• Blue
• Green
• Yellow
• Orange
• Grey
• White
• Pink

The first thing we need is a dataset to train our algorithm on. In a production system,
you might scrape a list of colors website or survey thousands of people.

For simple, I create a simple application that renders a random color and asks the user to select
one of the preceding nine options to classify it

The output of app: a comma-separated value (CSV) file that contains four values
per row: the red, green, and blue values (represented as a floating-point number
between zero and one), and one of the preceding nine names that the user assigned
to that color, like:

0.30928279150905513,0.7536768153744394,0.3244011790604804,Green

## Algorithm:
k-nearest neighbor

This algorithm relies on some kind of "distance" calculation
between points in the dataset (in our case, we can use a three-dimensional version of
the Pythagorean theorem). Given a new datapoint, it finds a certain number (referred
to as k, as in k-nearest neighbors) of datapoints that are closest to it when measured
by that distance calculation. Then it combines those datapoints in some way (an
average might work for linear calculations; for our classification problem, we'll use
the mode), and returns the result.

## Steps

1. Load the sample data from the file and construct a model from it.

2. Generate 100 random colors.

3. Classify each color and output it to a file in the same format as the input.

Once we have this second CSV file, another Kivy program can load the file and
render each color, asking a human user to confirm or deny the accuracy of the
prediction, thus informing us of how accurate our algorithm and initial data set are.

## Calculate color "distance"

To calculate the "distance" between two colors. Think of colors as being three
dimensional (red, green, and blue could map to x, y, and z axes, for example)

## install kivy
sudo apt-get install python3-kivy