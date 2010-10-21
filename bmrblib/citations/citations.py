#############################################################################
#                                                                           #
# The BMRB library.                                                         #
#                                                                           #
# Copyright (C) 2009-2010 Edward d'Auvergne                                 #
#                                                                           #
# This program is free software: you can redistribute it and/or modify      #
# it under the terms of the GNU General Public License as published by      #
# the Free Software Foundation, either version 3 of the License, or         #
# (at your option) any later version.                                       #
#                                                                           #
# This program is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
# GNU General Public License for more details.                              #
#                                                                           #
# You should have received a copy of the GNU General Public License         #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.     #
#                                                                           #
#############################################################################

# Module docstring.
"""The citations saveframe category.

For example, see http://www.bmrb.wisc.edu/dictionary/3.1html/SaveFramePage.html#citations.
"""

# relax module imports.
from bmrblib.base_classes import BaseSaveframe, TagCategory, TagCategoryFree
from bmrblib.misc import translate
from bmrblib.pystarlib.SaveFrame import SaveFrame
from bmrblib.pystarlib.TagTable import TagTable


class CitationsSaveframe(BaseSaveframe):
    """The citations saveframe class."""

    # Class variables.
    label = 'citation'
    sf_label = 'citations'

    def __init__(self, datanodes):
        """Initialise the class, placing the pystarlib data nodes into the namespace.

        @param datanodes:   The pystarlib data nodes object.
        @type datanodes:    list
        """

        # Place the data nodes into the namespace.
        self.datanodes = datanodes

        # The number of entities.
        self.citation_num = '0'

        # Add the specific tag category objects.
        self.add_tag_categories()


    def add(self, citation_label='citation', cas_abstract_code=None, medline_ui_code=None, authors=None, doi=None, pubmed_id=None, full_citation=None, title=None, status='published', type='journal', journal_abbrev=None, journal_full=None, volume=None, issue=None, page_first=None, page_last=None, year=None):
        """Add the citation information to the data nodes.

        @keyword citation_label:    A label to call the saveframe.  If left at 'citation', then the citation ID number will be appended.
        @type citation_label:       str
        @keyword authors:           The list of authors.  Each author element is a list of four elements: the first name, last name, first initial, and middle initials.
        @type authors:              list of lists of str
        @keyword doi:               The DOI number, e.g. "10.1000/182".
        @type doi:                  None or str
        @keyword pubmed_id:         The identification code assigned to the publication by PubMed.
        @type pubmed_id:            None or int
        @keyword full_citation:     A full citation in a format similar to that used in a journal article by either cutting and pasting from another document or by typing. Please include author names, title, journal, page numbers, and year or equivalent information for the type of publication given.
        @type full_citation:        str
        @keyword title:             The title of the publication.
        @type title:                str
        @keyword status:            The publication status.  Can be one of in "preparation", "in press", "published", "retracted", or "submitted".
        @type status:               str
        @keyword type:              The publication type.  Can be one of "abstract", "BMRB only", "book", "book chapter", "internet", "journal", "personal communication", or "thesis".
        @type type:                 str
        @keyword journal_abbrev:    A standard journal abbreviation as defined by the Chemical Abstract Services for the journal where the data are or will be published.  If the data in the deposition are related to a J. Biomol. NMR paper, the value must be 'J. Biomol. NMR' to alert the BMRB annotators so that the deposition is properly processed.  If the depositor truly does not know the journal, a value of 'not known' or 'na' is acceptable.
        @type journal_abbrev:       str
        @keyword journal_full:      The full journal name.
        @type journal_full:         str
        @keyword volume:            The volume number.
        @type volume:               int
        @keyword issue:             The issue number.
        @type issue:                int
        @keyword page_first:        The first page number.
        @type page_first:           int
        @keyword page_last:         The last page number.
        @type page_last:            int
        @keyword year:              The publication year.
        @type year:                 int
        """

        # Place the args into the namespace.
        self.doi = translate(doi)
        self.pubmed_id = translate(pubmed_id)
        self.full_citation = full_citation
        self.title = translate(title)
        self.status = translate(status)
        self.type = translate(type)
        self.journal_abbrev = translate(journal_abbrev)
        self.journal_full = translate(journal_full)
        self.volume = translate(volume)
        self.issue = translate(issue)
        self.page_first = translate(page_first)
        self.page_last = translate(page_last)
        self.year = translate(year)
        self.citation_label = translate(citation_label)
        self.cas_abstract_code = translate(cas_abstract_code)
        self.medline_ui_code = translate(medline_ui_code)

        # The author info.
        self.author_given_name = []
        self.author_family_name = []
        self.author_first_init = []
        self.author_mid_init = []
        self.author_family_title = []
        for i in range(len(authors)):
            self.author_given_name.append(authors[i][0])
            self.author_family_name.append(authors[i][1])
            self.author_first_init.append(authors[i][2])
            self.author_mid_init.append(authors[i][3])
            self.author_family_title.append(None)
        self.author_given_name = translate(self.author_given_name)
        self.author_family_name = translate(self.author_family_name)
        self.author_first_init = translate(self.author_first_init)
        self.author_mid_init = translate(self.author_mid_init)
        self.author_family_title = translate(self.author_family_title)
        #self.generate_data_ids(len(authors))

        # Increment the number of entities.
        self.citation_num = str(int(self.citation_num) + 1)
        self.citation_id_num = [str(translate(self.citation_num))]

        # Modify the citation label.
        if self.citation_label == 'citation':
            self.citation_label = 'citation ' + repr(self.citation_num)

        # Initialise the save frame.
        self.frame = SaveFrame(title=self.label)

        # Create the tag categories.
        self.citations.create()
        self.citations_author.create()

        # Add the saveframe to the data nodes.
        self.datanodes.append(self.frame)


    def add_tag_categories(self):
        """Create the tag categories."""

        # The tag category objects.
        self.citations = Citations(self)
        self.citations_author = CitationsAuthor(self)



class Citations(TagCategoryFree):
    """Base class for the Citations tag category."""

    def __init__(self, sf):
        """Setup the Citations tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(Citations, self).__init__(sf)

        # The tag category label.
        self.tag_category_label = 'Citation'

        # Database table names to class instance variables.
        self.data_to_var_name.append(['SfFramecode',        'citation_label'])
        self.data_to_var_name.append(['CitationID',         'citation_id_num'])
        self.data_to_var_name.append(['CASAbstractCode',    'cas_abstract_code'])
        self.data_to_var_name.append(['MEDLINEUICode',      'medline_ui_code'])
        self.data_to_var_name.append(['DOI',                'doi'])
        self.data_to_var_name.append(['PubMedID',           'pubmed_id'])
        self.data_to_var_name.append(['FullCitation',       'full_citation'])
        self.data_to_var_name.append(['Title',              'title'])
        self.data_to_var_name.append(['Status',             'status'])
        self.data_to_var_name.append(['Type',               'type'])
        self.data_to_var_name.append(['JournalAbbrev',      'journal_abbrev'])
        self.data_to_var_name.append(['JournalNameFull',    'journal_full'])
        self.data_to_var_name.append(['JournalVolume',      'volume'])
        self.data_to_var_name.append(['JournalIssue',       'issue'])
        self.data_to_var_name.append(['PageFirst',          'page_first'])
        self.data_to_var_name.append(['PageLast',           'page_last'])
        self.data_to_var_name.append(['Year',               'year'])

        # Database table name to tag name.
        self.data_to_tag_name['SfCategory'] =                  'Sf_category'
        self.data_to_tag_name['SfFramecode'] =                 'Sf_framecode'
        self.data_to_tag_name['CitationID'] =                  'ID'
        self.data_to_tag_name['CASAbstractCode'] =             'CAS_abstract_code'
        self.data_to_tag_name['MEDLINEUICode'] =               'MEDLINE_UI_code'
        self.data_to_tag_name['DOI'] =                         'DOI'
        self.data_to_tag_name['PubMedID'] =                    'PubMed_ID'
        self.data_to_tag_name['FullCitation'] =                'Full_citation'
        self.data_to_tag_name['Title'] =                       'Title'
        self.data_to_tag_name['Status'] =                      'Status'
        self.data_to_tag_name['Type'] =                        'Type'
        self.data_to_tag_name['JournalAbbrev'] =               'Journal_abbrev'
        self.data_to_tag_name['JournalNameFull'] =             'Journal_name_full'
        self.data_to_tag_name['JournalVolume'] =               'Journal_volume'
        self.data_to_tag_name['JournalIssue'] =                'Journal_issue'
        self.data_to_tag_name['JournalASTM'] =                 'Journal_ASTM'
        self.data_to_tag_name['JournalISSN'] =                 'Journal_ISSN'
        self.data_to_tag_name['JournalCSD'] =                  'Journal_CSD'
        self.data_to_tag_name['BookTitle'] =                   'Book_title'
        self.data_to_tag_name['BookChapterTitle'] =            'Book_chapter_title'
        self.data_to_tag_name['BookVolume'] =                  'Book_volume'
        self.data_to_tag_name['BookSeries'] =                  'Book_series'
        self.data_to_tag_name['BookPublisher'] =               'Book_publisher'
        self.data_to_tag_name['BookPublisherCity'] =           'Book_publisher_city'
        self.data_to_tag_name['BookISBN'] =                    'Book_ISBN'
        self.data_to_tag_name['ConferenceTitle'] =             'Conference_title'
        self.data_to_tag_name['ConferenceSite'] =              'Conference_site'
        self.data_to_tag_name['ConferenceStateProvince'] =     'Conference_state_province'
        self.data_to_tag_name['ConferenceCountry'] =           'Conference_country'
        self.data_to_tag_name['ConferenceStartDate'] =         'Conference_start_date'
        self.data_to_tag_name['ConferenceEndDate'] =           'Conference_end_date'
        self.data_to_tag_name['ConferenceAbstractNumber'] =    'Conference_abstract_number'
        self.data_to_tag_name['ThesisInstitution'] =           'Thesis_institution'
        self.data_to_tag_name['ThesisInstitutionCity'] =       'Thesis_institution_city'
        self.data_to_tag_name['ThesisInstitutionCountry'] =    'Thesis_institution_country'
        self.data_to_tag_name['WWWURL'] =                      'WWW_URL'
        self.data_to_tag_name['PageFirst'] =                   'Page_first'
        self.data_to_tag_name['PageLast'] =                    'Page_last'
        self.data_to_tag_name['Year'] =                        'Year'
        self.data_to_tag_name['Details'] =                     'Details'



class CitationsAuthor(TagCategory):
    """Base class for the CitationsAuthor tag category."""

    def __init__(self, sf):
        """Setup the CitationsAuthor tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(CitationsAuthor, self).__init__(sf)

        # The tag category label.
        self.tag_category_label = 'Citation_author'

        # Database table names to class instance variables.
        self.data_to_var_name.append(['Ordinal',         'data_ids'])
        self.data_to_var_name.append(['GivenName',       'author_given_name'])
        self.data_to_var_name.append(['FamilyName',      'author_family_name'])
        self.data_to_var_name.append(['FirstInitial',    'author_first_init'])
        self.data_to_var_name.append(['MiddleInitials',  'author_mid_init'])
        self.data_to_var_name.append(['FamilyTitle',     'author_family_title'])
        self.data_to_var_name.append(['CitationID',      'citation_id_num'])

        # Database table name to tag name.
        self.data_to_tag_name['Ordinal'] =         'Ordinal'
        self.data_to_tag_name['GivenName'] =       'Given_name'
        self.data_to_tag_name['FamilyName'] =      'Family_name'
        self.data_to_tag_name['FirstInitial'] =    'First_initial'
        self.data_to_tag_name['MiddleInitials'] =  'Middle_initials'
        self.data_to_tag_name['FamilyTitle'] =     'Family_title'
        self.data_to_tag_name['SfID'] =            'Sf_ID'
        self.data_to_tag_name['EntryID'] =         'Entry_ID'
        self.data_to_tag_name['CitationID'] =      'Citation_ID'
