import asyncio
import json
import time
from typing import Callable, Optional

import aiohttp
import requests
from bs4 import BeautifulSoup

company_data = []


def get_curr_ruble_exchange_rate() -> float:
    """
    Reach cbr.ru and collects current ruble_exchange_rate.
    """
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    try:
        response = requests.get(url)
    except requests.exceptions:
        raise ValueError("Unreachable {url}")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        find_value = soup.find(id='R01235').value.text.replace(',', '.')
        return float(find_value)


async def get_tab_pages(session, page_id: int) -> None:
    """Generates urls for tab pages with lists of companies.
    Checks connection, gets page text,
    pass received text to get_companies_url."""
    url = f'https://markets.businessinsider.com' \
          f'/index/components/s&p_500?p={page_id}'
    async with session.get(url) as resp:
        if resp.status == 200:
            resp_text = await resp.text()
            await get_companies_url(session, resp_text)


async def get_companies_url(session, response_text: str) -> None:
    """Receives a page text from get_tab_pages,
    finds part of company url, growth, adds them into
    company_data list of dist. Pass part of url to get_company_data.
    """
    soup = BeautifulSoup(response_text, "lxml")
    company_url = soup.findAll("td", class_="table__td table__td--big")
    growth = soup.findAll('td', class_='table__td')[7] \
        .text.split()[1].strip('%')

    for tags in company_url:
        comp_url = tags.find('a').get('href')
        url = f'https://markets.businessinsider.com{comp_url}'
        global company_data
        company_data.append({'url': url, 'growth': float(growth)})

        await get_company_data(session, url)


async def get_company_data(session, com_url: str) -> None:
    """
    Adds name, price, code, pe_ratio, potential_profit
    to company data list of dict.
    """
    async with session.get(com_url) as resp:
        if resp.status == 200:
            company_page_text = await resp.text()
    soup = BeautifulSoup(company_page_text, "lxml")

    global company_data
    for dictionary in company_data:
        if dictionary['url'] == com_url:
            dictionary.update({
                'name': get_name(soup), 'code': get_code(soup),
                'price': get_price(soup),
                'potential_profit': get_potential_profit(get_week_high,
                                                         get_week_low, soup),
                'pe_ratio': get_pe_ratio(soup)
            })


async def gather_data() -> None:
    """
    Creates tasks with asyncio, establish connection aiohttp session.
    """
    async with aiohttp.ClientSession() as session:
        tasks = [get_tab_pages(session, num) for num in range(1, 12)]
        await asyncio.gather(*tasks)


def get_week_low(soup) -> Optional[float]:
    """Gets a value of 52 Week Low."""
    try:
        week_low = soup.find(
            class_="snapshot__data-item snapshot__data-item--small"
        ).text.split()[0].replace(',', '')
        return float(week_low)
    except AttributeError:
        pass


def get_week_high(soup) -> Optional[float]:
    """Gets a value of 52 Week High."""
    week_high_preprocessing = \
        soup.find("div", class_="snapshot__data-item snapshot__"
                                "data-item--small snapshot__data-item--right")
    try:
        week_high = week_high_preprocessing.text.split()[0].replace(',', '')
        return float(week_high)
    except AttributeError:
        pass


def get_potential_profit(week_high: Callable,
                         week_low: Callable, soup) -> float:
    """Calculates a profit if bought at the lowest
     and sold at the highest in the last year."""
    try:
        potential_profit = \
            (week_high(soup) - week_low(soup)) * get_curr_ruble_exchange_rate()
        return potential_profit
    except TypeError:
        return 0.0


def get_code(soup) -> Optional[str]:
    """Gets a company code"""
    try:
        code = soup.find("span", class_="price-section__category") \
            .find('span').text.strip(', ')
        return code
    except AttributeError:
        pass


def get_name(soup) -> Optional[str]:
    """Gets a company name."""
    try:
        name = soup.find("span", class_="price-section__label").text.strip()
        return name
    except AttributeError:
        pass


def get_price(soup) -> Optional[float]:
    """Gets a share value converted into rubles."""
    try:
        price = soup.find("span", class_="price-section__current-value") \
            .text.replace(',', '')
        return float(price)*get_curr_ruble_exchange_rate()
    except AttributeError:
        pass


def get_pe_ratio(soup) -> float:
    """Gets the PE Ratio of a company."""
    try:
        pe_ratio = soup.find(
            "div", class_="snapshot__header",
            text='P/E Ratio'
        ).parent.text.split()[0].replace(',', '')
        return float(pe_ratio)
    except AttributeError:
        return 100.000


def sort_and_save_results_to_json(key: str, file_name: str) -> None:
    """
    Creates new list of dicts with code, name and received key,
    sorts company_data list by received key, saves data to a json file.
    """
    new_dict = [
        {
            k: v for k, v in d.items() if k in {'code', 'name', key}
        } for d in company_data]
    new_dict_sorted = sorted(new_dict, key=lambda k: k[key], reverse=True)
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(new_dict_sorted[:10], f)


if __name__ == "__main__":
    start_time = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(gather_data())

    sort_and_save_results_to_json('price', 'top_10_by_price.json')
    sort_and_save_results_to_json('growth', 'top_10_by_growth.json')
    sort_and_save_results_to_json('potential_profit', 'top_10_by_income.json')
    sort_and_save_results_to_json('pe_ratio', 'top_10_by_pe_ratio.json')
    print("--- %s seconds ---" % (time.time() - start_time))
    # running time 104.66454195976257 seconds
