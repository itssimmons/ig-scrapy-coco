class Helpers:
    @staticmethod
    def join_by(self, by: str, scope: str) -> str:
        return by.join(scope.split())
