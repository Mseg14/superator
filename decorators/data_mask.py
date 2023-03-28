import re

EMAIL_VALIDATE_PATTERN = r"^\S+@\S+\.\S+$"


class MaskingEvaluator:
    def should_mask(self, value) -> bool:
        raise NotImplementedError

    def mask(self, value):
        raise NotImplementedError


class AwsAccountIdMaskingEvaluator(MaskingEvaluator):
    def should_mask(self, value) -> bool:
        return type(value) in [str, int] and len(str(value)) == 12

    def mask(self, value):
        string_value = str(value)
        return string_value.replace(string_value[0: 8], 'XXXXXXXX', 1)


class EmailAddressMaskingEvaluator(MaskingEvaluator):
    def should_mask(self, value) -> bool:
        return type(value) in [str] and re.match(EMAIL_VALIDATE_PATTERN, value)

    def mask(self, value: str):
        at_index = value.index("@")
        return value.replace(value[3: at_index], "XXX", 1)


class MaskingManager:
    def __init__(self):
        self.evaluators = [AwsAccountIdMaskingEvaluator(), EmailAddressMaskingEvaluator()]

    def mask(self, value):
        for evaluator in self.evaluators:
            if evaluator.should_mask(value):
                return evaluator.mask(value)
        return value
