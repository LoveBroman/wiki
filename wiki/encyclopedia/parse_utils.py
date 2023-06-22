import re
from abc import ABC, abstractmethod

def to_html(s):
    if s is None:
        return False
    else:
        s = s.replace('\r', '')
        sls = list(filter(lambda x : len(x) > 0,s.split("\n\n")))
        matchers = [MatchFactory.create_match(subseq) for subseq in sls]
        ht = ""
        for matcher in matchers:
            ht += matcher.return_match()
            ht += "\n\n"

        return ht

class Matcher(ABC):
    def __init__(self, seq):
        self.seq = seq

    def return_match(self):
        self.seq = self.head_match()
        self.seq = self.match_links()
        self.seq = self.match_bolds()
        self.seq = self.match_itals()
        return self.seq

    @abstractmethod
    def head_match(self):
        pass

    @staticmethod
    def _bold_match_helper(match):
        return "<b>" + match.group(0)[2:-2] + "</b>"

    def match_bolds(self):
        return re.sub(r"\*\*(.+?)\*\*", self._bold_match_helper, self.seq)

    @staticmethod
    def _ital_match_helper(match):
        return "<i>" + match.group(0)[1:-1] + "</i>"

    def match_itals(self):
        return re.sub(r"\*(.+?)\*", self._ital_match_helper, self.seq)

    def __link_sub_helper(self, s, pattern):
        def sub_func(match):
            return match.group(0)[1:-1]
        #return re.sub(pattern,sub_func, s)
        return re.search(pattern, s).group(0)[1:-1]

    def _link_sub_helper(self, match):
        s = match.group(0)
        square_part = self.__link_sub_helper(s, r"\[.*?\]")
        print("sqpart", square_part)
        paran_part = self.__link_sub_helper(s, r"\(.*?\)")
        print("paranpart", paran_part)
        return "<a href=" + paran_part + ">" + square_part + "</a>"

    def match_links(self):
        #print("ursprunglig länk", re.findall(r"\[.*?\]\(.*?\)", self.seq))
        #print(f"substiterad länk", re.sub(r'\[.*?\]\(.*?\)', self._link_sub_helper, self.seq))
        return re.sub(r"\[.*?\]\(.*?\)", self._link_sub_helper, self.seq)

class BulletMatcher(Matcher):

    def _head_helper(self, seq):
        return "<ul>\n  <li>" + seq + "\n</ul>\n"

    def head_match(self):
        #self.seq = self._head_helper()
        #self.seq = re.sub("")
        return self._head_helper(re.sub(r"\n\* ", "</li>\n  <li> ",self.seq[1:]))

class HeaderMatcher(Matcher):
    def head_match(self):
        num_hashs = next((i for i, char in enumerate(self.seq) if char != '#'), -1)
        if num_hashs <= 4:
            return f"<h{num_hashs}>" + self.seq[num_hashs:] + f"</h{num_hashs}>"
        else:
            return f"<h{4}>" + self.seq[4:] + f"</h{4}>"

class ParagraphMatcher(Matcher):
    def head_match(self):
        return "<p>" + self.seq + "</p>"

class MatchFactory:
    @staticmethod
    def create_match(seq):
        if seq[0] == "#":
            return HeaderMatcher(seq)
        elif seq[:2] == "* ":
            return BulletMatcher(seq)
        else:
            return ParagraphMatcher(seq)