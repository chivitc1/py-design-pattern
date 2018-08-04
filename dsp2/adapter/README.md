# Adapter pattern

is designed to interact with existing code. We would not design
a brand new set of objects that implement the adapter pattern. Adapters are used
to allow two pre-existing objects to work together, even if their interfaces are not
compatible.

Like the display adapters that allow VGA projectors to be plugged into
HDMI ports, an adapter object sits between two different interfaces, translating
between them on the fly.

The adapter object's sole purpose is to perform this
translation job. Adapting may entail a variety of tasks, such as converting arguments
to a different format, rearranging the order of arguments, calling a differently named
method, or supplying default arguments.

Adapter pattern is very similar to Decorator pattern as it will wrap one object, pass its functionality with different interfaces which other object can use.