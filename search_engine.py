from string import punctuation
from dataclasses import dataclass
from collections import defaultdict, Counter
from math import log

TRANSLATION_TABLE = str.maketrans({char: " " for char in punctuation})


@dataclass
class SearchResult:
    name: str
    score: float


@dataclass
class DocWithWordFreq:
    name: str
    word_freq: int


def split_to_words(text: str) -> list[str]:
    lowercase_text = text.lower()
    cleaned_text = lowercase_text.translate(TRANSLATION_TABLE)
    words = cleaned_text.split()
    return words


class SearchEngine:
    def __init__(self, docs: list[str]) -> None:
        self._doc_wordcount: dict[str, int] = {}
        self._index: dict[str, list[DocWithWordFreq]] = defaultdict(list)

        self._build_index(docs)

    def search(self, query: str) -> list[SearchResult]:
        scores: dict[str, float] = defaultdict(float)

        words = split_to_words(query)
        for word in words:
            if word not in self._index:
                continue

            idf = self._count_idf(word)

            docs_with_word = self._index.get(word, [])
            for doc_with_word_freq in docs_with_word:
                tf = self._count_tf(doc_with_word_freq)

                word_relevance = idf * tf
                scores[doc_with_word_freq.name] += word_relevance

        search_results = [SearchResult(name, score) for name, score in scores.items()]
        search_results.sort(key=lambda s: s.score, reverse=True)
        return search_results

    def _build_index(self, docs: list[str]) -> None:
        for filepath in docs:
            with open(filepath, "r", encoding="utf-8") as fp:
                content = fp.read()
                self._add_to_index(filepath, content)

    def _add_to_index(self, doc: str, content: str) -> None:
        words = split_to_words(content)
        self._doc_wordcount[doc] = len(words)

        for word, freq in Counter(words).items():
            self._index[word].append(DocWithWordFreq(doc, freq))

    def _count_idf(self, word: str) -> float:
        doc_count = len(self._doc_wordcount)
        docs_with_word = self._index.get(word, [])
        doc_count_with_word = len(docs_with_word)

        idf = log((doc_count + 1) / (doc_count_with_word + 1))
        return idf

    def _count_tf(self, doc_with_word_freq: DocWithWordFreq) -> float:
        word_frequency_in_doc = doc_with_word_freq.word_freq
        doc_wordcount = self._doc_wordcount[doc_with_word_freq.name]

        tf = word_frequency_in_doc / doc_wordcount
        return tf


def main():
    docs = ["docs/a.txt", "docs/b.txt"]
    se = SearchEngine(docs)

    print(se.search("Inverted index (DATA STRUCTURE)."))


if __name__ == "__main__":
    main()
