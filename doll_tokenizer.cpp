/**********************************************************************************/
/* doll_tokenizer.cpp                                                             */
/**********************************************************************************/
/* Copyright (c) 2023 JeffVenancius                                               */
/**********************************************************************************/
/* Permission is hereby granted, free of charge, to any person obtaining a copy   */
/* of this software and associated documentation files (the "Software"), to deal  */
/* in the Software without restriction, including without limitation the rights   */
/* to use, copy, modify, merge, publish, distribute, sublicense, and/or sell      */
/* copies of the Software, and to permit persons to whom the Software is          */
/* furnished to do so, subject to the following conditions:                       */
/*                                                                                */
/* The above copyright notice and this permission notice shall be included in all */
/* copies or substantial portions of the Software.                                */
/**********************************************************************************/
/* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR     */
/* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,       */
/* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE    */
/* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER         */
/* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  */
/* OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  */
/* SOFTWARE.                                                                      */
/**********************************************************************************/

static const char *token_names[] = {
	"Empty",
	"Annotation",
	"((", // open comment
	"))", // close comment
	"Identifier",
	"Literal",

	//comparison
	"<",
	"<=",
	">", 
	">=", 
	"a", // equal to (==)
	"==", 
	"!=", 
	"not a", // not equal to 
					 
	// logical
	"and", 
	"or", 
	"not", 
	"&&",
	"||",
	"!",

	// Bitwise
	"&",
	"|",
	"~",
	"^",
	"<<",
	">>",

	// Math
	"+",
	"-", // indentation mark if in begining of line
	"*",
	"**",
	"/", // defines typing depending on context, which means: after item but before the item name and after ":" in howTo.
	"=",
	"+=",
	"is and", // concatenation
	"is but", // deconcatenation
	"*=",
	"**=",
	"/=",
	"%=",
	"<<=",
	">>=",
	"&=",
	"|=",
	"^=",
	// control flow
	"is",
	"then is",
	"well then",
	"?", // ternary if
	"??", // ternary else
	"do", // for
	"as long",
	"cut", // break
	"keep going", // continue
	"ignore", // pass
	"give", // return
	"what is", // switch
	"as",
	"wait for", // await, yield
	"breakpoint",
	"kind",
	"remember", // const
	"howTo", // func
	"in",
	"is",
	"nomenclature", // namespace
	"preload",
	"self",
	"signal",
	"genus", //super
	"item", // var
	"void",

	// punctuation
	"[",
	"]",
	"{",
	"}",
	"(",
	")",
	",",
	";", // indentation mark in the same line.
	".",
	"..",
	":",
	"$",
	"->",
	"//",
	"_",

	// whitespace
	"Newline",
	"Indent", // - 
	"Dedent",

	// constants
	"PI",
	"TAU",
	"NaN",
	"`",
	"Error",
	"End of file",
}
