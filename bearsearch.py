from googlesearch import search
from newspaper import Article
from newspaper.article import ArticleException 
import streamlit as st


st.title("Bear Projects")

def article_content(url):
    article = Article(url)
    
    try:
        article.download()
        article.parse()
        article.nlp()
        st.write(article.summary)
    except ArticleException as e:
        print("Error while processing article:", e)

def search_and_extract(query):
    search_results = search(query)
    for i, result in enumerate(search_results, start=1):
        if result in visited_links:
            continue
        visited_links.add(result)
        st.subheader(result)
        article_content(result)

if __name__ == "__main__":
    visited_links = {"https://www.sciencedirect.com/science/article/pii/S0306919218303816", "https://thehill.com/changing-america/sustainability/environment/592820-these-new-technologies-could-transform-wildlife/"}
    search_queries = ['technology that can be used to help bears', 'conservation technologies used to help bears','independent projects that can help bears','small-scale bear helping initiatives ']
    for search_query in search_queries:
        search_and_extract(search_query)
