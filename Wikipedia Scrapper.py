import wikipedia as wiki
print(wiki.search("Python (genus)"))
print(wiki.suggest("Python (genus)"))
print(wiki.summary("Python (genus)"))
print(wiki.summary("Python (genus)"))
p = wiki.page("Python (genus)")
print(p.title)
print(p.url)
print(p.content)
print(p.images)
print(p.links)