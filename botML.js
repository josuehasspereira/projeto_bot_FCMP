const {Builder, By, Key, until} = require('selenium-webdriver');

async function runBot() {
  let driver = await new Builder().forBrowser('chrome').build();

  try {
    await driver.get('https://www.mercadolivre.com.br/');
    await driver.findElement(By.name('as_word')).sendKeys('RTX 2060', Key.RETURN);
    await driver.wait(until.titleContains('RTX 2060'), 10000);

    let elements = await driver.findElements(By.className('ui-search-result__image'));

    for (let i = 0; i < Math.min(elements.length, 5); i++) {
      await elements[i].click();
      await driver.wait(until.titleContains('RTX 2060'), 10000);
      let price = await driver.findElement(By.className('price-tag-fraction')).getText();
      if (price <= 5000) {
        await driver.executeScript('window.open()');
        let handles = await driver.getAllWindowHandles();
        await driver.switchTo().window(handles[handles.length - 1]);
        await driver.get(await driver.findElement(By.css('.ui-pdp-action-modal__action-buttons button.ui-pdp-buybox__button-secondary')).getAttribute('data-modal-url'));
      }
      await driver.switchTo().window(handles[0]);
    }
  } finally {
    await driver.quit();
  }
}

runBot();
