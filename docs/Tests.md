# Testing 

Tests are very important for any application. Jacob Kaplan-Moss said "Code without tests is broken by design". And this statement can't be more true.

So we have multiple tests to check whether this application is _working as expected_. But these tests need certain _user input_ to run such as names of people saved in your WhatsApp contacts. ( To avoid spamming, this application *allows sending messages only to your WhatsApp contacts* ).

__I run the tests on a regular basis and manually update the feature badges__ at the top of this README, to indicate whether that particular feature is successfully working or not. 

If you find that any of the features is not working as expected, _feel free to create an issue_. Nonetheless, you could easily *clone this repo* and **run the tests locally** after configuring the variables in `testConfig.yml` file inside `test_wappdriver` directory. 


## Testing : Why not fully automated ?

These tests __could not be automatically run__ on server via Travis CI or GitHub Actions due to certain constraints due to the nature of WhatsApp and this application. 
These tests could not be automatically run on server via Travis CI or GitHub Actions due to certain constraints as mentioned below:


- Logging in to WhatsApp requires running the GUI Chrome, for scanning QR Codes, thus logging in could not be done in server.
- I thought of logging in from my computer, and then upload the cookies, so that the test runner could login and perform actions in headless mode. But that would compromise my security. As far as I know we cant upload an entire folder to GitHub secrets. There may be certian work-arounds which I might not have discovered or may be I was too lazy to implement those.
- WhatsApp allows you to be logged in only from one Chrome Tab. So if the tester is logged in, to keep it logged in, I have to sacrifice using WhatsApp from my web.
- Currently I have two WhatsApp numbers, one for personal use and the other for business use. To login from WhatsApp Web, your phone must have that WhatsApp account actively logged in and the phone must be connected to the internet. I have only one phone (ultra low spec) ( I know there can be work-around, but that would increase the complexity of my life.




## How to run Tests locally on your machine ?

To Do : add instructions

