#!/usr/bin/python
import requests
import sys
from lxml import etree

def get_jenkins_latest_release_version():

    # Jenkins RSS Feed
    url = "https://jenkins.io/changelog/rss.xml"

    # Fetch the RSS feed of Jenkins Changelog
    response = requests.request(method='GET', url=url)

    if response.status_code == 200:
        jenkins_changelog_rss = etree.fromstring(response.text)

        # Get the first element from the changelog
        recent_version = jenkins_changelog_rss.xpath('/rss/channel/item/title/text()')[0]

        # slice the string to get the version
        version = recent_version[8:]
        # return jenkins latest release version
        return version
    else:
        print('API ERROR!')
        sys.exit(0)

def get_current_installed_jenkins_version():
    # create element tree object
    # provide real path for jenkins config.xml
    tree = etree.parse('config.xml')
    # get root element
    root = tree.getroot()
    installed_version = root.xpath('/hudson/version/text()')[0]
    # return jenkins installed version
    return installed_version


def main():
    # Get Jenkins Latest version
    latest_version = get_jenkins_latest_release_version()

    # Get Installed Jenkins Version
    installed_version = get_current_installed_jenkins_version()

    if latest_version == installed_version:
        print('Jenkins is upto date!')
    else:
        print('A new version of jenkins is available!')

if __name__ == "__main__":
    # calling main function
    main()
