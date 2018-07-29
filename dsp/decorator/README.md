# Decorator pattern

"wrap" an object that provides core functionality
with other objects that alter this functionality. Any object that uses the decorated
object will interact with it in exactly the same way as if it were undecorated


• Enhancing the response of a component as it sends data to a second component
• Supporting multiple optional behaviors, thay thế cho multiple-inheritance

## Problem to solve

## Run example

1. Start the server in one terminal.

$ python server.py

2. Open a second terminal window and run the client.

$ python client.py

3. At the Enter a value: prompt in the server window, type a value and press enter.

4. The client will receive what you typed, print it to the console, and exit. Run
the client a second time; the server will prompt for a second value.

## Build the decorator/wrapper for socket with LogSocket class
Replace  respond(client)

with respond(LogSocket(client))

New functionality: The decorator LogSocket print the message sending to client before send it.

## Build GzipSocket decorator and use decorator wrap another decorator
