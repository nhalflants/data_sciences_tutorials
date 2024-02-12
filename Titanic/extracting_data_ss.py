import requests
from bs4 import BeautifulSoup
# from IPython.core.display import display, HTML

html_string = """

<!DOCTYPE htlm>

<html lang="en">
<head>
    <title>Raw HTML</title>
</head>

<body>

    <div id="mainbox">
        <h1 class="firstHeading">Raw HTML</h1>

        <p>With Sandvox you can add Raw HTML objects to a page, and Raw HTML pages (containing no Sandvox-generated content) to a site. For some Raw HTML object ideas, have a look at the "<a href="Raw_HTML_object_examples.html" title="Raw HTML object examples">Raw HTML object examples</a>" article.</p>

        <div class="warning">
            <p>The ability to use custom HTML code is an advanced ability of Sandvox. If you want to edit raw HTML, we assume that you already have a working knowledge of HTML or wish to obtain one; this page is by no means intended as an HTML tutorial, nor can Karelia provide specific troubleshooting advice related to an individual user's HTML code.</p>

            <p>If you want to learn more about HTML before attempting to edit raw HTML in your Sandvox site, we encourage you to visit the following third party sites that specifically address HTML issues:</p>

            <ul>
                <li><a href="http://www.htmlcodetutorial.com/" class="external text" title="http://www.htmlcodetutorial.com/">The HTML Code Tutorial</a></li>
                <li><a href="http://www.echoecho.com/html.htm" class="external text" title="http://www.echoecho.com/html.htm">EchoEcho.com HTML Tutorial</a></li>
                <li><a href="http://www.webmonkey.com/2010/02/html_cheatsheet/" class="external text" title="http://www.webmonkey.com/2010/02/html_cheatsheet/">The Webmonkey HTML Cheatsheet</a></li>
            </ul>
        </div>

        <p id="publish">Before <a href="Publishing_Your_Site.html" title="Publishing Your Site">publishing</a>, please be sure to <a href="HTML_Validation.html" title="HTML Validation">validate</a> any Raw HTML objects.</p><a name="Code_Guidelines" id="Code_Guidelines"></a>

        <h3><span class="mw-headline">Code Guidelines</span></h3>

        <p>For advice on the correct HTML to use, please see "<a href="HTML_code_guidelines_and_tips.html" title="HTML code guidelines and tips">HTML code guidelines and tips</a>."</p><a name="Raw_HTML_object" id="Raw_HTML_object"></a>

        <h2><span class="mw-headline">Raw HTML object</span></h2>

        <p>Raw HTML Objects allow you to manage HTML on part of your page.</p>

        <div class="related">
            <a name="Related_Articles" id="Related_Articles"></a>

            <h2><span class="mw-headline">Related Articles</span></h2>

            <ul>
                <li><a href="HTML_code_guidelines_and_tips.html" title="HTML code guidelines and tips">HTML code guidelines and tips</a></li>
                <li><a href="HTML_Validation.html" title="HTML Validation">HTML Validation</a></li>
                <li><a href="Adobe_Flash.html" title="Adobe Flash">Adobe Flash</a></li>
            </ul>
        </div>
    </div>
</html>
"""

# display(HTML(html_string))

ps = BeautifulSoup(html_string)
# print(ps)
body = ps.find(name="body")
print(body.find(name="h1").text)
# print(body.findAll(name="p"))
print(body.find(name="p", attrs={"id":"publish"}).text)