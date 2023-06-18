# Cell - Cell evolutionary lexical language.
A fake programing language based on biological paradigms.

That's a lexycal exercise, to be an actual language it would need a parser, compiler, etc...

The end goal - if any at all - is to be like Nim.

You write like a human and it transalates it into C++ - The language of the aliens, also known as programers.

## Philosophy
You do not do, you are.

Take the passive aproach and prioritize an active one.

Think like a human, a human computer.

Is that a gun inside your belly or are you just happy to see me?

## Do a barrel roll

Or, as we say, "hello world".
```
(( this is a comment ))

(( 
this
is
also
a
comment
))

(( 
everything that can be defined by the user needs a underscore somewhere, anywhere. 
This is a "social" contract and it exists for two reasons: future legacy and to 
be compatible with the nature of the language. Just assume that, even if a word without '_' 
is not reserved, the project reserve the possibility that it could one day be.
The compiler won't let you do everything you want, but it's for a reason: avoid headaches.
))

How to cry: (( The first thing any human being do, as they should - The entry point ))
- write with "hello world".
```

Use the keyword `How to` to define a function. It makes sense, right? You're telling how to do it.
Which `How to` did I've called? I've called the `How to` `write`. Did I've passed some argument? Yes.

The keyword `with` serves this purpose. it's not very short, but it is more lexycal. How the computer knows I'm done? With a final point, of course.

You can write a dot at the end of each line, but it's not necessary, the dot is only necessary if you're dealing with a function.

## You'll gonna mess the dot notation!

No I won't. You know why? Because you won't need it.
Instead, all you have to do to access properties inside properties is use a `//`

```
_like//this.
```
See? It's doable.

## To quack or not to quack. That is the question.

The first language I've learned was GDScript. I'll allways have a place in my heart for it.
That is to say, you can statically type a variable, function or whatever here - if you want to.

```
item _foo: 'foo' (( item is what you call a variable here ))
item str/_foo2: 'foo' (( See? That's why you need two slashes when accessing properties. one slash means you're typing it. ))

item str/1,4/_bar: "four" ((You can define the range by putting another slash between the item's name))
item str/\\[a-z]{40}/_bar2 = "you can also define the range with regex" (( by prepending it with "\\" ))

item int/-?[\d]{1,2}/_number = -20 (( an integer that is signed and can hold only two digits. ))
remember str/_OCTOBER: 'THIRD' (( remember is how you call a constant ))

remember _str_regex: '\w*'.
item str/@_str_regex/_baz: "the at symbol captures an item value as a regex". ((  if you want a @ on your regex, just use a \ before it ))

(( and you can of course define your own types in a OOP way, which I'll talke about later ))

How to _a_statically_typed_function: /str
- get "a string.". (( get means return. Again, it's more human that way. )).

How to get_nothing: /void
- get nothing.

```
## Ooops, I've did it again.

> Look, I understand the `with` thing and all, but won't it get confusing when passing functions inside functions?

Maybe, maybe not.

```
do_a_thing with this_function with 'a string'..

How to do_a_thing with _foo:
- write with _foo.

How to this_function str/_bar: /str
- get _bar.

How to disappear_completelly:
- ignore.

```
Yep, each `with` asks for a `.` 

You can't escape symbolic hell here either. Sorry.

## KISS the cook
You might noticed the weird identation.

Again, it is to be more human readable. just use hyphens instead of tabs or spaces, the last hyphen should follow a space, but it's not necessary (although none of this is necessary, to be fair.)

Think of it as a grocery list, and you'll gonna cook some stuff.

## A Link to the past

Pointers, oh boy, let's talk about them.

- I won't call them pointers, I think links are more like it.
- every parameter is immutable by default, as all arguments are passed as reference, if you want to change a argument you must prepend the parameter with the keyword "writable", like this:

```
item _foo = 'value'

How to start:
- change_a_variable_outside_the_scope with _foo.
- write with _foo. (( will print 'another value' )).
- copy_a_argument with _foo.

How to change_a_variable_outside_the_scope with writable _bar:
- _bar = 'another value'.

(( if you want to copy the argument into the param, the keyword is "copied"

How to copy_a_argument with copied _baz
- _baz += ' ' + _foo.
- write with foo. ((  will write 'another value' ))
- write with _baz. ((  will write 'another value another value' ))

```



## What if the wheel were squared?

Yep, the bones are almost there. So let me do some stuff.

### what if?
Here are some ways to write if/else statements:

```
(( First way ))

is duck a bird? (( 'is' is equal to if, 'a' is equal to == ))
- write with "duck is a bird.".
then is duck a whale? (( 'then is' is not exactly equal to 'else', but it's the same spirit, so there you have it, 'else if' ))
- write with "then how can they fly?".
well then: (( 'well' is just so you can comunicate better, think of it as the machine trying to do all the paths and then say it for itself "well, I'll do this then" ))
- write "What is life?".

(( ternary ))
duck is a bird ? write with "duck is a bird.". ?? duck is a whale ? write with "then how can they fly?".

(( ternary multiline ))
duck is a bird
- ? write with "duck is a bird.".
- ?? duck is a whale.
- ? write with "then how can they fly?".

```

### Face/Off
A switch statement:

```
item _phrase

what is duck:
- bird?
-- _phrase: "duck is a bird".
- _whale?
-- _phrase: "then how can they fly?".
- _airplane? _mermaid? _cat?
-- _phrase: "This duck is kinda weird.".
- _animal?
-- _phrase is and "animal it is, but what kind?". (( 'is and' means concatenation, always. if you do 'item foo: 1 is and 2' you'll get 12 ))
-- keep going. (( 'keep going' is like 'continue', don't need to break all the time, based on GDScript ))
- _swan?
-- _phrase += "A swan? That's why they bullied my boy!!".
- whatever: (( whatever is a wild card ))
-- _phrase: "I don't know what else to do!".

write with _phrase.

```
## Qu'est-ce que c'est? 
Talking about loops now.

### For for for for for for for for for for better
There are many ways to do a `for` loop, they're a gourmetized `while` statement, after all. Here are some I've thought:

```
item _arr: ['this', 'is', 'something']

do in _arr//size:
- write with 'this will repeat 3 times'.

do in _arr//size as _index_number:
- write with index_number. (( 0, 1, 2 ))

do in _arr as _arr_value:
- write with arr_value. (( arr_value will be the arr[index] each time ))

from 4 to 6 do as _i:
- write with _i. (( 4, 5, 6 ))
```

### while I'm still here
And this is the `while` way of doing stuff:

```
item _duck.
item _duck_age: 0.

as long duck is not a bird: (( 'is not' means ! in other languages, 'a', again, is just like ==. Finally, 'as long' is the 'while' per se ))
- ask_if_he_is_a_swan.

How to ask_if_he_is_a_swan:
- duck_age += 1. (( math calculations asks for math symbols, no other way around it. ))
- is duck_age > 2?
-- duck is a swan.
- then is duck_age a 0?
-- write with "he's ugly in a cute kind of way".
```

## Being oriented program

BOP BOP.
Everything is a being of a kind. Norman is a being of kind Human, BOP BOP.

### Do Right yo!
Constructor is DNA, Norman is a being of kind human, his DNA is Human. Totally a guy.

Let's teach the machine how to reproduce him.

```
kind Human.
inherits Animal.

- Human with name, surname:.(( don't boilerplate. The '.' after the ':' is all you need ))
```
If the DNA doesn't have a set of rules, it will assume all params should be assigned to their respective items.

If the items are not declared, it will create it as public items If you want to do something in the constructor beyond that, you should call a special function so it will do what is supposed to do AND what you want to do.

This function's name is make_me.

```
kind Human.
inherits Animal.

(( this: ))
- Human with name, surname:
-- make_me.

(( is exactly the same as: ))
- Human with name and surname:.

(( but you can do more stuff beyond just the ':.' ))

```

This is not done yet, but maybe you've noticed it turns out to be very funny to me. I do think it's doable.

Now you can check a table with the substitutions I've made/am making.

## Do not sin

auto in c++ is considered bad practice - and I agree.

The only reason people seem to accept it is so they don't have to write a very long type.

Well, if you have a really large name, what will people call you? A nickname, of course.

Nicknames will not only shorten the typing, it will also let you have a track to what it actually means - something you pretty much can't do with auto.

```
nickname int_vec_iterator: std::vector<int>::iterator
```


## The Table
if you're coming from any other language, it should be easier to read this. In a world where this language actually exists and is entirely functional, you won't need to.

|standard|substitution 1|
|---|---|
|function|How to|
|(|with|
|)|.|
|(start of a comment)| (( |
|(end of a comment)| ))|
|return|get|
|pass|ignore|
|continue|keep going|
|break|cut|
|==|a|
|(as concatenation) +=|is and|
|(any operand)=|(any operand)=|
|var|item|
|const|remember|
|if|is|
|(ternary) ?|?|
|(ternary) :|??|
|else if|then is|
|else|well then|
|switch|what is|
|while|as long|
|do while|cop|
|for 10|do in 10|
|for i of var|do in var as i|
|for i in range(4,10)|from 4 to 10 do as i|
|object|being|
|class|kind|
|super|genus|
|namespace|surname|






<!-- Ignore this for now, they're just ideas.

|Instead of|use this|or this|
|---|---|---|
|function|How to
|if|is|?|
|else if|then is|??|
|else|then|...|
|for|do in||
|while|keep as|as long as|
|switch|what|itemName:|
|return|give|
|var|item
|const|remember
|class|kind
|object|being
|(|with
|)|.



## About "use this"

- How to - When you define a function, you're actually giving instructions, when you call a function, you ask the computer to follow them.
- is - Think of yourself as the computer instead of the master, sometimes it makes more sense to think in the first person.
- then is - Same idea.
- do in - Giving priority to action here.
- keep as - As long as statement is true;
- what - What is the statement equal to? Then look for what to do in the instructions.
- give - more informal than return. Action asks for informality.
- item - phisical aproach.

## About "or this"
- ? - He's just asking.
- ?? - He's just asking again.
- ... - He gave up.
- itemName: - That's it, I believe you don't need to actually say it is a switch statement as long as it looks like a duck, if you know what I mean (duck typing is what I mean).

## Typing

This language is dinamically typed with optional static typing but, if you gonna static type your "items" and "How tos", you better do it all the way: with ranges.

Let's declare a item:
```
# this is a comment, by the way
item foo =  10 # dinamically
item foo2 := 10 # fixed, but let the "compiler" define  what it's gonna be.
item foo3 : number(INT) = 10 # normally fixed, you can use all the datatypes from c++, but do it in all caps as they are actually constant values.
item foo4 : number([0,10]) = 10 # with a range
```
Now with text:
```
item foo = "text"
item foo2 : text(STR) = "text"
item foo3 : text([0, 126]) = "text" # range based on the ANSI table, which is to say that I'll only use ASCII here
item foo4 : text([[65,126]) = "text" # or maybe I just want to use A to ~, you know.
```
I'm basing all this is gdcript and python, as you might have guessed.

The thing is though, if you can define so easily the range in memory you're gonna need, than you can save a lot of space if you implement it right.

As I've said, this is just a lexycal exercise, it's not better or worse than any other language - after all, it's not a language at all, and even at that it doesn't have all the basics.
