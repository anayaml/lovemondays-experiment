const puppeteer = require("puppeteer");
const chalk = require("chalk");
var fs = require("fs");

// MY OCD of colorful console.logs for debugging... IT HELPS
const error = chalk.bold.red;
const success = chalk.keyword("green");

(async () => {
  try {
    // open the headless browser
    var browser = await puppeteer.launch({ headless: false });
    // open a new page
    var page = await browser.newPage();
    // enter url in page
    await page.goto(`https://www.lovemondays.com.br/trabalhar-na-accenture/avaliacoes`);
    await page.waitForSelector("ul.lm-List-default");

    var news = await page.evaluate(() => {
      var username = document.querySelectorAll(`span.reviewer`);
      var avaliation = document.querySelectorAll(`div.lm-Review-contribution`);
      var titleLinkArray = [];
      for (var i = 0; i < username.length; i++) {
        titleLinkArray[i] = {
          user: titleNodeList[i].innerText.trim(),
          avaliation: avaliation[i].innerText.trim()
        };
      }
      return titleLinkArray;
    });
    // console.log(news);
    await browser.close();
    // Writing the news inside a json file
    fs.writeFile("teste.json", JSON.stringify(news), function(err) {
      if (err) throw err;
      console.log("Saved!");
    });
    console.log(success("Browser Closed"));
  } catch (err) {
    // Catch and display errors
    console.log(error(err));
    await browser.close();
    console.log(error("Browser Closed"));
  }
})();