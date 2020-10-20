#file

#@dataclass
class AutoCompleteDataClass:

    def __init__(self,completed_sentence,source_text,source_line,offset,score):
        self.completed_sentence=completed_sentence #str
        self.source_text=source_text #str
        self.source_line=source_line #int
        self.offset=offset #int
        self.score=score #int
    # methods that you need to define by yourself
