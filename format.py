from os import listdir;
import markdown
import re
import json
from datetime import datetime, date
from collections import defaultdict
import pytz
from feedgen.feed import FeedGenerator
from framework import generateFuncTemplate
"""
logic goes:
    # Go through each markdown file
    # Create post data object
        # Note that post.md will have special syntax for determining file 

    # After creating post data file order posts by:
        # Date
        # Topic

        # Then append this information for each post


    # This is all information required to actually generate file for each post type
        # If byDate is empty then don't include it etc
        # To generate the correct header, base it on the directory structure for posts (?)
            # e.g if posts/art then replace post object with desired html and so on
        

    # For light and dark, generate 2 css variables for light and dark and then conditionally create them        
        # Constants folder(? - Good enough)

    # Then use this to generate navigation for each type
        # Include special markdown file for topics

topics: [
    {
        topic: string
        descrip: string
    }
]

post: {
    id: randomValue:
    name: string,
    date: date,
    topic: enum, 
    path: file.html,
    nextPost: {
        byDate: string
        byTopic: string
    },
    prevPost: {
        byDate: string
        byTopic: string
    }
}
"""

def getTopics():
    with open("assets/topics.json", 'r') as f:
        topics = f.readlines()
        topics = ''.join(topic.strip() for topic in topics)
        topics =  json.loads(topics)
        for i in topics:
            i["posts"] = []
        return topics

        #[
        #    {topic: name,
        #    posts: [name]
        #    }
        #]


def initOutput(focused, posts):
    return generateFuncTemplate("./assets/template.html") (
        generateFuncTemplate("./assets/header.html") (
        ricky = "focused" if focused == "ricky" else "",
        posts = "focused" if focused == "posts" else "",
        archive = "focused" if focused == "archive" else "",
        mostRecentPost = posts[0]["path"] + ".html"
        )
    )


# Should be fairly easy to implement now :)

posts = []
topics = getTopics() # Gets correct topics
for i in listdir("./posts/"):
    with open("./posts/"+i, 'r') as f:
        post = {}
        line = f.readline()
        while(line.startswith("^")):
            # Extract tag - set to lower case
            # Extract description and set as value
            tag = re.match("\^[a-zA-Z0-9]*", line).group(0)[1:]
            description = line.replace("^"+tag, "").rstrip().lstrip()
            if (tag.lower() == "date"):
                post[tag.lower()] = datetime.strptime(description.strip(), "%Y-%m-%d")
            else:
                post[tag.lower()] = description.strip()
            line = f.readline()
        post["path"] = i[:-3]
       
        post["nextPost"] = {"byDate": None, "byTopic": None}
        post["prevPost"] = {"byDate": None, "byTopic": None}
        

        # Throw error here if topic is undefined or not within specified enum
        if ("title" not in post):
            raise AssertionError("no title provided")
        if ("date" not in post):
            raise AssertionError("no date provided")
        if ("topic" not in post):
            raise AssertionError("no topic provided")
        topicList = [e["name"] for e in topics]
        if (post["topic"] not in topicList):

            raise AssertionError("topic not defined")

        posts.append(post)


# Now we need to order based on date and topic
posts = sorted(posts, key = lambda x: x["date"])
posts.reverse()
    # should be earliest to latest


prev = posts[0]
for post in posts[1:]:
    post["nextPost"]["byDate"] = prev["path"]
    prev["prevPost"]["byDate"] = post["path"]
    prev = post


# Put each post into corresponding sublist based on topic:


topicsPostHolder = defaultdict(list)
for post in posts:
    topicsPostHolder[post["topic"]].append(post)

for topic in topicsPostHolder:
    prev = topicsPostHolder[topic][0]
    for post in topicsPostHolder[topic][1:]:
        post["nextPost"]["byTopic"] = prev["path"]
        prev["prevPost"]["byTopic"] = post["path"]
        prev = post

for topic in topics:
    list1 = []
    for post in topicsPostHolder[topic["name"]]:
        list1.append(post)
    topic["posts"] = list1


# Put each post into corresponding sublist based on year:
yearPostHolder = defaultdict(list)
for post in posts:
    yearPostHolder[post["date"].year].append(post)



# So now we have topics, and posts which should be everything required to generate every page and thingy 

latestPost = posts[0]

# Begin generating pages:
for post in posts:

    with open("./posts/"+post['path']+".md" , 'r') as f:

        output = initOutput("posts", posts)
        line = f.readline()
        while(line.startswith("^")):
            line = f.readline()

        format1 = "<h1>" + post["title"] + "</h1>\n"
        format1 += "<p class = \"date\">" + post["date"].strftime("published on  %B %d, %Y") + "</p>\n"


        post["description"] = markdown.markdown(f.read())
        format1 +=     "<div class = \"bodyStyle\">" +(post['description']) + "</div>"
        output = output(body = format1)
       
        output = output(generateFuncTemplate("./assets/footer.html")(
            nextPost = "" if post["nextPost"]["byDate"] else "invisible",
            nextPart = "" if post["nextPost"]["byTopic"] else "invisible",
            prevPost = "" if post["prevPost"]["byDate"] else "invisible",
            prevPart = "" if post["prevPost"]["byTopic"] else "invisible"
        )(
            nextPostLink = post["nextPost"]["byDate"]+ ".html" if post["nextPost"]["byDate"] else "",
            nextPartLink = post["nextPost"]["byTopic"]+ ".html" if post["nextPost"]["byTopic"] else "",
            prevPostLink = post["prevPost"]["byDate"]+ ".html" if post["prevPost"]["byDate"] else "",
            prevPartLink =  post["prevPost"]["byTopic"]+ ".html" if post["prevPost"]["byTopic"] else ""
        ))
        
    with open("./compiled/" + post['path'] + ".html", 'w' ) as f:
        f.write(output)





output = initOutput("archive", posts)

# Generate navigation by date:

body = generateFuncTemplate("./assets/navigationTemplate.html")(
        navigation="By date"
    )(
        navigationLink = "<a href=\"topicNavigation.html\">By topic</a>"
    )

for year in yearPostHolder.keys():
    body += "<h2 >" + str(year) + "</h2>\n"
    for post in yearPostHolder[year]:
        body += "<div class = \"rowFlexBox archiveNav\" ><div class = \"navDate navPadding\">"+ post["date"].strftime("%B %d")  +"</div><a href = "+ post["path"] + ".html class = \"navPadding\">"+ post["title"]+"</a></div>\n"
   
output = output(body = body)(footer="")

with open("./compiled/" + "dateNavigation" + ".html", 'w' ) as f:
    f.write(output)




output = initOutput("archive", posts)

# Generate navigation by topic:
body = generateFuncTemplate("./assets/navigationTemplate.html")(
        navigation="By topic"
    )(
        navigationLink = "<a href=\"dateNavigation.html\">By date</a>"
    )    

for topic in topics:
    body += "<h2 style=\"margin-bottom:0;\">" + topic["name"] + "</h2>\n"
    body += "<p class = \"description\">" + topic["Description"] + "</p>\n"
    for post in topic["posts"]:
        body += "<div class = \"rowFlexBox archiveNav\" ><div class = \"navDate navPadding\">"+ post["date"].strftime("%B %d, %Y")  +"</div><a href = "+ post["path"] + ".html class = \"navPadding\">"+ post["title"]+"</a></div>\n"

output = output(body = body)(footer="")

with open("./compiled/" + "topicNavigation" + ".html", 'w' ) as f:
    f.write(output)





output = initOutput("ricky", posts)

output = output(body = "")(footer="")

with open("./compiled/" + "index" + ".html", 'w' ) as f:
    f.write(output)



# Feed generator
fg = FeedGenerator()
fg.title("RSS Feed for rleek.github.io")
fg.link(href="https://rleek.github.io/")
fg.description("Hi, I'm Ricky and this is my personal blog")
fg.author({'name':'Ricky Liu', 'email':'rky.w.liu@gmail.com'})
fg.language("en-au")
fg.pubDate(pytz.utc.localize(datetime.today()))


posts.reverse();

for post in posts:
    fe = fg.add_entry()
    fe.title(post["title"])
    fe.link(href = "https://rleek.github.io/" + post["path"] + ".html")
    fe.author({'name':'Ricky Liu', 'email':'rky.w.liu@gmail.com'})
    fe.description(post["description"])
    fe.id("https://rleek.github.io/" + post["path"] + ".html")
    fe.pubDate(pytz.utc.localize(post["date"]))

fg.rss_file('compiled/rss.xml') 










