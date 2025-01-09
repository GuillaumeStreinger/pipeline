using NUnit.Framework;

namespace MyDotNetApp.Tests
{
    [TestFixture]
    public class UnitTest1
    {
        [SetUp]
        public void Setup()
        {
            // Code exécuté avant chaque test
        }

        [Test]
        public void TestAddition()
        {
            int result = 2 + 2;
            Assert.AreEqual(4, result, "Addition should return 4");
        }

        [Test]
        public void TestSubtraction()
        {
            int result = 10 - 5;
            Assert.AreEqual(5, result, "Subtraction should return 5");
        }
    }
}
