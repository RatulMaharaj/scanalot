import { expect, test } from "@playwright/test";
import { sendPushNotification } from "./notify";

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

test("Check incredible.co.za", async ({ page }) => {
  const url = "https://www.incredible.co.za/apple-iphone-16-pro";
  await page.goto(url);

  // find the button that says white titanium and click it
  await page.locator("#option-label-sap_colour-889-item-25567").click();

  // check if the 128GB option div is disabled
  // 256: option-label-storage_capacity-955-item-11384
  const storageBtn = page.locator(
    "#option-label-storage_capacity-955-item-11382"
  );

  // check if storage button is disabled
  const isDisabled = await storageBtn.getAttribute("disabled");

  // if it is available, click it
  if (isDisabled?.toLowerCase() !== "disabled") {
    // send pushover notification
    await sendPushNotification(
      `iPhone 16 Pro available at Incredible Connection`,
      url
    ).catch(console.error);
  }
});

test("Check istore.co.za", async ({ page }) => {
  const url = "https://www.istore.co.za/shop-iphone-16-pro";
  await page.goto(url);

  // click cookie button if it exists
  const cookieBtn = page.locator("#btn-cookie-allow");
  if (await cookieBtn.isVisible()) {
    await cookieBtn.click();
  }

  // find the button that says white titanium and click it
  await page.locator("#option-label-color-93-item-9006").click();

  // check if the 128GB option div is disabled
  // 256: option-label-storage_capacity-955-item-11384
  await page.locator("#option-label-capacity-363-item-253").click();

  // decline trade in
  await page.getByText("I don't want to trade in").click();
  await page.getByText("No, thank you").click();

  // check if storage button is disabled
  const addToCartButton = page.locator("#product-addtocart-button");

  // check inner text of button
  await sleep(2000);
  const isBackOrdered = await addToCartButton.innerText();
  console.log(isBackOrdered.toLocaleLowerCase().includes("back order"));

  // if it is available, click it
  if (!isBackOrdered.toLocaleLowerCase().includes("back order")) {
    // send pushover notification
    await sendPushNotification(
      `iPhone 16 Pro available at the iStore`,
      url
    ).catch(console.error);
  }
});

test("Check digicape.co.za", async ({ page }) => {
  const url =
    "https://www.digicape.co.za/product/iphone-16-pro-128gb-white-titanium";
  await page.goto(url);

  // get the element with id btn
  const addToCartBtn = await page
    .locator(
      '[data-product-action="https://www.digicape.co.za/index.php?route=checkout/cart/add"]'
    )
    .innerText();

  console.log({ addToCartBtn });

  const isBackOrdered = addToCartBtn.toLowerCase().includes("backorder");

  // if it is available, click it
  if (!isBackOrdered) {
    // send pushover notification
    await sendPushNotification(
      `iPhone 16 Pro available at Digicape`,
      url
    ).catch(console.error);
  }
});

test("Check Takealot", async ({ page }) => {
  const url =
    "https://www.takealot.com/apple-iphone-16-pro-128gb/PLID95955146?colour_variant=White+Titanium";
  await page.goto(url);

  await page.waitForSelector(".pdp-module_sidebar-buybox_1m6Sm");

  const sidebarContent = await page
    .locator(".pdp-module_sidebar-buybox_1m6Sm")
    .allInnerTexts();

  let isInStock = false;
  sidebarContent.map((content) => {
    if (content.toLowerCase().includes("add to cart")) {
      isInStock = true;
    }

    if (content.toLowerCase().includes("supplier out of stock")) {
      isInStock = false;
    }
  });

  if (isInStock) {
    // if it is available, click it
    // send pushover notification
    await sendPushNotification(
      `iPhone 16 Pro available at Takealot`,
      url
    ).catch(console.error);
  }
});
