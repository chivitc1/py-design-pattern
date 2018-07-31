# Singleton pattern

The singleton pattern is one of the most controversial patterns; many have accused it
of being an "anti-pattern", a pattern that should be avoided, not promoted. In Python,
if someone is using the singleton pattern, they're almost certainly doing something
wrong, probably because they're coming from a more restrictive programming
language.

The basic idea behind the singleton pattern is to allow exactly one instance of a
certain object to exist.

# Of anti pattern

Singletons can interfere with distributed
computing, parallel programming, and automated testing, for example. In all those
cases, it can be very useful to have multiple or alternative instances of a specific object,
even though a "normal' operation may never require one.

Module variables can mimic singletons. It's not as "safe" as a singleton in that people could reassign
those variables at any time

If someone has a valid
reason to change those variables, why should we stop them?

It also doesn't stop people from instantiating multiple instances of the object, but again, if they have
a valid reason to do so, why interfere?