# State pattern

The goal of the state pattern is to represent state-transition
systems: systems where it is obvious that **an object can be in a specific state**, and that
**certain activities may drive it to a different state**.

To make this work, we need a manager, or context class that provides an interface
for switching states. Internally, this class contains a pointer to the current state; each
state knows what other states it is allowed to be in and will transition to those states
depending on actions invoked upon it.

We have two types of classes, the context class and multiple state classes. The
context class maintains the current state, and forwards actions to the state classes.
The state classes are typically hidden from any other objects that are calling the
context;

# States being used

• FirstTag

• ChildNode

• OpenTag

• CloseTag

• Text

# Problem to solve
Build an XML parsing tool.

The context class will be the parser itself.

Take a string as input and place the tool in an initial parsing state.

The various parsing states will eat characters, looking for a specific value, and
when that value is found, change to a different state

The goal is to create a tree of node objects for each tag and its contents.

# State versus strategy
The state pattern looks very similar to the strategy pattern; indeed, the UML
diagrams for the two are identical. The implementation, too, is identical;

We could even have written our states as first-class functions instead of wrapping them in
objects, as was suggested for strategy.

While the two patterns have identical structures, they solve completely different
problems. The strategy pattern is used to choose an algorithm at runtime; generally,
only one of those algorithms is going to be chosen for a particular use case. The state
pattern, on the other hand is designed to allow switching between different states
dynamically, as some process evolves. In code, the primary difference is that the
strategy pattern is not typically aware of other strategy objects. In the state pattern,
either the state or the context needs to know which other states that it can switch to.