# Method overloading
#  In Python, method overloading is not supported in the same way as it is in some other programming languages like Java or C++.



class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b

# Creating an instance of the Calculator class
calc = Calculator()

# Overloaded method call
print(calc.add(2, 3))       # Output: 5
print(calc.add(2, 3, 4))    # Output: 9
print(calc.add(2, 5))       # Output: 7

"""
c# method overloading
using System;

class Calculator
{
    // Method overloading
    public int Add(int a, int b)
    {
        return a + b;
    }

    public double Add(double a, double b)
    {
        return a + b;
    }

    public int Add(int a, int b, int c)
    {
        return a + b + c;
    }
}

class Program
{
    static void Main(string[] args)
    {
        Calculator calc = new Calculator();

        // Calls the Add method with two integer arguments
        Console.WriteLine(calc.Add(2, 3));            // Output: 5

        // Calls the Add method with two double arguments
        Console.WriteLine(calc.Add(2.5, 3.5));        // Output: 6.0

        // Calls the Add method with three integer arguments
        Console.WriteLine(calc.Add(2, 3, 4));         // Output: 9
    }
}
"""