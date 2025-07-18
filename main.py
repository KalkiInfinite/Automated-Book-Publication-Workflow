import sys
import asyncio

if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
from scraping.scrapper import fetch_chapter
from llm.writer import ai_writer
from llm.reviewer import ai_reviewer
from feedback.human_interface import run_human_loop

    
def main():
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    chapter_id = "chapter1"
    version = 1

    raw_text = fetch_chapter(url)
    spun_text = ai_writer(raw_text)
    reviewed_text = ai_reviewer(spun_text)

    run_human_loop(raw_text, spun_text, reviewed_text, chapter_id, version)

if __name__ == "__main__":
    main()
