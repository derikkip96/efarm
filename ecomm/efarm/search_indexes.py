
from haystack import indexes
from .models import Product

class ProductIndex(indexes.SearchIndex,indexes.Indexable):
    text =indexes.CharField(document=True ,use_template=True, template_name="search/indexes/search/product_search.txt")
    name =indexes.NgramField(model_attr='name')

    content_auto = indexes.NgramField(model_attr='name')

    def get_model(self):
        return Product


    def index_query(self,using=None):
        return self.get_model().objects.all()


