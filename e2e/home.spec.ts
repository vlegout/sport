import { test, expect } from "@playwright/test";

test("has title", async ({ page }) => {
  await page.goto("/");

  await expect(page).toHaveTitle(/Stride/);
});

test("has activities header link", async ({ page }) => {
  await page.goto("/");

  await expect(page.getByText("Activities")).toBeDefined();
});
