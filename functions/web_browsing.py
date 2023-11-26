from functions.duck_duck_go_search import DuckDuckGoSearchManager
from functions.web_scraper import WebContentScraper

web = DuckDuckGoSearchManager()
scraper = WebContentScraper()


def text_search(query: str, num_results: int = 3) -> str:
    """Conducts a general web text search and retrieves information from the internet in response to user queries.

    This function is best used when the user's query is seeking broad information available on various websites. It
    is ideal for queries that require diverse perspectives or data from multiple sources, not limited to current
    events or specific topics. Use this function for general inquiries, research, or when the user's query is not
    explicitly news-related. It fetches relevant data from the internet in response to user queries, enhancing GPT's
    knowledge base.

    :param query: The search query string for finding relevant web text results.
    :param num_results: The maximum number of URLs to return. Defaults to 3 if not provided. (optional)

    :return: A JSON-formatted string. Each element in the JSON represents the result of scraping a single URL,
    containing either the scraped content or an error message.
    """
    urls = web.text_search(query, int(num_results))
    scraped_data = scraper.scrape_multiple_websites(urls)
    return scraped_data


def news_search(query, num_results=5):
    """Conducts a search for news articles and retrieves information from the internet in response to user queries.

    This function is specifically designed for queries that require up-to-date information from news sources. It
    should be employed when the user is looking for recent developments, news stories, or when the query is
    explicitly about current events, politics, or other timely topics. Opt for this function for news-related
    inquiries or when the query demands the latest information from reliable news outlets. It fetches relevant data
    from the internet in response to user queries, enhancing GPT's knowledge base.

    :param query: The search query string for finding relevant news articles.
    :param num_results: The maximum number of news article URLs to return. Defaults to 3 if not provided.

    :return: A JSON-formatted string. Each element in the JSON represents the result of scraping a single URL,
    containing either the scraped content or an error message.
    """
    urls = web.news_search(query, int(num_results))
    scraped_data = scraper.scrape_multiple_websites(urls)
    return scraped_data


def images_search(query, num_results=3):
    """Performs the image search for a specific query. For example, "puppies". If possible, output to the user as markdown format.

    This function enables real-time image search and information retrieval for GPT models. It fetches relevant data from the internet in response to user queries, enhancing GPT's knowledge base.

    :param query: The search query string for the image search.
    :param num_results: The maximum number of URLs to return. Defaults to 3 if not provided. (optional)

    :return: A list of dictionaries, where each dictionary contains 'image' (URL of the actual image) and 'thumbnail' (URL of the image's thumbnail).
    """

    image_info = web.images_search(query, int(num_results))
    return image_info


def videos_search(query, num_results=3):
    """Performs the video for a specific query. For example, "video tutorial for Excel pivot table". If possible, output to the user as markdown format.

    This function enables real-time video search and information retrieval for GPT models. It fetches relevant data from the internet in response to user queries, enhancing GPT's knowledge base.

    :param query: The search query string for finding relevant video results.
    :param num_results: The maximum number of URLs to return. Defaults to 3 if not provided. (optional)

    :return: A list of dictionaries, where each dictionary represents a search result. Each dictionary contains two keys: 'title', title of the content, and 'content', URL to the resource.
    """

    video_info = web.videos_search(query, int(num_results))
    return video_info


def maps_search(query, place, num_results=3):
    """Performs the location for a specific query. For example, "Italian restaurant in Berlin". If possible, output to the user as a table format.

    This function enables real-time location search and information retrieval for GPT models. It fetches relevant data from the internet in response to user queries, enhancing GPT's knowledge base.

    :param query: The search query string for finding relevant location results.
    :param place: The place where the search is performed.
    :param num_results: The maximum number of URLs to return. Defaults to 3 if not provided. (optional)

    :return: A list of dictionaries, each representing a restaurant. Each dictionary includes the location's title, address, phone number, URL, and a nested dictionary of operating hours with keys indicating days of the week and additional status information like 'closes_soon', 'is_open', and 'state_switch_time'.
    """
    map_info = web.maps_search(query, place, int(num_results))
    return map_info


# Debug code
# print(text_search("Is Sam Altman fired from OpenAI?", 5))
print(news_search("Is Sam Altman fired from OpenAI?", 5))
# print(images_search("puppies", 5))
# print(videos_search("video tutorial for Excel pivot table", 5))
# print(maps_search("Italian  restaurant", "berlin", 5))

# from core.parser import FunctionDefinitionParser
# parser = FunctionDefinitionParser()
# print(parser.convert_function_to_json_schema(text_search))