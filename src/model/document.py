class Document:

    def __init__(self, type="", score=0.0, label=0, box=[], data=[]):
        if not isinstance(type, str):
            raise TypeError("type must of type string (str)")
        if not isinstance(score, float):
            raise TypeError("score must of type float (float)")
        if not isinstance(label, int):
            raise TypeError("label must of type integer (int)")
        if not isinstance(box, list):
            raise TypeError("box must of type list (list)")
        if not isinstance(data, list):
            raise TypeError("data must of type list (list)")

        self._type = type
        self._score = score
        self._label = label
        self._box = box
        self._data = data


    def __str__(self):
        """
        Show all attribut of the class 
        :return: string of all attribut
        """
        box_str = ", ".join(map(str, self._box)) if self._box else "[]"
        data_str = ", ".join(map(str, self._data)) if self._data else "[]"

        return (
            f"Type: {self._type}\n"
            f"Score: {self._score:.2f}\n"
            f"Label: {self._label}\n"
            f"Box: [{box_str}]\n"
            f"Data: [{data_str}]"
        )

    def _get_type(self):
        """
        get the type of document
        :return: self._type the type of the document
        """
        return self._type
    
    def _set_type(self, type):
        if not isinstance(type, str):
            raise TypeError("type must of type string (str)")
        self._type = type
    
    def _del_type(self):
        del self._type

    def _get_score(self):
        """
        get the score of document
        :return: self._score the score of the document
        """
        return self._score
    
    def _set_score(self, score):
        if not isinstance(score, float):
            raise TypeError("score must of type float (float)")
        self._score = score
    
    def _del_score(self):
        del self._score

    def _get_label(self):
        """
        get the label of document
        :return: self._label the type of the document
        """
        return self._label
    
    def _set_label(self, label):
        if not isinstance(label, int):
            raise TypeError("label must of type integer (int)")
        self._label = label
    
    def _del_label(self):
        del self._label

    def _get_box(self):
        """
        get the box of document
        :return: self._box the box of the document
        """
        return self._box
    
    def _set_box(self, box):
        if not isinstance(box, list):
            raise TypeError("box must of type list (list)")
        self._box = box
    
    def _del_box(self):
        del self._box

    def _get_data(self):
        """
        get the data of document
        :return: self._data the data of the document
        """
        return self._data
    
    def _set_data(self, data):
        if not isinstance(data, list):
            raise TypeError("data must of type list (list)")
        self._data = data
    
    def _del_data(self):
        del self._data
    
    type = property(_get_type, _set_type, _del_type, "the type property (Banque or Facture)")
    score = property(_get_score, _set_score, _del_score, "the score property (score of the document with percent to detect array)")
    label = property(_get_label, _set_label, _del_label, "the label property (label match with the model type)")
    box = property(_get_box, _set_box, _del_box, "the box property (dimension array in document)")
    data = property(_get_data, _set_data, _del_data, "the data property (exctract word find in the document )")