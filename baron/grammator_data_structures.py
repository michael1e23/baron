def include_data_structures(pg):
    @pg.production("atom : LEFT_PARENTHESIS RIGHT_PARENTHESIS")
    def tuple((left_parenthesis, right_parenthesis,)):
        return {
                "type": "tuple",
                "first_space": left_parenthesis.after_space,
                "second_space": "",
                "value": []
               }


    @pg.production("atom : LEFT_PARENTHESIS testlist_comp RIGHT_PARENTHESIS")
    def tuple_one((left_parenthesis, testlist_comp, right_parenthesis,)):
        return {
                "type": "tuple",
                "first_space": left_parenthesis.after_space,
                "second_space": right_parenthesis.before_space,
                "value": testlist_comp
               }


    @pg.production("testlist_comp : test COMMA")
    def testlist_comp((test, comma)):
        return [test, {"type": "comma", "value": ","}]