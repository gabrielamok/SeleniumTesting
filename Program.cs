using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using System;
using System.IO;

class Program
{
    static void Main(string[] args)
    {
        // Set up WebDriver
        IWebDriver driver = new ChromeDriver();

        try
        {
            // Navigate to the target page
            driver.Navigate().GoToUrl("http://the-internet.herokuapp.com");
            
            // Maximize the window
            driver.Manage().Window.Maximize();

            // Click the "Notification Messages" link
            var notificationLink = driver.FindElement(By.LinkText("Notification Messages"));
            notificationLink.Click();

            // Take a screenshot of the Notification Messages page
            TakeScreenshot(driver, "NotificationMessagesPage.png");

            // Click the "Click Here" link in the Notification Messages page
            var clickHereLink = driver.FindElement(By.LinkText("Click here"));
            clickHereLink.Click();

            // Wait for the page to load
            System.Threading.Thread.Sleep(2000);

            // Take a screenshot after clicking the link
            TakeScreenshot(driver, "AfterClickHere.png");

            Console.WriteLine("Test completed successfully!");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred: {ex.Message}");
        }
        finally
        {
            // Close the browser
            driver.Quit();
        }
    }

    static void TakeScreenshot(IWebDriver driver, string fileName)
    {
        try
        {
            // Capture screenshot
            Screenshot screenshot = ((ITakesScreenshot)driver).GetScreenshot();

            // Save the screenshot as a .png file
            string filePath = Path.Combine(Directory.GetCurrentDirectory(), fileName);
            File.WriteAllBytes(filePath, screenshot.AsByteArray);
            Console.WriteLine($"Screenshot saved at: {filePath}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error taking screenshot: {ex.Message}");
        }
    }
}
