import asyncio
import json
import time
from typing import Callable, Optional

import aiohttp
from bs4 import BeautifulSoup

company_data = []


async def get_curr_ruble_exchange_rate(session) -> float:
    """
    Reach cbr.ru and collects current ruble_exchange_rate.
    """
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    async with session.get(url) as resp:
        if resp.status == 200:
            resp_text = await resp.text()
            soup = BeautifulSoup(resp_text, 'lxml')
            find_value = soup.find(id='R01235').value.text.replace(',', '.')
            return float(find_value)


async def get_tab_pages(page_id: int) -> str:
    """Generates urls for tab pages with lists of companies."""
    url = f'https://markets.businessinsider.com' \
          f'/index/components/s&p_500?p={page_id}'
    return url


async def get_companies_url(session, url: str, rubles: float) -> None:
    """
    Receives url, checks connection, gets page text,
    pass received text to get_companies_url.
    Finds part of company url, growth, adds them into
    company_data list of dist. Pass part of url to get_company_data.
    """
    async with session.get(url) as resp:
        if resp.status == 200:
            resp_text = await resp.text()
            soup = BeautifulSoup(resp_text, "lxml")
            company_url = soup.findAll("td", class_="table__td table__td--big")
            growth = soup.findAll('td', class_='table__td')[7] \
                .text.split()[1].strip('%')

            for tags in company_url:
                comp_url = tags.find('a').get('href')
                url = f'https://markets.businessinsider.com{comp_url}'
                global company_data
                company_data.append({'url': url, 'growth': float(growth)})

                await get_company_data(session, url, rubles)


async def get_company_data(session, com_url: str, rubles: float) -> None:
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
                'price': get_price(soup) * rubles,
                'potential_profit': get_potential_profit(
                    soup, get_week_high, get_week_low) * rubles,
                'pe_ratio': get_pe_ratio(soup)
            })


async def gather_data() -> None:
    """
    Gets ruble exchange rate, a list of tab pages. Passes them to
    get_companies_url func.
    Creates tasks with asyncio, establish connection aiohttp session.
    """
    async with aiohttp.ClientSession() as session:
        rubles = await get_curr_ruble_exchange_rate(session)
        initial_pages = [await get_tab_pages(num) for num in range(1, 12)]
        tasks = []
        for page in initial_pages:
            tasks.append(get_companies_url(session, page, rubles))
        await asyncio.gather(*tasks)


def get_week_low(soup: BeautifulSoup) -> Optional[float]:
    """Gets a value of 52 Week Low."""
    week_low_tag = soup.find(
        class_="snapshot__data-item snapshot__data-item--small")
    try:
        week_low_tag.text
    except AttributeError:
        pass
    else:
        week_low = week_low_tag.text.split()[0].replace(',', '')
        return float(week_low)


def get_week_high(soup: BeautifulSoup) -> Optional[float]:
    """Gets a value of 52 Week High."""
    week_high_tag = \
        soup.find("div", class_="snapshot__data-item snapshot__"
                                "data-item--small snapshot__data-item--right")
    try:
        week_high_tag.text
    except AttributeError:
        pass
    else:
        week_high = week_high_tag.text.split()[0].replace(',', '')
        return float(week_high)


def get_potential_profit(soup: BeautifulSoup, week_high: Callable,
                         week_low: Callable) -> float:
    """Calculates a profit if bought at the lowest
     and sold at the highest in the last year."""
    try:
        potential_profit = week_high(soup) - week_low(soup)
        return potential_profit
    except TypeError:
        return 0.0


def get_code(soup: BeautifulSoup) -> Optional[str]:
    """Gets a company code"""
    code_tag = soup.find("span", class_="price-section__category")
    try:
        code_tag.text
    except AttributeError:
        pass
    else:
        code = code_tag.find('span').text.strip(', ')
        return code


def get_name(soup: BeautifulSoup) -> Optional[str]:
    """Gets a company name."""
    name_tag = soup.find("span", class_="price-section__label")
    try:
        name_tag.text
    except AttributeError:
        pass
    else:
        name = name_tag.text.strip()
        return name


def get_price(soup: BeautifulSoup) -> float:
    """Gets a share value converted into rubles."""
    price_tag = soup.find("span", class_="price-section__current-value")
    try:
        price_tag.text
    except AttributeError:
        return 0.0
    else:
        price = price_tag.text.replace(',', '')
        return float(price)


def get_pe_ratio(soup: BeautifulSoup) -> float:
    """Gets the PE Ratio of a company."""
    pe_ratio_tag = soup.find("div", class_="snapshot__header",
                             text='P/E Ratio')
    try:
        pe_ratio_tag.text
    except AttributeError:
        return 100.000
    else:
        pe_ratio = pe_ratio_tag.parent.text.split()[0].replace(',', '')
        return float(pe_ratio)


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
        json.dump(new_dict_sorted[:10], f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    start_time = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(gather_data())

    sort_and_save_results_to_json('price', 'top_10_by_price.json')
    sort_and_save_results_to_json('growth', 'top_10_by_growth.json')
    sort_and_save_results_to_json('potential_profit', 'top_10_by_income.json')
    sort_and_save_results_to_json('pe_ratio', 'top_10_by_pe_ratio.json')
    print("--- %s seconds ---" % (time.time() - start_time))
    # running time 49.071895599365234 seconds
