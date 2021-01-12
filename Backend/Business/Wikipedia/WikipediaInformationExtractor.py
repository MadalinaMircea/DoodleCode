import wikipediaapi


class WikipediaInformationExtractor:
    def __init__(self):
        self.wiki = wikipediaapi.Wikipedia('en')

    def page_exists(self, title):
        page = self.wiki.page(title)

        return page.exists()

    def get_page_summary(self, title):
        if self.page_exists(title):
            page = self.wiki.page(title)
            return page.summary
        return ""

    def get_sections(self, title):
        if self.page_exists(title):
            page = self.wiki.page(title)
            return page.sections
        return []

    def get_section_titles(self, title):
        if self.page_exists(title):
            page = self.wiki.page(title)
            return [s.title for s in page.sections]
        return []
