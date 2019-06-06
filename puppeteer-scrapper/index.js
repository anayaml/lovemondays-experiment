const puppeteer = require("puppeteer");
const chalk = require("chalk");
var fs = require("fs");

// MY OCD of colorful console.logs for debugging... IT HELPS
const error = chalk.bold.red;
const success = chalk.keyword("green");
const lastPageNumber = 10;

loveMondaysLogin = () =>
{
  
}

(async () => {
  try {
    // open the headless browser
    var browser = await puppeteer.launch({headless: false });
    // open a new page
    var page = await browser.newPage();

    await page.goto(`https://www.lovemondays.com.br/usuarios/entrar#email-sign-in`, {waitUntil: 'networkidle2'});

    //document.getElementById("email-sign-in").setAttribute("aria-expanded", "true");
    // await page.type('input[name=search]', 'Adenosine triphosphate');
    // enter url in page
    // for (let index = 1; index < lastPageNumber; index++) {      
    //   await page.goto(`URLHERE` +index);
    //   await page.waitForSelector("ul.lm-List-default");
    //   var ratings = await page.evaluate(() => {
    //     var job = document.querySelectorAll(`span.reviewer`);
    //     var avaliation = document.querySelectorAll(`div.lm-Review-contribution`);
    //     var titleLinkArray = [];
    //     for (var i = 0; i < job.length; i++) {
    //         titleLinkArray[i] = {
    //           user: job[i].innerText,
    //           avaliation: avaliation[i].innerText
    //         };
    //     }
    //     return titleLinkArray;
    //   });
    //   fs.writeFile(index + ".json", JSON.stringify(ratings), function(err) {
    //     if (err) throw err;
    //     console.log(index);
    //   });
    //}
  } catch (err) {
    // Catch and display errors
    console.log(error(err));
    await browser.close();
    console.log(error("Browser Closed"));
  }
})();