using NUnit.Framework;

namespace MyDotNetApp.Tests;

public class Tests
{
    [SetUp]
    public void Setup()
    {
    }

    [Test]
        public void Addition_ReturnsCorrectSum()
        {
            // Arrange
            int a = 2;
            int b = 3;

            // Act
            int result = a + b;

            // Assert
            Assert.AreEqual(5, result, "Addition should return the correct sum");
        }

        [Test]
        public void Subtraction_ReturnsCorrectDifference()
        {
            // Arrange
            int a = 5;
            int b = 3;

            // Act
            int result = a - b;

            // Assert
            Assert.AreEqual(2, result, "Subtraction should return the correct difference");
        }

        [Test]
        public void Division_ThrowsDivideByZeroException()
        {
            // Arrange
            int a = 10;
            int b = 0;

            // Act & Assert
            Assert.Throws<System.DivideByZeroException>(() =>
            {
                var result = a / b;
            }, "Division by zero should throw an exception");
        }
}