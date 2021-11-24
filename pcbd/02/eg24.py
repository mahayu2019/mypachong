#!/usr/bin/env python
# coding=utf-8

import asyncio
from pyppeteer import launch


async def main():
    browser = await  launch()

    page = await browser.newPage()
    await page.goto('https://www.phei.com.cn')
    await page.screenshot({'path': 'example.jpg'})
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
