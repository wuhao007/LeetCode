class HtmlParser:
    # @param {string} content source code
    # @return {string[]} a list of links
    def parseUrls(self, content):
        # Write your code here
        import re
        links = re.findall(r'\s*(?!)href\s*=\s*"?\'?([^"\'>\s]*)', content, re.I)
        return [link for link in links if len(link) and not link.startswith('#')]

