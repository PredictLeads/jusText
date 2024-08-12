import justext


def test_words_should_be_split_by_br_tag():
    paragraphs = justext.justext("abc<br/>def becoming abcdef", justext.get_stoplist("English"))

    assert [p.text for p in paragraphs] == ["abc def becoming abcdef"]


def test_test_node_words_should_be_split_by_text_node_separator():
    paragraphs = justext.justext(
        "<span>Some text.</span><span>Some other text.</span>", justext.get_stoplist("English"), text_node_separator=" "
    )

    assert [p.text for p in paragraphs] == ["Some text. Some other text."]