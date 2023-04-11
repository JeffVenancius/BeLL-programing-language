# DoLanguage
A fake programing language.

That's a lexycal exercise, to be an actual language it would need a parser, compiler, etc...

## Philosophy
You are the wheelman. You do not say what to do, you do.
You are the computer, take the passive aproach and prioritize an active one.
This is a language, it comunicates and, as such, tries to get closer to the human logic.
Think like a human, a human computer.

## Do a barrel roll

Or, as we say, "hello world".
```
(this is a comment)

(
this
is
also
a
comment () still not done
) (now I'm done)

(parenthesis are comments, as we do when writing other stuff. 
howTo is the keyword you'll use to define a function, as you
tell yourself how to do stuff. I'll keep calling them functions
just so it'll be easier to explain.)

howTo start: (start is the first thing a program do.)
- write with "hello world". (you know what this is?
                             a comment.)


```
Use the keyword howTo to define a function. It makes sense, right? You're telling how to do it.
Which howTo did I've called? I've called the howTo write. Did I've passed some argument? Yes.

The keyword with serves this purpose. it's not very short, but it is more lexycal. How the computer knows I'm done? With a final point, of course.

## You'll gonna mess the dot notation!

No I won't. You know why? Because you won't need it.
Instead, all you have to do to access properties inside properties is use a //

```
like//this
```
See? It's doable.

## To quack or not to quack. That is the question.

The first language I've learned was GDScript. I'll allways have a place in my heart for it.
That is to say, you can statically type a variable, function or whatever here. If you want to.

```
item foo: 'foo'
item str/foo: 'foo' (See? That's why you need two slashes when accessing properties. one slash means you're typing it.)
remember str/OCTOBER: 'THIRD' (this is a constant, by the way)

howTo a_static_function: /str
- give "a string." (give means return. Again, it's more human that way.)

```
Notice that I've 'changed' the word var/let to item. It's more human that way and I really want to reinventing the wheel.

It doesn't matter, this language is fake.

## Ooops, I've did it again.

Look, I understand the with thing and all, but won't it get confused when passing "functions" inside "functions"?

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
Yep, each with asks for a dot. 

You can't escape symbolic hell here either.

## Kiss the cook
You might noticed the weird identation.

Again, it is to be more human readable. just use hyphens instead of tabs or spaces, the the last hyphen should follow a space, but it's not necessary (although none of this is necessary, to be fair.)

Think of it as a grocery list, and you'll gonna be cooking some stuff.

## What if the wheel were squared?

Yep, the bones are almost there. So let me do some stuff.

### what if?
Here are some ways to write if/else statements:
```
(First way)

is duck a bird? (is is equal to if, a is equal to ==)
- write with "duck is a bird.".
then is duck a whale? (then is not exactly equal to else, but it's the same spirit)
- write with "then how can they fly?".
well then: (well is equal to I don't know what else to do man is there something I could do with this?)
- write "What is life?".

(Second way)
duck is a bird:
- ?
-- write with "duck is a bird.".
- ?? duck is a whale:
-- write with "then how can they fly?".
- ...
-- write "What is life?".
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
-- phrase += "animal it is, but what kind?" (need to find something to replace +=, you know, more human readable)
-- keep going (don't need to break all the time, based on GDScript)
- swan?
-- phrase += "A swan? That's why they bullied my boy!!"
- whatever: (whatever is a wild card)
-- phrase: "I don't know what else to do!"

write with phrase.

```
## Qu'est-ce que c'est? 
Talking about loops now.

### For for for for for for for for for for better
There are many ways to do a for loop, they're a gourmetized while one, after all. Here are some I've thought:

```
item arr: ['this', 'is', 'something']

do in arr//size:
- write with 'this will repeat 3 times'.

do in arr//size as index_number:
- write with index_number. (0, 1, 2)

do in arr as arr_value:
- write with arr_value. (arr_value will be the arr[index] each time)

from 4 to 6 do as i:
- write with i. (4, 5, 6)
```

### while I'm still here
And this is the while like way of doing:

```
item duck
item duck_age: 0

as long duck is not a bird:
- ask_if_he_is_a_swan.

howTo ask_if_he_is_a_swan:
- duck_age += 1
- is duck_age > 2?
-- duck is a swan
```


This is not done yet, but maybe you've noticed it turns out to be very funny to me. I do think it's doable.

#### Ignore this for now, they're just ideas.

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
