class Helpers:
    @staticmethod
    def join_by(by: str, scope: str) -> str:
        return by.join(scope.split())

    @staticmethod
    def replace(search: str, replace: str, scope: str) -> str:
        return scope.replace(search, replace)
