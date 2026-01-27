import html
from rich.console import Console
from bs4 import BeautifulSoup as bs

console = Console()

def decode(text):
    return bs(html.unescape(text), "html.parser").get_text("\n") if text else ""