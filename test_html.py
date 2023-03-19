import pytest
from project_1 import getTextAndLinks

# HTML
@pytest.mark.parametrize("link, expected_result_link, expected_result_text", [('https://pmpu.space', 'https://vk.com/sspmpu', 'Факультет прикладной математики — процессов управления/n')])
def testgetTextAndLinks(link, expected_result_link, expected_result_text):
    assert expected_result_link in getTextAndLinks(link)[0]
    assert expected_result_text in getTextAndLinks(link)[1]


s = """
/nPolicy -- /WWW/n
/n
/n
/nPolicy/nThis outlines the policy of  the
/nW3 project/n at CERN.  Whilst not legally
binding, this attempts to explain
my understanding of the CERN rules
and the desires of the team at CERN.
/nAim/nThe basic aim of the project is to
promote communication and information
availability for the High Energy
Physics (HEP) community.  The project
is based at CERN, whose budget is
provided by contributions of taxpayer's
money from the European member states.
 It is in the interests of HEP, CERN,
and the project itself that it should
interwork with systems and information
in many other fields, and so active
collaboration with other groups is
essential.   To produce an information
system isolating HEP from the rest
of the world would be counter-productive,
so the aim can be seen as furthering
a global web of information./n
The WWW team are all enthusiastic
that  information of all types should
be available as widely as possible.
/nCollaboration/nWe encourage collaboration by academic
or commercial parties. There are
always many things to be done, ports
to be made to different environments,
new browsers to be written, and additional
data to be incorporated into the
"web". There have already been many
contributions in these terms, and
also with hardware support from manufacturers./n
If you may be interested in extending
the web or the software, please mail
or phone us.
/nCode distribution/nCode written at CERN  is covered
by the CERN copyright. In practice
the interpretation of this in the
case of the W3 project is that the
programs are freely available to
academic bodies. To commercial organizations
who are not reselling it, but are
using it to participate in global
information exchange,  the charge
is generally waived in order to cut
administrative costs. Code is of
course shared freely with all collaborators.
Commercial organizations wishing
to sell software based on W3 code
should contact CERN./n
We are in the process of getting
agreement to release certain parts
of the WWW project code with the
General Public License (and GP Library
License)./n
Where CERN code is included in otherwise
public domain code, that CERN code
becomes also public domain./n
Code not originating at CERN is of
course covered by terms set by the
copyright holder involved.
/nProtocols and Data Formats/nThe definition of protocols such
as /nHTTP/n and data formats such as/n
HTML/n are in the public domain and
may be freely used by anyone.
/nTim BL/n
/n
"""

# Html: all links and text
@pytest.mark.parametrize("link, expected_result_link, expected_result_text", 
                         [('http://info.cern.ch/hypertext/WWW/Policy.html', 
                           ['http://info.cern.ch/hypertext/WWW/TheProject.html', 'http://info.cern.ch/hypertext/WWW/Protocols/HTTP/AsImplemented.html', 'http://info.cern.ch/hypertext/WWW/MarkUp/MarkUp.html', 'http://info.cern.ch./hypertext/TBL_Disclaimer.html'],
                           s)])
def testgetTextAndLinks2(link, expected_result_link, expected_result_text):
    links = getTextAndLinks(link)[0]
    assert len(links) == len(expected_result_link)
    #for exp_link in expected_result_link:
        #assert exp_link in links
    assert getTextAndLinks(link)[1] == expected_result_text

s = """HyperText Design Issues: Annotation/n
/n
/nAnnotation /nAnnotation is the  linking of a new commentary node to someone else's
existing node. It is the essence of a collaborative hypertext.  (See/n
Multiuser considerations/n )/n
There is a problem when the web includes more than one authentication
domain. See Šprotectionš.  /n
See also:  /nThe problem of linking to living documents/n ."""

# Html all text and text with specific symbols
@pytest.mark.parametrize("link, expected_result_text", 
                         [('http://info.cern.ch/hypertext/WWW/DesignIssues/Annotation.html', 
                           s)])
def testgetTextAndLinks3(link, expected_result_text):
    assert getTextAndLinks(link)[1] == expected_result_text

s = """/nПМ-ПУ :: Статьи о факультете 1975-1980г./n"""

# Russian site
@pytest.mark.parametrize("link, expected_result_text", 
                         [('http://old.apmath.spbu.ru/ru/misc/articles/1975_1980.html', 
                           s)])
def testgetTextAndLinks4(link, expected_result_text):
    assert expected_result_text in getTextAndLinks(link)[1]