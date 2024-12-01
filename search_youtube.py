from pytubefix.contrib.search import Search, Filter

f ={
    "upload_data":Filter.get_upload_data("Today"),
    "type":Filter.get_type("Video"),
    "duration":Filter.get_duration("Live"),
    "features":[Filter.get_features("4K"), Filter.get_features("Creative Commons")],
    "sort_by": Filter.get_sort_by("Upload date")

}

s = Search("gaming", filters=f)

for c in s.videos:
    print(c.title)
    print(c.watch_url)
    print(c.length)
    print(c.likes)
