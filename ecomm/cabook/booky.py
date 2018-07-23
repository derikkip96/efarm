from hire.models import Input
from django.conf import settings
from decimal import Decimal



class Book(object):
    # initialise book session

    def __init__(self, request):
        # gettin the current session
        self.session = request.session
        book = self.session.get(settings.BOOK_SESSION_ID)
        if not book:
            # save empty book
            book = self.session[settings.BOOK_SESSION_ID] = {}
        self.book = book

    def remove(self, input):
        input_id = str(input.id)
        if input_id in self.book:
            del self.book[input_id]
            self.save()

    def add(self, input ):
        # add a input to the shopping book or update its quantity
        input_id = str(input.id)
        # checking if the input is not in the book
        if input_id not in self.book:
            self.book[input_id] = {'price': str(input.price)}
        self.save()

    def save(self):
        # update the session book
        self.session[settings.BOOK_SESSION_ID] = self.book
        self.session.modified = True
    def clear(self):
        # remove book from the session
        del self.session[settings.BOOK_SESSION_ID]
        self.session.modified = True

    def __iter__(self):
        # iterate over the items in the book and get inputs from the datebase
        inputs_id = self.book.keys()

        # retrieving input instances availabe in the book and add the to the item book
        inputs = Input.objects.filter(id__in=inputs_id)
        for input in inputs:
            self.book[str(input.id)]['input'] = input

        # iterating over the items in the shopping book and getting the total price
        for item in self.book.values():
            item['price'] = Decimal(item['price'])
            yield item

    def get_total_cost(self):
        return sum(Decimal(item['price']) for item in self.book.values())


