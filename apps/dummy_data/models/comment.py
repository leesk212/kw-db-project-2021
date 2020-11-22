import random
from datetime import timedelta


class CommentModel:
    def __init__(self, fake, post_ids, student_ids):
        self._fake = fake

        self._post_ids = set(post_ids)
        self._student_ids = set(student_ids)

        self._id = -1
        self._added_comment = dict()  # comment_id: created_time

    def _get_id(self):
        self._id += 1
        return self._id

    def _get_random_created_time(self, created_time):
        return created_time + timedelta(seconds=random.randint(1, 3600 * 24 * 90))

    def __iter__(self):
        return self

    def __next__(self):
        try:
            id_ = self._get_id()

            if self._fake.boolean() and id_ > 5:
                comment = random.randint(0, id_ - 1)
                board = None
                created_time = self._added_comment[comment]
            else:
                comment = None
                board, created_time = random.sample(self._post_ids, 1)[0]
            content = "\n".join(self._fake.sentences(random.randint(1, 10)))
            like_, hate = random.randint(0, 100), random.randint(0, 100)

            author = random.sample(self._student_ids, 1)[0]
            created_time = self._get_random_created_time(created_time)
            self._added_comment[id_] = created_time

            return (id_, comment, board, content, like_, hate, author, created_time)
        except KeyError:
            raise StopIteration from None
