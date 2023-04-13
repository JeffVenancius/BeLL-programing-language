# Doll - Do Lexycal Language.
A fake programing language.

That's a lexycal exercise, to be an actual language it would need a parser, compiler, etc...

## Philosophy
You are the wheelman. You do not say what to do, you do.

You are the computer, take the passive aproach and prioritize an active one.

This is a language, it comunicates with the most human readable aproach I can get.

If you can comunicate better, than you can think better as well.

Think like a human, a human computer.

## Do a barrel roll

Or, as we say, "hello world".
```
((this is a comment))

((
this
is
also
a
comment
))

howTo start: ((start is the first thing a program do.))
- write with "hello world". ((you know what this is?
                             a comment.))
```
Use the keyword `howTo` to define a function. It makes sense, right? You're telling how to do it.
Which `howTo` did I've called? I've called the `howTo write`. Did I've passed some argument? Yes.

The keyword `with` serves this purpose. it's not very short, but it is more lexycal. How the computer knows I'm done? With a final point, of course.

## You'll gonna mess the dot notation!

No I won't. You know why? Because you won't need it.
Instead, all you have to do to access properties inside properties is use a `//`

```
like//this
```
See? It's doable.

## To quack or not to quack. That is the question.

The first language I've learned was GDScript. I'll allways have a place in my heart for it.
That is to say, you can statically type a variable, function or whatever here - if you want to.

```
item foo: 'foo' ((item is what you call a variable here))
item str/foo: 'foo' ((See? That's why you need two slashes when accessing properties. one slash means you're typing it.))
item str/[a-z]{29}/bar = "range can be defined by regex"
item int/-?[\d]{1,2}/number = -20 ((an integer that is signed and can hold two digits.))
remember str/OCTOBER: 'THIRD' ((remember is how you call a constant))

howTo a_static_function: /str
- give "a string." ((give means return. Again, it's more human that way.))

```
## Ooops, I've did it again.

> Look, I understand the `with` thing and all, but won't it get confusing when passing functions inside functions?

Maybe, maybe not.

```
do_a_thing with this_function with 'a string'..

howTo do_a_thing with foo:
- write with value.

howTo this_function str/bar: /str
- give bar

howTo disappear_completelly:
- ignore

```
Yep, each `with` asks for a `.` 

You can't escape symbolic hell here either. Sorry.

## KISS the cook
You might noticed the weird identation.

Again, it is to be more human readable. just use hyphens instead of tabs or spaces, the last hyphen should follow a space, but it's not necessary (although none of this is necessary, to be fair.)

Think of it as a grocery list, and you'll gonna cook some stuff.

## What if the wheel were squared?

Yep, the bones are almost there. So let me do some stuff.

### what if?
Here are some ways to write if/else statements:

```
((First way))

is duck a bird? (('is' is equal to if, 'a' is equal to ==))
- write with "duck is a bird.".
then is duck a whale? (('then is' is not exactly equal to 'else', but it's the same spirit, so there you have it, 'else if'))
- write with "then how can they fly?".
well then: (('well' is just so you can comunicate better, think of it as the machine trying to do all the paths and then say it for itself "well, I'll do this then"))
- write "What is life?".

((ternary))
duck is a bird ? write with "duck is a bird.". ?? duck is a whale ? write with "then how can they fly?".

((ternary multiline))
duck is a bird
- ? write with "duck is a bird.".
- ?? duck is a whale
- ? write with "then how can they fly?".

```

### Face/Off
A switch statement:

```
item phrase

what is duck:
- bird?
-- phrase: "duck is a bird"
- whale?
-- phrase: "then how can they fly?"
- airplane? mermaid? cat?
-- phrase: "This duck is kinda weird."
- animal?
-- phrase is and "animal it is, but what kind?" (('is and' means concatenation, always. if you do 'item foo: 1 is and 2' you'll get 12))
-- keep going (('keep going' is like 'continue', don't need to break all the time, based on GDScript))
- swan?
-- phrase += "A swan? That's why they bullied my boy!!"
- whatever: ((whatever is a wild card))
-- phrase: "I don't know what else to do!"

write with phrase.

```
## Qu'est-ce que c'est? 
Talking about loops now.

### For for for for for for for for for for better
There are many ways to do a `for` loop, they're a gourmetized `while` statement, after all. Here are some I've thought:

```
item arr: ['this', 'is', 'something']

do in arr//size:
- write with 'this will repeat 3 times'.

do in arr//size as index_number:
- write with index_number. ((0, 1, 2))

do in arr as arr_value:
- write with arr_value. ((arr_value will be the arr[index] each time))

from 4 to 6 do as i:
- write with i. ((4, 5, 6))
```

### while I'm still here
And this is the `while` way of doing stuff:

```
item duck
item duck_age: 0

as long duck is not a bird: (('is not' means ! in other languages, 'a', again, is just like ==. Finally, 'as long' is the 'while' per se))
- ask_if_he_is_a_swan.

howTo ask_if_he_is_a_swan:
- duck_age += 1 ((math calculations asks for math symbols, no other way around it.))
- is duck_age > 2?
-- duck is a swan
- then is duck_age a 0?
-- write with "he's ugly in a cute kind of way"
```

## Being oriented program

BOP BOP.
Everything is a being of a kind. Norman is a being of kind Human, BOP BOP.

### Do Right yo!
Constructor is DNA, Norman is a being of kind human, his DNA is Human. Totally a guy.

Let's teach the machine how to reproduce him.

```
kind Human
inherits Animal

- Human with name, surname:.((don't boilerplate. The '.' after the ':' is all you need))
```
If the DNA doesn't have a set of rules, it will assume all params should be assigned to their respective items.

If the items are not declared, it will create it as public items If you want to do something in the constructor beyond that, you should call a special function so it will do what is supposed to do AND what you want to do.

This function's name is make_me.

```
kind Human
inherits Animal

((this:))
- Human with name, surname:
-- make_me.

((is exactly the same as:))
- Human with name and surname:.

((but you can do more stuff beyond just the ':.'))

```

This is not done yet, but maybe you've noticed it turns out to be very funny to me. I do think it's doable.

Now you can check a table with the substitutions I've made/am making.

## The Table
if you're coming from any other language, it should be easier to read this. In a world where this language actually exists and is entirely functional, you won't need to.

|standard|substitution 1|
|---|---|
|function|howTo|
|(|with|
|)|.|
|(start of a comment)| ((|
|(end of a comment)| ))|
|return|give|
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
|namespace|nomenclature|












<!-- Ignore this for now, they're just ideas.

|Instead of|use this|or this|
|---|---|---|
|function|howTo
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

- howTo - When you define a function, you're actually giving instructions, when you call a function, you ask the computer to follow them.
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

This language is dinamically typed with optional static typing but, if you gonna static type your "items" and "howTos", you better do it all the way: with ranges.

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
