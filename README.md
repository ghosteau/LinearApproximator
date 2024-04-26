# Linear Approximation
Built off of some of the functions I used for my Newton's Method application, I decided to make another calculus application that performs linearization using derivatives and finding tangent lines. The general formula for linearization is f(a) + f'(a)(x - a), which turns into a function called L(x), and therefore prepares it for linearization. Why do we do this process? Originally, it was a concept used to approximate very complex or weird values, such as the square root of 1.99, or 3.99 cubed. Understandably, doing this with a real function would be quite difficult, but using derivatives and tangents simplifies complex functions into basic linear functions, therefore allowing us to find very close answers to the real value with much less work. 

With the modern marvel of computers, this may not necessarily be an issue, but I figured writing a program that could show the difference between approximated values on the tangent line and the actual function would be pretty neat, and be a cool little study that we can think of using calculus. Additionally, this is still a pretty useful concept especially when dealing with very complex functions, and in particular when you just need a rough answer. 

I have displayed a desmos image as an example of the function x^3, in which I show a red tangent line, and the real function in black. As you can see, when we get closer to the tangent line's "touching" value with the real function, the better the approximation is. This visualization is exactly what the program does in effect, allowing us to observe these differences within a quick Python environment.

Another fun fact about this is that it is the first expansion of the Taylor Series, if you have ever taken calculus 2 this may seem familiar.

Thank you and enjoy!
