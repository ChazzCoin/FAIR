from F.DATE import TODAY
from F.LOG import Log
from FM.QueryHelper import O
from FNLP.Language import Words

from F import DATE, CONVERT, DICT, LIST
from FNLP.Models import BaseModel
from FNLP.Models.Paragraphs import ParagraphsModel
from FNLP.Models.Sentences import SentencesEngine
from FNLP.Models.Variables import ContentVariables, BaseVariables
from FNLP.Models.Words import WordsEngine
Log = Log("ContentModel")

CONTENT = lambda content, date: {"content": content, "date": date}
class ContentManager(BaseModel, BaseVariables, ContentVariables):
    """ VARIABLES ARE IN 'CONTENTVARIABLES' UNDER VARIABLES MODEL """

    def run_analyzer(self):
        self.model_words = WordsEngine(input_models=self.input_models)
        self.model_words.analyze_dates()
        self.model_sentences = SentencesEngine(input_models=self.input_models)
        self.model_sentences.analyze_dates()
        # self.model_paragraphs = ParagraphsModel(input_p_content=self.input_contents).run_analyzer()
        # self.model_paragraphs.run_analyzer()

    def prepare_content(self):
        pass

    def add_webpages(self, webpages:list):
        for ac in Log.ProgressBarYielder(webpages, prefix="Preparing Content..."):
            self.add_webpage(ac)

    def add_webpage(self, webpage:dict):
        # Internal for The Brain
        id = DICT.get("_id", webpage, default="Unknown")
        new_date = DICT.get("pub_date", webpage, None)
        model = { "_id": O.TO_OBJECT_ID(id), "webpage_date": new_date, "updatedDate": TODAY }
        self.webpage_models.append(model)
        # Add Date
        if new_date:
            self._dates_analyzed.append(new_date)
        # Category Scores
        # cat_scores = DICT.get("category_scores", webpage, None)
        # if cat_scores:
        #     self.category_scores = DICT.add_word_count(self.category_scores, cat_scores)
        self.extract_content(webpage)
        self.post_add_webpage_work()

    def extract_content(self, webpage):
        title = DICT.get("title", webpage, "")
        body = DICT.get("body", webpage, None)
        new_date = DICT.get("pub_date", webpage, None)
        if body:
            main_content = str(title) + " " + str(body)
            main_content_model = CONTENT(main_content, new_date)
            self.input_models.append(main_content_model)
        else:
            new_content = CONVERT.dict_TO_List_OF_Values(webpage)
            main_content_model = CONTENT(new_content, "Unknown")
            self.input_models.append(main_content_model)

    def post_add_webpage_work(self):
        # self.input_tokens = LIST.flatten(self.input_tokens_by_content)
        self._dates_analyzed = LIST.remove_duplicates(self._dates_analyzed)
        self._dates_analyzed_count = len(self._dates_analyzed)
        self._webpages_analyzed_count = len(self.input_contents)




















































