const {Builder, By, Key, until} = require('selenium-webdriver');

async function example() {
  let driver = await new Builder().forBrowser('chrome').build();
  try {
    await driver.get('https://www.mercadolivre.com.br/');

    // Inserir a pesquisa e pressionar Enter
    await driver.findElement(By.name('as_word')).sendKeys('RTX 2060', Key.RETURN);

    // Esperar o botão "Usado" estar disponível e clicar nele
    await driver.wait(until.elementLocated(By.xpath('//label[@for="ITEM_CONDITION2230581"]/input')));
    await driver.findElement(By.xpath('//label[@for="ITEM_CONDITION2230581"]/input')).click();

    // Esperar o botão "Menos de 8 GB" estar disponível e clicar nele
    await driver.wait(until.elementLocated(By.xpath('//label[@for="RAM_MEMORY_QTY_6-8"]/input')));
    await driver.findElement(By.xpath('//label[@for="RAM_MEMORY_QTY_6-8"]/input')).click();

    // Inserir o preço mínimo e máximo
    await driver.findElement(By.name('priceMin')).sendKeys('900');
    await driver.findElement(By.name('priceMax')).sendKeys('1600', Key.RETURN);

    // Esperar até que 5 resultados de busca estejam disponíveis
    await driver.wait(until.elementsLocated(By.xpath('//li[contains(@class, "search-result ")]')), 10000);
    const elements = await driver.findElements(By.xpath('//li[contains(@class, "search-result ")]'));
    if (elements.length < 5) {
      console.log(`Apenas ${elements.length} resultados de busca encontrados.`);
    } else {
      // Selecionar os 5 primeiros resultados e abrir em novas abas
      for (let i = 0; i < 5; i++) {
        await elements[i].findElement(By.xpath('.//a')).sendKeys(Key.chord(Key.CONTROL, Key.RETURN));
      }
    }

  } finally {
    // Fechar o navegador
    await driver.quit();
  }
}

example();
