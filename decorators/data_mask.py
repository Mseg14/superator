import re

from consts import (AWS_ACCOUNT_NUMBER_OF_DIGITS, MASK_CHAR, AT_CHAR, EMAIL_VALIDATE_PATTERN,
                    AWS_ACCOUNT_NUMBER_OF_DIGITS_TO_MASK, EMAIL_MASKING_FROM_INDEX, EMAIL_NUMBER_OF_MASKED_CHARS)


class MaskingEvaluator:
    def should_mask(self, value) -> bool:
        raise NotImplementedError

    def mask(self, value):
        raise NotImplementedError


class AwsAccountIdMaskingEvaluator(MaskingEvaluator):
    def should_mask(self, value) -> bool:
        return type(value) in [str, int] and len(str(value)) == AWS_ACCOUNT_NUMBER_OF_DIGITS

    def mask(self, value):
        string_value = str(value)
        return string_value.replace(
            string_value[0: AWS_ACCOUNT_NUMBER_OF_DIGITS_TO_MASK], MASK_CHAR * AWS_ACCOUNT_NUMBER_OF_DIGITS_TO_MASK, 1
        )


class EmailAddressMaskingEvaluator(MaskingEvaluator):
    def should_mask(self, value) -> bool:
        return type(value) in [str] and re.match(EMAIL_VALIDATE_PATTERN, value)

    def mask(self, value: str):
        at_index = value.index(AT_CHAR)
        return value.replace(value[EMAIL_MASKING_FROM_INDEX: at_index], MASK_CHAR * EMAIL_NUMBER_OF_MASKED_CHARS, 1)


class MaskingManager:
    def __init__(self):
        self.evaluators = [AwsAccountIdMaskingEvaluator(), EmailAddressMaskingEvaluator()]

    def mask(self, value):
        for evaluator in self.evaluators:
            if evaluator.should_mask(value):
                return evaluator.mask(value)
        return value
